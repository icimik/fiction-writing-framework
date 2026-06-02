---
name: fiction-publish
description: 虚构文学出版与发布准备。当用户需要构建 epub/html/pdf 出版文件、做发布前核验、校样收口时触发。
---

# 出版

流程层模块。出版准备、产物构建、校样收口。

## 构建出版产物

运行 `scripts/build_publication_with_pandoc.py --project-root <项目目录> --config <构建配置.json>`：
- 支持平铺章节与分卷目录
- 输出 epub / html / print html / pdf
- 样式见 `assets/`，配置示例见 `assets/publication-build.sample.json`

## 发布前核验

按 `templates` 的 references/发布/ 下的模板执行：
- 正文完整性、格式一致性、设定连续性、口径统一性

## 校样收口

校样级问题（错别字、标点、格式）单独处理，不触发正文大修。

## 硬约束

- 问题降到校样/措辞/口径层时，停止正文大修
- 发布准备时对象粒度升级为整书/发布资产包
