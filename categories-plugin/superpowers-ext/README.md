# Superpowers Ext 分类说明

该目录是一个可独立安装的软件开发插件，也可以与 `claude-code-superpowers` 搭配使用。它聚焦具体工程实现层面的补充能力，例如前后端模式、数据库实践、文档检索、安全审查、浏览器验证与部署协作。

## 当前目录功能

- **工程实现与技术资料支持**：提供实现参考、文档检索与问题定位辅助。
- **前后端工程模式**：提供 frontend/backend/postgres 等常见软件开发模式参考。
- **验证与发布辅助**：覆盖浏览器 QA、安全审查、部署观察等研发场景。
- **体验与内容优化**：提供设计系统、SEO 与文档检索能力。
- **专门化执行入口**：提供与上述技能配套的 agents，便于独立使用。

## 设计取舍

- 该目录提供 **skills + agents**，让插件可独立用于常见工程任务。
- 该目录刻意**不包含与 `claude-code-superpowers` 重复的规划、通用代码评审、工作流编排、代码库上手类入口**。
- 该目录**不内置 hooks**，避免复制 ECC 核心脚本依赖，也避免与 `claude-code-superpowers` 的启动类 hooks 职责重叠。
- 与 `categories-plugin/claude-code-superpowers` 搭配时：后者负责通用开发流程与编排，本目录负责软件开发专题能力与专门化执行器。

## Skills 简要说明

- **backend-patterns**：提供 Node.js、Express 和 Next.js API 的后端架构与服务端最佳实践。
- **browser-qa**：用于部署后通过浏览器自动化做界面验证和交互检查。
- **canary-watch**：用于在发布、合并或升级后持续监控线上 URL 的回归问题。
- **click-path-audit**：沿用户点击路径追踪状态变化，定位按钮流程互相抵消或最终状态错误的问题。
- **database-migrations**：提供数据库 schema 变更、数据迁移、回滚与零停机发布实践。
- **deployment-patterns**：提供 CI/CD、Docker、健康检查、回滚与生产发布流程模式。
- **design-system**：用于生成或审查设计系统，并检查视觉一致性。
- **documentation-lookup**：用于查询最新库和框架文档，而不是只依赖训练数据。
- **frontend-design**：用于构建高质量、可上线的前端界面和视觉体验。
- **frontend-patterns**：提供 React、Next.js、状态管理与性能优化等前端开发模式。
- **postgres-patterns**：提供 PostgreSQL 的查询优化、schema 设计、索引与安全实践。
- **security-review**：在认证、输入处理、密钥和敏感功能开发时提供安全检查清单。
- **seo**：用于 SEO 审计、技术优化、结构化数据和搜索可见性改进。

## 组件清单

```json
"agents": [
  "./agents/database-reviewer.md",
  "./agents/docs-lookup.md",
  "./agents/e2e-runner.md",
  "./agents/security-reviewer.md"
],
"skills": [
  "./skills/backend-patterns",
  "./skills/browser-qa",
  "./skills/canary-watch",
  "./skills/click-path-audit",
  "./skills/database-migrations",
  "./skills/deployment-patterns",
  "./skills/design-system",
  "./skills/documentation-lookup",
  "./skills/frontend-design",
  "./skills/frontend-patterns",
  "./skills/postgres-patterns",
  "./skills/security-review",
  "./skills/seo"
]
```
