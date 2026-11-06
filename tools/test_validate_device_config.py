"""Unit tests for the host-only device metadata validator."""

import tempfile
import unittest
from pathlib import Path

from validate_device_config import validate_config

VALID_CONFIG = '''\
[device]
name = Motorola Moto G60
model = XT2135-2
status = research-only

[safety]
writes_to_device = false
firmware_in_repository = false
bootable_image_available = false
'''


class ValidateDeviceConfigTests(unittest.TestCase):
    def validate_text(self, content: str) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "device.conf"
            path.write_text(content, encoding="utf-8")
            return validate_config(path)

    def test_accepts_research_only_configuration(self) -> None:
        self.assertEqual(self.validate_text(VALID_CONFIG), [])

    def test_rejects_wrong_model(self) -> None:
        errors = self.validate_text(VALID_CONFIG.replace("XT2135-2", "XT2135-1"))
        self.assertTrue(any("model must be" in error for error in errors))

    def test_rejects_enabled_device_operation_flag(self) -> None:
        content = VALID_CONFIG.replace("writes_to_device = false", "writes_to_device = true")
        errors = self.validate_text(content)
        self.assertTrue(any("writes_to_device must remain false" in error for error in errors))

    def test_rejects_missing_safety_flag(self) -> None:
        content = VALID_CONFIG.replace("firmware_in_repository = false\n", "")
        errors = self.validate_text(content)
        self.assertTrue(any("Missing [safety] firmware_in_repository" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
