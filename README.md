# DroidXNU

**Independent XNU / Darwin kernel-port research for the Motorola Moto G60 (XT2135-2).**

DroidXNU is an experimental operating-system research project. Its goal is to investigate what would be required to bring an XNU-derived kernel environment to the Moto G60, beginning with source study, hardware documentation, and safe host-side development.

> **Status: early research — no bootable image, device port, EFI loader, or iOS 26 compatibility is available.**
>
> This project is independent and is not affiliated with or endorsed by Apple or Motorola. XNU is one component of Darwin; it is not the complete iOS operating system.

## Target device and host

| Item | Project target | Status |
|---|---|---|
| Phone | Motorola Moto G60, XT2135-2 | Confirmed model identity by Motorola declaration |
| Device family codename | hanoip | Family-level community mapping; exact variant mapping still to verify |
| SoC | Reported Qualcomm Snapdragon 732G / SM7150 family | Research lead; verify for this exact regional variant |
| CPU architecture | ARM64 / AArch64 | To verify against reliable SoC and device data |
| Host OS | Windows with WSL2 | Requested development environment |
| Host memory | 6 GB RAM | Planning baseline; may be insufficient for some builds |
| Device bootloader | Unlocked | A requested project condition, not proof of compatibility |
| Kernel research | Apple open-source XNU | Source study and portability investigation |

These are not proof that the phone can boot XNU. Device compatibility depends on the exact SoC and board revision, boot chain, memory map, interrupt controller, timers, storage, display, USB, power management, and drivers.

## Project layout

- docs/ — requirements, roadmap, hardware research, boot-chain research, XNU porting checklist, testing strategy and licensing notes.
- kernel/ — future XNU integration and project-owned patches; currently a research placeholder.
- loader/efi/ — loader feasibility research; no device boot code yet.
- boot-menu/ — boot-menu specification and a harmless host-side menu mock-up.
- devices/moto-g60/ — device facts, structured hardware inventory and compatibility status.
- drivers/ — future, independently developed driver work and research matrix.
- tools/ — host-only metadata validators, research report generator and unit tests.
- .github/workflows/host-checks.yml — repository-only validation and tests in CI.

## Host-side checks

From the repository root in WSL2, run:

```sh
make check
```

Equivalent direct commands:

```sh
python3 tools/validate_device_config.py
python3 tools/validate_hardware_inventory.py
python3 -m unittest discover -s tools -p 'test_*.py'
```

These checks only read project files. They do not connect to or modify a phone. GitHub Actions runs the same checks on Python 3.11 and 3.12 for pushes and pull requests.

## Hardware research

The structured inventory lives in devices/moto-g60/hardware-inventory.csv. Every subsystem is marked with an evidence status and an open research question. Unknown hardware values are intentionally left unknown rather than guessed.

The public Moto Common target index corroborates hanoip as a family name for Moto G40 Fusion / Moto G60, but it is archived and marks that target as dropped. This is family-level historical evidence, not proof of exact XT2135-2 board equivalence or current support. See docs/research-sources.md.

## Boot-menu concept

The proposed menu has two entries:

1. **Boot DroidXNU / experimental XNU environment** — unavailable until a verified port exists.
2. **Reboot to Original Android** — a design goal for a future, carefully validated boot flow.

The current host mock-up only prints menu choices. It does not access EFI services, reboot a computer, modify partitions, or interact with a phone.

## Current research direction

1. Verify the XT2135-2 hardware identity and distinguish facts from family-level assumptions.
2. Map the boot chain and platform interfaces using public documentation only.
3. Review available Motorola device-tree and vendor kernel-source references for useful hardware clues.
4. Study XNU's ARM64 platform dependencies and identify the gap between those requirements and the Moto G60.
5. Keep development host-side and non-destructive until the platform is understood.

**QEMU is not part of this project's roadmap.** DroidXNU is focusing on the physical Moto G60 target and host-side source analysis; no emulator test bench is planned.

## Source references

- [Motorola EU Declaration of Conformity for XT2135-2](https://en-us.support.motorola.com/ci/fattach/get/79315385/1664922506/redirect/1/filename/XT2135-2_Moto%2BG60%2BVision%2BMC38C%2BRED%2BDoC.pdf)
- [Public hanoip Android device tree](https://github.com/motorola-sm6150-devs/device_motorola_hanoip)
- [Moto Common Motorola target index](https://github.com/moto-common/android_device_motorola_targets)
- [Motorola kernel source release discussion for XT2135-2](https://github.com/MotorolaMobilityLLC/kernel-msm/issues/559)
- [Structured source register](docs/research-sources.json)\n- [Apple XNU source](https://github.com/apple-oss-distributions/xnu)
- [Apple distribution-iOS source tree supplied for research](https://github.com/apple-oss-distributions/distribution-iOS/tree/ios-260)
- [HakiOS reference project](https://github.com/oosexgang/hakios-xnu-kernel)

We will study references and licenses, but will not copy another project's implementation wholesale. No proprietary iOS image, Apple firmware, device keys, or vendor firmware is included.

## Safety and data protection

No device-modification tools are provided. Do not test experimental code on the daily-use phone. Keep original Android recovery options and personal data protected. Do not commit proprietary system images, credentials, keys, or private data.

## Contributing

See CONTRIBUTING.md, docs/requirements.md, docs/roadmap.md, docs/hardware-research.md, docs/xnu-porting-checklist.md, docs/testing-strategy.md, and docs/compatibility.md.

## License

No single project-wide license has been selected yet. See docs/licensing.md before contributing or reusing code.
