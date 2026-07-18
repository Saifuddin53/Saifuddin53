#!/usr/bin/env python3
"""Generate the self-hosted animated hero for the profile README."""

from __future__ import annotations

from html import escape
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps


ROOT = Path(__file__).resolve().parents[1]
AVATAR = ROOT / "assets" / "avatar.png"
OUTPUT = ROOT / "assets" / "profile-terminal.svg"


def avatar_to_ascii(columns: int = 32, rows: int = 24) -> list[str]:
    image = Image.open(AVATAR).convert("RGB")
    image = ImageOps.fit(image, (columns, rows), method=Image.Resampling.LANCZOS)
    image = ImageEnhance.Contrast(ImageOps.grayscale(image)).enhance(1.35)
    palette = " .:-=+*#%@"

    lines: list[str] = []
    for y in range(rows):
        line = "".join(
            palette[round((255 - image.getpixel((x, y))) / 255 * (len(palette) - 1))]
            for x in range(columns)
        )
        lines.append(line.rstrip())
    return lines


def render_ascii(lines: list[str]) -> str:
    rows = []
    for index, line in enumerate(lines):
        delay = 0.04 * index
        rows.append(
            f'<text x="82" y="{128 + index * 12}" class="ascii reveal" '
            f'style="animation-delay:{delay:.2f}s">{escape(line or " ")}</text>'
        )
    return "\n    ".join(rows)


def build_svg() -> str:
    ascii_rows = render_ascii(avatar_to_ascii())
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="500" viewBox="0 0 1200 500" role="img" aria-labelledby="title desc">
  <title id="title">Saifuddin Adenwala, Mobile Product Engineer</title>
  <desc id="desc">Animated terminal introducing skills in native and cross-platform mobile engineering, connected devices, real-time systems, backend, cloud, and product delivery.</desc>
  <defs>
    <linearGradient id="background" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#07111f"/>
      <stop offset="0.55" stop-color="#0b1728"/>
      <stop offset="1" stop-color="#101827"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#22d3ee"/>
      <stop offset="1" stop-color="#fbbf24"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop offset="0" stop-color="#22d3ee" stop-opacity=".18"/>
      <stop offset="1" stop-color="#22d3ee" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#93c5fd" stroke-opacity=".035"/>
    </pattern>
    <clipPath id="screen"><rect x="24" y="24" width="1152" height="452" rx="18"/></clipPath>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#000814" flood-opacity=".55"/>
    </filter>
    <style>
      text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
      .muted {{ fill:#718096; }}
      .body {{ fill:#d8e2f0; font-size:18px; }}
      .label {{ fill:#7dd3fc; font-size:15px; letter-spacing:1.4px; }}
      .ascii {{ fill:#fbbf24; font-size:12px; white-space:pre; }}
      .reveal {{ opacity:0; animation:reveal .55s cubic-bezier(.2,.75,.25,1) forwards; }}
      .cursor {{ animation:blink 1s steps(1,end) infinite; }}
      .scan {{ animation:scan 5.5s ease-in-out infinite; }}
      .pulse {{ animation:pulse 2.8s ease-in-out infinite; transform-origin:center; }}
      @keyframes reveal {{ from {{ opacity:0; transform:translateY(8px); }} to {{ opacity:1; transform:translateY(0); }} }}
      @keyframes blink {{ 50% {{ opacity:0; }} }}
      @keyframes scan {{ 0%,15% {{ transform:translateY(-80px); opacity:0; }} 35% {{ opacity:.45; }} 70%,100% {{ transform:translateY(420px); opacity:0; }} }}
      @keyframes pulse {{ 0%,100% {{ opacity:.4; }} 50% {{ opacity:1; }} }}
      @media (prefers-reduced-motion: reduce) {{
        .reveal {{ opacity:1; animation:none; }} .cursor,.scan,.pulse {{ animation:none; }}
      }}
    </style>
  </defs>

  <rect width="1200" height="500" rx="24" fill="#030712"/>
  <rect x="24" y="24" width="1152" height="452" rx="18" fill="url(#background)" filter="url(#shadow)"/>
  <g clip-path="url(#screen)">
    <rect x="24" y="24" width="1152" height="452" fill="url(#grid)"/>
    <circle cx="1000" cy="90" r="260" fill="url(#glow)"/>
    <rect x="24" y="24" width="1152" height="48" fill="#0a1220"/>
    <circle cx="52" cy="48" r="6" fill="#fb7185"/>
    <circle cx="74" cy="48" r="6" fill="#fbbf24"/>
    <circle cx="96" cy="48" r="6" fill="#34d399"/>
    <text x="600" y="54" text-anchor="middle" fill="#718096" font-size="14">saifuddin@mobile-systems: ~</text>
    <rect class="scan" x="24" y="72" width="1152" height="70" fill="url(#accent)" opacity=".08"/>
  </g>

  <rect x="58" y="94" width="386" height="322" rx="14" fill="#060d18" stroke="#1e3a4a"/>
  <text x="82" y="116" class="label">AVATAR // ASCII MODE</text>
  {ascii_rows}
  <circle cx="407" cy="112" r="4" fill="#22d3ee" class="pulse"/>

  <g>
    <text x="500" y="111" class="body reveal" style="animation-delay:.15s"><tspan fill="#34d399">$</tspan> whoami</text>
    <text x="500" y="160" fill="#f8fafc" font-size="35" font-weight="700" class="reveal" style="animation-delay:.45s">Saifuddin Adenwala</text>
    <text x="500" y="190" fill="#7dd3fc" font-size="20" class="reveal" style="animation-delay:.68s">Mobile Product Engineer</text>

    <text x="500" y="231" class="body reveal" style="animation-delay:.92s"><tspan fill="#34d399">$</tspan> capabilities --core</text>
    <text x="522" y="264" class="body reveal" style="animation-delay:1.12s"><tspan fill="#fbbf24">→</tspan> Native Android + iOS</text>
    <text x="522" y="294" class="body reveal" style="animation-delay:1.30s"><tspan fill="#fbbf24">→</tspan> Flutter + Kotlin Multiplatform</text>
    <text x="522" y="324" class="body reveal" style="animation-delay:1.48s"><tspan fill="#fbbf24">→</tspan> BLE / IoT + realtime systems</text>
    <text x="522" y="354" class="body reveal" style="animation-delay:1.66s"><tspan fill="#fbbf24">→</tspan> Backend + cloud + release engineering</text>

    <text x="500" y="396" class="body reveal" style="animation-delay:1.90s"><tspan fill="#34d399">$</tspan> status</text>
    <text x="522" y="426" fill="#d8e2f0" font-size="18" class="reveal" style="animation-delay:2.08s">shipping products end-to-end<tspan class="cursor" fill="#22d3ee">_</tspan></text>
  </g>

  <g class="reveal" style="animation-delay:2.28s">
    <rect x="58" y="438" width="190" height="24" rx="12" fill="#0e2938" stroke="#155e75"/>
    <text x="153" y="455" text-anchor="middle" fill="#a5f3fc" font-size="12">50K+ INSTALLS</text>
    <rect x="260" y="438" width="184" height="24" rx="12" fill="#2b2110" stroke="#854d0e"/>
    <text x="352" y="455" text-anchor="middle" fill="#fde68a" font-size="12">4.4★ RATING</text>
    <rect x="500" y="438" width="236" height="24" rx="12" fill="#0e2938" stroke="#155e75"/>
    <text x="618" y="455" text-anchor="middle" fill="#a5f3fc" font-size="12">30+ UPSTREAM PRs</text>
    <rect x="748" y="438" width="330" height="24" rx="12" fill="#11241d" stroke="#166534"/>
    <text x="913" y="455" text-anchor="middle" fill="#bbf7d0" font-size="12">END-TO-END PRODUCT OWNERSHIP</text>
  </g>
</svg>
'''


def main() -> None:
    OUTPUT.write_text(build_svg(), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
