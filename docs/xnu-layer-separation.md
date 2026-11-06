# XNU architecture versus platform-specific code

**Review date:** 2026-11-06  
**Basis:** Apple XNU README and ARM64 startup / platform-expert source paths reviewed for the first feasibility pass.  
**Scope:** conceptual source-tree classification; no code copied or modified.

## Why this separation matters

XNU contains architecture-specific kernel mechanisms and platform-specific integration. ARM64 support alone does not make a kernel portable to every ARM64 device. The platform layer must supply the hardware description, early memory mappings, interrupt and timer setup, CPU startup, console and other machine services expected by the kernel.

## First-pass source-tree classification

| XNU area | Role described by upstream source | Porting interpretation |
|---|---|---|
| `osfmk/` | Mach kernel subsystems | Core kernel facilities; some code is architecture- or platform-conditioned |
| `osfmk/arm64/` | ARM64 low-level startup, exceptions, CPU and memory mechanisms | Potential architecture reference, but assumptions and configuration must be checked against the target SoC |
| `pexpert/` | Platform-specific code such as interrupt handling and atomics | High-priority platform integration area; not a drop-in generic layer |
| `pexpert/arm/` and `pexpert/arm64/` | ARM platform initialization, machine identification and platform configuration | Must be reconciled with HANOIP boot handoff and SDMMAGPIE hardware |
| `libsa/` | Kernel bootstrap code | Requires review alongside the actual loader and boot-argument contract |
| `iokit/` and `libkern/` | C++ driver framework and kernel support | Driver framework availability does not provide Moto-specific drivers |
| `bsd/` | BSD subsystems | Higher-level kernel functionality; still depends on lower-level platform services |

## What may be reusable as a reference

- ARM64 architectural concepts and low-level mechanisms that conform to the target CPU's documented architecture.
- Generic Mach and BSD subsystem designs after their dependencies are understood.
- Existing interfaces and abstractions as study material.

"Reusable" here means suitable for analysis as a design reference. It does not mean source files can be copied unchanged or that they are automatically compatible with DroidXNU's license and build configuration.

## What requires platform-specific work

- Entry contract, boot arguments and memory-map handoff.
- SoC identification and MMIO mapping.
- Interrupt-controller discovery, initialization and routing.
- Architectural/platform timer initialization and timebase calibration.
- CPU topology, PSCI or other secondary-CPU startup mechanism.
- Console and early diagnostics.
- Device-tree schema and platform property compatibility.
- Power, storage, display, touch, audio, networking and sensor drivers.
- Security/firmware interfaces and any dependencies on Apple-specific boot stages or services.

## HANOIP assessment

The Motorola source gives a Linux ARM64 configuration and SDMMAGPIE/HANOIP device-tree descriptions. It is a useful hardware reference, but it does not supply an XNU platform expert, XNU boot-argument handoff, an established UEFI environment, or XNU drivers.

The project should therefore treat `osfmk/arm64` as a source of architecture-level references and treat `pexpert`, bootstrap, and device-driver integration as unresolved porting work. No loader implementation should begin until the platform gaps are individually documented.

## Sources

- [Apple XNU README](https://github.com/apple-oss-distributions/xnu/blob/main/README.md)
- [XNU ARM64 startup](https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/start.s)
- [XNU ARM platform initialization](https://github.com/apple-oss-distributions/xnu/blob/main/pexpert/arm/pe_init.c)
- [XNU ARM machine identification](https://github.com/apple-oss-distributions/xnu/blob/main/pexpert/arm/pe_identify_machine.c)
- [Motorola HANOIP source review](source-review-motorola-hanoip.md)
- [XNU ARM64 bootstrap requirements](xnu-arm64-bootstrap-requirements.md)
