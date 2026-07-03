# Media AI 分类说明

该目录提供媒体内容生成与处理相关能力，面向图文、视频等创作与生产场景。

## 当前目录功能

- **内容生成**：支持多模态内容创作与增强。
- **视频相关工作流**：支持视频编辑与处理类能力。
- **媒体工具整合**：将媒体 AI 工具能力封装为可复用技能。

## Skills 简要说明

- **article-writing**：用于撰写文章、教程、博客和 newsletter 等长篇内容，并保持统一文风。
- **fal-ai-media**：通过 fal.ai 统一生成图片、视频与音频等多模态内容。
- **frontend-slides**：把 PPT 转成网页演示，或直接生成动画丰富的 HTML 幻灯片。
- **manim-video**：用于制作技术概念、系统图和产品讲解类的 Manim 动画视频。
- **remotion-video-creation**：提供基于 Remotion 的 React 视频创作规则与实践。
- **ui-demo**：用 Playwright 录制网页产品演示、操作 walkthrough 和教程视频。
- **video-editing**：提供 AI 辅助的视频剪辑、结构整理、增强和成片流程。
- **videodb**：用于视频音频内容的导入、理解、检索、转码和时间线处理。

## 组件清单

```json
"agents": [],
"skills": [
  "./skills/article-writing",
  "./skills/fal-ai-media",
  "./skills/frontend-slides",
  "./skills/manim-video",
  "./skills/remotion-video-creation",
  "./skills/ui-demo",
  "./skills/video-editing",
  "./skills/videodb"
],
"commands": []
```
