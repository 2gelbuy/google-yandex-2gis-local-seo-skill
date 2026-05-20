#!/usr/bin/env python3
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
AI_HERO_SOURCE = ASSETS / "ai-generated-google-yandex-2gis-local-seo.png"
WORKFLOW_SOURCE = ASSETS / "ai-generated-local-seo-map-background.png"
HERO_OUT = ASSETS / "gpt-image-google-yandex-2gis-local-seo-cover.png"
WORKFLOW_OUT = ASSETS / "local-seo-workflow-promo.png"
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
    if not WORKFLOW_SOURCE.exists():
        raise FileNotFoundError(f"missing internal generated source: {WORKFLOW_SOURCE}")

    target = (1600, 760)
    src = Image.open(WORKFLOW_SOURCE).convert("RGB")
    scale = max(target[0] / src.width, target[1] / src.height)
    resized = src.resize(
        (math.ceil(src.width * scale), math.ceil(src.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - target[0]) // 2
    top = (resized.height - target[1]) // 2
    img = resized.crop((left, top, left + target[0], top + target[1])).convert("RGBA")

    # Darken and add left-side readability gradient without flattening the map.
    shade = Image.new("RGBA", target, (2, 8, 23, 62))
    img.alpha_composite(shade)
    grad = Image.new("RGBA", target, (0, 0, 0, 0))
    gp = grad.load()
    for x in range(target[0]):
        t = max(0, 1 - x / 1040)
        alpha = int(198 * (t**1.35))
        for y in range(target[1]):
            gp[x, y] = (2, 6, 23, alpha)
    img.alpha_composite(grad)

    draw = ImageDraw.Draw(img)

    def card(box, border, title, body):
        x1, y1, x2, y2 = box
        layer = Image.new("RGBA", target, (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        d.rounded_rectangle((x1, y1, x2, y2), radius=24, fill=(6, 18, 36, 214), outline=border, width=2)
        img.alpha_composite(layer)
        draw.text((x1 + 28, y1 + 24), title, font=font(24, True), fill="#ffffff")
        draw.text((x1 + 28, y1 + 64), body, font=font(18), fill="#cbd5e1")

    draw.rounded_rectangle((56, 56, 404, 106), radius=25, fill=(15, 23, 42, 188), outline="#38bdf8", width=2)
    draw.text((86, 69), "skill для СНГ и RU/KZ", font=font(24, True), fill="#38bdf8")

    draw.text((56, 176), "Как работает", font=font(68, True), fill="#ffffff")
    draw.text((56, 258), "локальное SEO", font=font(86, True), fill="#ffffff")
    draw.text((56, 352), "Google + Яндекс + 2ГИС", font=font(47, True), fill="#facc15")
    draw.text((60, 420), "Факты бизнеса -> карты -> NAP/schema -> безопасные правки", font=font(28, True), fill="#dbeafe")

    card((60, 506, 388, 640), "#38bdf8", "1. Факты", "адрес, телефон,\nчасы, город, филиал")
    card((420, 506, 748, 640), "#facc15", "2. Карты", "Google, Яндекс,\n2ГИС и справочники")
    card((780, 506, 1108, 640), "#22c55e", "3. Сверка", "NAP, schema,\nдубли и рубрики")
    card((1140, 506, 1540, 640), "#fb7185", "4. Правки", "без фейковых отзывов,\nфилиалов и обещаний топа")

    chips = [
        (60, 682, "нет накрутки отзывов", "#facc15"),
        (386, 682, "нет фейковых филиалов", "#38bdf8"),
        (734, 682, "только проверенные факты", "#22c55e"),
        (1138, 682, "правки только после OK", "#fb7185"),
    ]
    for x, y, text, color in chips:
        w = 292 if "OK" not in text else 338
        draw.rounded_rectangle((x, y, x + w, y + 48), radius=24, fill=(15, 23, 42, 220), outline=color, width=2)
        draw.text((x + 24, y + 13), text, font=font(17, True), fill=color)

    img.convert("RGB").save(WORKFLOW_OUT, optimize=True, quality=92)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    render_generated_hero()
    render_workflow()
    print(f"rendered {HERO_OUT.relative_to(ROOT)} and {WORKFLOW_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
