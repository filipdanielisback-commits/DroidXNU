# Requirements and assumptions

This document records the project's requested starting environment. It does not certify that these requirements are sufficient to boot XNU on the Moto G60.

## Host requirements (planning baseline)

| Requirement | Requested target | Notes |
|---|---|---|
| Host | Windows 10/11 | Version/build to record during setup |
| Linux environment | WSL2 | Distribution and kernel version to record |
| RAM | 6 GB | Planning minimum only; large source builds may need more |
| Storage | TBD | Measure checkout, build and QEMU image needs before setting a number |
| Toolchain | TBD | Select only after the first QEMU target is defined |
| Emulator | QEMU | Initial experiments should remain off-device |

## Device requirements (research target)

| Requirement | Target | Verification |
|---|---|---|
| Manufacturer/model | Motorola Moto G60 | User-specified target |
| Model number | XT2135-2 | Confirm from device settings/label |
| Bootloader state | Unlocked | User-specified condition; not a guarantee of compatibility |
| CPU architecture | ARM64/AArch64 | Verify against reliable device/SoC documentation |
| SoC and board revision | TBD | Must be established before any port |
| RAM | Device-specific | Record actual reported memory |
| Display, touch, storage, USB, Wi-Fi, audio, sensors | TBD | Each needs separate hardware research and driver status |

## Technical prerequisites still unknown

- Exact SoC identifier and board revision for XT2135-2.
- Available public device-tree and kernel-source information.
- Boot ROM / bootloader chain and supported boot image formats.
- Exception level, memory map, page-table assumptions and cache coherency.
- Interrupt controller, timer, serial console and watchdog.
- Storage controller, display pipeline, touch controller and power management.
- Whether a supported XNU platform configuration can be adapted without unavailable Apple-specific dependencies.

## Important distinction

XNU is a kernel, not a complete iOS installation. A working operating-system environment also needs compatible user space, libraries, drivers, boot support and platform integration. The supplied Apple `distribution-iOS` branch must be examined file-by-file; its existence does not establish that a complete installable iOS 26 system is available for third-party hardware.

## Acceptance rule

A requirement becomes **verified** only when a source, test result, or reproducible observation is recorded in `docs/compatibility.md`. Do not label the Moto G60 supported merely because it is ARM64 or has an unlocked bootloader.
