---
name: fiction-writing-framework
description: 基于当前 framework 的虚构文学创作执行技能。可从一句话设定启动，完成设定、大纲、样章、评审与迭代闭环。
---

# 虚构文学创作 Skill

## 适用范围
- 从一句话设定启动新项目。
- 生成或重写世界观、角色、分卷大纲、章节样稿。
- 对已有稿件执行评审、改写与复盘。
- 对已有项目与历史材料进行重组后续写。

## 目录分层

- `framework/`：框架层（可执行规范 + 参考文档）。
- `projects/`：项目层（统一目录运行）。
- `archive/legacy/`：历史层（仅追溯）。

## 框架主文档（执行规范）

1. 方法总纲：`framework/01-methods/创作方法总纲.md`
2. 方法库索引：`framework/01-methods/方法库索引.md`
3. Rulebook 分册：`framework/01-methods/rulebook/00.index.md` 到 `framework/01-methods/rulebook/10.shared-review-template.md`
4. Playbook 分册：`framework/01-methods/playbook/README.md`
5. 标准流程：`framework/02-process/标准创作流程.md`
6. 项目结构：`framework/02-process/项目结构模板.md`
7. 文档模板：`framework/03-templates/文档模板集.md`
8. 质量检查：`framework/04-checklists/质量检查清单.md`
9. 复用规则：`framework/05-reusable-rules/可复用规则库.md`
10. 治理机制：`framework/06-governance/项目治理与复盘机制.md`
11. 更新机制：`framework/06-governance/框架更新机制.md`
12. 变更记录：`framework/06-governance/框架变更记录.md`

## 参考文档（镜像与追溯）

1. 创作总指南：`framework/references/methods/全方位虚构文学创作实操指南.md`
2. 大师 Prompt：`framework/references/methods/master-of-story-writing.md`
3. Guide 镜像：`framework/references/guide/00.index.md` 到 `framework/references/guide/10.shared-review-template.md`
4. Workflow 详规：`framework/references/process/workflow.md`

## 快速入口

创作者入口：
1. `framework/02-process/标准创作流程.md`
2. `framework/02-process/项目结构模板.md`
3. `framework/03-templates/文档模板集.md`
4. `framework/04-checklists/质量检查清单.md`

Agent入口：
1. `SKILL.md`
2. `framework/01-methods/方法库索引.md`
3. `framework/02-process/标准创作流程.md`
4. `framework/04-checklists/质量检查清单.md`
5. `framework/02-process/项目结构模板.md`
6. `framework/06-governance/框架更新机制.md`

## 日志要求

每个关键动作必须可追溯：
- 为什么做（设定原因/决策依据）
- 做了什么（变更内容）
- 完成到什么程度（完成度）
- 有什么风险（未决问题）

## 多 Agent 角色

1. Writer（创作 Agent）
- 输出设定、大纲、章节草稿与改稿版本。

2. Editor（编辑 Agent）
- 审阅结构与叙事问题，汇总各方反馈，形成 Writer 可执行改稿清单。

3. Reviewer（评审 Agent）
- 按 Rubric 与检查清单执行规则化评审与问题定位。

4. Reader（读者 Agent）
- 以不同读者画像给出体验反馈（男频、女频、轻小说、现实向等）。

角色操作流程入口：
- `framework/02-process/多Agent操作流程.md`

## 唯一执行入口
1. `framework/02-process/标准创作流程.md`
2. `framework/02-process/项目结构模板.md`
3. `framework/03-templates/文档模板集.md`
4. `framework/04-checklists/质量检查清单.md`

## 输入契约
必填字段：
1. 类型与题材
2. 目标体量（字数或章数）
3. 目标读者
4. 创作目标（新建/续写/重写/审阅）
5. 运行模式（通用创作/网文连载）

一句话启动缺省策略：
- 未给创作目标：默认“新建”。
- 未给类型与题材：按关键词自动归类，无法判定则默认“都市异能”。
- 未给目标读者：默认“18-35 岁网文读者，偏剧情驱动”。
- 平台：默认“待定（按通用创作标准输出，可后置适配）”。
- 更新节奏：默认“每周 3 更”。
- 目标体量：默认“长篇，预计 120 章”。
- 禁用项：默认“无现实敏感映射、无超出设定边界的能力跳变”。

## 标准执行链
1. 阶段0：立项输入与一句话检验（主角-冲突-目标-代价）。
2. 阶段1：设定完善（世界观/角色/阵营/规则手册）。
3. 阶段2：分析与规划（读者画像/市场匹配/分卷大纲/前三章节拍）。
4. 阶段3：样章验证（前3章 + 样章评审）。
5. 阶段4：反馈迭代（反馈归类 + 变更记录 + 工作日志）。
6. 阶段5：持续生产（章节产出 + 章节质检）。
7. 阶段6：周期复盘（周/月/N章/分卷）。

## 多 Agent 协作循环
1. Writer 先产出当轮稿件（设定/大纲/章节）。
2. Reviewer 使用 `framework/03-templates/模板_Reviewer评审单.md` 产出规则评审单（评分 + 问题清单 + 严重级别）。
3. Reader 产出读者反馈单（爽点、节奏、代入感、弃读风险）。
4. Editor 汇总 Reviewer + Reader 结果，形成改稿优先级（P0/P1/P2）。
5. Writer 按优先级改稿并回传。
6. Editor 验收通过后进入下一轮；未通过则回到第4步。

## 联动更新强约束（Writer 必做）

当发生以下任一改动：
- 新增章节
- 修改大纲
- 修改设定

必须同步更新：
- `03-foundation/角色设定.md`
- `03-foundation/世界观设定.md`
- `03-foundation/阵营设定.md`
- `08-operations/change-log/变更记录_*.md`
- `08-operations/logs/工作日志_*.md`

执行模板：`framework/03-templates/模板_联动更新清单.md`

## 变更粒度与写作纪律（硬规则）

1. 单次只允许变更一个对象：
- 章节 / 大纲 / 设定 三选一。
- 完成联动更新并通过 Reviewer、Reader、Editor 后，才可进入下一对象。

2. 单章节重写必须整章重写：
- 禁止仅做局部查找替换。
- 禁止仅在原文末尾追加段落代替重写。

3. 禁止创建 bak 副本：
- 不通过复制 `.bak`、`_old` 等方式保存正文版本。
- 历史恢复依赖设定文档、大纲、变更记录、日志与评审记录重建。

4. 生成后强制质检：
- 严格检查字数与格式约束。
- 检查叙述风格、视角稳定、节奏一致。
- 检查编码与字符问题（乱码、异常符号、不可见异常字符）。

## 新项目与既有项目双模式

1. 新项目模式
- Editor + Writer 联合做选题分析（市场匹配、差异化、可持续性）后再立项。

2. 既有项目模式
- 先按 `framework/02-process/项目结构模板.md` 重组历史材料。
- 再按标准执行链接入多 Agent 协作，继续创作与迭代。

## 方法与模板调用顺序
1. 方法内核：`framework/01-methods/方法库索引.md`
2. Rulebook：`framework/01-methods/rulebook/00.index.md`
3. 阶段分册：`framework/01-methods/playbook/README.md`
4. 模板入口：`framework/03-templates/文档模板集.md`
5. 多Agent流程：`framework/02-process/多Agent操作流程.md`
6. Reader角色模板：`framework/03-templates/模板_Reader读者角色卡.md`

## 最小交付（MVP）
1. 一页式世界观
2. 三角色卡 + 关系矩阵
3. 10 章节拍大纲
4. 1 章样章

## 验收标准（Rubric）
- 规则一致性
- 角色驱动性
- 情节因果性
- 叙事有效性
- 语言可读性

建议阈值：
- 通用创作：平均分 >= 3.5
- 网文连载：平均分 >= 3.5 且章节钩子强度 >= 4

## 输出约束
- 输出必须为中文。
- 每次输出包含：输入摘要、执行链路、产出清单、下一步动作。
- 改动后必须同步更新：日志、反馈、变更、复盘。
- Editor 必须在每轮输出“汇总反馈 -> 改稿指令 -> 验收结论”三段式结果。
- Editor 汇总必须使用：`framework/03-templates/模板_Editor汇总与改稿指令.md`。
- Editor 每条关键结论必须引用信息来源；P0 项必须至少引用 2 个来源（Reviewer + Reader）。
- Reader 反馈必须声明所用角色卡（可多选）并给出对应评价倾向。
