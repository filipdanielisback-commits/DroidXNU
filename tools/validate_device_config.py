#!/usr/bin/env python3
"""Validate DroidXNU's Moto G60 metadata without accessing any device."""

from __future__ import annotations

import argparse
import configparser
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "devices" / "moto-g60" / "device.conf"
REQUIRED_VALUES = {
    ("device", "name"): "Motorola Moto G60",
    ("device", "model"): "XT2135-2",
    ("device", "status"): "research-only",
}
REQUIRED_FALSE_FLAGS = (
    ("safety", "writes_to_device"),
    ("safety", "firmware_in_repository"),
    ("safety", "bootable_image_available"),
)


def _unquote(value: str) -> str:
    """Accept ordinary INI values and values wrapped in matching double quotes."""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def validate_config(path: Path) -> list[str]:
    """Return validation errors; an empty list means the metadata is valid."""
    parser = configparser.ConfigParser()
    try:
        loaded = parser.read(path, encoding="utf-8")
    except (OSError, configparser.Error) as exc:
        return [f"Could not read configuration: {exc}"]

    if not loaded:
        return [f"Configuration file not found or unreadable: {path}"]

    errors: list[str] = []
    for (section, key), expected in REQUIRED_VALUES.items():
        if not parser.has_option(section, key):
            errors.append(f"Missing [{section}] {key}")
            continue
        actual = _unquote(parser.get(section, key))
        if actual != expected:
            errors.append(f"[{section}] {key} must be {expected!r}, not {actual!r}")

    for section, key in REQUIRED_FALSE_FLAGS:
        if not parser.has_option(section, key):
            errors.append(f"Missing [{section}] {key}")
            continue
        value = _unquote(parser.get(section, key)).lower()
        if value not in {"true", "false"}:
            errors.append(f"[{section}] {key} must be true or false")
        elif value == "true":
            errors.append(f"[{section}] {key} must remain false in this research phase")

    return errors


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("config", nargs="?", type=Path, default=DEFAULT_CONFIG)
    args = cli.parse_args()

    errors = validate_config(args.config)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("DroidXNU device metadata: valid")
    print("Target: Motorola Moto G60 (XT2135-2)")
    print("Mode: research-only; no device operations are performed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
