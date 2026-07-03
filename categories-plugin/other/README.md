# Other 分类说明

该目录提供通用补充能力与跨领域实验性工作流，作为核心与垂直分类之外的扩展集合。

## 当前目录功能

- **通用扩展技能**：收纳跨场景但不归属单一分类的能力。
- **辅助命令入口**：提供轻量命令用于循环与评估等任务。
- **实验性能力容器**：便于快速试验并沉淀到正式分类。

## Skills 简要说明

- **claude-api**：提供 Claude API 与 Anthropic SDK 的集成模式和开发实践。
- **enterprise-agent-ops**：用于长期运行 agent 的观测、边界控制与生命周期管理。
- **eval-harness**：为 Claude Code 会话提供正式评测框架，支持 EDD 评估流程。
- **finance-billing-ops**：用于收入、定价、退款和团队计费等账单问题的证据化分析。
- **investor-materials**：用于创建和维护 pitch deck、一页纸、投资备忘录和财务模型等融资材料。
- **investor-outreach**：用于撰写投资人冷邮件、暖介绍、跟进和更新类沟通内容。
- **liquid-glass-design**：提供 iOS 26 Liquid Glass 风格的设计系统与实现参考。
- **market-research**：用于市场研究、竞品分析、尽调和决策支持型行业调研。
- **mcp-server-patterns**：提供基于 Node/TypeScript SDK 的 MCP Server 构建模式。
- **openclaw-persona-forge**：用于为 OpenClaw 生成完整角色设定、SOUL.md 和头像提示词。
- **product-lens**：在开工前验证产品动机、诊断方向并检查需求是否成立。
- **project-guidelines-example**：提供项目专用 skill 的示例模板，便于按项目复制和改造。

## 组件清单

```json
"skills": [
  "./skills/claude-api",
  "./skills/enterprise-agent-ops",
  "./skills/eval-harness",
  "./skills/finance-billing-ops",
  "./skills/investor-materials",
  "./skills/investor-outreach",
  "./skills/liquid-glass-design",
  "./skills/market-research",
  "./skills/mcp-server-patterns",
  "./skills/openclaw-persona-forge",
  "./skills/product-lens",
  "./skills/project-guidelines-example"
],
"commands": [
  "./commands/eval.md",
  "./commands/loop-start.md",
  "./commands/loop-status.md"
]
```
