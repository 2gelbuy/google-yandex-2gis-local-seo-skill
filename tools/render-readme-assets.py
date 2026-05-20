#!/usr/bin/env python3
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
AI_HERO_SOURCE = ASSETS / "ai-generated-google-yandex-2gis-local-seo.png"
HERO_OUT = ASSETS / "gpt-image-google-yandex-2gis-local-seo-cover.png"
WORKFLOW_OUT = ASSETS / "local-seo-workflow.png"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(BOLD if bold else FONT, size)


def vertical_gradient(size, top, bottom):
    img = Image.new("RGB", size)
    pix = img.load()
    for y in range(size[1]):
        t = y / max(1, size[1] - 1)
        color = tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        for x in range(size[0]):
            pix[x, y] = color
    return img.convert("RGBA")


def shadow_layer(size, box, radius, opacity=38, blur=18, offset=(0, 10)):
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    moved = (
        box[0] + offset[0],
        box[1] + offset[1],
        box[2] + offset[0],
        box[3] + offset[1],
    )
    d.rounded_rectangle(moved, radius=radius, fill=(15, 23, 42, opacity))
    return layer.filter(ImageFilter.GaussianBlur(blur))


def render_generated_hero() -> None:
    if not AI_HERO_SOURCE.exists():
        raise FileNotFoundError(f"missing internal generated source: {AI_HERO_SOURCE}")

    src = Image.open(AI_HERO_SOURCE).convert("RGB")
    target = (1600, 840)
    scale = max(target[0] / src.width, target[1] / src.height)
    resized = src.resize(
        (math.ceil(src.width * scale), math.ceil(src.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - target[0]) // 2
    top = (resized.height - target[1]) // 2
    resized.crop((left, top, left + target[0], top + target[1])).save(
        HERO_OUT,
        optimize=True,
        quality=92,
    )


def draw_box(draw, img, box, fill, title, lines):
    x1, y1, x2, y2 = box
    img.alpha_composite(shadow_layer(img.size, box, 24))
    draw.rounded_rectangle(box, radius=24, fill=fill)
    draw.text((x1 + 30, y1 + 32), title, font=font(22, True), fill="#0f172a")
    for i, line in enumerate(lines):
        draw.text((x1 + 30, y1 + 70 + 27 * i), line, font=font(16), fill="#475569")


def draw_arrow(draw, start, end):
    draw.line((*start, *end), fill="#334155", width=4)
    ang = math.atan2(end[1] - start[1], end[0] - start[0])
    for da in (2.65, -2.65):
        p = (end[0] - math.cos(ang + da) * 18, end[1] - math.sin(ang + da) * 18)
        draw.line((end[0], end[1], p[0], p[1]), fill="#334155", width=4)


def render_workflow() -> None:
    w, h = 1400, 540
    img = vertical_gradient((w, h), (248, 250, 252), (232, 244, 255))
    draw = ImageDraw.Draw(img)

    draw.text(
        (64, 70),
        "Проверенные факты -> безопасные правки в картах",
        font=font(34, True),
        fill="#0f172a",
    )
    draw.text(
        (64, 108),
        "Skill не обещает топ. Он находит расхождения и готовит действия по правилам платформ.",
        font=font(19),
        fill="#475569",
    )

    boxes = [
        ((64, 178, 304, 316), "#ffffff", "Бизнес-факты", ["название, адрес, телефон", "часы, сайт, geo, город"]),
        ((388, 132, 626, 222), "#dbeafe", "Google", ["Business Profile / Maps"]),
        ((388, 242, 626, 332), "#fef3c7", "Яндекс", ["Бизнес / Карты / Webmaster"]),
        ((388, 352, 626, 442), "#dcfce7", "2ГИС", ["карточки, рубрики, отзывы"]),
        ((726, 198, 992, 338), "#ffffff", "NAP + schema", ["сайт, карты, справочники", "JSON-LD и соцпрофили"]),
        ((1080, 178, 1340, 316), "#ffffff", "Приоритеты", ["что исправить первым", "как проверить результат"]),
    ]
    for box, fill, title, lines in boxes:
        draw_box(draw, img, box, fill, title, lines)

    for start, end in [
        ((304, 246), (382, 178)),
        ((304, 246), (382, 286)),
        ((304, 246), (382, 398)),
        ((626, 178), (716, 252)),
        ((626, 286), (716, 276)),
        ((626, 398), (716, 312)),
        ((992, 270), (1072, 246)),
    ]:
        draw_arrow(draw, start, end)

    chips = [
        (64, "нет фейковых филиалов", "#fee2e2", "#991b1b"),
        (404, "нет накрутки отзывов", "#fee2e2", "#991b1b"),
        (704, "нет обещаний топа", "#fee2e2", "#991b1b"),
        (1000, "только проверенные факты", "#dcfce7", "#166534"),
    ]
    for x, label, fill, color in chips:
        draw.rounded_rectangle((x, 456, x + 320, 502), radius=23, fill=fill)
        draw.text((x + 24, 468), label, font=font(17, True), fill=color)

    img.save(WORKFLOW_OUT, optimize=True)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    render_generated_hero()
    render_workflow()
    print(f"rendered {HERO_OUT.relative_to(ROOT)} and {WORKFLOW_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
