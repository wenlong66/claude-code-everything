# Software 分类说明

该目录提供面向通用软件工程场景的能力集合，覆盖规划、评审、测试、构建修复与研发协作流程。

## 当前目录功能

- **方案规划与编排**：支持任务拆解、执行计划与多步骤编排。
- **质量与安全审查**：提供代码审查、安全审查与语言专项审查。
- **测试与验证**：支持 TDD、E2E 与回归验证工作流。
- **构建与故障修复**：支持构建问题定位与修复。
- **工程辅助自动化**：提供文档更新、代码地图更新与钩子扩展能力。

## 组件清单

```json
"agents": [
  "./agents/architect.md",
  "./agents/build-error-resolver.md",
  "./agents/code-reviewer.md",
  "./agents/database-reviewer.md",
  "./agents/doc-updater.md",
  "./agents/docs-lookup.md",
  "./agents/e2e-runner.md",
  "./agents/planner.md",
  "./agents/python-reviewer.md",
  "./agents/security-reviewer.md",
  "./agents/tdd-guide.md",
  "./agents/typescript-reviewer.md"
],
"skills": [
  "./skills/ai-regression-testing",
  "./skills/algorithmic-art",
  "./skills/api-design",
  "./skills/backend-patterns",
  "./skills/blueprint",
  "./skills/canvas-design",
  "./skills/claude-devfleet",
  "./skills/coding-standards",
  "./skills/cost-aware-llm-pipeline",
  "./skills/database-migrations",
  "./skills/documentation-lookup",
  "./skills/e2e-testing",
  "./skills/frontend-design",
  "./skills/frontend-patterns",
  "./skills/nextjs-turbopack",
  "./skills/postgres-patterns",
  "./skills/python-patterns",
  "./skills/python-testing",
  "./skills/security-review",
  "./skills/security-scan",
  "./skills/seo",
  "./skills/tdd-workflow",
  "./skills/web-artifacts-builder",
  "./skills/webapp-testing"
],
"commands": [
  "./commands/build-fix.md",
  "./commands/code-review.md",
  "./commands/devfleet.md",
  "./commands/e2e.md",
  "./commands/orchestrate.md",
  "./commands/plan.md",
  "./commands/tdd.md",
  "./commands/update-codemaps.md",
  "./commands/update-docs.md"
],
"hooks": [
  "./hooks/hooks.json"
]
```