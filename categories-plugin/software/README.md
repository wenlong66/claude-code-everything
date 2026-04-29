# Software 分类说明

该目录提供面向通用软件工程场景的能力集合，覆盖从需求规划、测试驱动开发、代码审查到构建修复的完整开发流程。

## 当前目录功能

- **规划与设计**：通过 `planner` 等组件支持实现方案拆解与执行计划制定。
- **质量保障**：通过 `code-reviewer`、`security-reviewer`、`typescript-reviewer` 提供代码质量与安全审查能力。
- **测试与验证**：通过 `tdd-guide`、`e2e-runner` 等能力支持测试驱动与端到端验证。
- **构建与修复**：通过 `build-error-resolver` 等能力定位并修复构建问题。
- **命令化工作流**：提供 `/plan`、`/tdd`、`/code-review`、`/build-fix` 等命令入口，便于直接触发流程。

## 组件清单

```json
"agents": [
  "./agents/architect.md",
  "./agents/build-error-resolver.md",
  "./agents/code-reviewer.md",
  "./agents/database-reviewer.md",
  "./agents/e2e-runner.md",
  "./agents/planner.md",
  "./agents/security-reviewer.md",
  "./agents/tdd-guide.md",
  "./agents/typescript-reviewer.md"
],
"skills": [
  "./skills/ai-regression-testing",
  "./skills/algorithmic-art",
  "./skills/api-design",
  "./skills/backend-patterns",
  "./skills/canvas-design",
  "./skills/claude-devfleet",
  "./skills/coding-standards",
  "./skills/database-migrations",
  "./skills/e2e-testing",
  "./skills/frontend-design",
  "./skills/frontend-patterns",
  "./skills/nextjs-turbopack",
  "./skills/postgres-patterns",
  "./skills/security-review",
  "./skills/security-scan",
  "./skills/tdd-workflow",
  "./skills/web-artifacts-builder",
  "./skills/webapp-testing"
],
"commands": [
  "./commands/build-fix.md",
  "./commands/code-review.md",
  "./commands/devfleet.md",
  "./commands/e2e.md",
  "./commands/gradle-build.md",
  "./commands/orchestrate.md",
  "./commands/plan.md",
  "./commands/tdd.md"
]
```