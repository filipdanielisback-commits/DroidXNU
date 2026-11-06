# Requirements and assumptions

This document records the project's requested starting environment. It does not certify that these requirements are sufficient to boot XNU on the Moto G60.

## Host requirements (planning baseline)

| Requirement | Requested target | Notes |
|---|---|---|
| Host | Windows 10/11 | Version/build to record during setup |
| Linux environment | WSL2 | Distribution and kernel version to record |
| RAM | 6 GB | Planning minimum only; large source builds may need more |
| Python | 3.9+ | Standard-library-only host metadata checker and unit tests |
| Storage | TBD | Measure checkout and build needs before setting a number |
| Toolchain | TBD | Select after source and build requirements are reviewed |

## Device requirements (research target)

| Requirement | Target | Verification |
|---|---|---|
| Manufacturer/model | Motorola Moto G60 | Confirmed by Motorola declaration |
| Model number | XT2135-2 | Confirmed by Motorola declaration |
| Device family codename | hanoip | Public Android device-tree reference; exact mapping still to verify |
| Bootloader state | Unlocked | User-requested condition; not a guarantee of compatibility |
| CPU architecture | ARM64/AArch64 | Verify against reliable SoC/device documentation |
| SoC and board revision | Reported SM7150 / Snapdragon 732G family; revision TBD | Verify for this exact regional model |
| RAM | Device-specific | Record actual reported memory; 6 GB is a host planning target, not device evidence |
| Display, touch, storage, USB, Wi-Fi, audio, sensors | TBD | Each needs separate hardware research and driver status |

## Technical prerequisites still unknown

- Exact SoC identifier, silicon revision, and board revision for XT2135-2.
- Exact mapping between this regional model and the public `hanoip` device tree.
- Available public device-tree and kernel-source information, including matching release tags.
- Boot ROM / bootloader chain and supported boot image formats.
- Whether native EFI exists; do not assume Android boot firmware implements UEFI.
- Exception level, memory map, page-table assumptions and cache coherency.
- Interrupt controller, timer, serial console and watchdog.
- Storage controller, display pipeline, touch controller and power management.
- Whether a supported XNU platform configuration can be adapted without unavailable Apple-specific dependencies.

## Important distinction

XNU is a kernel, not a complete iOS installation. A working operating-system environment also needs compatible user space, libraries, drivers, boot support and platform integration. The supplied Apple `distribution-iOS` branch must be examined file-by-file; its existence does not establish that a complete installable iOS 26 system is available for third-party hardware.

## Acceptance rule

A requirement becomes **verified** only when a source, test result, or reproducible observation is recorded in `docs/compatibility.md`. Do not label the Moto G60 supported merely because it belongs to an ARM64-capable product family or has an unlocked bootloader.
