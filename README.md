# Fiction Writing Framework

虚构文学创作全生命周期编排器。从立项到出版的完整创作流程管理。

## 安装

```bash
npx skills add icimik/fiction-writing-framework --skill '*'
```

## Skill 一览

| Skill | 层级 | 职责 |
|-------|------|------|
| `fiction-writing-framework` | 编排层 | 全生命周期路由，任务分发到子 skill |
| `fiction-create` | 流程层 | 新建项目、续写章节、规划大纲、写样章 |
| `fiction-rewrite` | 流程层 | 改写、精修、中文重塑已有正文 |
| `fiction-review` | 流程层 | 审阅、评审、打分、达标判定 |
| `fiction-publish` | 流程层 | 构建出版文件、发布前核验、校样收口 |
| `fiction-import` | 流程层 | 外部资产导入、融合评估、基线统一 |
| `chinese-writing-constraints` | 知识层 | 中文反翻译腔规则、检查流程、精修方法 |
| `narrative-knowledge` | 知识层 | 叙事理论、结构选型、角色/情节/世界观设计 |
| `review-rubric` | 知识层 | 评审标准、MBTI 读者 personas、评分体系 |
| `market-research` | 知识层 | 市场调研方法论 |
| `intimacy-levels` | 知识层 | 亲密内容分级（L0-L5） |
| `project-structure` | 结构层 | 项目目录规范、编号规则、命名约定 |
| `templates` | 结构层 | 所有文档模板，按用途分类 |
| `project-governance` | 结构层 | 治理机制、协作流程、更新机制、字数统计 |

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
