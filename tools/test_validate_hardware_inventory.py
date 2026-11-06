"""Unit tests for the host-only hardware inventory validator."""
import tempfile
import unittest
from pathlib import Path
from validate_hardware_inventory import validate_inventory

HEADER = "subsystem,status,reported_value,evidence,open_question\n"
BASE = (
    "device_family,family-reported,hanoip,https://example.invalid/source,Verify exact model mapping\n"
    "soc,unknown,Unknown,,Verify exact SoC\n"
)


class ValidateHardwareInventoryTests(unittest.TestCase):
    def validate_text(self, content: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.csv"
            path.write_text(content, encoding="utf-8")
            return validate_inventory(path)

    def test_accepts_valid_rows(self) -> None:
        self.assertEqual(self.validate_text(HEADER + BASE), [])

    def test_rejects_duplicate_subsystems(self) -> None:
        errors = self.validate_text(HEADER + BASE + "soc,unknown,Unknown,,Verify SoC\n")
        self.assertTrue(any("duplicate subsystem 'soc'" in error for error in errors))

    def test_requires_evidence_for_reported_facts(self) -> None:
        errors = self.validate_text(HEADER + "soc,family-reported,SM7150,,Verify SoC\n")
        self.assertTrue(any("needs an evidence reference" in error for error in errors))

    def test_rejects_unknown_status_spelling(self) -> None:
        errors = self.validate_text(HEADER + "soc,confirmed,Unknown,,Verify SoC\n")
        self.assertTrue(any("unsupported status" in error for error in errors))

    def test_requires_core_subsystems(self) -> None:
        errors = self.validate_text(HEADER + BASE)
        self.assertTrue(any("Missing required subsystem: boot_chain" in error for error in errors))

    def test_rejects_missing_columns(self) -> None:
        errors = self.validate_text("subsystem,status\nsoc,unknown\n")
        self.assertTrue(any("Missing CSV columns" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
