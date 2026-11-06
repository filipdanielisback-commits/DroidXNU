# Proposed architecture

DroidXNU is organized as a device-port research project. The layers below are proposed boundaries, not implemented components.

## Layers

1. **Host tools** — source inspection, configuration validation, documentation checks and build orchestration.
2. **Boot-chain research** — document the Moto G60's existing boot stages and supported image formats; no device boot code yet.
3. **EFI / loader research** — determine whether an EFI-compatible interface exists or whether a different platform-specific loader boundary would be required. Do not assume UEFI is present.
4. **Kernel integration** — study XNU's Mach, BSD, IOKit, platform expert and bootstrap code; identify required changes and their licenses.
5. **SoC support** — research architecture and SoC-specific interrupt, timer, memory and bus integration.
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
│   └── efi/         # loader / EFI feasibility research
└── tools/           # host-only metadata validation and tests
```

## Boot menu goals

The conceptual menu has two choices:

- **Boot experimental DroidXNU** — only enabled after a verified, compatible boot target exists.
- **Reboot to original Android** — a future return path, subject to platform-specific validation.

The menu must never imply that Android recovery is guaranteed. No code in this repository currently performs either action.

## Porting principles

- Start with public-source analysis and host-side development.
- Keep common kernel work separate from SoC and device-specific work.
- Record provenance and license for every imported or modified file.
- Do not include proprietary firmware, private keys, certificates, or system images.
- Treat unsupported hardware as unsupported; do not silently skip essential initialization.
- Keep any future device experiment separate from normal daily use and require a reviewed recovery plan.

## Non-goals

- QEMU or emulator-based development and testing.
- Impersonating an Apple device or accessing Apple services.
- Circumventing activation, signatures, encryption, or access controls.
- Redistributing proprietary iOS firmware or user-space images.
- Claiming compatibility before repeatable evidence exists.


## XNU bootstrap research status

The first-pass XNU ARM64 bootstrap requirements are documented in [xnu-arm64-bootstrap-requirements.md](xnu-arm64-bootstrap-requirements.md). The note identifies the expected boot handoff and platform services but does not claim that Motorola HANOIP supplies an XNU-compatible interface.
