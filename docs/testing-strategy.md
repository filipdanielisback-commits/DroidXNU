# DroidXNU testing strategy

## Current testable scope

The repository supports host-side metadata validation and tests. It does not contain a runnable XNU port, device loader, device driver or bootable image.

## Test layers

### Metadata checks

- Parse the device configuration.
- Require the expected model identity and research-only status.
- Require device-operation and firmware-inclusion safety flags to remain false.
- Validate the structured hardware inventory and its evidence fields.

### Unit tests

- Use Python's standard-library unittest.
- Use temporary files for malformed-input tests.
- Do not require network access, root privileges, connected hardware or proprietary files.
- Test valid and invalid input cases.

### CI checks

- Run host-side validation on supported Python versions.
- Run the full unit-test discovery command.
- Keep CI limited to repository content; it must not download firmware or interact with a phone.

### Future source/build checks

A future source build may be added only after the exact upstream revision, license, toolchain and build dependencies are documented. A successful compile is not proof of boot or hardware support.

## Local commands

```sh
make check
python3 tools/validate_device_config.py
python3 tools/validate_hardware_inventory.py
python3 -m unittest discover -s tools -p 'test_*.py'
```

## Reporting a test

Include commit, host OS, Python version, command, exit code and concise output. Redact usernames, local paths and personal data.

## Explicit exclusions

- No QEMU or emulator test bench.
- No firmware flashing, partition writes or bootloader changes.
- No proprietary images, keys or vendor binaries.
- No claim of Moto G60 compatibility based on host tests alone.
