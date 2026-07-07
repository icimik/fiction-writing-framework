---
name: fiction-writing-framework
description: 虚构文学创作全生命周期编排器。当用户需要走完整创作流程（从立项到出版）、或任务涉及多个阶段时触发。单一任务优先触发对应的原子 skill。
metadata:
  version: 4.0
  author: Kimmy Liu (@kenpusney)
---

# 虚构文学创作框架

本 skill 是路由层。不含领域知识，只负责把任务分发到正确的子 skill。

## Skill 索引

### 概念层（被引用，不直接触发）

| Skill | 职责 |
|-------|------|
| `chinese-writing-constraints` | 中文反翻译腔规则、检查流程、精修方法 |
| `narrative-knowledge` | 叙事理论、结构选型、角色/情节/世界观设计 |
| `review-rubric` | 评审标准、MBTI 读者 personas、评分体系 |
| `market-research` | 市场调研方法论 |
| `intimacy-levels` | 亲密内容分级（L0-L5） |

### 流程层（可独立触发）

| Skill | 触发场景 |
|-------|---------|
| `fiction-create` | 新建项目、续写章节、规划大纲、写样章 |
| `fiction-rewrite` | 改写、精修、中文重塑已有正文 |
| `fiction-review` | 审阅、评审、打分、达标判定 |
| `fiction-publish` | 构建出版文件、发布前核验、校样收口 |
| `fiction-import` | 外部资产导入、融合评估、基线统一 |

### 结构层（被引用，不直接触发）

| Skill | 职责 |
|-------|------|
| `project-structure` | 项目目录规范、编号规则、命名约定 |
| `templates` | 所有文档模板，按用途分类 |
| `project-governance` | 治理机制、协作流程、更新机制、字数统计 |

## 全生命周期

```
立项 → 设定 → 规划 → 样章 → 审阅 → 改写 → 持续生产 → 终稿审阅 → 出版 → 结项
```

| 阶段 | 调用 |
|------|------|
| 立项 | `fiction-create` |
| 设定 | `fiction-create` + `narrative-knowledge` |
| 规划 | `fiction-create` + `narrative-knowledge` |
| 样章 | `fiction-create` + `chinese-writing-constraints` |
| 审阅 | `fiction-review` + `review-rubric` |
| 改写 | `fiction-rewrite` + `chinese-writing-constraints` |
| 持续生产 | `fiction-create` + `chinese-writing-constraints` |
| 终稿审阅 | `fiction-review` + `review-rubric` |
| 出版 | `fiction-publish` |
| 结项 | `project-governance` |

## 核心原则

1. 先保结构，再修表达
2. 过程资产必须沉淀
3. 分阶段裁决，不无限返工
4. 中文表达服从中文习惯
