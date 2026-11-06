#!/usr/bin/env python3
"""Validate the Moto G60 research inventory; never accesses a device."""
from __future__ import annotations
import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "devices" / "moto-g60" / "hardware-inventory.csv"
COLUMNS = {"subsystem", "status", "reported_value", "evidence", "open_question"}
REQUIRED = {
    "device_family", "soc", "cpu_architecture", "memory", "interrupt_controller",
    "timers", "boot_chain", "efi_environment", "storage", "display_gpu", "touch",
    "usb", "wifi_bluetooth", "audio", "sensors", "power_thermal",
}
STATUSES = {"unknown", "family-reported", "model-confirmed", "researched"}


def validate_inventory(path: Path) -> list[str]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            missing = COLUMNS - set(reader.fieldnames or [])
            if missing:
                return [f"Missing CSV columns: {', '.join(sorted(missing))}"]
            rows = list(reader)
    except (OSError, csv.Error, UnicodeError) as exc:
        return [f"Could not read inventory: {exc}"]

    errors: list[str] = []
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        name = (row.get("subsystem") or "").strip()
        status = (row.get("status") or "").strip()
        value = (row.get("reported_value") or "").strip()
        evidence = (row.get("evidence") or "").strip()
        question = (row.get("open_question") or "").strip()
        if not name:
            errors.append(f"Line {line}: subsystem is blank")
            continue
        if name in seen:
            errors.append(f"Line {line}: duplicate subsystem {name!r}")
        seen.add(name)
        if status not in STATUSES:
            errors.append(f"Line {line}: unsupported status {status!r}")
        if not value:
            errors.append(f"Line {line}: reported_value is blank for {name}")
        if status != "unknown" and not evidence:
            errors.append(f"Line {line}: {name} needs an evidence reference")
        if not question:
            errors.append(f"Line {line}: open_question is blank for {name}")
    for name in sorted(REQUIRED - seen):
        errors.append(f"Missing required subsystem: {name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inventory", nargs="?", type=Path, default=DEFAULT)
    errors = validate_inventory(parser.parse_args().inventory)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("DroidXNU hardware inventory: structurally valid")
    print("Research metadata only; no device access or hardware probing")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
