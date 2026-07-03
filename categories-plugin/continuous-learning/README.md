# Continuous Learning 分类说明

该目录提供持续学习与能力演化相关能力，用于从历史会话和实践中提炼模式、沉淀知识并持续优化。

## 当前目录功能

- **学习闭环**：支持学习、评估、推广与裁剪等演化流程。
- **知识导入导出**：支持 instinct 的导入、导出与状态管理。
- **技能成长**：支持技能创建与项目维度的持续优化。

## Skills 简要说明

- **continuous-learning**：从 Claude Code 会话中自动提炼可复用模式并沉淀为技能。
- **continuous-learning-v2**：基于 instinct 的学习系统，可观察会话并逐步演化为技能、命令或代理。

## 组件清单

```json
"agents": [
  "./skills/continuous-learning-v2/agents/observer.md"
],
"skills": [
  "./skills/continuous-learning",
  "./skills/continuous-learning-v2"
],
"commands": [
  "./commands/evolve.md",
  "./commands/instinct-export.md",
  "./commands/instinct-import.md",
  "./commands/instinct-status.md",
  "./commands/learn-eval.md",
  "./commands/learn.md",
  "./commands/projects.md",
  "./commands/promote.md",
  "./commands/prune.md",
  "./commands/skill-create.md"
]
```
