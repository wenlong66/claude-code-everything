# Software 分类说明

该目录提供面向通用软件工程场景的能力集合，覆盖规划、评审、测试、构建修复与研发协作流程。

## 当前目录功能

- **方案规划与编排**：支持任务拆解、执行计划与多步骤编排。
- **质量与安全审查**：提供代码审查、安全审查与语言专项审查。
- **测试与验证**：支持 TDD、E2E 与回归验证工作流。
- **构建与故障修复**：支持构建问题定位与修复。
- **工程辅助自动化**：提供文档更新、代码地图更新与钩子扩展能力。

## Skills 简要说明

- **ai-regression-testing**：提供面向 AI 辅助开发场景的回归测试策略和盲点补漏方法。
- **algorithmic-art**：用于用 p5.js 创作算法艺术、生成式图形和交互式视觉作品。
- **api-design**：提供 REST API 的命名、分页、错误响应、版本化与限流设计模式。
- **backend-patterns**：提供 Node.js、Express 和 Next.js API 的后端架构与服务端最佳实践。
- **blueprint**：把一句目标拆成可跨会话、跨代理执行的分步实施蓝图。
- **canvas-design**：用于生成海报、艺术图和静态视觉设计作品。
- **claude-devfleet**：用于规划项目、并行派发代理并监控多代理编码任务。
- **coding-standards**：提供 TypeScript、JavaScript、React 和 Node.js 的通用编码规范。
- **cost-aware-llm-pipeline**：提供 LLM 调用的成本控制、模型路由、重试与缓存模式。
- **database-migrations**：提供数据库 schema 变更、数据迁移、回滚与零停机发布实践。
- **documentation-lookup**：用于查询最新库和框架文档，而不是只依赖训练数据。
- **e2e-testing**：提供 Playwright E2E 测试、页面对象和 CI 集成模式。
- **frontend-design**：用于构建高质量、可上线的前端界面和视觉体验。
- **frontend-patterns**：提供 React、Next.js、状态管理与性能优化等前端开发模式。
- **nextjs-turbopack**：聚焦 Next.js 16+ 与 Turbopack 的增量构建和调试体验优化。
- **postgres-patterns**：提供 PostgreSQL 的查询优化、schema 设计、索引与安全实践。
- **python-patterns**：提供 Pythonic 写法、类型标注和可维护实现模式。
- **python-testing**：提供 pytest、fixture、mock、参数化与覆盖率导向的测试方法。
- **security-review**：在认证、输入处理、密钥和敏感功能开发时提供安全检查清单。
- **security-scan**：扫描 `.claude/` 配置中的安全漏洞、错误配置和注入风险。
- **seo**：用于 SEO 审计、技术优化、结构化数据和搜索可见性改进。
- **tdd-workflow**：在新功能、修 bug 和重构时提供测试驱动开发流程。
- **web-artifacts-builder**：用于构建复杂的 Claude HTML artifact，适合多组件和有状态界面。
- **webapp-testing**：用 Playwright 交互测试本地 Web 应用，支持截图、日志和行为验证。

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
