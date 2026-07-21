#!/usr/bin/env python3
"""Generate the self-hosted animated build-pipeline hero."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "profile-terminal.svg"


def build_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="430" viewBox="0 0 1200 430" role="img" aria-labelledby="title desc">
  <title id="title">Saifuddin Adenwala, Mobile and Full-Stack Product Engineer</title>
  <desc id="desc">A product build pipeline spanning native mobile, cross-platform engineering, connected systems, backend, cloud, deployment, and scale.</desc>
  <defs>
    <linearGradient id="background" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#07111f"/>
      <stop offset="0.58" stop-color="#0b1728"/>
      <stop offset="1" stop-color="#101827"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#22d3ee"/>
      <stop offset="0.55" stop-color="#60a5fa"/>
      <stop offset="1" stop-color="#a78bfa"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#102235"/>
      <stop offset="1" stop-color="#0a1625"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop offset="0" stop-color="#22d3ee" stop-opacity=".16"/>
      <stop offset="1" stop-color="#22d3ee" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#93c5fd" stroke-opacity=".035"/>
    </pattern>
    <clipPath id="screen"><rect x="24" y="24" width="1152" height="382" rx="18"/></clipPath>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#000814" flood-opacity=".55"/>
    </filter>
    <filter id="softGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      text { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
      .eyebrow { fill:#7dd3fc; font-size:13px; letter-spacing:1.6px; }
      .panel-title { fill:#e2e8f0; font-size:14px; font-weight:700; letter-spacing:.7px; }
      .panel-copy { fill:#8fa6bf; font-size:12px; }
      .flow { animation:flow 2.6s linear infinite; }
      .cursor { animation:blink 1s steps(1,end) infinite; }
      .signal { animation:signal 4.8s ease-in-out infinite; }
      .signal-delay { animation-delay:1.2s; }
      .signal-delay-2 { animation-delay:2.4s; }
      .signal-delay-3 { animation-delay:3.6s; }
      @keyframes flow { to { stroke-dashoffset:-30; } }
      @keyframes blink { 50% { opacity:0; } }
      @keyframes signal { 0%,22%,100% { stroke:#1e3a4a; } 8%,14% { stroke:#22d3ee; } }
      @media (prefers-reduced-motion: reduce) {
        .flow,.cursor,.signal { animation:none; }
      }
    </style>
  </defs>

  <rect width="1200" height="430" rx="24" fill="#030712"/>
  <rect x="24" y="24" width="1152" height="382" rx="18" fill="url(#background)" filter="url(#shadow)"/>
  <g clip-path="url(#screen)">
    <rect x="24" y="24" width="1152" height="382" fill="url(#grid)"/>
    <circle cx="1030" cy="80" r="290" fill="url(#glow)"/>
    <rect x="24" y="24" width="1152" height="48" fill="#0a1220"/>
    <circle cx="52" cy="48" r="6" fill="#fb7185"/>
    <circle cx="74" cy="48" r="6" fill="#fbbf24"/>
    <circle cx="96" cy="48" r="6" fill="#34d399"/>
    <text x="600" y="54" text-anchor="middle" fill="#718096" font-size="14">~/product-engineering</text>
  </g>

  <g>
    <text x="68" y="108" class="eyebrow">MOBILE · SYSTEMS · PRODUCT</text>
    <text x="68" y="151" fill="#f8fafc" font-size="38" font-weight="700">Saifuddin Adenwala</text>
    <text x="68" y="181" fill="#7dd3fc" font-size="19">Mobile &amp; Full-Stack Product Engineer</text>

    <text x="1132" y="112" text-anchor="end" fill="#718096" font-size="12" letter-spacing="1.2px">OPEN SOURCE</text>
    <text x="1132" y="142" text-anchor="end" fill="#a5f3fc" font-size="17">30+ merged upstream PRs</text>
  </g>

  <g>
    <text x="68" y="219" fill="#d8e2f0" font-size="17"><tspan fill="#34d399">$</tspan> build-product --targets all<tspan class="cursor" fill="#22d3ee">_</tspan></text>
    <path d="M68 232H1132" stroke="url(#accent)" stroke-width="1.5" stroke-dasharray="7 8" opacity=".6" class="flow"/>
  </g>

  <g>
    <rect x="68" y="252" width="257" height="76" rx="12" fill="url(#panel)" stroke="#1e3a4a" class="signal"/>
    <text x="88" y="279" class="panel-title">01  NATIVE MOBILE</text>
    <text x="88" y="306" class="panel-copy">Kotlin · Swift · watchOS</text>

    <rect x="337" y="252" width="257" height="76" rx="12" fill="url(#panel)" stroke="#1e3a4a" class="signal signal-delay"/>
    <text x="357" y="279" class="panel-title">02  CROSS-PLATFORM</text>
    <text x="357" y="306" class="panel-copy">Flutter · Kotlin Multiplatform</text>

    <rect x="606" y="252" width="257" height="76" rx="12" fill="url(#panel)" stroke="#1e3a4a" class="signal signal-delay-2"/>
    <text x="626" y="279" class="panel-title">03  CONNECTED SYSTEMS</text>
    <text x="626" y="306" class="panel-copy">BLE · IoT · Realtime</text>

    <rect x="875" y="252" width="257" height="76" rx="12" fill="url(#panel)" stroke="#1e3a4a" class="signal signal-delay-3"/>
    <text x="895" y="279" class="panel-title">04  PRODUCT INFRA</text>
    <text x="895" y="306" class="panel-copy">Backend · Cloud · CI/CD</text>
  </g>

  <g>
    <text x="68" y="371" fill="#718096" font-size="12" letter-spacing="1.4px">DELIVERY PIPELINE</text>
    <text x="238" y="371" fill="#d8e2f0" font-size="14">IDEA</text>
    <text x="296" y="371" fill="#22d3ee" font-size="14">→</text>
    <text x="330" y="371" fill="#d8e2f0" font-size="14">ARCHITECTURE</text>
    <text x="454" y="371" fill="#22d3ee" font-size="14">→</text>
    <text x="488" y="371" fill="#d8e2f0" font-size="14">BUILD</text>
    <text x="546" y="371" fill="#22d3ee" font-size="14">→</text>
    <text x="580" y="371" fill="#d8e2f0" font-size="14">DEPLOY</text>
    <text x="646" y="371" fill="#22d3ee" font-size="14">→</text>
    <text x="680" y="371" fill="#d8e2f0" font-size="14">OBSERVE</text>
    <text x="756" y="371" fill="#22d3ee" font-size="14">→</text>
    <text x="790" y="371" fill="#d8e2f0" font-size="14">SCALE</text>
    <path d="M852 366H1132" stroke="#164e63" stroke-width="2" stroke-dasharray="5 8" class="flow"/>
    <circle cx="1128" cy="366" r="4" fill="#22d3ee" filter="url(#softGlow)"/>
  </g>
</svg>
'''


def main() -> None:
    OUTPUT.write_text(build_svg(), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
