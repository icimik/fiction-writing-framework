#!/usr/bin/env python3

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys
from dataclasses import dataclass


CHINESE_CHAR_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
ENGLISH_WORD_RE = re.compile(r"[A-Za-z]+(?:[A-Za-z0-9'_-]*[A-Za-z0-9]+)?")
TITLE_RE = re.compile(r"^\s{0,3}#{1,6}\s+")
HORIZONTAL_RULE_RE = re.compile(r"^\s{0,3}(?:[-*_])(?:\s*[-*_]){2,}\s*$")
META_LINE_RE = re.compile(
    r"^\s*(?:[-*+]\s*)?(?:备注|注|附注|尾注|后记|跋|作者有话说|作者的话|PS|P\.S\.)[:：]"
)
FRONT_MATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|$)", re.DOTALL)


@dataclass
class FileStat:
    path: pathlib.Path
    chinese_chars: int
    english_words: int

    @property
    def total_words(self) -> int:
        return self.chinese_chars + self.english_words


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "统计作品正文字数：每个中文字符算 1 字，每个英文单词算 1 字，标点不计。"
        )
    )
    parser.add_argument("project_dir", help="项目目录，或直接指向正文目录")
    parser.add_argument(
        "--include-samples",
        action="store_true",
        help="同时统计 07-writing/samples/ 下的样稿",
    )
    parser.add_argument(
        "--extensions",
        nargs="+",
        default=[".md", ".txt"],
        help="要统计的文件扩展名，默认 .md .txt",
    )
    return parser.parse_args()


def resolve_text_roots(project_dir: pathlib.Path, include_samples: bool) -> list[pathlib.Path]:
    if not project_dir.exists():
        raise FileNotFoundError(f"路径不存在: {project_dir}")

    if project_dir.is_file():
        return [project_dir]

    writing_dir = project_dir / "07-writing"
    chapters_dir = writing_dir / "chapters"
    samples_dir = writing_dir / "samples"

    if chapters_dir.exists():
        roots = [chapters_dir]
        if include_samples and samples_dir.exists():
            roots.append(samples_dir)
        return roots

    return [project_dir]


def iter_text_files(roots: list[pathlib.Path], extensions: set[str]) -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for root in roots:
        if root.is_file():
            if root.suffix.lower() in extensions:
                files.append(root)
            continue
        for path in sorted(root.rglob("*")):
            if path.is_file() and path.suffix.lower() in extensions:
                files.append(path)
    return sorted(files, key=natural_sort_key)


def natural_sort_key(path: pathlib.Path) -> list[object]:
    parts = []
    for chunk in re.split(r"(\d+)", str(path)):
        if chunk.isdigit():
            parts.append(int(chunk))
        else:
            parts.append(chunk)
    return parts


def strip_non_body_lines(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    text = FRONT_MATTER_RE.sub("", text, count=1)

    lines = []
    in_code_block = False
    for line in text.split("\n"):
        stripped = line.strip()

        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if TITLE_RE.match(line):
            continue
        if HORIZONTAL_RULE_RE.match(line):
            continue
        if META_LINE_RE.match(line):
            continue
        lines.append(line)

    return "\n".join(lines)


def count_words(text: str) -> tuple[int, int]:
    body = strip_non_body_lines(text)
    chinese_chars = len(CHINESE_CHAR_RE.findall(body))
    english_words = len(ENGLISH_WORD_RE.findall(body))
    return chinese_chars, english_words


def format_rel_path(base: pathlib.Path, path: pathlib.Path) -> str:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def main() -> int:
    args = parse_args()
    project_dir = pathlib.Path(args.project_dir).resolve()
    roots = resolve_text_roots(project_dir, args.include_samples)
    extensions = {ext.lower() if ext.startswith(".") else f".{ext.lower()}" for ext in args.extensions}
    files = iter_text_files(roots, extensions)

    if not files:
        print("未找到可统计的正文文件。", file=sys.stderr)
        return 1

    stats: list[FileStat] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        chinese_chars, english_words = count_words(text)
        stats.append(
            FileStat(
                path=path,
                chinese_chars=chinese_chars,
                english_words=english_words,
            )
        )

    total_chinese = sum(item.chinese_chars for item in stats)
    total_english = sum(item.english_words for item in stats)
    total_words = total_chinese + total_english
    volume_summary: collections.OrderedDict[str, dict[str, int]] = collections.OrderedDict()
    for item in stats:
        volume = item.path.parent.name
        if volume not in volume_summary:
            volume_summary[volume] = {
                "files": 0,
                "chinese_chars": 0,
                "english_words": 0,
                "total_words": 0,
            }
        volume_summary[volume]["files"] += 1
        volume_summary[volume]["chinese_chars"] += item.chinese_chars
        volume_summary[volume]["english_words"] += item.english_words
        volume_summary[volume]["total_words"] += item.total_words

    print(f"统计范围: {project_dir}")
    print("规则: 中文字符=1字, 英文单词=1字, 标点不计")
    print(f"文件数: {len(stats)}")
    print(f"中文字符: {total_chinese}")
    print(f"英文单词: {total_english}")
    print(f"总字数: {total_words}")
    print("")
    print("分目录汇总:")
    for volume, data in volume_summary.items():
        print(
            f"{volume}\t文件数={data['files']}\t总字数={data['total_words']}\t"
            f"中文={data['chinese_chars']}\t英文={data['english_words']}"
        )
    print("")
    print("分文件明细:")
    for item in stats:
        rel_path = format_rel_path(project_dir, item.path)
        print(
            f"{rel_path}\t总字数={item.total_words}\t中文={item.chinese_chars}\t英文={item.english_words}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
