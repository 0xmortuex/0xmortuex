#!/usr/bin/env python3
"""Generate the profile README stat cards as SVGs (light + dark).

Runs in CI (see .github/workflows/stats.yml) so the cards are served from
raw.githubusercontent.com — no third-party stats service, nothing to 503,
nothing for an ad-blocker to eat.

    GITHUB_TOKEN=... python .github/scripts/gen_stats.py

Writes generated/overview-{light,dark}.svg and generated/languages-{light,dark}.svg.
"""
import json
import os
import sys
import urllib.request

USER = "0xmortuex"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "generated")
API = "https://api.github.com"

# Colors follow the entity (the language), never its rank. Hues come from a
# CVD-validated categorical palette, stepped separately for GitHub's light
# (#ffffff) and dark (#0d1117) README surfaces.
LANG_COLORS = {  # name: (light, dark)
    "JavaScript": ("#eda100", "#c98500"),
    "Python": ("#2a78d6", "#3987e5"),
    "HTML": ("#eb6834", "#d95926"),
    "CSS": ("#4a3aa7", "#9085e9"),
    "TypeScript": ("#0f9bbd", "#1ba3c7"),
    "Lua": ("#e87ba4", "#d55181"),
    "Shell": ("#008300", "#008300"),
    "Assembly": ("#e34948", "#e66767"),
}
FALLBACK = ("#818b98", "#818b98")

INK = {
    "light": {"primary": "#1f2328", "secondary": "#59636e", "accent": "#2a78d6",
              "hairline": "#d1d9e0"},
    "dark": {"primary": "#e6edf3", "secondary": "#9198a1", "accent": "#3987e5",
             "hairline": "#30363d"},
}

FONT = 'font-family="system-ui,-apple-system,\'Segoe UI\',sans-serif"'

# Simplified 16x16 octicon-style glyphs, drawn with the accent color.
ICONS = {
    "star": "M8 .5l2.1 4.4 4.9.7-3.5 3.4.8 4.8L8 11.5l-4.3 2.3.8-4.8L1 5.6l4.9-.7z",
    "repo": "M3 1.5h9a1 1 0 0 1 1 1v11l-3-1.8-3 1.8-3-1.8-2 1.2v-10.4a1 1 0 0 1 1-1z",
    "people": "M5.5 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM.5 14c0-2.8 2.2-5 5-5s5 2.2 5 5zm10.4-6.3a3 3 0 0 0 0-5.4 3.3 3.3 0 0 1 0 5.4zm1.6 6.3c0-1.7-.7-3.3-1.8-4.4 2.5.4 4.3 2.2 4.3 4.4z",
    "fork": "M5 3a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm9 0a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zM3.5 4.5v2A2.5 2.5 0 0 0 6 9h1v2.6a1.5 1.5 0 1 0 1 0V9h1a2.5 2.5 0 0 0 2.5-2.5v-2h-1v2A1.5 1.5 0 0 1 9 8H6a1.5 1.5 0 0 1-1.5-1.5v-2z",
}


def get(path):
    req = urllib.request.Request(API + path, headers={
        "Authorization": "Bearer " + os.environ["GITHUB_TOKEN"],
        "Accept": "application/vnd.github+json",
        "User-Agent": "gen-stats",
    })
    with urllib.request.urlopen(req) as r:
        link = r.headers.get("Link", "")
        return json.load(r), link


def get_all(path):
    items, page = [], 1
    while True:
        chunk, link = get(f"{path}{'&' if '?' in path else '?'}per_page=100&page={page}")
        items += chunk
        if 'rel="next"' not in link:
            return items
        page += 1


def compact(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 10_000:
        return f"{n / 1000:.0f}K"
    if n >= 1_000:
        return f"{n / 1000:.1f}K"
    return str(n)


def fetch():
    user, _ = get(f"/users/{USER}")
    repos = [r for r in get_all(f"/users/{USER}/repos?type=owner") if not r["fork"]]
    stars = sum(r["stargazers_count"] for r in repos)
    forks = sum(r["forks_count"] for r in repos)
    langs = {}
    for r in repos:
        data, _ = get(f"/repos/{r['full_name']}/languages")
        for lang, size in data.items():
            langs[lang] = langs.get(lang, 0) + size
    return {
        "followers": user["followers"],
        "repos": len(repos),
        "stars": stars,
        "forks": forks,
        "langs": sorted(langs.items(), key=lambda kv: -kv[1]),
    }


def overview_svg(s, mode):
    ink = INK[mode]
    tiles = [("star", "Total stars", s["stars"]), ("people", "Followers", s["followers"]),
             ("repo", "Public repos", s["repos"]), ("fork", "Forks of my repos", s["forks"])]
    cells = []
    for i, (icon, label, value) in enumerate(tiles):
        x, y = 32 + (i % 2) * 210, 62 + (i // 2) * 62
        cells.append(f"""
  <g transform="translate({x},{y})">
    <path d="{ICONS[icon]}" fill="{ink['accent']}" transform="translate(0,4)"/>
    <text x="26" y="14" font-size="12" fill="{ink['secondary']}" {FONT}>{label}</text>
    <text x="26" y="40" font-size="24" font-weight="600" fill="{ink['primary']}" {FONT}>{compact(value)}</text>
  </g>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="450" height="195" viewBox="0 0 450 195" role="img" aria-label="GitHub stats for {USER}">
  <text x="32" y="36" font-size="15" font-weight="600" fill="{ink['primary']}" {FONT}>Fadi &#183; {USER} &#8212; GitHub stats</text>
  <line x1="32" y1="48" x2="418" y2="48" stroke="{ink['hairline']}" stroke-width="1"/>
  {''.join(cells)}
</svg>
"""


def bar_path(x, y, w, h):
    # Square at the baseline (left), 4px rounded data-end (right).
    r = min(4, w / 2, h / 2)
    return (f"M{x} {y} h{w - r:.1f} a{r} {r} 0 0 1 {r} {r} v{h - 2 * r:.1f} "
            f"a{r} {r} 0 0 1 -{r} {r} h-{w - r:.1f} z")


def languages_svg(s, mode):
    ink = INK[mode]
    ci = 0 if mode == "light" else 1
    top = s["langs"][:6]
    total = sum(size for _, size in s["langs"]) or 1
    biggest = top[0][1] if top else 1
    x0, xmax = 150, 380
    rows = []
    for i, (lang, size) in enumerate(top):
        y = 64 + i * 22
        color = LANG_COLORS.get(lang, FALLBACK)[ci]
        w = max(6, (size / biggest) * (xmax - x0))
        pct = 100 * size / total
        pct_txt = f"{pct:.1f}%" if pct < 10 else f"{pct:.0f}%"
        rows.append(f"""
  <circle cx="38" cy="{y + 5}" r="4" fill="{color}"/>
  <text x="50" y="{y + 9}" font-size="12" fill="{ink['primary']}" {FONT}>{lang}</text>
  <path d="{bar_path(x0, y, w, 10)}" fill="{color}"/>
  <text x="{x0 + w + 8:.1f}" y="{y + 9}" font-size="11" fill="{ink['secondary']}" {FONT}>{pct_txt}</text>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="450" height="195" viewBox="0 0 450 195" role="img" aria-label="Most used languages for {USER}">
  <text x="32" y="36" font-size="15" font-weight="600" fill="{ink['primary']}" {FONT}>Top languages, by code size</text>
  <line x1="32" y1="48" x2="418" y2="48" stroke="{ink['hairline']}" stroke-width="1"/>
  {''.join(rows)}
</svg>
"""


def main():
    if not os.environ.get("GITHUB_TOKEN"):
        sys.exit("GITHUB_TOKEN is required")
    s = fetch()
    os.makedirs(OUT, exist_ok=True)
    for mode in ("light", "dark"):
        for name, svg in (("overview", overview_svg(s, mode)),
                          ("languages", languages_svg(s, mode))):
            path = os.path.join(OUT, f"{name}-{mode}.svg")
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(svg)
            print("wrote", os.path.relpath(path))
    print("languages:", [(l, f"{100 * v / sum(x for _, x in s['langs']):.1f}%")
                         for l, v in s["langs"][:8]])


if __name__ == "__main__":
    main()
