---
name: fiction-writing-framework
description: 虚构文学创作全生命周期编排器。当用户需要走完整创作流程（从立项到出版）、或任务涉及多个阶段（如创作+审阅+改写+出版）时，触发此 skill。单一任务（只改写、只审阅、只出版）优先触发对应的原子 skill。
metadata:
  version: 3.0
  author: Kimmy Liu (@kenpusney)
---

# 虚构文学创作框架（编排器）

## 定位

本 skill 是虚构文学创作的全生命周期编排器。它不直接执行创作任务，而是按阶段调用原子 skill 完成完整流程。

## Skill 索引

### 操作层（可独立触发）

| Skill | 用途 | 触发场景 |
|-------|------|---------|
| `fiction-create` | 创作 | 新建项目、续写章节、规划大纲、写样章 |
| `fiction-rewrite` | 改写 | 精修、润色、中文重塑已有正文 |
| `fiction-review` | 审阅 | 系统评审、MBTI 读者反馈、量化评分、达标判定 |
| `fiction-publish` | 出版 | 字数统计、构建产物、发布前核验、校样收口 |
| `fiction-import` | 导入 | 外部资产融合评估、重写归并、基线统一 |

### 知识层（被操作层引用，不直接触发）

| Skill | 用途 | 主要内容 |
|-------|------|---------|
| `chinese-writing-constraints` | 中文生成约束 | 反翻译腔规则、三阶段检查、语言规格 |
| `narrative-knowledge` | 叙事知识库 | 结构工具箱、角色、情节、世界观、修辞、类型、审阅方法论 |
| `review-rubric` | 评审标准 | 评分轴、MBTI personas、评审模板、检查清单 |
| `market-research` | 市场调研 | 网文趋势、日本轻小说市场 |
| `project-governance` | 项目治理 | 阶段流程、协作模式、项目结构、变更机制 |
| `intimacy-levels` | 亲密分级 | L0-L5 分级定义、高级指南 |

## 全生命周期流程

```
立项 → 导入融合 → 规划 → 样章 → 审阅 → 改写 → 持续生产 → 周期复盘 → 终稿审阅 → 出版准备
```

### 阶段与 Skill 映射

| 阶段 | 调用 Skill | 产出 |
|------|-----------|------|
| 0. 立项 | fiction-create | 前提句、世界观框架、角色设定、结构选型 |
| 1. 导入融合 | fiction-import | 融合评估报告、基线统一 |
| 2. 规划 | fiction-create | 分卷大纲、章节规划、伏笔台账 |
| 3. 样章 | fiction-create | 样章草稿 |
| 4. 样章评审 | fiction-review | 评审报告、修订清单 |
| 5. 改稿 | fiction-rewrite | 改写后的章节 |
| 6. 持续生产 | fiction-create | 章节批次 |
| 7. 周期复盘 | fiction-review | 复盘报告 |
| 8. 整书精修 | fiction-rewrite | 精修后的全文 |
| 9. 终稿评审 | fiction-review | 终稿评审报告、达标判定 |
| 10. 出版准备 | fiction-publish | epub/html/pdf 产物、校样 |

## 核心原则

1. **先保结构，再修表达**：任何精修先确认叙事任务，再动句子
2. **过程资产必须沉淀**：每一轮都要留下可追溯的文档资产
3. **分阶段裁决，不无限返工**：样章期允许大改，终稿期以收口为主
4. **中文表达服从中文习惯**：不把"译得通"当成"写得像中文"

## 输入契约

必填字段：类型与题材、目标体量、目标读者、创作目标、运行模式。

一句话启动缺省策略：未给目标则询问用户；未给类型则按关键词归类，无法判定则询问用户。

## 多 Agent 协作

- Writer → fiction-create / fiction-rewrite
- Editor → fiction-review（整合输出）
- Reviewer → fiction-review（规则化评审）
- Reader → fiction-review（MBTI 反馈）

详细流程见 `project-governance` 的 references/collaboration.md。
