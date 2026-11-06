"""Unit tests for the host-only hardware inventory validator."""
import tempfile
import unittest
from pathlib import Path
from validate_hardware_inventory import validate_inventory

HEADER = "subsystem,status,reported_value,evidence,open_question\n"
SUBSYSTEMS = (
    "device_family", "soc", "cpu_architecture", "memory", "interrupt_controller",
    "timers", "boot_chain", "efi_environment", "storage", "display_gpu", "touch",
    "usb", "wifi_bluetooth", "audio", "sensors", "power_thermal",
)


def valid_rows() -> list[str]:
    rows = []
    for name in SUBSYSTEMS:
        if name == "device_family":
            rows.append(
                "device_family,family-reported,hanoip,https://example.invalid/source,"
                "Verify exact model mapping\n"
            )
        else:
            rows.append(f"{name},unknown,Unknown,,Verify {name}\n")
    return rows


class ValidateHardwareInventoryTests(unittest.TestCase):
    def validate_text(self, content: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.csv"
            path.write_text(content, encoding="utf-8")
            return validate_inventory(path)

    def test_accepts_complete_valid_inventory(self) -> None:
        self.assertEqual(self.validate_text(HEADER + "".join(valid_rows())), [])

    def test_rejects_duplicate_subsystems(self) -> None:
        rows = valid_rows()
        rows.append("soc,unknown,Unknown,,Verify duplicate\n")
        errors = self.validate_text(HEADER + "".join(rows))
        self.assertTrue(any("duplicate subsystem 'soc'" in error for error in errors))

    def test_requires_evidence_for_reported_facts(self) -> None:
        rows = valid_rows()
        rows[0] = "device_family,family-reported,hanoip,,Verify exact model mapping\n"
        errors = self.validate_text(HEADER + "".join(rows))
        self.assertTrue(any("needs an evidence reference" in error for error in errors))

    def test_rejects_unknown_status_spelling(self) -> None:
        rows = valid_rows()
        rows[1] = "soc,confirmed,Unknown,,Verify SoC\n"
        errors = self.validate_text(HEADER + "".join(rows))
        self.assertTrue(any("unsupported status" in error for error in errors))

    def test_requires_core_subsystems(self) -> None:
        rows = [row for row in valid_rows() if not row.startswith("boot_chain,")]
        errors = self.validate_text(HEADER + "".join(rows))
        self.assertTrue(any("Missing required subsystem: boot_chain" in error for error in errors))

    def test_rejects_missing_columns(self) -> None:
        errors = self.validate_text("subsystem,status\nsoc,unknown\n")
        self.assertTrue(any("Missing CSV columns" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
