---
name: project-governance
description: 虚构文学项目的治理机制。当需要了解阶段流程、多 Agent 协作模式、框架更新机制或统计字数时，读取此 skill。
---

# 项目治理

结构层模块。阶段流程、协作模式、更新机制、字数统计。

## 参考文档

| 文档 | 内容 |
|------|------|
| `references/stages.md` | 标准创作流程（执行入口） |
| `references/stage-details.md` | 阶段详细定义 |
| `references/workflow-rules.md` | 停改规则、周期机制、异常处理 |
| `references/collaboration.md` | 多 Agent 协作流程 |
| `references/update-mechanism.md` | 框架更新机制 |

## 字数统计

运行 `scripts/count_manuscript_words.py <项目目录>`：
- 默认统计 `07-writing/chapters/`
- 中文字符算 1 字，英文单词算 1 字，标点不计
- 用于体量核验、续写前评估、终稿确认
