"""Unit tests for the metadata-only research report generator."""
import json
import tempfile
import unittest
from pathlib import Path

from generate_research_report import build_html, build_markdown, load_inventory, load_sources

ROOT = Path(__file__).resolve().parents[1]


class ResearchReportTests(unittest.TestCase):
    def test_repository_metadata_generates_report(self) -> None:
        inventory = load_inventory(ROOT / "devices/moto-g60/hardware-inventory.csv")
        sources = load_sources(ROOT / "docs/research-sources.json")
        report = build_markdown(inventory, sources)
        self.assertIn("Research-only", report)
        self.assertIn("efi_environment", report)
        self.assertIn("Does not establish", report)
        self.assertIn("No network requests", report)

    def test_unknowns_are_counted_without_guessing(self) -> None:
        inventory = load_inventory(ROOT / "devices/moto-g60/hardware-inventory.csv")
        report = build_markdown(inventory, [])
        self.assertIn(f"- Unknown: {sum(row['status'] == 'unknown' for row in inventory)}", report)

    def test_rejects_duplicate_source_ids(self) -> None:
        data = {"schema_version": 1, "sources": [
            {"id": "same", "title": "A", "url": "https://example.com/a", "category": "test",
             "confidence": "test", "supports": "A", "limitations": "B"},
            {"id": "same", "title": "B", "url": "https://example.com/b", "category": "test",
             "confidence": "test", "supports": "B", "limitations": "C"}
        ]}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sources.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate source id"):
                load_sources(path)

    def test_rejects_non_https_source(self) -> None:
        data = {"schema_version": 1, "sources": [
            {"id": "bad", "title": "A", "url": "http://example.com", "category": "test",
             "confidence": "test", "supports": "A", "limitations": "B"}
        ]}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sources.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "HTTPS"):
                load_sources(path)

    def test_html_escapes_report_text(self) -> None:
        rendered = build_html("# Report <script>alert('x')</script>")
        self.assertNotIn("<script>", rendered)
        self.assertIn("&lt;script&gt;", rendered)

    def test_rejects_unknown_inventory_status(self) -> None:
        inventory_path = ROOT / "devices/moto-g60/hardware-inventory.csv"
        text = inventory_path.read_text(encoding="utf-8").replace(
            "device_family,family-reported", "device_family,unverified"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.csv"
            path.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Unsupported status"):
                load_inventory(path)


if __name__ == "__main__":
    unittest.main()
