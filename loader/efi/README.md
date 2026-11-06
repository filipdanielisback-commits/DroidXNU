# EFI loader research

No EFI executable or device bootloader is implemented here.

The future loader research must first establish whether the target platform provides an EFI environment or needs a separate, documented firmware/boot-chain layer. Do not assume that a generic UEFI application can run directly on the Moto G60.

## Planned responsibilities

- Display device and build information.
- Validate a candidate test image before offering it.
- Present the two conceptual menu choices documented in [boot-flow.md](../../docs/boot-flow.md).
- Fail safely when a required component is absent.
- Keep project logs free of personal data and secrets.

## Current state

The only menu code is a host-side terminal mock-up under `boot-menu/`. It does not call UEFI services, load a kernel, reboot, flash, or access phone storage.
