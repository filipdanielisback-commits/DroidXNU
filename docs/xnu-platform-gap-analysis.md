# DroidXNU XNU platform-service gap analysis

**Review date:** 2026-11-06  
**Target:** Motorola Moto G60 XT2135-2 / HANOIP software target  
**Evidence baseline:** Motorola kernel tag `MMI-S2RIS32.32-20-9-9-2-1`; Apple XNU commit `f6217f891ac0bb64f3d375211650a4c1ff8ca1ea` (`xnu-12377.1.9`)  
**Status:** preliminary research gap analysis, not an implementation plan or bootability claim.

## Status scale

- **Evidence found:** source describes a related Linux-side hardware/platform element.
- **Partially mapped:** some source evidence exists, but XNU interface or exact device behavior is unknown.
- **Unknown:** no sufficient model-linked evidence has been reviewed.
- **Not implemented:** DroidXNU contains no implementation for the service.

## Gap matrix

| Required service | Motorola evidence | XNU-side expectation / research reference | Current gap | Status |
|---|---|---|---|---|
| Kernel entry and boot arguments | Android kernel source and DT metadata; no XNU handoff contract identified | ARM64 entry and boot-argument use in `osfmk/arm64/start.s` | Need a documented loader-to-kernel contract and compatible boot-argument data | Unknown / not implemented |
| Physical memory map | Linux DTS includes reserved-memory regions | XNU startup consumes physical base, virtual base and memory size | Need complete RAM map, reserved ranges and exact handoff semantics | Partially mapped |
| Device-tree handoff | SDMMAGPIE/HANOIP Linux DTS and overlays exist | XNU platform code uses Secure Device Tree lookup APIs | Need to establish the actual composed tree, property semantics and compatible access layer | Partially mapped |
| SoC identification / MMIO | SDMMAGPIE SoC DTS describes platform nodes | XNU platform expert locates SoC base and maps registers | Need a target-specific XNU platform description and safe MMIO map | Partially mapped |
| CPU topology | Eight ARMv8 CPU nodes appear in SDMMAGPIE DTS | XNU ARM64 startup identifies CPUs using MPIDR and CPU data | Need exact physical IDs, affinity topology and XNU CPU data mapping | Partially mapped |
| Secondary CPU startup | Linux DTS declares PSCI 1.0 using SMC | XNU reset/start code has platform-dependent CPU startup paths | Need confirm firmware PSCI behavior and a compatible XNU startup implementation | Partially mapped |
| Interrupt controller | ARM GIC bindings and interrupt-controller references exist in Linux DTS | XNU platform initialization expects a master interrupt-controller description and interrupt setup | Need exact controller version, register map, routing and XNU driver | Partially mapped |
| Timer / timebase | Linux DTS includes timer-related platform data, but no XNU-compatible timer contract established | XNU platform code maps a timer and initializes timebase/frequency data | Need timer identity, register map, frequency, interrupt route and XNU implementation | Unknown |
| Early console | Linux source has serial-related support and UART aliases | XNU ARM platform code has serial/console paths | Need exact UART instance, clock/pin configuration and XNU console support | Unknown |
| Storage | Linux DTS describes eMMC, SD and UFS controller aliases | XNU requires storage controller and block-device support for a usable system | Need exact populated controller, protocol details, driver and filesystem integration | Partially mapped |
| Display / GPU | HANOIP panel and DSI descriptions exist | XNU/iOS graphics stack requires platform display and GPU support beyond a panel description | Need compatible display controller, GPU, firmware, display pipeline and proprietary-interface assessment | Partially mapped |
| Touch | HANOI touchscreen DTS declares an Ilitek SPI device | XNU input stack needs a working device driver and event integration | Need exact controller variant, protocol details and driver | Partially mapped |
| Audio | HANOI audio overlay describes WCD937x and Awinic amplifier components | XNU audio services require codec, DSP, routing and driver integration | Need complete DSP/firmware dependency map and drivers | Partially mapped |
| Wi-Fi / Bluetooth | Not established in the reviewed HANOIP fragments | Network and Bluetooth stacks need hardware drivers and firmware interfaces | Need exact chip/transport, firmware requirements and licensing review | Unknown |
| USB | General Qualcomm USB support exists in source tree | XNU needs controller, PHY, role and device-stack support | Need exact controller/PHY configuration and port role | Unknown |
| Power / charging / thermal | Battery/thermal overlay describes PM6150-related configuration | Stable platform operation needs power, thermal and battery services | Need full PMIC configuration, sensors and XNU integration | Partially mapped |
| Security / firmware services | Android device tree includes firmware and reserved-memory declarations | XNU startup/security configurations may depend on platform firmware and privileged services | Need a documented firmware interface map; Apple-specific secure services cannot be assumed | Unknown |
| Boot firmware / loader interface | Motorola source is for Android/Linux; no UEFI proof | A loader must provide the exact entry and memory/device-tree contract | Need boot-chain evidence and a supported handoff strategy before loader work | Unknown |

## Overall assessment

The strongest available evidence is for a HANOIP Android/Linux hardware description on ARM64 and SDMMAGPIE. That is useful input for research, but it is not a working XNU platform layer.

The most fundamental blockers are the undocumented XNU-compatible boot handoff, complete memory map, interrupt-controller and timer integration, CPU startup contract, and the absence of XNU platform drivers. Graphics, storage, wireless, audio and security add further substantial work.

**Decision gate:** do not start an EFI loader or claim a kernel port until the boot-chain research and core platform-service gaps have enough evidence to define a testable, lawful, non-destructive development plan.

## Next evidence tasks

1. Review the HANOIP base DTS and all overlay candidates together to locate timer and interrupt-controller nodes and their properties.
2. Determine whether the Motorola source release documents enough boot stages and image handoff to define the loader boundary. Keep UEFI as unknown unless directly evidenced.
3. Complete the XNU porting checklist with references to this matrix.
4. Revisit exact SoC SKU, board revision, RAM size and peripheral variants using model-matched primary sources.

## Sources

- [XNU ARM64 startup](https://github.com/apple-oss-distributions/xnu/blob/f6217f891ac0bb64f3d375211650a4c1ff8ca1ea/osfmk/arm64/start.s)
- [XNU ARM platform initialization](https://github.com/apple-oss-distributions/xnu/blob/f6217f891ac0bb64f3d375211650a4c1ff8ca1ea/pexpert/arm/pe_init.c)
- [XNU ARM machine identification](https://github.com/apple-oss-distributions/xnu/blob/f6217f891ac0bb64f3d375211650a4c1ff8ca1ea/pexpert/arm/pe_identify_machine.c)
- [Motorola SDMMAGPIE base DTS](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie.dtsi)
- [Motorola HANOIP common overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-common-overlay.dtsi)
- [Motorola HANOIP source review](source-review-motorola-hanoip.md)
- [XNU ARM64 bootstrap requirements](xnu-arm64-bootstrap-requirements.md)
- [XNU layer separation](xnu-layer-separation.md)
