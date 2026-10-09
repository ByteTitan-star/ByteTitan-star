#!/usr/bin/env python3
"""Inject a count-up (0 -> value) SMIL animation into the 3-stats summary cards.

GitHub renders README images through <img>, where scripts never execute but
SMIL animations do play, and the timeline restarts on every page load. Each
stats number is rewritten as a stack of frame <text> elements that are revealed
one by one with an ease-out curve, so the value appears to count up from 0.

Runs after the cards are regenerated (see .github/workflows/stats.yml) so the
effect survives the daily refresh. Idempotent: animated files no longer match
the plain-number pattern and are left untouched.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGETS = [
    ROOT / "profile-summary-card-output" / "github" / "3-stats.svg",
    ROOT / "profile-summary-card-output" / "github_dark" / "3-stats.svg",
]

SLICES = 18   # keyframes sampled per number
DUR = 1.5     # seconds each number takes to count up
STAGGER = 0.08  # delay per row (5 rows -> last number ends at 1.82s)

# value texts are the only purely-numeric <text> elements in the card
TEXT_RE = re.compile(r'<text ([^>]*?)>(\d+(?:\.\d+)?k?)</text>')
NUM_RE = re.compile(r'^(\d+(?:\.\d+)?)(k?)$')


def fmt(v: float, k: bool) -> str:
    if v <= 0:
        return "0"
    return f"{v / 1000:.1f}k" if k else str(int(round(v)))


def frames_for(target: float, k: bool):
    """(label, eased-time-pos) pairs counting 0 -> target, duplicates dropped."""
    out = []
    for j in range(SLICES):
        t = j / (SLICES - 1)
        eased = 1 - (1 - t) ** 3  # ease-out cubic
        v = target * eased
        v = round(v / 100) * 100 if k else round(v)  # k values tick in 0.1k steps
        label = fmt(v, k)
        if not out or out[-1][0] != label:
            out.append((label, t))
    final = fmt(target, k)
    if out[-1][0] != final:
        out.append((final, 1.0))
    return out


def animate(match: re.Match) -> str:
    attrs, label = match.group(1), match.group(2)
    m = NUM_RE.match(label)
    num, k = float(m.group(1)), bool(m.group(2))
    target = num * (1000 if k else 1)

    idx_m = re.search(r'--gpsc-i:\s*(\d+)', attrs)
    t0 = (int(idx_m.group(1)) if idx_m else 0) * STAGGER

    frames = frames_for(target, k)
    texts = []
    for fi, (lab, tpos) in enumerate(frames):
        begin = t0 + tpos * DUR
        end = t0 + (frames[fi + 1][1] if fi + 1 < len(frames) else 1.0) * DUR
        freeze = ' fill="freeze"' if fi == len(frames) - 1 else ""
        anim = (
            f'<animate attributeName="opacity" values="1;1" calcMode="discrete" '
            f'begin="{begin:.2f}s" dur="{max(end - begin, 0.02):.2f}s"{freeze}/>'
        )
        texts.append(f'<text {attrs} opacity="0">{lab}{anim}</text>')
    return "".join(texts)


def main() -> None:
    for path in TARGETS:
        svg = path.read_text()
        patched, n = TEXT_RE.subn(animate, svg)
        if n == 0:
            print(f"{path.relative_to(ROOT)}: no numeric texts found (already animated?)")
            continue
        path.write_text(patched)
        print(f"{path.relative_to(ROOT)}: animated {n} numbers")


if __name__ == "__main__":
    main()
