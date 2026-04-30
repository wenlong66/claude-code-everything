# Common 分类说明

该目录提供跨项目通用能力，覆盖 AI 工程方法、文档处理、搜索研究与多格式文档工作流。

## 当前目录功能

- **工程方法与规范**：提供 AI-first、代码库入门、缓存模式等通用工程技能。
- **研究与检索**：支持深度研究、文档查找与结构化文本处理。
- **文档生产与处理**：支持 PDF、DOCX、XLSX 等常见文档格式工作流。
- **会话型辅助能力**：支持在不同项目中复用的通用命令与代理。

## 组件清单

```json
"agents": [
  "./agents/update-codemaps.md",
  "./agents/update-docs.md"
],
"skills": [
  "./skills/ai-first-engineering",
  "./skills/codebase-onboarding",
  "./skills/content-hash-cache-pattern",
  "./skills/deep-research",
  "./skills/docx",
  "./skills/pdf",
  "./skills/regex-vs-llm-structured-text",
  "./skills/search-first",
  "./skills/xlsx"
],
"commands": [
  "./commands/aside.md",
  "./commands/refactor-clean.md",
  "./commands/resume-session.md",
  "./commands/save-session.md",
  "./commands/sessions.md",
  "./commands/skill-health.md"
]
```