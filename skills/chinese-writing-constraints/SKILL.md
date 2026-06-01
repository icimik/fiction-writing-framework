---
name: chinese-writing-constraints
description: 中文虚构文学生成的核心语言约束。当需要生成、改写或精修任何中文小说正文时，必须先读取此 skill。包含反翻译腔规则、三阶段检查流程和详细模式清单。
---

# 中文生成约束

## 定位

知识层模块，为 fiction-create、fiction-rewrite、fiction-review 提供中文语言规格。

## 核心问题

LLM 的中文输出默认带有翻译腔——内部推理以英语逻辑组织句子，再用中文词汇填充。句子逻辑正确，但不像中文母语者会写的文字。不能只靠事后精修解决，必须在生成环节施加结构性约束。

## 执行要求

1. 生成任何中文正文前，必须已读 `references/language/anti-patterns.md` 和 `references/language/checking-process.md`
2. 精修阶段必须已读 `references/language/refine-methods.md`
3. 不可以"事后精修会处理"为由跳过生成环节的约束

## 参考文档

| 文档 | 内容 |
|------|------|
| `references/language/中文生成约束.md` | 总览与执行入口 |
| `references/language/anti-patterns.md` | 12 种反翻译腔模式 + 正面特征 + 伪高级句式清单 |
| `references/language/checking-process.md` | 三阶段检查流程 + 快速自检 8 问 |
| `references/language/refine-methods.md` | 重述法、锚文本法、分层法、删减法 |
| `references/language/现代汉语_词汇规范.md` | 语言学参考 |
| `references/language/现代汉语_语法规范.md` | 语言学参考 |
| `references/language/现代汉语_修辞规范.md` | 语言学参考 |
