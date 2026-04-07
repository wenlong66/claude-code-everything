# CLAUDE Code Everything (personal)

对原仓库内容做了自己大概会用的内容精简，保留核心能力与可扩展分类目录。

## 分类与目录说明（按分类目录直接复制）

```
core/                核心基座（默认基础能力）
  skills/            核心技能
  agents/            核心代理
  commands/          核心命令
categories/          按分类整理后的可复制目录
  framework-language/
    ts-js/           TypeScript/JavaScript
    python/
    docker/
    go/
    cpp/
    flutter/
    django/
    springboot/
  business-content/  业务/内容
    skills/
    agents/
    commands/
  research-api/      研究/检索/API
    skills/
    agents/
    commands/
  media-ai/          媒体/AI
    skills/
    agents/
    commands/
  continuous-learning/  持续学习（自定义）
    skill/
    commands/
  social-ai/         社交 AI（自定义）
    skills/
    agents/
  other/             其他技能
    skills/
    agents/
    commands/
skills/              扩展技能库（原始来源）
agents/              扩展代理库（原始来源）
commands/            扩展命令库（原始来源）
rules/               规则层（common + language）
zh-CN/               中文镜像与说明
hooks/               hooks 示例与配置
mcp-configs/         MCP 配置示例
.claude/             本地运行配置（非安装源）
```

### 分类（来自 core/skills/configure-ecc）

- **框架与语言**：TypeScript/JavaScript、Python、Docker、Go、C++、Flutter、Django、Springboot
- **工作流与质量**：TDD / E2E / 评估 / 安全审查等通用质量流程
- **业务与内容**：市场研究、投资材料、写作与对外沟通
- **研究与 API**：深度研究、Exa 搜索、Claude API
- **媒体与 AI**：图像/视频/音频等生成与处理
- **独立技能**：项目模板与设计范式（如 project-guidelines-example、liquid-glass-design、mcp-server-patterns）

## 分类使用方式

- **核心能力**：优先从 `core/` 复制到目标环境（稳定、通用）。
- **分类复制**：从 `categories/<分类>/skills|agents|commands`（或 `categories/<分类>/<子类>/skills|agents|commands`）直接复制。
- **原始来源**：`skills/agents/commands` 保留为原始库，便于溯源。
- **自定义分类**：如 `categories/continuous-learning/`（`skill/` + `commands/`）、`categories/social-ai/`（`skills/` + `agents/`）。

## 示例场景

### 场景 1：做网页 + App
- 复制：
  - `categories/framework-language/ts-js/skills|agents|commands`
  - `categories/framework-language/flutter/skills|agents|commands`
- 视需求叠加：`categories/workflow-quality/skills|agents|commands`

### 场景 2：Python 作为服务端
- 复制：`categories/framework-language/python/skills|agents|commands`
- 可叠加：`categories/framework-language/django/skills/`
- 视需求叠加：`categories/workflow-quality/skills|agents|commands`

### 场景 3：Go 作为服务端
- 复制：`categories/framework-language/go/skills|agents|commands`
- 视需求叠加：`categories/workflow-quality/skills|agents|commands`

## 设计目标

- 使用“目录即分类”的思路，避免维护冗长的手工映射表。
- 让实际使用时更接近“选目录 → 复制 → 即用”。
