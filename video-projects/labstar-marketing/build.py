"""
Labstar Marketing Video — build.py
YouTube-style 16:9 marketing video, ~54 seconds, 1920x1080 @ 30fps.
Run: python3 build.py
Output: out/labstar-marketing.mp4
"""

import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy import (
    VideoClip, ColorClip, ImageClip, CompositeVideoClip,
    concatenate_videoclips, AudioFileClip,
)

# ── Constants ──────────────────────────────────────────────────────────────────
W, H = 1920, 1080
FPS = 30
OUT_DIR = "out"
os.makedirs(OUT_DIR, exist_ok=True)

# Brand palette
BLUE       = "#0077CC"
BLUE_LIGHT = "#29A8FF"
TEAL       = "#00C9A7"
BG_DARK    = "#030d18"
BG_MID     = "#071828"
WHITE      = "#FFFFFF"
GREY       = "#a0bcd0"


# ── PIL helpers ────────────────────────────────────────────────────────────────

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def pil_to_array(img):
    return np.array(img.convert("RGB"))


def make_gradient_bg(w=W, h=H, top=BG_DARK, bottom=BG_MID):
    """Vertical gradient background."""
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    tr, tg, tb = hex_to_rgb(top)
    br, bg_, bb = hex_to_rgb(bottom)
    for y in range(h):
        t = y / h
        r = int(tr + (br - tr) * t)
        g = int(tg + (bg_ - tg) * t)
        b = int(tb + (bb - tb) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def best_font(size):
    """Try to load a nice system font, fall back to default."""
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def best_font_regular(size):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def draw_text_centered(draw, text, y, font, color=WHITE, shadow=True):
    """Draw horizontally-centered text with optional drop shadow."""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    if shadow:
        draw.text((x + 3, y + 3), text, font=font, fill=(0, 0, 0, 180))
    draw.text((x, y), text, font=font, fill=hex_to_rgb(color) if isinstance(color, str) else color)


def draw_accent_line(draw, y, color=BLUE_LIGHT, width=6, margin=200):
    """Draw a thin horizontal accent line."""
    draw.rectangle([(margin, y), (W - margin, y + width)], fill=hex_to_rgb(color))


def draw_pill(draw, text, cx, cy, font, bg_color=BLUE, text_color=WHITE, pad_x=32, pad_y=16):
    """Draw a rounded pill/badge."""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x0, y0 = cx - tw // 2 - pad_x, cy - th // 2 - pad_y
    x1, y1 = cx + tw // 2 + pad_x, cy + th // 2 + pad_y
    r = (y1 - y0) // 2
    draw.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=hex_to_rgb(bg_color))
    draw.text((cx - tw // 2, cy - th // 2), text, font=font, fill=hex_to_rgb(text_color))


# ── Scene builders ─────────────────────────────────────────────────────────────

def make_frame_static(pil_img):
    """Return a moviepy make_frame function for a static PIL image."""
    arr = pil_to_array(pil_img)
    def make_frame(t):
        return arr
    return make_frame


def fade_frame(base_fn, duration, fade_in=0.5, fade_out=0.5):
    """Wrap a make_frame with linear fade in/out."""
    def make_frame(t):
        frame = base_fn(t).astype(float)
        alpha = 1.0
        if t < fade_in:
            alpha = t / fade_in
        elif t > duration - fade_out:
            alpha = (duration - t) / fade_out
        return (frame * alpha).astype(np.uint8)
    return make_frame


# ── Scene 1: Title (7s) ────────────────────────────────────────────────────────

def build_title_frames(duration=7.0):
    bg = make_gradient_bg()
    draw = ImageDraw.Draw(bg)

    # Background glow blobs
    for cx, cy, r, col in [
        (W // 2, H // 2, 420, (0, 80, 180, 40)),
        (300, 200, 200, (0, 180, 160, 25)),
        (W - 300, H - 200, 250, (0, 100, 220, 30)),
    ]:
        blob = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        bd = ImageDraw.Draw(blob)
        bd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
        bg = Image.alpha_composite(bg.convert("RGBA"), blob).convert("RGB")
        draw = ImageDraw.Draw(bg)

    # Accent line top
    draw_accent_line(draw, 80, color=BLUE_LIGHT, width=4, margin=120)

    # Brand label
    label_font = best_font(28)
    draw_text_centered(draw, "LABSTAR DIAGNOSTIC LAB", 110, label_font, GREY)

    # Main headline lines
    h1 = best_font(130)
    h2 = best_font(90)
    draw_text_centered(draw, "Lab Tests.", 220, h1, WHITE)
    draw_text_centered(draw, "Fast.  Affordable.  Accurate.", 380, h2, BLUE_LIGHT)

    # Tagline
    tag_font = best_font_regular(46)
    draw_text_centered(draw, "Your community diagnostic lab — labstar.net", 530, tag_font, GREY)

    # Accent line bottom
    draw_accent_line(draw, 620, color=TEAL, width=4, margin=120)

    # Services row
    svc_font = best_font(36)
    services = ["Urinalysis", "Drug Screening", "PCR Testing", "Disease Panels"]
    spacing = W // (len(services) + 1)
    for i, svc in enumerate(services):
        cx = spacing * (i + 1)
        color = BLUE_LIGHT if i % 2 == 0 else TEAL
        draw_pill(draw, svc, cx, 720, svc_font, bg_color=color, pad_x=28, pad_y=14)

    # Bottom URL
    url_font = best_font_regular(38)
    draw_text_centered(draw, "labstar.net  ·  (267) 791-0272", 830, url_font, GREY)

    base_arr = pil_to_array(bg)

    def make_frame(t):
        frame = base_arr.astype(float)
        # Fade in over first 0.8s
        alpha = min(1.0, t / 0.8)
        # Fade out last 0.5s
        if t > duration - 0.5:
            alpha = min(alpha, (duration - t) / 0.5)
        return (frame * alpha).astype(np.uint8)

    return VideoClip(make_frame, duration=duration).with_fps(FPS)


# ── Scene 2: Problem (10s) ─────────────────────────────────────────────────────

def build_problem_frames(duration=10.0):
    problems = [
        ("⏳", "Days of waiting for results"),
        ("💸", "Expensive, unexpected costs"),
        ("📍", "Inconvenient locations & long queues"),
        ("😕", "Confusing results, no clear answers"),
    ]

    bg_base = make_gradient_bg(top="#0a0520", bottom="#050d1a")
    draw = ImageDraw.Draw(bg_base)

    # Header
    draw_accent_line(draw, 80, color="#CC2244", width=4, margin=120)
    label_font = best_font(28)
    draw_text_centered(draw, "THE PROBLEM", 110, label_font, "#FF6688")

    h2_font = best_font(78)
    draw_text_centered(draw, "Traditional labs let you down", 180, h2_font, WHITE)
    draw_accent_line(draw, 295, color="#CC2244", width=3, margin=120)

    # Problem cards (static layout)
    card_font = best_font(44)
    icon_font = best_font(54)
    card_h = 130
    card_w = 800
    start_y = 350
    margin_x = (W - card_w * 2 - 60) // 2

    for i, (icon, text) in enumerate(problems):
        row, col = divmod(i, 2)
        cx = margin_x + col * (card_w + 60)
        cy = start_y + row * (card_h + 24)

        # Card background
        card_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        cd = ImageDraw.Draw(card_img)
        cd.rounded_rectangle(
            [cx, cy, cx + card_w, cy + card_h],
            radius=20,
            fill=(180, 20, 50, 60),
            outline=(200, 40, 70, 120),
            width=2,
        )
        bg_base = Image.alpha_composite(bg_base.convert("RGBA"), card_img).convert("RGB")
        draw = ImageDraw.Draw(bg_base)

        # Icon and text
        draw.text((cx + 24, cy + card_h // 2 - 30), icon, font=icon_font, fill=hex_to_rgb(WHITE))
        draw.text((cx + 100, cy + card_h // 2 - 22), text, font=card_font, fill=hex_to_rgb(WHITE))

    base_arr = pil_to_array(bg_base)

    def make_frame(t):
        frame = base_arr.astype(float)
        alpha = min(1.0, t / 0.6)
        if t > duration - 0.5:
            alpha = min(alpha, (duration - t) / 0.5)
        return (frame * alpha).astype(np.uint8)

    return VideoClip(make_frame, duration=duration).with_fps(FPS)


# ── Scene 3: Solution (8s) ─────────────────────────────────────────────────────

def build_solution_frames(duration=8.0):
    highlights = [
        "No referral needed — walk in or book online",
        "Results delivered quickly & clearly explained",
        "Transparent, affordable pricing",
    ]

    bg_base = make_gradient_bg(top="#012a20", bottom="#031818")
    draw = ImageDraw.Draw(bg_base)

    draw_accent_line(draw, 80, color=TEAL, width=4, margin=120)
    label_font = best_font(28)
    draw_text_centered(draw, "THE SOLUTION", 110, label_font, TEAL)

    h2_font = best_font(88)
    draw_text_centered(draw, "There is a better way.", 185, h2_font, WHITE)

    body_font = best_font_regular(46)
    desc = "Labstar brings clinical-grade diagnostics to your community"
    draw_text_centered(draw, desc, 310, body_font, GREY)
    draw_text_centered(draw, "— fast, affordable, and stress-free.", 368, body_font, GREY)

    draw_accent_line(draw, 445, color=TEAL, width=3, margin=120)

    check_font = best_font(50)
    body2_font = best_font_regular(46)
    for i, h in enumerate(highlights):
        y = 490 + i * 110
        draw.text((240, y), "✓", font=check_font, fill=hex_to_rgb(TEAL))
        draw.text((320, y + 3), h, font=body2_font, fill=hex_to_rgb(WHITE))

    base_arr = pil_to_array(bg_base)

    def make_frame(t):
        frame = base_arr.astype(float)
        alpha = min(1.0, t / 0.6)
        if t > duration - 0.5:
            alpha = min(alpha, (duration - t) / 0.5)
        return (frame * alpha).astype(np.uint8)

    return VideoClip(make_frame, duration=duration).with_fps(FPS)


# ── Scene 4: Services (10s) ────────────────────────────────────────────────────

def build_services_frames(duration=10.0):
    services = [
        ("🔬", "Urinalysis",               "Quick, thorough urine analysis\nwith reliable results", BLUE_LIGHT),
        ("💊", "Drug & Toxicity\nScreening", "Efficient testing at\ngreat prices", TEAL),
        ("🧬", "PCR Testing",              "Accurate molecular\ndiagnostics", BLUE_LIGHT),
        ("🩺", "Disease Panels",           "Comprehensive infectious &\nchronic disease screening", TEAL),
    ]

    bg_base = make_gradient_bg()
    draw = ImageDraw.Draw(bg_base)

    draw_accent_line(draw, 80, color=BLUE_LIGHT, width=4, margin=120)
    label_font = best_font(28)
    draw_text_centered(draw, "OUR SERVICES", 110, label_font, GREY)

    h2_font = best_font(72)
    draw_text_centered(draw, "Everything You Need in One Place", 180, h2_font, WHITE)
    draw_accent_line(draw, 285, color=BLUE, width=3, margin=120)

    # 2×2 cards
    card_w, card_h = 820, 290
    gap = 40
    total_w = card_w * 2 + gap
    start_x = (W - total_w) // 2
    start_y = 320

    icon_font = best_font(64)
    title_font = best_font(48)
    desc_font = best_font_regular(34)

    for i, (icon, title, desc, color) in enumerate(services):
        row, col = divmod(i, 2)
        cx = start_x + col * (card_w + gap)
        cy = start_y + row * (card_h + gap)

        card_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        cd = ImageDraw.Draw(card_img)
        cd.rounded_rectangle(
            [cx, cy, cx + card_w, cy + card_h],
            radius=24,
            fill=(*hex_to_rgb(BG_MID), 200),
            outline=(*hex_to_rgb(color), 180),
            width=2,
        )
        bg_base = Image.alpha_composite(bg_base.convert("RGBA"), card_img).convert("RGB")
        draw = ImageDraw.Draw(bg_base)

        # Icon
        draw.text((cx + 24, cy + 20), icon, font=icon_font, fill=hex_to_rgb(WHITE))
        # Title (may be multiline)
        ty = cy + 20
        for line in title.split("\n"):
            draw.text((cx + 110, ty), line, font=title_font, fill=hex_to_rgb(color))
            ty += 55
        # Desc
        dy = cy + 145
        for line in desc.split("\n"):
            draw.text((cx + 24, dy), line, font=desc_font, fill=hex_to_rgb(GREY))
            dy += 42

    base_arr = pil_to_array(bg_base)

    def make_frame(t):
        frame = base_arr.astype(float)
        alpha = min(1.0, t / 0.6)
        if t > duration - 0.5:
            alpha = min(alpha, (duration - t) / 0.5)
        return (frame * alpha).astype(np.uint8)

    return VideoClip(make_frame, duration=duration).with_fps(FPS)


# ── Scene 5: Why Labstar stats (9s) ───────────────────────────────────────────

def build_stats_frames(duration=9.0):
    stats = [
        ("⚡", "FAST",  "Same-day results available",      BLUE_LIGHT),
        ("💚", "LOW",   "Affordable — no surprise bills",  TEAL),
        ("🎯", "99%",   "Clinical-grade accuracy",          BLUE_LIGHT),
    ]

    bg_base = make_gradient_bg(top="#020f20", bottom="#041525")
    draw = ImageDraw.Draw(bg_base)

    draw_accent_line(draw, 80, color=BLUE_LIGHT, width=4, margin=120)
    label_font = best_font(28)
    draw_text_centered(draw, "WHY THOUSANDS CHOOSE LABSTAR", 110, label_font, GREY)

    h2_font = best_font(72)
    draw_text_centered(draw, "Fast. Affordable. Accurate.", 185, h2_font, WHITE)
    draw_accent_line(draw, 295, color=BLUE, width=3, margin=120)

    # Stat cards row
    card_w = 520
    gap = 60
    total_w = card_w * 3 + gap * 2
    start_x = (W - total_w) // 2
    card_h = 420
    cy = 340

    icon_font = best_font(70)
    val_font = best_font(100)
    lbl_font = best_font_regular(38)

    for i, (icon, value, label, color) in enumerate(stats):
        cx = start_x + i * (card_w + gap)

        card_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        cd = ImageDraw.Draw(card_img)
        cd.rounded_rectangle(
            [cx, cy, cx + card_w, cy + card_h],
            radius=28,
            fill=(*hex_to_rgb(BG_MID), 220),
            outline=(*hex_to_rgb(color), 200),
            width=3,
        )
        bg_base = Image.alpha_composite(bg_base.convert("RGBA"), card_img).convert("RGB")
        draw = ImageDraw.Draw(bg_base)

        # Accent top strip
        draw.rectangle([cx + 3, cy + 3, cx + card_w - 3, cy + 16], fill=hex_to_rgb(color))

        # Icon
        icon_bb = draw.textbbox((0, 0), icon, font=icon_font)
        ix = cx + (card_w - (icon_bb[2] - icon_bb[0])) // 2
        draw.text((ix, cy + 40), icon, font=icon_font, fill=hex_to_rgb(WHITE))

        # Value
        val_bb = draw.textbbox((0, 0), value, font=val_font)
        vx = cx + (card_w - (val_bb[2] - val_bb[0])) // 2
        draw.text((vx, cy + 140), value, font=val_font, fill=hex_to_rgb(color))

        # Label (wrap at ~20 chars)
        words = label.split()
        lines, line = [], []
        for w in words:
            line.append(w)
            if len(" ".join(line)) > 18:
                lines.append(" ".join(line[:-1]))
                line = [w]
        lines.append(" ".join(line))

        ly = cy + card_h - len(lines) * 46 - 24
        for ln in lines:
            lb = draw.textbbox((0, 0), ln, font=lbl_font)
            lx = cx + (card_w - (lb[2] - lb[0])) // 2
            draw.text((lx, ly), ln, font=lbl_font, fill=hex_to_rgb(GREY))
            ly += 46

    base_arr = pil_to_array(bg_base)

    def make_frame(t):
        frame = base_arr.astype(float)
        alpha = min(1.0, t / 0.6)
        if t > duration - 0.5:
            alpha = min(alpha, (duration - t) / 0.5)
        return (frame * alpha).astype(np.uint8)

    return VideoClip(make_frame, duration=duration).with_fps(FPS)


# ── Scene 6: CTA (10s) ────────────────────────────────────────────────────────

def build_cta_frames(duration=10.0):
    bg_base = make_gradient_bg(top="#001533", bottom="#000d22")
    draw = ImageDraw.Draw(bg_base)

    # Glow center
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([(W//2 - 500, H//2 - 400), (W//2 + 500, H//2 + 400)], fill=(0, 100, 220, 30))
    bg_base = Image.alpha_composite(bg_base.convert("RGBA"), glow).convert("RGB")
    draw = ImageDraw.Draw(bg_base)

    draw_accent_line(draw, 80, color=BLUE_LIGHT, width=4, margin=120)
    label_font = best_font(28)
    draw_text_centered(draw, "LABSTAR DIAGNOSTIC LAB", 110, label_font, GREY)

    h1_font = best_font(120)
    draw_text_centered(draw, "Get Tested Today", 200, h1_font, WHITE)

    tag_font = best_font_regular(50)
    draw_text_centered(draw, "Affordable diagnostics for your whole community", 360, tag_font, GREY)

    draw_accent_line(draw, 450, color=TEAL, width=4, margin=300)

    # CTA buttons
    btn_font = best_font(52)
    # Website button
    draw_pill(draw, "  Visit labstar.net  ", W // 2 - 330, 550, btn_font, bg_color=BLUE, text_color=WHITE, pad_x=40, pad_y=22)
    # Phone button
    draw_pill(draw, "  (267) 791-0272  ", W // 2 + 350, 550, btn_font, bg_color="#0e2d45", text_color=BLUE_LIGHT, pad_x=40, pad_y=22)

    # Bottom tagline
    sub_font = best_font_regular(40)
    draw_text_centered(draw, "Your health can't wait — and neither should you.", 680, sub_font, GREY)

    # Stars / trust row
    star_font = best_font(50)
    draw_text_centered(draw, "★ ★ ★ ★ ★   Trusted by your community", 780, star_font, BLUE_LIGHT)

    draw_accent_line(draw, 880, color=BLUE, width=3, margin=120)
    foot_font = best_font_regular(32)
    draw_text_centered(draw, "contact@labstar.net  ·  labstar.net", 910, foot_font, GREY)

    base_arr = pil_to_array(bg_base)

    def make_frame(t):
        frame = base_arr.astype(float)
        alpha = min(1.0, t / 0.8)
        if t > duration - 0.8:
            alpha = min(alpha, (duration - t) / 0.8)
        # Pulse glow on CTA text
        pulse = 1.0 + 0.03 * np.sin(t * 2 * np.pi * 0.8)
        frame = np.clip(frame * alpha * pulse, 0, 255)
        return frame.astype(np.uint8)

    return VideoClip(make_frame, duration=duration).with_fps(FPS)


# ── Assemble & render ──────────────────────────────────────────────────────────

def main():
    print("Building Labstar marketing video...")

    print("  Scene 1/6: Title")
    s1 = build_title_frames(7.0)

    print("  Scene 2/6: Problem")
    s2 = build_problem_frames(10.0)

    print("  Scene 3/6: Solution")
    s3 = build_solution_frames(8.0)

    print("  Scene 4/6: Services")
    s4 = build_services_frames(10.0)

    print("  Scene 5/6: Why Labstar")
    s5 = build_stats_frames(9.0)

    print("  Scene 6/6: CTA")
    s6 = build_cta_frames(10.0)

    print("  Concatenating scenes...")
    final = concatenate_videoclips([s1, s2, s3, s4, s5, s6])

    out_path = os.path.join(OUT_DIR, "labstar-marketing.mp4")
    print(f"  Rendering → {out_path}  ({final.duration:.1f}s @ {FPS}fps, {W}x{H})")
    final.write_videofile(
        out_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="medium",
        ffmpeg_params=["-crf", "18"],
        logger="bar",
    )
    print(f"\nDone! Output: {out_path}")
    print(f"Duration: {final.duration:.1f}s  |  Resolution: {W}x{H}")


if __name__ == "__main__":
    main()
