---
name: fiction-create
description: 虚构文学创作执行技能。当用户要从零启动新项目、续写章节、规划大纲、生成世界观和角色设定、写样章时，触发此 skill。
---

# 创作

## 定位

操作层模块，负责虚构文学的创作执行。从一句话设定启动，完成设定、大纲、样章与持续生产。

## 执行流程

### 1. 读取约束

- **必读**：`chinese-writing-constraints`（涉及中文正文生成时，不可跳过）
- **必读**：`project-governance` 的 references/stages.md（阶段流程）
- **按需**：`narrative-knowledge`、`intimacy-levels`、`market-research`

### 2. 输入契约

必填：类型与题材、目标体量、目标读者、创作目标、运行模式。

缺省策略：未给目标默认"新建"；未给类型按关键词归类，无法判定则询问用户；未给读者则询问用户。

### 3. 阶段执行

按 `project-governance` 的 references/stage-details.md 执行。关键阶段：

- **阶段 0 — 立项**：前提句 → 世界观框架 → 角色设定 → 结构选型
- **阶段 1 — 规划**：分卷大纲 → 章节规划 → 伏笔台账
- **阶段 2 — 样章**：写样章 → 三方审阅
- **阶段 3+ — 持续生产**：按批次写章节 → 周期复盘

### 4. 输出要求

- 输出必须为中文
- 每次输出至少交代：输入摘要、当前阶段、产出清单、下一步动作

## 参考文档

- `references/templates-README.md` — 文档模板索引
- 创作模板见 `references/` 目录
