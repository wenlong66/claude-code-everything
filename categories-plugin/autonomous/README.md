# Autonomous 分类说明

该目录提供自动化与自驱执行相关能力，面向持续运行、评估闭环与质量闸门场景。

## 当前目录功能

- **自动化循环**：支持定时或持续执行任务循环。
- **评估与质量控制**：提供评估框架与质量门禁能力。
- **自驱流程模板**：提供多种 autonomous workflow 的技能化实现。

## Skills 简要说明

- **autonomous-agent-harness**：把 Claude Code 组织成可持续运行的自治代理系统，支持记忆、定时任务和任务队列。
- **autonomous-loops**：提供自治循环的常见架构模式，适合搭建串行或多代理自动流程。
- **continuous-agent-loop**：构建带质量闸门、评测与恢复控制的持续代理循环。
- **eval-harness**：为 Claude Code 会话提供正式评测框架，支持 EDD 评估流程。
- **nanoclaw-repl**：操作和扩展 NanoClaw v2，会话感知的零依赖 REPL。
- **plankton-code-quality**：通过 hooks 在写代码时自动格式化、lint 并修复常见质量问题。
- **ralphinho-rfc-pipeline**：基于 RFC 的多代理 DAG 执行管线，支持质量门和合并队列。

## 组件清单

```json
"agents": [],
"skills": [
  "./skills/autonomous-agent-harness",
  "./skills/autonomous-loops",
  "./skills/continuous-agent-loop",
  "./skills/eval-harness",
  "./skills/nanoclaw-repl",
  "./skills/plankton-code-quality",
  "./skills/ralphinho-rfc-pipeline"
],
"commands": [
  "./commands/quality-gate.md"
]
```
