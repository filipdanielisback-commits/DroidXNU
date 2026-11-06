# Motorola XT2135-2 kernel-source review

**Review date:** 2026-11-06  
**Target firmware:** `XT2135-2_HANOIP_RETEU_12_S2RIS32.32-20-9-9-2-1`  
**Motorola source tag:** `MMI-S2RIS32.32-20-9-9-2-1`  
**Tag commit:** `f6673a1302e3b9ca84c54e956ad4075d676fdf59`  
**Kernel base version:** Linux 4.14.190

## Result

The source tag is located and inspected. Motorola issue #559 requests kernel source for the exact XT2135-2 Android 12 firmware build above. A Motorola contributor replied that the code was released and linked the tag. The Git tag is present and its source tree is accessible, even though the GitHub Releases API does not currently return a release object for that tag.

The annotated tag message is `Hanoip push for Android 12`. The tag object points to commit `f6673a1302e3b9ca84c54e956ad4075d676fdf59`. GitHub reports the tag as unsigned; the commit's committer is a Motorola contributor. Record provenance, but do not describe the tag as cryptographically verified.

## Confirmed from the matching source tree

1. **HANOIP model family:** the source tree contains HANOIP device-tree overlays. For example, `sdmmagpie-hanoip-dvt1-overlay.dts` sets `model = "hanoip"`; DVT1, DVT2 and EVT1 overlay files are present. The source tag is tied by Motorola's issue to the XT2135-2 firmware build. This upgrades HANOIP from a broad family-only lead to a model/build-matched source association. It does not identify which board revision is in a particular handset.
2. **ARM64 / ARMv8:** the HANOIP base tree is under `arch/arm64/boot/dts/qcom`. Its include chain reaches `sdmmagpie.dtsi`, which describes CPU nodes with `compatible = "arm,armv8"`. The common SoC description contains eight CPU nodes. This is model/build-matched kernel evidence for an ARMv8 64-bit platform.
3. **Qualcomm platform identifier:** the same include chain identifies the SoC platform as `qcom,sdmmagpie` / `SDMMAGPIE`. Treat that as the kernel device-tree platform identifier. The consumer-facing chip name and silicon revision are not established by this inspection alone.
4. **Device-tree organization:** HANOIP DVT/EVT overlays are listed in the QCOM device-tree Makefile and are based on `sdmmagpie-hanoi-base.dtb`. The common overlay references display, battery/thermal, sensor, touch and audio fragments.
5. **Boot-interface clue:** the SoC description includes PSCI 1.0 with the SMC conduit and Android firmware metadata. These are Linux device-tree descriptions, not proof of UEFI. No UEFI protocol environment is established here.
6. **Kernel version:** the tagged root Makefile identifies Linux 4.14.190.

## Licensing and reuse

The tagged tree's root `COPYING` contains GNU GPL version 2. The inspected HANOIP device-tree source files carry headers specifying GPL version 2 only. This is useful provenance for those files, but it is not a substitute for checking the license and copyright header of every file before any reuse. No Motorola source code or binary was copied into DroidXNU during this review.

## Still unknown

- Exact retail SoC marketing name and silicon revision for XT2135-2.
- Which EVT/DVT board overlay corresponds to the user's individual hardware revision.
- Complete memory map and actual installed RAM configuration.
- Full peripheral inventory and the exact enabled device-tree composition for the shipping XT2135-2 variant.
- Bootloader stages, image acceptance rules, secure-boot state, and whether any UEFI interface exists.
- Whether any Linux driver or firmware interface can be adapted to an XNU platform port.
- Any XNU or iOS compatibility.

## Source files reviewed

- [Tag tree](https://github.com/MotorolaMobilityLLC/kernel-msm/tree/MMI-S2RIS32.32-20-9-9-2-1)
- [Tag commit](https://github.com/MotorolaMobilityLLC/kernel-msm/commit/f6673a1302e3b9ca84c54e956ad4075d676fdf59)
- [HANOIP DVT1 overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-dvt1-overlay.dts)
- [HANOIP common overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-common-overlay.dtsi)
- [HANOIP base device tree](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoi-base.dts)
- [SDMMAGPIE SoC description](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie.dtsi)
- [Kernel COPYING](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/COPYING)

## Next research task

Map the Linux drivers and device-tree nodes relevant to HANOIP onto DroidXNU's hardware inventory. Keep that as analysis only: no source import, binary redistribution, phone access, or boot experiments.
