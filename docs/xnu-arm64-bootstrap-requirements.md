# XNU ARM64 bootstrap and platform requirements — first-pass review

**Review date:** 2026-11-06  
**Upstream reviewed:** Apple `apple-oss-distributions/xnu`, branch `main`  
**Target evidence:** Motorola HANOIP / SDMMAGPIE Android 12 source tag `MMI-S2RIS32.32-20-9-9-2-1`  
**Scope:** public source reading only. No source copied, no kernel build, no bootloader changes, and no phone interaction.

## Executive result

The reviewed XNU ARM64 startup code is not a generic "jump to kernel" interface. It expects a structured boot handoff and platform services. The Motorola HANOIP Linux device tree describes useful hardware, but the reviewed files do not demonstrate that the phone supplies the boot arguments, device-tree shape, interrupt-controller description, timer description, or other platform contract expected by XNU.

**Feasibility status: undetermined; significant platform adaptation appears necessary.** This is not a claim that a port is impossible, nor evidence that it will boot.

## XNU requirements visible in the reviewed source

| Requirement | Evidence in XNU source | Implication for DroidXNU |
|---|---|---|
| ARM64 entry and CPU state | `osfmk/arm64/start.s` defines `_start`, reset vectors and early CPU startup | A future loader/entry environment must be designed against the exact XNU build's entry contract; a normal Android boot handoff cannot be assumed compatible |
| Structured boot arguments | `start.s` reads boot-argument fields for virtual base, physical base, memory size and boot flags | Need a documented, model-specific memory map and a correctly constructed boot-argument structure before kernel entry |
| CPU identity and multiprocessor startup | `start.s` reads `MPIDR_EL1` and CPU data; HANOIP DTS declares eight ARMv8 CPU nodes with PSCI | CPU topology, affinity IDs, power-on method and secondary CPU startup must be reconciled; Linux DTS alone is not an XNU CPU-start implementation |
| Device-tree services | `pexpert/arm/pe_init.c` uses Secure Device Tree lookups for `/chosen`, memory-map, and platform data | Need a valid handoff tree and compatible property semantics; the Android DT/DTBO composition must be understood, not guessed |
| SoC identification and MMIO | `pexpert/arm/pe_identify_machine.c` searches for an `arm-io` node and reads its `ranges` property | The reviewed HANOIP Linux DTS does not yet establish an XNU-compatible `arm-io` node or the required physical mapping convention |
| Interrupt controller and timer | `pe_identify_machine.c` searches for an interrupt-controller marked `master` and a node with `device_type = "timer"`, then maps their `reg` ranges | Exact controller register layout, interrupt routing, timer source/frequency and compatible XNU support remain unverified |
| Console / diagnostics | XNU ARM platform code includes serial-console and platform initialization paths | A safe, documented diagnostic path would be required for useful bring-up; no compatible console path is established yet |

These are observations from the cited source files, not a complete specification of every requirement for a particular iOS/XNU build.

## Comparison with Motorola HANOIP source evidence

What the Motorola source does provide:

- SDMMAGPIE base DTS identifies the Qualcomm platform and declares ARMv8 CPU nodes.
- The CPU nodes use `enable-method = "psci"`.
- The base DTS includes interrupt-controller bindings and platform device nodes.
- The source contains HANOIP-specific overlays and a model-linked ARM64 kernel configuration.
- The DTS describes buses and several peripheral components, which can guide later driver research.

What it does not yet prove:

- That an XNU-compatible boot-argument block is supplied by the existing boot chain.
- That the phone's boot chain offers UEFI or any other documented interface expected by a proposed loader.
- That the composed Android device tree contains the exact `arm-io`, master interrupt-controller and timer nodes/semantics XNU's reviewed platform code looks for.
- That XNU can use the Linux device tree unchanged.
- That a complete set of platform expert, interrupt, timer, memory-management, power, security and device-driver services can be implemented for this SoC.
- That the public kernel source is sufficient to boot XNU or full iOS.

## Required follow-up research

1. Review the exact HANOIP base DTS and all candidate overlays as a set; identify the actual board overlay only if a model-matched source proves it.
2. Locate and document the interrupt-controller and timer nodes, their register ranges, interrupt routing and frequency metadata in the composed tree.
3. Map the HANOIP CPU/PSCI description to XNU's CPU initialization assumptions at a conceptual level.
4. Research the documented boot stages and image handoff independently. Do not assume UEFI.
5. Build a requirement-by-requirement gap table before considering any loader or kernel implementation.

## Primary source references

### Apple XNU

- [XNU README and architecture overview](https://github.com/apple-oss-distributions/xnu/blob/main/README.md)
- [ARM64 startup and reset code — osfmk/arm64/start.s](https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/start.s)
- [ARM platform initialization — pexpert/arm/pe_init.c](https://github.com/apple-oss-distributions/xnu/blob/main/pexpert/arm/pe_init.c)
- [ARM machine identification, interrupt-controller and timer mapping — pexpert/arm/pe_identify_machine.c](https://github.com/apple-oss-distributions/xnu/blob/main/pexpert/arm/pe_identify_machine.c)
- [ARM boot-argument access — pexpert/arm/pe_bootargs.c](https://github.com/apple-oss-distributions/xnu/blob/main/pexpert/arm/pe_bootargs.c)

### Motorola HANOIP

- [SDMMAGPIE base DTS](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie.dtsi)
- [HANOIP common overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-common-overlay.dtsi)
- [HANOIP DVT1 overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-dvt1-overlay.dts)
- [HANOIP Motorola ARM64 configuration fragment](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/configs/vendor/ext_config/moto-sdmmagpie-hanoip.config)

## Licensing and reuse

The XNU source repository is distributed under Apple Public Source License 2.0 with file-specific notices and conditions. Motorola kernel files carry their own notices; the repository's root COPYING file identifies GPL version 2 for the kernel. This note contains descriptions and links only. No upstream source code is copied into DroidXNU. Review exact file licenses and project compatibility before any future code reuse.
