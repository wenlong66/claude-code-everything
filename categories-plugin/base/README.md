# Base 分类说明

该目录提供插件基础层能力，聚焦通用维护与基础工作流，作为其他分类可复用的底层能力集合。

## 当前目录功能

- **基础命令能力**：提供基础更新命令入口。
- **基础代理能力**：提供文档更新与循环执行相关代理。
- **基础技能能力**：提供文档检索、上下文预算与结构化处理等通用技能。

## 组件清单

```json
"agents": [
  "./agents/doc-updater.md",
  "./agents/loop-operator.md",
  "./agents/refactor-cleaner.md"
],
"skills": [
  "./skills/context-budget",
  "./skills/documentation-lookup",
  "./skills/nutrient-document-processing",
  "./skills/strategic-compact"
],
"commands": [
  "./commands/update-codemaps.md",
  "./commands/update-docs.md"
]
```