# Proposed architecture

DroidXNU is organized as a device-port research project. The layers below are proposed boundaries, not implemented components.

## Layers

1. **Host tools** — source checks, configuration validation, build orchestration and QEMU test helpers.
2. **Emulated reference platform** — the first place to test project-owned kernel and loader code.
3. **EFI loader research** — a future platform-independent loader interface and menu. No EFI executable exists yet.
4. **Kernel integration** — study XNU's Mach, BSD, IOKit, platform expert and bootstrap code; identify required changes and their licenses.
5. **SoC support** — architecture and SoC-specific interrupt, timer, memory and bus integration.
6. **Device support** — Moto G60 board configuration and independently developed drivers.
7. **User space** — a separate, compatible user environment; not assumed to be supplied by XNU or the linked source branch.

## Proposed source tree

```text
DroidXNU/
├── boot-menu/       # menu specification and safe host mock-up
├── docs/            # research and compatibility records
├── devices/
│   └── moto-g60/    # device facts and board status
├── drivers/         # future project-owned drivers
├── kernel/
│   └── xnu/         # future source integration / patch notes
├── loader/
│   └── efi/         # EFI research; no bootloader implementation yet
└── tests/
    └── qemu/        # future emulator tests
```

## Boot menu goals

The conceptual menu has two choices:

- **Boot experimental DroidXNU** — only enabled after a verified, compatible boot target exists.
- **Reboot to original Android** — a future fallback path, subject to platform-specific validation.

The menu must never imply that Android recovery is guaranteed. No code in this repository currently performs either action.

## Porting principles

- Start with QEMU and project-owned test code.
- Keep common kernel work separate from SoC and device-specific work.
- Record provenance and license for every imported or modified file.
- Do not include proprietary firmware, private keys, certificates, or system images.
- Treat unsupported hardware as unsupported; do not silently skip essential initialization.
- Keep any future device experiment separate from normal daily use and require a reviewed recovery plan.

## Non-goals

- Impersonating an Apple device or accessing Apple services.
- Circumventing activation, signatures, encryption, or access controls.
- Redistributing proprietary iOS firmware or user-space images.
- Claiming compatibility before repeatable tests exist.
