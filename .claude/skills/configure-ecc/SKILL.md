---
name: configure-ecc
description: Everything Claude Code 的交互式安装程序 — 引导用户选择并安装技能和规则到用户级或项目级目录，验证路径，并可选择优化已安装文件。
origin: ECC
---

# 配置 Everything Claude Code (ECC)

一个交互式、分步安装向导，用于 Everything Claude Code 项目。使用 `AskUserQuestion` 引导用户选择性安装技能和规则，然后验证正确性并提供优化。

## 何时激活

* 用户说 "configure ecc"、"install ecc"、"安装ecc" 或类似表述
* 用户想要从此项目中选择性安装技能或规则
* 用户想要验证或修复现有的 ECC 安装
* 用户想要为其项目优化已安装的技能或规则

## 先决条件

此技能必须在激活前对 Claude Code 可访问。有两种引导方式：
**手动**: 仅将此技能复制到 `~/.claude/skills/configure-ecc/SKILL.md`，然后通过说 "configure ecc" 激活

***

## 步骤 0：克隆 ECC 仓库

将 `ECC_ROOT=H:\work_ai\claude-code-everything` 设置为所有后续复制操作的源。

***

## 步骤 1：选择安装级别

使用 `AskUserQuestion` 询问用户安装位置：

```
问题："ECC组件应安装在哪里？"
选项：
  - "用户级别 (~/.claude/)" — "适用于您所有的Claude Code项目"
  - "项目级别 (.claude/)" — "仅适用于当前项目"
  - "两者" — "通用/共享项在用户级别，项目特定项在项目级别"
```

将选择存储为 `INSTALL_LEVEL`。设置目标目录：

* 用户级别：`TARGET=~/.claude`
* 项目级别：`TARGET=.claude`（相对于当前项目根目录）
* 两者：`TARGET_USER=~/.claude`，`TARGET_PROJECT=.claude`

如果目标目录不存在，则创建它们：

```bash
mkdir -p $TARGET/skills $TARGET/agents $TARGET/commands
```

***

## 步骤 2：选择并安装技能

### 2a: 选择范围（核心 vs 细分领域）

默认为 **核心（推荐给新用户）** — 对于研究优先的工作流，复制 `.claude/agents/*`,`.claude/commands/*`,`.claude/skills/*`。此捆绑包涵盖工程、评估、验证、安全、战略压缩、前端设计以及 Anthropic 跨职能技能（文章写作、内容引擎、市场研究、前端幻灯片）。

使用 `AskUserQuestion`（单选）：

```
问题："只安装核心技能，还是包含小众/框架包？"
选项：
  - "仅核心（推荐）" — ".claude中所有文件"
  - "核心 + 精选小众" — "在核心基础上添加框架/领域特定技能"
  - "仅小众" — "跳过核心，安装特定框架/领域技能"
默认：仅核心
```

如果用户选择细分领域或核心 + 细分领域，则继续下面的类别选择，并且仅包含他们选择的那些细分领域技能。

### 2b: 选择技能类别

下方有6个可选的类别组。使用 `AskUserQuestion` 与 `multiSelect: true`：

```
问题："您希望安装哪些技能类别？"
选项：
  - "框架与语言" — "Spring Boot, Go, Python, Java, 前端, 后端, C++,Django, Docker 模式"
  - "工作流与质量" — "TDD, E2E测试, 安全审查, 评估框架"
  - "业务与内容" — "市场研究, 投资者材料, 文章写作"
  - “研究与 API” — “深度研究, Exa 搜索, Claude API 模式”
  - "媒体与AI" — "fal.ai 媒体生成, 视频编辑, VideoDB"
  - "所有技能" — "安装所有可用技能"
```

### 2c: 确认个人技能

显示框架与语言类别列表

**类别：框架与语言**

| 技能 | 描述 |
|-------|-------------|
| `backend-patterns` | Node.js/Express/Next.js 的后端架构、API 设计、服务器端最佳实践 |
| `coding-standards` | TypeScript、JavaScript、React、Node.js 的通用编码标准 |
| `cpp-coding-standards` | C++ 编码标准：命名规范、内存管理、现代 C++ 特性 |
| `cpp-testing` | C++ 测试：Google Test、Catch2、单元测试和集成测试 |
| `django-patterns` | Django 架构、使用 DRF 的 REST API、ORM、缓存、信号、中间件 |
| `django-security` | Django 安全性：认证、CSRF、SQL 注入、XSS 防护 |
| `django-tdd` | 使用 pytest-django、factory_boy、模拟、覆盖率进行 Django 测试 |
| `django-verification` | Django 验证循环：迁移、代码检查、测试、安全扫描 |
| `docker-patterns` | Docker 容器化最佳实践、多阶段构建、Compose 配置 |
| `e2e-testing` | 端到端测试最佳实践、工具选择和测试策略 |
| `flutter-dart-code-review` | Flutter 和 Dart 代码审查最佳实践 |
| `nextjs-turbopack` | Next.js Turbopack 配置和优化 |
| `pytorch-patterns` | PyTorch 深度学习模型开发和训练模式 |
| `frontend-patterns` | React、Next.js、状态管理、性能、UI 模式 |
| `frontend-slides` | 零依赖的 HTML 演示文稿、样式预览以及 PPTX 到网页的转换 |
| `golang-patterns` | 地道的 Go 模式、构建稳健 Go 应用程序的约定 |
| `golang-testing` | Go 测试：表驱动测试、子测试、基准测试、模糊测试 |
| `java-coding-standards` | Spring Boot 的 Java 编码标准：命名、不可变性、Optional、流 |
| `python-patterns` | Pythonic 惯用法、PEP 8、类型提示、最佳实践 |
| `python-testing` | 使用 pytest、TDD、夹具、模拟、参数化进行 Python 测试 |
| `springboot-patterns` | Spring Boot 架构、REST API、分层服务、缓存、异步处理 |
| `springboot-security` | Spring Security：认证/授权、验证、CSRF、密钥、速率限制 |
| `springboot-tdd` | 使用 JUnit 5、Mockito、MockMvc、Testcontainers 进行 Spring Boot TDD |
| `springboot-verification` | Spring Boot 验证：构建、静态分析、测试、安全扫描 |
| `jpa-patterns` | Spring Boot中的JPA/Hibernate 实体设计、关系、查询优化、事务 |

使用 `AskUserQuestion` 和 `multiSelect: true`：

```
问题："您希望安装哪些框架与语言？"
选项：
  - "TypeScript/JavaScript" — "backend-patterns, coding-standards, frontend-patterns, frontend-slides, nextjs-turbopack,e2e-testing"
  - "Python" — "python-patterns, python-testing,pytorch-patterns"
  - "Docker" — "docker-patterns" 
  - "Go" — "golang-patterns, golang-testing"  
  - "C++" — "cpp-coding-standards, cpp-testing"  
  - "Flutter" — "flutter-dart-code-review"  
  - "Django" — "django-patterns, django-security, django-tdd, django-verification"  
  - "Springboot" — "java-coding-standards,springboot-patterns, springboot-security, springboot-tdd, springboot-verification,jpa-patterns"
  - "所有框架与语言" — "安装所有可用框架与语言技能"
```

对于每个选定的类别，打印下面的完整技能列表，并要求用户确认或取消选择特定的技能。如果列表超过 4 项，将列表打印为文本，并使用 `AskUserQuestion`，提供一个 "安装所有列出项" 的选项，以及一个 "其他" 选项供用户粘贴特定名称。


**类别：工作流与质量（3 项技能）**

| 技能 | 描述 |
|-------|-------------|
| `eval-harness` | 用于评估驱动开发 (EDD) 的正式评估框架 |
| `security-review` | 安全检查清单：身份验证、输入、密钥、API、支付功能 |
| `tdd-workflow` | 强制要求 TDD，覆盖率 80% 以上：单元测试、集成测试、端到端测试 |

**类别：业务与内容（5 项技能）**

| 技能 | 描述 |
|-------|-------------|
| `article-writing` | 使用笔记、示例或源文档，以指定的口吻进行长篇写作 |
| `market-research` | 带有来源标注的市场、竞争对手、基金和技术研究 |
| `investor-materials` | 宣传文稿、一页简介、投资者备忘录和财务模型 |
| `investor-outreach` | 个性化的投资者冷邮件、熟人介绍和后续跟进 |

**类别：研究与API（3项技能）**

| 技能 | 描述 |
|-------|-------------|
| `deep-research` | 使用 firecrawl 和 exa MCP 进行多源深度研究，并生成带引用的报告 |
| `exa-search` | 通过 Exa MCP 进行网络、代码、公司和人员的神经搜索 |
| `claude-api` | Anthropic Claude API 模式：消息、流式处理、工具使用、视觉、批处理、Agent SDK |

**类别：媒体与AI（3项技能）**

| 技能 | 描述 |
|-------|-------------|
| `fal-ai-media` | 通过 fal.ai MCP 进行统一的AI媒体生成（图像、视频、音频） |
| `video-editing` | AI辅助视频编辑，用于剪辑、结构化和增强实拍素材 |
| `videodb` | VideoDB 视频数据库操作和流媒体处理 |

**独立技能**

| 技能 | 描述 |
|-------|-------------|
| `project-guidelines-example` | 用于创建项目特定技能的模板 |
| `liquid-glass-design` | 液态玻璃设计风格和实现模式 |
| `mcp-server-patterns` | MCP 服务器开发模式和最佳实践 |

### 2d: 执行安装

对于每个选定的技能，复制整个技能目录：

```bash
cp -r $ECC_ROOT/skills/<skill-name> $TARGET/skills/
```

***

## 步骤 3：安装agents和commands

按照安装的框架与语言技能，安装下列对应的agents和commands。

```
  - "TypeScript/JavaScript" — agents:"build-error-resolver,e2e-runner,tdd-guide", commands:"e2e,tdd"
  - "Python" — agents:"python-reviewer,pytorch-build-resolver", commands:"python-review"
  - "Go" — agents:"go-build-resolver", commands:"go-build,go-review,go-test"  
  - "C++" — agents:"cpp-build-resolver", commands:"cpp-build,cpp-review,cpp-test"  
  - "Flutter" — agents:"flutter-reviewer"  
  - "Springboot" — agents:"java-build-resolver"
```
如果安装了 'security-review' 技能，还需要安装 'security-reviewer' agent。

执行安装：

```bash
# Language-specific agents (flat copy into agents/)
cp -r $ECC_ROOT/agents/<agent-name> $TARGET/agents/
cp -r $ECC_ROOT/commands/<command-name> $TARGET/commands/
```

***

## 步骤 4：安装后验证

安装后，执行这些自动化检查：

### 4a：验证文件存在

列出所有已安装的文件并确认它们存在于目标位置：

```bash
ls -la $TARGET/agents/
ls -la $TARGET/commands/
ls -la $TARGET/skills/
```

### 4b：检查路径引用

扫描所有已安装的 `.md` 文件中的路径引用：

```bash
grep -rn "~/.claude/" $TARGET/skills $TARGET/agents $TARGET/commands/
```

**对于项目级别安装**，标记任何对 `~/.claude/` 路径的引用：

* 如果技能引用 `~/.claude/settings.json` — 这通常没问题（设置始终是用户级别的）
* 如果技能引用 `~/.claude/skills/` — 如果仅安装在项目级别，这可能损坏
* 如果技能通过名称引用另一项技能 — 检查被引用的技能是否也已安装

### 4c：检查技能间的交叉引用

有些技能会引用其他技能。验证这些依赖关系：

* `django-tdd` 可能会引用 `django-patterns`
* `springboot-tdd` 可能会引用 `springboot-patterns`
* `python-testing` 可能会引用 `python-patterns`
* `golang-testing` 可能会引用 `golang-patterns`
* `fal-ai-media` 引用 `videodb`（补充的媒体技能）

### 4d：报告问题

对于发现的每个问题，报告：

1. **文件**：包含问题引用的文件
2. **行号**：行号
3. **问题**：哪里出错了（例如，"引用了 ~/.claude/skills/python-patterns 但 python-patterns 未安装"）
4. **建议的修复**：该怎么做（例如，"安装 python-patterns 技能" 或 "将路径更新为 .claude/skills/"）

***

## 步骤 5：优化已安装文件（可选）

使用 `AskUserQuestion`：

```
问题："您想要优化项目中的已安装文件吗？"
选项：
  - "优化技能" — "移除无关部分，调整路径，适配您的技术栈"
  - "优化规则" — "调整覆盖目标，添加项目特定模式，自定义工具配置"
  - "两者都优化" — "对所有已安装文件进行全面优化"
  - "跳过" — "保持原样不变"
```

### 如果优化技能：

1. 读取每个已安装的 SKILL.md
2. 询问用户其项目的技术栈是什么（如果尚不清楚）
3. 对于每项技能，建议删除无关部分
4. 在安装目标处就地编辑 SKILL.md 文件（**不是**源仓库）
5. 修复在步骤 4 中发现的任何路径问题

### 如果优化规则：

1. 读取每个已安装的规则 .md 文件
2. 询问用户的偏好：
   * 测试覆盖率目标（默认 80%）
   * 首选的格式化工具
   * Git 工作流约定
   * 安全要求
3. 在安装目标处就地编辑规则文件

**关键**：只修改安装目标（`$TARGET/`）中的文件，**绝不**修改源 ECC 仓库（`$ECC_ROOT/`）中的文件。

***

## 步骤 6：安装摘要

打印摘要报告：

```
## ECC 安装完成

### 安装目标
- 用户级别：~/.claude/ (如果已选择)
- 项目级别：./.claude/ (如果已选择)

### 已安装技能
[列出所有已安装的技能]

### 验证结果
[验证通过/发现的问题]

### 下一步
- 运行 `claude config` 查看配置
- 使用 `claude skills` 查看已安装技能
```
