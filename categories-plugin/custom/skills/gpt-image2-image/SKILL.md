---
name: gpt-image2-image
description: Use this skill whenever the user wants a brand-new image created with OpenAI gpt-image-2 from a rough idea, a visual brief, or a reference style direction, including 生图、出图、生成配图、画一张图、做封面、做海报、做插画、做头像、做商品图、做概念图、做壁纸、做活动主视觉等. Be proactive in turning vague intent into a strong final prompt, ask the user to choose an aspect ratio when size is missing, and then generate the image. Do not use this skill for editing existing images, changing text inside an uploaded image, screenshot analysis, OCR, upscaling, or coding tasks about image-generation systems.
user-invocable: true
allowed-tools: Bash, Read, Write, Glob
---

# gpt-image2-image —— 通用图片生成

这个 skill 负责把用户的图片需求整理成适合 `gpt-image-2` 的最终提示词，再生成高质量图片文件。

重点不是把请求硬套进“海报 / 封面 / banner”这些固定品类，而是理解用户真正想要的画面，再把需求转成能出图的 prompt。

## 何时使用

只要用户的目标是“生成图片”，就用这个 skill。

常见但不限于：
- 海报、封面图、banner、KV、thumbnail
- 社媒配图、文章头图、产品主视觉、商品图
- 插画、角色图、场景图、概念图、故事板
- 图标、头像、壁纸、品牌视觉、活动视觉
- 基于参考图做风格延展、改图方向探索
- 用户明确提到 `gpt-image-2`
- 用户用中文说“生图 / 出图 / 画一张 / 生成配图”

## 不适用场景

遇到下面这些情况，不要触发这个 skill：
- 用户要修改现有图片里的文字、背景、局部元素
- 用户要抠图、修图、放大、增强清晰度、补细节
- 用户要分析截图、读取图片文字、解释界面问题
- 用户要写调用 `gpt-image-2` 的代码、搭建图片生成应用或调 API
- 用户要 SVG、HTML、Canvas、前端组件这类可编辑代码产物，而不是位图图片

如果用户的请求同时沾到“图片”与“生成”这两个词，也要先判断他到底是要一张新图，还是在处理已有图片或开发相关功能。

## 先理解任务，不要先套模板

优先识别这几个维度：
1. **主体**：画什么
2. **用途**：这张图要用在哪里
3. **视觉方向**：风格、质感、配色、氛围
4. **画面约束**：构图、镜头、背景、是否要文字
5. **尺寸 / 比例**：横版、竖版、方图，或明确像素尺寸
6. **数量**：先出 1 张还是直接多张变体

如果用户只给了一个很粗的想法，不要立刻抱怨信息不够。先把可推断的信息补全，缺关键项时再追问最少的问题。

## 缺少尺寸时，先让用户选

如果用户没有说明尺寸或比例，先用最短的选项式提问让用户选一个，不要静默假设，也不要围绕尺寸来回追问太多轮。

默认给用户这三个选项：
- `1:1`：方图，适合头像、图标、卡片封面、商品主图
- `16:9`：横图，适合网页头图、演示封面、横版主视觉
- `9:16`：竖图，适合手机壁纸、短视频封面、竖版海报

可以直接这样问：

```text
你这张图要做成哪种比例？
1) 1:1 方图
2) 16:9 横图
3) 9:16 竖图
如果你愿意，我也可以按用途帮你推荐一个。
```

如果用户说“你来定”，再按用途推荐并继续执行。

## 先整理 prompt，再出图

生成前，先把用户需求整理成一版最终 prompt。目标是让 prompt 清楚表达：
- 主体与场景
- 构图与镜头关系
- 风格与材质
- 光线、颜色、氛围
- 是否包含文字，以及文字如何出现
- 明确的约束，例如“不要水印、不要多余 UI、不要低清晰度、不要变形手部”

如果用户描述很简略，先在心里补足，再输出一版精炼的最终 prompt 去生成；不要把用户的原话不加整理地直接扔给模型。

## prompt 组织原则

按下面顺序组织最终 prompt：
1. 用户真正要的画面结果
2. 画面主体与环境
3. 构图、镜头、景别或视角
4. 风格、质感、材质、渲染方式
5. 配色、光线、情绪氛围
6. 文字要求（如果有）
7. 负向约束或避免项

如果用户提供参考图：
- 把它当作风格、配色、材质或氛围参考
- 生成“全新的图”，不要承诺复制原图
- 如果参考图里有文字或品牌元素，默认不要原样搬运，除非用户明确要求

## 风格选择

风格是可选增强，不是必填项。

如果用户指定了内置风格，只读取对应的 `styles/<style-id>.md`。

如果用户让你帮选，可以从这些方向推荐 2-3 个：
- AI / 科技 / 开发者产品：`dark-aurora`, `gradient-glass`
- 商务 / 企业 / 路演视觉：`clean-tech-blue`, `editorial-mono`
- 教育 / 品牌故事 / 插画感：`vector-illustration`, `hand-sketch`
- 文化 / 生活方式 / 高级感：`japanese-wabi`, `swiss-grid`
- 年轻化 / 潮流 / 活动主视觉：`risograph`, `y2k-chrome`

不要因为有内置风格，就把所有任务都强行往这些风格上套。用户没要风格库时，可以直接根据需求写 prompt。

## 后端选择规则

按下面顺序选择生成方式：

1. **如果 skill 目录下存在可用 `.env`，且其中可提供 `OPENAI_BASE_URL` 和 `OPENAI_API_KEY`**
   - 走 `scripts/generate_images.py`
   - 使用 `.env` / 进程环境变量中的配置调用 `gpt-image-2`
   - 这是默认的脚本化路径，适合稳定复现、批量生成和保存 manifest

2. **如果没有可用 `.env`，或缺少 `OPENAI_BASE_URL` / `OPENAI_API_KEY`**
   - 直接使用当前运行环境自带的内置生图能力
   - 不要求 `.env`
   - 先整理出最终 prompt，再直接出图

3. **如果既没有可用 `.env`，当前环境也没有内置生图能力**
   - 再提示用户补充 `.env` 或提供 API 配置

## 工作流

### 1. 默认先出 1 张样图

除非用户明确要求直接批量，否则先生成 1 张，让用户确认方向。

### 2. 整理最终 prompt

在真正出图前，把用户的粗需求压缩成一版可执行 prompt。

### 3. 执行生成

#### 方式 A：有 `.env` 时，走脚本

```bash
python ".claude/skills/gpt-image2-image/scripts/generate_images.py" \
  --prompt "<整理后的最终 prompt>" \
  --style dark-aurora \
  --aspect 16:9 \
  --count 1
```

如果 prompt 很长，用 heredoc：

```bash
python ".claude/skills/gpt-image2-image/scripts/generate_images.py" \
  --prompt "$(cat <<'EOF'
<完整 prompt>
EOF
)" \
  --style dark-aurora \
  --aspect 16:9 \
  --count 1
```

#### 方式 B：没有 `.env` 时，走内置生图

- 先整理出最终 prompt
- 直接使用当前环境自带的 image generation / image tool 出图
- 同样默认先生成 1 张，不要一开始就批量生成

### 4. 回报结果

如果走脚本，默认输出到：

```text
outputs/<timestamp>/
```

其中包含：
- `image-01.png`, `image-02.png`, ...
- `manifest.json`

如果走内置生图，明确告诉用户：
- 你使用的是内置生图能力
- 本次未走 `.env + 脚本`
- 产物保存路径或当前返回结果位置在哪里

## 批量生成原则

- 用户要多张同主题变体时，再用 `--count N`
- 默认不要一上来就生成很多张，先确认第一张方向
- 如果用户要迭代，优先改单一变量：prompt、风格、比例、文字内容中的一个
- 如果第一张方向不对，先总结偏差，再改 prompt，不要盲目重复生图

## 环境要求

分两种情况：

- **有可用 `.env`，且包含 `OPENAI_BASE_URL` 与 `OPENAI_API_KEY`**：
  - 走脚本路径
  - 可额外读取：
    - `GPT_IMAGE_MODEL_NAME`（默认 `gpt-image-2`）
    - `GPT_IMAGE_QUALITY`（默认 `high`）
    - `GPT_IMAGE_ENDPOINT`（默认 `auto`）

- **没有可用 `.env`，或缺少 `OPENAI_BASE_URL` / `OPENAI_API_KEY`**：
  - 优先使用当前环境的内置生图能力
  - 不强制要求 `.env`

脚本只从 skill 自己目录附近的受限 `.env` 位置读取，不会向上递归扫描项目目录。

## 禁止事项

- 不要把这个 skill 限制成少数几个固定品类
- 不要在用户没确认方向时直接批量生很多张
- 不要未经确认就替用户拍板尺寸；尺寸缺失时先让用户选，除非用户明确让你决定
- 不要承诺精确复刻参考图、商标或受保护素材
