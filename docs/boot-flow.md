# Boot-flow design goals

This is a design note only. DroidXNU does not currently contain a working EFI loader or a phone boot implementation.

## Conceptual menu

1. **Boot experimental DroidXNU** — initially unavailable; may only become selectable after a compatible image and platform initialization have been demonstrated.
2. **Reboot to original Android** — a future return path whose behavior must be verified for the exact device.

## Design requirements

- Clearly show project name, build identifier and device target.
- Show a visible experimental / unsupported warning when applicable.
- Never show a boot option as available unless its image and platform checks pass.
- Default to a non-destructive exit when checks fail.
- Do not write to Android partitions as part of normal experimentation.
- Keep logs minimal and avoid collecting personal data.
- Do not bundle firmware, keys, certificates, or proprietary operating-system files.
- A recovery path must be independently reviewed and tested before any physical-device experiment.

## Current implementation status

The menu mock-up in `boot-menu/host-menu.c` is a terminal-only demonstration. It does not use UEFI protocols, load kernels, reboot, flash, or access device storage.
