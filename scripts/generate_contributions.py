#!/usr/bin/env python3
"""Render a self-hosted SVG from GitHub's public contribution calendar."""

from __future__ import annotations

import re
import urllib.request
from datetime import date
from html import escape
from html.parser import HTMLParser
from pathlib import Path


USERNAME = "Saifuddin53"
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "contribution-graph.svg"


class ContributionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.days: dict[str, dict[str, str | int]] = {}
        self.tooltip_for: str | None = None
        self.tooltip_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "td" and values.get("data-date"):
            cell_id = values.get("id", "")
            self.days[cell_id] = {
                "date": values["data-date"] or "",
                "level": int(values.get("data-level", "0") or 0),
                "count": 0,
            }
        elif tag == "tool-tip" and values.get("for") in self.days:
            self.tooltip_for = values["for"]
            self.tooltip_text = []

    def handle_data(self, data: str) -> None:
        if self.tooltip_for:
            self.tooltip_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "tool-tip" or not self.tooltip_for:
            return
        text = "".join(self.tooltip_text).strip()
        match = re.match(r"(\d+) contributions?", text)
        if match:
            self.days[self.tooltip_for]["count"] = int(match.group(1))
        self.tooltip_for = None
        self.tooltip_text = []


def fetch_days() -> list[dict[str, str | int]]:
    request = urllib.request.Request(
        f"https://github.com/users/{USERNAME}/contributions",
        headers={"User-Agent": f"{USERNAME}-profile-readme"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8")

    parser = ContributionParser()
    parser.feed(html)
    days = sorted(parser.days.values(), key=lambda day: str(day["date"]))
    if not days:
        raise RuntimeError("GitHub returned no contribution-calendar cells")
    return days


def month_labels(days: list[dict[str, str | int]], start: date) -> list[tuple[int, str]]:
    labels: list[tuple[int, str]] = []
    seen: set[tuple[int, int]] = set()
    for day in days:
        current = date.fromisoformat(str(day["date"]))
        key = (current.year, current.month)
        if key in seen:
            continue
        seen.add(key)
        column = (current - start).days // 7
        labels.append((column, current.strftime("%b")))
    return labels


def build_svg(days: list[dict[str, str | int]]) -> str:
    start = date.fromisoformat(str(days[0]["date"]))
    x0, y0, cell, gap = 84, 78, 14, 4
    palette = ["#182235", "#164e63", "#0e7490", "#06b6d4", "#67e8f9"]
    cells: list[str] = []

    for index, day in enumerate(days):
        current = date.fromisoformat(str(day["date"]))
        column = (current - start).days // 7
        row = (current.weekday() + 1) % 7
        x = x0 + column * (cell + gap)
        y = y0 + row * (cell + gap)
        level = int(day["level"])
        count = int(day["count"])
        label = f"{current.strftime('%b %d, %Y')}: {count} contribution{'s' if count != 1 else ''}"
        delay = min(1.75, 0.025 * column + 0.018 * row)
        cells.append(
            f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" '
            f'fill="{palette[level]}" opacity="0"><title>{escape(label)}</title>'
            f'<animate attributeName="opacity" from="0" to="1" dur=".35s" begin="{delay:.3f}s" fill="freeze"/></rect>'
        )

    labels = []
    for column, label in month_labels(days, start):
        x = x0 + column * (cell + gap)
        labels.append(f'<text x="{x}" y="58" class="month">{label}</text>')

    total = sum(int(day["count"]) for day in days)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="245" viewBox="0 0 1120 245" role="img" aria-labelledby="title desc">
  <title id="title">Public GitHub contributions for the last 12 months</title>
  <desc id="desc">An animated calendar heatmap showing {total:,} public contribution events by Saifuddin Adenwala.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#07111f"/>
      <stop offset="1" stop-color="#101827"/>
    </linearGradient>
    <style>
      text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
      .heading {{ fill:#e5edf8; font-size:17px; font-weight:600; }}
      .subtle,.month,.day {{ fill:#718096; font-size:12px; }}
      .pulse {{ animation:pulse 2.8s ease-in-out infinite; }}
      @keyframes pulse {{ 0%,100% {{ opacity:.35; }} 50% {{ opacity:1; }} }}
      @media (prefers-reduced-motion: reduce) {{ .pulse {{ animation:none; }} }}
    </style>
  </defs>
  <rect width="1120" height="245" rx="18" fill="url(#bg)"/>
  <rect x="1" y="1" width="1118" height="243" rx="17" fill="none" stroke="#20304a"/>
  <circle cx="27" cy="29" r="4" fill="#22d3ee" class="pulse"/>
  <text x="40" y="35" class="heading">public contribution rhythm</text>
  <text x="1090" y="35" text-anchor="end" class="subtle">last 12 months</text>
  {''.join(labels)}
  <text x="48" y="108" class="day">Mon</text>
  <text x="48" y="144" class="day">Wed</text>
  <text x="48" y="180" class="day">Fri</text>
  {''.join(cells)}
  <g transform="translate(815 222)">
    <text x="0" y="0" class="subtle">less</text>
    <rect x="38" y="-11" width="12" height="12" rx="3" fill="{palette[0]}"/>
    <rect x="56" y="-11" width="12" height="12" rx="3" fill="{palette[1]}"/>
    <rect x="74" y="-11" width="12" height="12" rx="3" fill="{palette[2]}"/>
    <rect x="92" y="-11" width="12" height="12" rx="3" fill="{palette[3]}"/>
    <rect x="110" y="-11" width="12" height="12" rx="3" fill="{palette[4]}"/>
    <text x="132" y="0" class="subtle">more</text>
  </g>
</svg>
'''


def main() -> None:
    OUTPUT.write_text(build_svg(fetch_days()), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
