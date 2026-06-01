# 框架更新机制

管理 skill 层级结构的变更，确保可追溯、可回滚。

## 层级结构

```
knowledge/          知识层：chinese-writing-constraints, narrative-knowledge, review-rubric,
                          market-research, project-governance, intimacy-levels
operations/         操作层：fiction-create, fiction-rewrite, fiction-review, fiction-publish, fiction-import
orchestrator        编排层：fiction-writing-framework/SKILL.md
```

## 更新原则

1. **单一真源**：每个概念只在一个 skill 中定义，其他 skill 通过名字引用
2. **知识层不动流程**：知识层只提供参考材料，不定义执行流程
3. **操作层不动知识**：操作层引用知识层，不内联知识内容
4. **先改源再改引用**：修改知识层内容后，更新所有引用它的操作层

## 变更流程

1. **定位**：确认变更属于哪个层级、哪个 skill
2. **执行**：修改源文件，检查所有引用点
3. **校验**：
   - 断链检查（引用的文件是否存在）
   - SKILL.md 描述是否仍然准确
   - 跨 skill 引用是否正确
4. **记录**：在项目级 `08-operations/change-log/` 中记录（非框架级）

## 回滚

变更导致执行中断时，回滚到上一个可用版本。回滚必须记录原因和范围。
