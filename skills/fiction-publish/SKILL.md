---
name: fiction-publish
description: 虚构文学出版与发布准备技能。当用户需要构建 epub/html/pdf 出版文件、做发布前核验、校样收口时，触发此 skill。
---

# 出版与发布

## 定位

本 skill 是操作层模块，负责虚构文学作品的出版准备、产物构建和校样收口。

## 功能

### 构建出版产物

运行 `scripts/build_publication_with_pandoc.py --project-root <项目目录> --config <构建配置.json>`：
- 支持平铺章节与分卷目录两种正文结构
- 输出 epub / html / print html / pdf
- 默认样式见 `assets/pandoc-book.css` 和 `assets/vivliostyle-book.css`
- 示例配置见 `assets/publication-build.sample.json`

### 发布前核验

按 `references/模板_发布前最终核对单.md` 和 `references/模板_发布前最终核验.md` 执行：
- 正文完整性检查
- 格式一致性检查
- 设定连续性终检
- 口径统一性检查

### 校样收口

- 校样级问题（错别字、标点、格式）单独处理，不触发正文大修
- 按 `references/模板_编辑修订与投稿检查.md` 执行

## 硬约束

- 当问题已下降到校样、措辞、发布口径层，必须停止正文大修，转入发布收口
- 发布准备时对象粒度升级为"整书/发布资产包对象"
- 改动后必须同步更新日志和变更记录
