#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
CWD = Path.cwd()
STYLE_DIR = SCRIPT_DIR.parent / "styles"
OUTPUT_BASE_DIR = "outputs"


def configure_console_encoding() -> None:
    if os.name == "nt":
        try:
            import ctypes

            ctypes.windll.kernel32.SetConsoleOutputCP(65001)
            ctypes.windll.kernel32.SetConsoleCP(65001)
        except Exception:
            pass

    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def find_and_load_env() -> bool:
    env_locations = []
    explicit = os.getenv("GPT_IMAGE2_IMAGE_ENV")
    if explicit:
        env_locations.append(Path(explicit))
    env_locations.extend(
        [
            SCRIPT_DIR.parent / ".env",
            Path.home() / ".claude" / "skills" / "gpt-image2-image" / ".env",
            Path.home() / "skills" / "gpt-image2-image" / ".env",
        ]
    )

    for env_path in env_locations:
        if env_path.exists():
            load_dotenv(env_path, override=True)
            print(f"Loaded environment from: {env_path}")
            return True

    print("Warning: No .env file found in scoped locations; using process env vars only.")
    return False


def resolve_style_path(style: str | None) -> Path | None:
    if not style:
        return None

    raw_path = Path(style)
    if raw_path.exists():
        return raw_path

    candidate = STYLE_DIR / f"{style}.md"
    if candidate.exists():
        return candidate

    raise FileNotFoundError(f"Style file not found: {style}")


def extract_style_prompt(style_path: Path) -> str:
    content = style_path.read_text(encoding="utf-8")
    marker = "## 基础视觉提示词"
    start = content.find(marker)
    if start == -1:
        return content.strip()

    section_start = start + len(marker)
    next_section = content.find("\n## ", section_start)
    extracted = content[section_start:] if next_section == -1 else content[section_start:next_section]
    return extracted.strip()


def build_prompt(user_prompt: str, style_prompt: str | None) -> str:
    if not style_prompt:
        return user_prompt.strip()

    return (
        f"{style_prompt}\n\n---\n\n"
        "请基于以上视觉方向生成一张全新的图片。\n"
        "优先保证整体气质、材质、配色、构图与完成度。\n"
        "不要输出解释，只生成符合要求的最终图片。\n\n"
        f"具体需求如下：\n{user_prompt.strip()}"
    )


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate one or more images with gpt-image-2")
    parser.add_argument("--prompt", help="Prompt text")
    parser.add_argument("--prompt-file", help="Path to a UTF-8 text file containing the prompt")
    parser.add_argument("--style", help="Style id or style markdown file path")
    parser.add_argument("--aspect", choices=["1:1", "16:9", "9:16"], default="1:1")
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--output-dir", help="Output directory path")
    parser.add_argument("--base-name", default="image")
    parser.add_argument("--quality", choices=["low", "medium", "high", "auto"])
    return parser


def load_prompt(args: argparse.Namespace) -> str:
    if args.prompt:
        return args.prompt
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8")
    raise ValueError("Either --prompt or --prompt-file is required")


def build_output_dir(output_dir: str | None) -> Path:
    if output_dir:
        path = Path(output_dir)
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = CWD / OUTPUT_BASE_DIR / timestamp
    path.mkdir(parents=True, exist_ok=True)
    return path


def main() -> None:
    find_and_load_env()

    parser = create_parser()
    args = parser.parse_args()

    if args.count < 1:
        parser.error("--count must be at least 1")

    prompt = load_prompt(args)
    style_path = resolve_style_path(args.style)
    style_prompt = extract_style_prompt(style_path) if style_path else None
    final_prompt = build_prompt(prompt, style_prompt)
    output_dir = build_output_dir(args.output_dir)

    from image_generator import GptImage2Generator

    generator = GptImage2Generator(aspect_ratio=args.aspect)
    if args.quality:
        generator.quality = args.quality

    manifest: dict[str, Any] = {
        "model": generator.model_name,
        "aspect": args.aspect,
        "style": str(style_path) if style_path else None,
        "count": args.count,
        "output_dir": str(output_dir),
        "prompt": final_prompt,
        "images": [],
    }

    for index in range(1, args.count + 1):
        output_path = output_dir / f"{args.base_name}-{index:02d}.png"
        scene_data = {
            "index": index,
            "image_prompt": final_prompt,
        }
        saved_path = generator.generate_scene_image(
            scene_data=scene_data,
            output_path=str(output_path),
        )
        manifest["images"].append(str(saved_path))

    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print("=" * 60)
    print("Image generation complete")
    print("=" * 60)
    print(f"Output directory: {output_dir}")
    for image_path in manifest["images"]:
        print(f"Image: {image_path}")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
