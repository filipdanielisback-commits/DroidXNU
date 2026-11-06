# DroidXNU

**Independent XNU / Darwin kernel-port research for the Motorola Moto G60 (XT2135-2).**

DroidXNU is an experimental operating-system research project. Its goal is to investigate what would be required to bring an XNU-derived kernel environment to the Moto G60, beginning with source study, hardware documentation, and safe emulation work.

> **Status: early research — no bootable image, device port, EFI loader, or iOS 26 compatibility is available yet.**
>
> This project is independent and is not affiliated with or endorsed by Apple or Motorola. The name iOS is used only when discussing the user's compatibility research target. XNU is one component of Darwin; it is not the complete iOS operating system.

## Target device and host

| Item | Project target | Status |
|---|---|---|
| Phone | Motorola Moto G60, XT2135-2 | Target identified; hardware inventory pending |
| SoC | Qualcomm platform in the Moto G60 family | Exact board/SoC mapping to verify |
| CPU architecture | ARM64 / AArch64 | To verify against device data |
| Host OS | Windows with WSL2 | Requested development environment |
| Host memory | 6 GB RAM | Minimum project planning target; may be insufficient for some builds |
| Device bootloader | Unlocked | Required only for any future, separately reviewed device experiments |
| Kernel research | Apple open-source XNU | Source study and portability investigation |
| Emulator | QEMU | First execution and test target |

These are planning targets, not proof that the phone can boot XNU. Device compatibility depends on the exact SoC, boot chain, memory map, interrupt controller, timers, storage, display, USB, power management, and drivers.

## Project layout

- `docs/` — requirements, architecture, compatibility and licensing notes.
- `kernel/` — future XNU integration and project-owned patches; currently a placeholder.
- `loader/efi/` — EFI research notes; no device boot code yet.
- `boot-menu/` — boot-menu specification and a harmless host-side menu mock-up.
- `devices/moto-g60/` — device facts and compatibility status.
- `drivers/` — future, independently developed driver work.
- `tests/qemu/` — future emulator experiments.

## Boot-menu concept

The proposed menu has two entries:

1. **Boot DroidXNU / experimental XNU environment** — unavailable until a verified port exists.
2. **Reboot to original Android** — a design goal for a future, carefully validated boot flow.

The current host mock-up only prints menu choices. It does not access EFI services, reboot a computer, modify partitions, or interact with a phone.

## Source references

- [Apple XNU source](https://github.com/apple-oss-distributions/xnu)
- [Apple distribution-iOS source tree supplied for research](https://github.com/apple-oss-distributions/distribution-iOS/tree/ios-260)
- [HakiOS reference project](https://github.com/oosexgang/hakios-xnu-kernel)

We will study references and licenses, but will not copy another project's implementation wholesale. No proprietary iOS image, Apple firmware, device keys, or vendor firmware is included.

## First milestones

1. Record the exact device hardware and boot-chain facts from public documentation.
2. Establish a reproducible host/QEMU research environment.
3. Identify which XNU components and architecture assumptions are relevant.
4. Prototype and test project-owned code in QEMU before considering hardware.
5. Document each device feature as **unknown**, **researched**, **implemented**, or **tested**.

## Safety and data protection

No flashing scripts or partition-writing tools are provided. Do not test experimental code on the daily-use phone. Keep original Android recovery options and personal data protected. Firmware, keys, certificates, and proprietary system images must not be committed.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md), [requirements](docs/requirements.md), and [compatibility status](docs/compatibility.md).

## License

No single project-wide license has been selected yet. See [docs/licensing.md](docs/licensing.md) before contributing or reusing code.
