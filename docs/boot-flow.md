# Boot-flow design goals

This is a design note only. DroidXNU does not currently contain a working EFI loader or a phone boot implementation. Native UEFI support on the Moto G60 has not been established and must not be assumed.

## Conceptual menu

1. **Boot experimental DroidXNU** — initially unavailable; may only become selectable after a compatible image and platform initialization have been demonstrated.
2. **Reboot to original Android** — a future return path whose behavior must be verified for the exact device.

## Design requirements

- Clearly show project name, build identifier and device target.
- Show a visible experimental / unsupported warning when applicable.
- Never show a boot option as available unless its image and platform checks pass.
- Default to a non-destructive exit when checks fail.
- Avoid changes to the existing Android installation during the research phase.
- Keep logs minimal and avoid collecting personal data.
- Do not bundle proprietary firmware, keys, certificates, or operating-system files.
- A recovery path must be independently reviewed before any physical-device experiment.

## Current implementation status

The menu mock-up in `boot-menu/host-menu.c` is a terminal-only demonstration. It does not use UEFI protocols, load kernels, reboot, or access device storage.
