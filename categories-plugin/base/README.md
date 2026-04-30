# Core 分类说明

该目录提供跨场景通用能力，主要用于文档检索、研究、上下文管理、会话管理与维护类工作流。

## 当前目录功能

- **文档与知识检索**：支持基于外部文档源的查询、总结与引用。
- **研究与分析**：提供深度研究、迭代检索、成本与上下文分析等能力。
- **维护与运营**：支持文档更新、重构清理、周期性任务与会话管理。
- **通用命令入口**：提供 `/docs`、`/update-docs`、`/sessions` 等核心命令化入口。

## 组件清单

```json
"agents": [
  "./agents/doc-updater.md",
  "./agents/docs-lookup.md",
  "./agents/loop-operator.md",
  "./agents/refactor-cleaner.md"
],
"skills": [
  "./skills/ai-first-engineering",
  "./skills/blueprint",
  "./skills/codebase-onboarding",
  "./skills/content-hash-cache-pattern",
  "./skills/context-budget",
  "./skills/cost-aware-llm-pipeline",
  "./skills/deep-research",
  "./skills/documentation-lookup",
  "./skills/iterative-retrieval",
  "./skills/market-research",
  "./skills/nutrient-document-processing",
  "./skills/regex-vs-llm-structured-text",
  "./skills/search-first",
  "./skills/strategic-compact"
],
"commands": [
  "./commands/aside.md",
  "./commands/build-fix.md",
  "./commands/gradle-build.md",
  "./commands/refactor-clean.md",
  "./commands/resume-session.md",
  "./commands/save-session.md",
  "./commands/sessions.md",
  "./commands/skill-health.md",
  "./commands/update-codemaps.md",
  "./commands/update-docs.md"
]
```