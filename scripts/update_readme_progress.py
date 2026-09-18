from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARD = ROOT / "assets/readme/progress-card.svg"
MINI = ROOT / "assets/readme/progress-mini.svg"
README = ROOT / "README.md"
STATUS = ROOT / "STATUS.md"
LEGACY_PATTERNS = (
    re.compile(r"[█▓▒░]{4,}"),
    re.compile(r"\[(?:[#=\-]{4,})\]"),
)


def card_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="180" viewBox="0 0 1200 180" role="img" aria-labelledby="title desc">
  <title id="title">Ryzen 5 5600G + A320M EFI product progress</title><desc id="desc">Product progress is N/A because this hardware-specific reference has no authoritative product roadmap.</desc>
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#02050A"/><stop offset="1" stop-color="#07111C"/></linearGradient><pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M36 0H0V36" fill="none" stroke="#62E5FF" stroke-opacity=".05"/></pattern></defs>
  <rect x="1" y="1" width="1198" height="178" rx="22" fill="url(#bg)" stroke="#62E5FF" stroke-opacity=".24"/><rect x="1" y="1" width="1198" height="178" rx="22" fill="url(#grid)"/>
  <text x="50" y="38" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="700" letter-spacing="3">SWIR PROGRESS</text>
  <text x="50" y="76" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="26" font-weight="800">Ryzen 5 5600G + A320M EFI</text>
  <text x="50" y="103" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="14">Hardware reference scope · no authoritative product roadmap</text>
  <text x="1150" y="76" text-anchor="end" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="32" font-weight="800">N/A</text>
  <rect x="50" y="120" width="1100" height="16" rx="8" fill="#0B1928" stroke="#62E5FF" stroke-opacity=".16"/>
  <text x="50" y="160" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="12">Hardware-specific configuration · no universal compatibility or release-readiness score.</text>
</svg>
"""


def mini_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" width="900" height="72" viewBox="0 0 900 72" role="img" aria-labelledby="title desc">
  <title id="title">Ryzen 5 5600G + A320M EFI product progress</title><desc id="desc">N/A product progress; no authoritative roadmap exists.</desc>
  <rect x="1" y="1" width="898" height="70" rx="16" fill="#02050A" stroke="#62E5FF" stroke-opacity=".25"/>
  <text x="24" y="28" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700">Ryzen 5 5600G + A320M EFI · hardware-reference progress</text>
  <text x="24" y="51" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="12">No authoritative roadmap — numeric fallback: N/A</text>
  <text x="868" y="43" text-anchor="end" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="22" font-weight="800">N/A</text>
</svg>
"""


def validate_svg(text: str) -> None:
    root = ET.fromstring(text)
    values = root.attrib.get("viewBox", "").split()
    if root.tag.rsplit("}", 1)[-1] != "svg" or len(values) != 4:
        raise ValueError("invalid SVG root/viewBox")
    for value in values:
        float(value)


def expected() -> dict[Path, str]:
    return {CARD: card_svg(), MINI: mini_svg()}


def check() -> int:
    errors: list[str] = []
    for path, text in expected().items():
        validate_svg(text)
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            errors.append(f"stale generated file: {path.relative_to(ROOT)}")
    for path in (README, STATUS):
        text = path.read_text(encoding="utf-8")
        if any(pattern.search(text) for pattern in LEGACY_PATTERNS):
            errors.append(f"legacy progress meter detected in {path.relative_to(ROOT)}")
    if "assets/readme/progress-card.svg" not in README.read_text(encoding="utf-8"):
        errors.append("README does not embed progress-card.svg")
    if "assets/readme/progress-mini.svg" not in STATUS.read_text(encoding="utf-8"):
        errors.append("STATUS.md does not embed progress-mini.svg")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Ryzen 5 5600G + A320M EFI: product progress = N/A (no authoritative roadmap)")
    return 0


def write() -> None:
    for path, text in expected().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        validate_svg(text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        write()
    return check()


if __name__ == "__main__":
    raise SystemExit(main())
