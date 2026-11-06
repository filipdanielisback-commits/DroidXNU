#!/usr/bin/env python3
"""Generate a metadata-only DroidXNU research report; never accesses the network or a device."""
from __future__ import annotations

import argparse
import csv
import html
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INVENTORY = ROOT / "devices" / "moto-g60" / "hardware-inventory.csv"
DEFAULT_SOURCES = ROOT / "docs" / "research-sources.json"
DEFAULT_OUTPUT = ROOT / "build" / "research-report.md"
VALID_INVENTORY_STATUSES = {"unknown", "family-reported", "model-confirmed", "researched"}


def load_inventory(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"subsystem", "status", "reported_value", "evidence", "open_question"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError("Hardware inventory is empty or missing required columns")
    seen: set[str] = set()
    for row in rows:
        name = row["subsystem"].strip()
        status = row["status"].strip()
        if not name or name in seen:
            raise ValueError(f"Blank or duplicate hardware subsystem: {name!r}")
        if status not in VALID_INVENTORY_STATUSES:
            raise ValueError(f"Unsupported status for {name}: {status!r}")
        if not row["reported_value"].strip() or not row["open_question"].strip():
            raise ValueError(f"Missing value or open question for subsystem: {name}")
        if status != "unknown" and not row["evidence"].strip():
            raise ValueError(f"Non-unknown subsystem lacks evidence: {name}")
        seen.add(name)
    return rows


def load_sources(path: Path) -> list[dict[str, str]]:
    data: Any = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not isinstance(data.get("sources"), list):
        raise ValueError("Unsupported source register schema")
    required = {"id", "title", "url", "category", "confidence", "supports", "limitations"}
    sources = data["sources"]
    seen: set[str] = set()
    for source in sources:
        if not isinstance(source, dict) or not required.issubset(source):
            raise ValueError("Each source must include all required metadata fields")
        if any(not isinstance(source[key], str) or not source[key].strip() for key in required):
            raise ValueError("Source metadata fields must be non-empty strings")
        if source["id"] in seen:
            raise ValueError(f"Duplicate source id: {source['id']}")
        if not source["url"].startswith("https://"):
            raise ValueError(f"Source URL must use HTTPS: {source['id']}")
        seen.add(source["id"])
    return sources


def build_markdown(inventory: list[dict[str, str]], sources: list[dict[str, str]]) -> str:
    counts = Counter(row["status"] for row in inventory)
    lines = [
        "# DroidXNU research status report",
        "",
        "> Generated from repository metadata only. No network requests, device access, hardware probing, builds, or boot tests are performed.",
        "",
        "## Project status",
        "",
        "**Research-only.** No XNU port, EFI loader, device driver set, bootable image, or iOS compatibility has been demonstrated.",
        "",
        "## Hardware inventory",
        "",
        f"- Subsystems tracked: {len(inventory)}",
        f"- Unknown: {counts['unknown']}",
        f"- Family-reported: {counts['family-reported']}",
        f"- Model-confirmed: {counts['model-confirmed']}",
        f"- Researched: {counts['researched']}",
        "",
        "| Subsystem | Status | Current record | Evidence reference | Open question |",
        "|---|---|---|---|---|",
    ]
    for row in inventory:
        evidence = f"[reference]({row['evidence']})" if row["evidence"].strip() else "—"
        values = [row["subsystem"], row["status"], row["reported_value"], evidence, row["open_question"]]
        lines.append("| " + " | ".join(value.replace("|", "\\|").replace("\n", " ") for value in values) + " |")
    lines.extend(["", "## Source register", "", f"Curated references: {len(sources)}", ""])
    for source in sources:
        lines.extend([
            f"### {source['title']}",
            "",
            f"- Reference: [{source['url']}]({source['url']})",
            f"- Category / confidence: {source['category']} / {source['confidence']}",
            f"- Supports: {source['supports']}",
            f"- Does not establish: {source['limitations']}",
            "",
        ])
    lines.extend([
        "## Current engineering gates",
        "",
        "- Exact XT2135-2 board and SoC identity remain to be verified from model-matched evidence.",
        "- Boot-chain and EFI availability remain unknown; an Android bootloader is not assumed to provide UEFI.",
        "- XNU ARM64 platform requirements have not yet been mapped to this device.",
        "- No physical-device experimentation is part of the current roadmap.",
        "- Project-wide licensing remains to be selected.",
        "",
        "## Reproducibility",
        "",
        "Run `make report` to regenerate this file. Run `make check` to validate repository metadata and execute host-side unit tests.",
        "",
    ])
    return "\n".join(lines)


def build_html(markdown_text: str) -> str:
    # Keep the optional HTML artifact dependency-free and safe: render the report as escaped preformatted text.
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>DroidXNU research status</title>\n"
        "<style>body{font:16px/1.55 system-ui,sans-serif;max-width:1100px;margin:2rem auto;padding:0 1rem}"
        "pre{white-space:pre-wrap;overflow-wrap:anywhere}</style>\n</head>\n<body>\n"
        f"<pre>{html.escape(markdown_text)}</pre>\n</body>\n</html>\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--html-output", type=Path, help="Also write an escaped, dependency-free HTML report")
    args = parser.parse_args()
    try:
        report = build_markdown(load_inventory(args.inventory), load_sources(args.sources))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        if args.html_output:
            args.html_output.parent.mkdir(parents=True, exist_ok=True)
            args.html_output.write_text(build_html(report), encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError, csv.Error) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print(f"DroidXNU research report written: {args.output}")
    if args.html_output:
        print(f"DroidXNU HTML report written: {args.html_output}")
    print("Metadata-only output; no network or device access performed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
