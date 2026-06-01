# 标准创作流程

本文件是执行层唯一流程入口。详细阶段定义见 `stage-details.md`，停改与收口规则见 `workflow-rules.md`。

## 运行契约

角色分工：
- Writer：负责创作与改稿落地。
- Editor：负责编辑审阅、反馈汇总、改稿指令、停改裁决与阶段验收。
- Reviewer：负责规则化评审与质量打分。
- Reader：负责多读者画像反馈，包括单章体验、整书连读体验与渠道感知。

协作扩展：见 `project-governance` 的 references/collaboration.md。

执行硬规则：
- 生成任何中文正文前，必须已读 `chinese-writing-constraints` 的 references/language/中文生成约束.md，并执行三阶段检查。
- 单次只允许变更一个对象：章节 / 大纲 / 设定（三选一）。
- 单章节改写必须整章重写，不得以查找替换或末尾追加代替。
- 禁止创建 `.bak` 或同类正文副本。
- 每次生成后必须完成字数、格式、风格、视角、节奏、编码检查。

运行模式：
- 通用创作模式：短中长篇、非日更、样章或全稿改写。
- 网文连载模式：日更/周更、市场验证与反馈循环强约束。
- 短篇小说集模式：多篇共享世界观、强调横向统一与纵向差异。

必填输入：类型与题材、目标体量、目标读者、创作目标、运行模式。

缺省策略：未给目标默认"新建"；未给类型按关键词归类，无法判定则询问用户；未给读者则询问用户。

## 标准执行链

1. 阶段 0：立项输入
2. 导入融合前置流程
3. 阶段 1：设定完善
4. 阶段 2：分析与规划
5. 阶段 3：样章验证
6. 阶段 4：反馈迭代
7. 阶段 5：持续生产
8. 阶段 6：周期复盘
9. 阶段 7：整书审读与中文表达精修
10. 阶段 7b：中文重塑（条件触发，非必经）
11. 阶段 8：终稿级多方评审与发布裁决
12. 阶段 9：发布准备 / 校样准备
13. 阶段 10：结项复盘与框架反哺

各阶段详细定义见 `stage-details.md`。停改规则、质量门槛、异常处理见 `workflow-rules.md`。

## 参考入口

1. 领域分册：`narrative-knowledge` 的 references/
2. 项目结构模板：`project-governance` 的 references/project-structure.md
3. 文档模板集：`fiction-create` 的 references/templates-README.md
4. 多 Agent 操作流程：`project-governance` 的 references/collaboration.md
5. 质量检查清单：`review-rubric` 的 references/checklists.md
6. 中文生成约束：`chinese-writing-constraints` 的 references/language/中文生成约束.md
