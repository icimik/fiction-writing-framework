#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSETS_ROOT = SKILL_ROOT / "assets"
DEFAULT_PANDOC_CSS = ASSETS_ROOT / "pandoc-book.css"
DEFAULT_VIVLIOSTYLE_CSS = ASSETS_ROOT / "vivliostyle-book.css"


def chapter_sort_key(path: Path) -> tuple[int, int | str]:
    match = re.search(r"第(\d+)章", path.name)
    if match:
        return (0, int(match.group(1)))
    return (1, path.name)


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def try_run(cmd: list[str]) -> tuple[bool, str]:
    try:
        completed = subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=60)
    except FileNotFoundError as exc:
        return False, str(exc)
    except subprocess.TimeoutExpired:
        return False, f"命令超时: {' '.join(cmd)}"
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()
        return False, detail or f"命令失败: {' '.join(cmd)}"
    else:
        detail = (completed.stderr or completed.stdout or "").strip()
        return True, detail


def load_config(config_path: Path) -> dict[str, Any]:
    return json.loads(config_path.read_text(encoding="utf-8"))


def resolve_path(project_root: Path, value: str | None) -> Path | None:
    if not value:
        return None
    path = Path(value)
    if path.is_absolute():
        return path
    return project_root / path


def normalize_output_basename(title: str, override: str | None) -> str:
    if override:
        return override
    normalized = title.replace("：", "_").replace(":", "_")
    normalized = re.sub(r"\s+", "", normalized)
    normalized = re.sub(r"[\\/]+", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized or "publication"


def normalize_output_date(override: str | None) -> str:
    if override:
        return override
    return datetime.now().strftime("%Y%m%d")


def detect_chapter_mode(chapters_root: Path, configured_mode: str | None) -> str:
    if configured_mode and configured_mode != "auto":
        return configured_mode
    child_dirs = [path for path in chapters_root.iterdir() if path.is_dir()]
    child_files = [path for path in chapters_root.iterdir() if path.is_file() and path.suffix == ".md"]
    if child_dirs and not child_files:
        return "volumes"
    return "flat"


def demote_heading(text: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith("# "):
            lines[index] = "#" + line
        break
    return "\n".join(lines).strip() + "\n"


def extract_afterword_body(text: str) -> str:
    if "## 后记正文" not in text:
        return text.strip() + "\n"

    start = text.index("## 后记正文")
    body = text[start:].splitlines()
    collected: list[str] = ["# 后记"]
    started = False

    for line in body[1:]:
        if line.startswith("## "):
            break
        if line.startswith("# "):
            break
        if not started and not line.strip():
            continue
        started = True
        collected.append(line)

    return "\n".join(collected).strip() + "\n"


def collect_flat_chapters(chapters_root: Path) -> list[Path]:
    return sorted(chapters_root.glob("*.md"), key=chapter_sort_key)


def collect_volume_dirs(chapters_root: Path, volume_order: list[str]) -> list[Path]:
    if volume_order:
        return [chapters_root / volume for volume in volume_order if (chapters_root / volume).is_dir()]
    return sorted([path for path in chapters_root.iterdir() if path.is_dir()], key=lambda item: item.name)


def build_manuscript(project_root: Path, config: dict[str, Any], build_dir: Path, output_basename: str, output_date: str) -> Path:
    chapters_root = resolve_path(project_root, config.get("chapters_root", "07-writing/chapters"))
    if chapters_root is None or not chapters_root.exists():
        raise FileNotFoundError("未找到正文目录")

    chapter_mode = detect_chapter_mode(chapters_root, config.get("chapter_mode"))
    afterword_path = resolve_path(project_root, config.get("afterword_path"))
    manuscript_path = build_dir / f"{output_basename}_出版稿_{output_date}.md"
    parts: list[str] = []

    if chapter_mode == "volumes":
        for volume_dir in collect_volume_dirs(chapters_root, config.get("volume_order", [])):
            chapter_files = collect_flat_chapters(volume_dir)
            if not chapter_files:
                continue
            parts.append(f"# {volume_dir.name}\n")
            for chapter_file in chapter_files:
                parts.append(demote_heading(chapter_file.read_text(encoding="utf-8")))
                parts.append("\n")
    else:
        for chapter_file in collect_flat_chapters(chapters_root):
            parts.append(chapter_file.read_text(encoding="utf-8").strip() + "\n")
            parts.append("\n")

    if afterword_path and afterword_path.exists():
        parts.append(extract_afterword_body(afterword_path.read_text(encoding="utf-8")))

    manuscript_path.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")
    return manuscript_path


def rewrite_html_css_path(html_path: Path, css_file: Path) -> None:
    text = html_path.read_text(encoding="utf-8")
    rel_css = os.path.relpath(css_file, html_path.parent)
    html_path.write_text(text.replace(str(css_file), rel_css), encoding="utf-8")


def inject_pdf_cover(html_path: Path, cover_file: Path) -> None:
    if not cover_file.exists():
        return
    cover_markup = (
        '<section id="cover" class="cover-page">\n'
        f'  <img src="{cover_file.name}" alt="封面" />\n'
        "</section>\n"
    )
    text = html_path.read_text(encoding="utf-8")
    html_path.write_text(text.replace("<body>", "<body>\n" + cover_markup, 1), encoding="utf-8")


def metadata_args(config: dict[str, Any], title: str, author: str | None) -> list[str]:
    metadata = {
        "title": title,
        "lang": config.get("language", "zh-CN"),
        "toc-title": config.get("toc_title", "目录"),
        **config.get("metadata", {}),
    }
    if author:
        metadata["author"] = author

    args: list[str] = []
    for key, value in metadata.items():
        if value is None or value == "":
            continue
        args.extend(["--metadata", f"{key}={value}"])
    return args


def stage_pdf_assets(build_dir: Path, css_file: Path, cover_file: Path | None) -> tuple[Path, Path | None]:
    staged_css = build_dir / css_file.name
    shutil.copy2(css_file, staged_css)

    staged_cover: Path | None = None
    if cover_file and cover_file.exists():
        staged_cover = build_dir / cover_file.name
        shutil.copy2(cover_file, staged_cover)

    return staged_css, staged_cover


def build_html_output(
    manuscript: Path,
    metadata_flags: list[str],
    css_file: Path,
    project_root: Path,
    output_path: Path,
    *,
    toc: bool,
) -> None:
    cmd = [
        "pandoc",
        str(manuscript),
        "--standalone",
        "--resource-path",
        str(project_root),
        "--section-divs",
        *metadata_flags,
        "--css",
        str(css_file),
    ]
    if toc:
        cmd.append("--toc")
    cmd.extend(["-o", str(output_path)])
    run(cmd)
    rewrite_html_css_path(output_path, css_file)


def latex_font_name() -> str:
    font_dir = Path("/System/Library/Fonts/Supplemental")
    if font_dir.exists():
        available = "".join(path.name for path in font_dir.glob("*"))
        if "Songti" in available:
            return "Songti SC"
    return "Songti"


def build_outputs(project_root: Path, config: dict[str, Any], author_override: str | None) -> int:
    title = config["title"]
    author = author_override or config.get("author")
    output_date = normalize_output_date(config.get("output_date"))
    output_basename = normalize_output_basename(title, config.get("output_basename"))
    build_dir = resolve_path(project_root, config.get("build_dir", "10-publication/build"))
    if build_dir is None:
        raise FileNotFoundError("未找到构建输出目录")
    build_dir.mkdir(parents=True, exist_ok=True)

    manuscript = build_manuscript(project_root, config, build_dir, output_basename, output_date)
    pandoc_css = resolve_path(project_root, config.get("pandoc_css")) or DEFAULT_PANDOC_CSS
    pdf_css = resolve_path(project_root, config.get("vivliostyle_css")) or DEFAULT_VIVLIOSTYLE_CSS
    cover_file = resolve_path(project_root, config.get("cover_image"))
    staged_pdf_css, staged_pdf_cover = stage_pdf_assets(build_dir, pdf_css, cover_file)

    metadata_flags = metadata_args(config, title, author)
    common = [
        "pandoc",
        str(manuscript),
        "--standalone",
        "--resource-path",
        str(project_root),
        *metadata_flags,
        "--css",
        str(pandoc_css),
    ]

    epub_out = build_dir / f"{output_basename}_{output_date}.epub"
    html_out = build_dir / f"{output_basename}_{output_date}.html"
    pdf_html_out = build_dir / f"{output_basename}_{output_date}_print.html"
    pdf_out = build_dir / f"{output_basename}_{output_date}.pdf"

    epub_cmd = common + ["--split-level=2"]
    if cover_file and cover_file.exists():
        epub_cmd.extend(["--epub-cover-image", str(cover_file)])
    run(epub_cmd + ["-o", str(epub_out)])

    build_html_output(manuscript, metadata_flags, pandoc_css, project_root, html_out, toc=False)
    build_html_output(manuscript, metadata_flags, staged_pdf_css, project_root, pdf_html_out, toc=True)
    if staged_pdf_cover:
        inject_pdf_cover(pdf_html_out, staged_pdf_cover)

    pdf_engine = shutil.which("xelatex") or shutil.which("lualatex")
    if pdf_engine:
        pdf_cmd = [
            "pandoc",
            str(manuscript),
            "--standalone",
            "--resource-path",
            str(project_root),
            *metadata_flags,
            "--toc",
            "--pdf-engine",
            Path(pdf_engine).name,
            "-V",
            f"mainfont={latex_font_name()}",
            "-V",
            "sansfont=Hiragino Sans GB",
            "-o",
            str(pdf_out),
        ]
        run(pdf_cmd)
        pdf_status = f"ok ({Path(pdf_engine).name})"
    else:
        pdf_status = "skipped"
        vivliostyle_cmds: list[list[str]] = []
        if shutil.which("vivliostyle"):
            vivliostyle_cmds.append(["vivliostyle", "build", str(pdf_html_out), "-o", str(pdf_out)])
        if shutil.which("vivliostyle-cli"):
            vivliostyle_cmds.append(["vivliostyle-cli", "build", str(pdf_html_out), "-o", str(pdf_out)])

        vivliostyle_errors: list[str] = []
        for cmd in vivliostyle_cmds:
            ok, detail = try_run(cmd)
            if ok and pdf_out.exists():
                pdf_status = "ok (vivliostyle)"
                break
            if detail:
                vivliostyle_errors.append(detail)

        if pdf_status == "skipped" and vivliostyle_errors:
            pdf_status = "未生成（Vivliostyle 尝试失败: " + " | ".join(vivliostyle_errors[:2]) + ")"
        elif pdf_status == "skipped":
            pdf_status = "未生成（缺少 xelatex/lualatex，且未发现可用 Vivliostyle 入口）"

    print(f"MANUSCRIPT={manuscript}")
    print(f"EPUB={epub_out}")
    print(f"HTML={html_out}")
    print(f"PRINT_HTML={pdf_html_out}")
    print(f"PDF={pdf_out if pdf_status.startswith('ok') else pdf_status}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="使用 pandoc 和 Vivliostyle 构建出版文件。")
    parser.add_argument("--project-root", required=True, help="项目根目录")
    parser.add_argument("--config", required=True, help="构建配置 JSON 文件")
    parser.add_argument("--author", default="", help="可选作者名覆盖配置值")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    config_path = Path(args.config).resolve()
    config = load_config(config_path)
    return build_outputs(project_root, config, args.author.strip() or None)


if __name__ == "__main__":
    sys.exit(main())
