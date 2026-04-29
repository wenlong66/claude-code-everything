# Autonomous 分类说明

该目录提供自动化与自驱执行相关能力，面向持续运行、评估闭环与质量闸门场景。

## 当前目录功能

- **自动化循环**：支持定时或持续执行任务循环。
- **评估与质量控制**：提供评估框架与质量门禁能力。
- **自驱流程模板**：提供多种 autonomous workflow 的技能化实现。

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