# Base 分类说明

该目录提供插件基础层能力，聚焦通用维护与基础工作流，作为其他分类可复用的底层能力集合。

## 当前目录功能

- **基础命令能力**：提供基础更新命令入口。
- **基础代理能力**：提供文档更新与循环执行相关代理。
- **基础技能能力**：提供文档检索、上下文预算与结构化处理等通用技能。

## Skills 简要说明

- **ai-first-engineering**：提供 AI 产出占比较高团队的工程协作与交付模式。
- **ck**：提供项目级持久记忆、会话跟踪与上下文自动加载能力。
- **codebase-onboarding**：快速分析陌生代码库并生成上手指南、结构图和初始 CLAUDE.md。
- **content-hash-cache-pattern**：用内容哈希缓存昂贵处理结果，文件变化后自动失效。
- **context-budget**：审计 Claude Code 的上下文消耗，定位冗余并给出压缩建议。
- **council**：用四视角 council 讨论模糊决策与方案取舍。
- **knowledge-ops**：管理知识库的导入、整理、去重、同步与检索。
- **regex-vs-llm-structured-text**：帮助判断结构化文本该用正则还是 LLM 解析。
- **search-first**：编码前先搜索现有工具、库和实现模式的研究流程。

## 组件清单

```json
"agents": [
  "./agents/doc-updater.md",
  "./agents/loop-operator.md",
  "./agents/refactor-cleaner.md"
],
"skills": [
  "./skills/ai-first-engineering",
  "./skills/ck",
  "./skills/codebase-onboarding",
  "./skills/content-hash-cache-pattern",
  "./skills/context-budget",
  "./skills/council",
  "./skills/knowledge-ops",
  "./skills/regex-vs-llm-structured-text",
  "./skills/search-first"
],
"commands": [
  "./commands/update-codemaps.md",
  "./commands/update-docs.md"
]
```
