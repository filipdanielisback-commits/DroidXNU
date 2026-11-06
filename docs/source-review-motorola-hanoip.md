# Motorola Hanoip kernel-source review

**Review date:** 2026-11-06  
**Target under study:** Moto G60 XT2135-2 (type MC38C)  
**Source release:** `MMI-S2RIS32.32-20-9-9-2-1`  
**Scope:** public source metadata and device-tree review only; no kernel build or device interaction.

## Finding summary

Motorola's public kernel repository contains a source tag explicitly named `MMI-S2RIS32.32-20-9-9-2-1`. The tag is linked from Motorola contributor activity on issue #559, whose request names the XT2135-2 HANOIP RETEU Android 12 firmware build. The tag message says "Hanoip push for Android 12".

At that tag, the source tree contains:
- ARM64 device-tree sources under `arch/arm64/boot/dts/qcom/`.
- Hanoip-specific device-tree overlays, including `sdmmagpie-hanoip-dvt1-overlay.dts`.
- A Hanoip-specific Motorola kernel configuration fragment: `arch/arm64/configs/vendor/ext_config/moto-sdmmagpie-hanoip.config`.
- The fragment enables `CONFIG_HANOIP_DTB=y`.
- The common Hanoip overlay includes Moto common, audio, panel, battery/thermal, sensor and touchscreen device-tree fragments.
- The SoC device-tree declares `model = "Qualcomm Technologies, Inc. SDMMAGPIE"`, `compatible = "qcom,sdmmagpie"`, and CPU nodes with `compatible = "arm,armv8"`.

This is strong, model-linked evidence that the XT2135-2 HANOIP Android 12 software target has a Motorola ARM64 Linux kernel/device-tree configuration for the Qualcomm SDMMAGPIE platform. It is not proof that every XT2135-2 hardware revision is identical.

## Direct references

- [Motorola issue #559 — XT2135-2 HANOIP RETEU Android 12 source request](https://github.com/MotorolaMobilityLLC/kernel-msm/issues/559)
- [Motorola contributor comment linking the published source release](https://github.com/MotorolaMobilityLLC/kernel-msm/issues/559#issuecomment-1831904688)
- [Exact source tag](https://github.com/MotorolaMobilityLLC/kernel-msm/tree/MMI-S2RIS32.32-20-9-9-2-1)
- [Hanoip DVT1 device-tree overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-dvt1-overlay.dts)
- [Hanoip common overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-common-overlay.dtsi)
- [Hanoip Motorola configuration fragment](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/configs/vendor/ext_config/moto-sdmmagpie-hanoip.config)
- [SDMMAGPIE SoC device tree](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie.dtsi)
- [Motorola kernel source COPYING file at the tag](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/COPYING)

## What this confirms

| Item | Evidence-backed conclusion |
|---|---|
| XT2135-2 source relationship | Issue #559 identifies the XT2135-2 HANOIP RETEU Android 12 firmware build; Motorola contributor links the published tag |
| Device codename | Hanoip appears in the tag message, Hanoip config fragment and Hanoip device-tree overlays |
| Kernel architecture | The Hanoip configuration and device-tree files are in the ARM64 source tree; the shared SoC DTS declares ARMv8 CPU nodes |
| Qualcomm platform identifier | The shared device tree identifies the platform as Qualcomm SDMMAGPIE |
| Board variants | The source contains EVT1, DVT1 and DVT2 Hanoip overlays; this does not identify the user's individual board revision |
| License lead | The repository's `COPYING` file contains GNU GPL version 2; individual files may carry additional or different notices, so review per file before reuse |

## What remains unconfirmed

- The exact commercial SoC SKU and silicon revision for this XT2135-2 unit. Snapdragon 732G / SM7150 remains a community-reported lead, not a conclusion drawn from the reviewed files.
- The exact board revision of the target unit.
- Complete physical memory size/map and runtime hardware configuration.
- The complete boot-chain, image handoff and whether any UEFI protocols are available.
- Whether XNU's ARM64 bootstrap and platform services can be adapted to this hardware.
- Whether any Linux driver or device-tree content can be reused; this requires per-file technical and license review.

## Engineering interpretation

This source release is useful as a hardware reference. It provides a concrete Hanoip configuration and device-tree starting point for continued research. It does **not** make the Linux kernel a drop-in XNU kernel, and it does not provide an EFI loader, XNU platform support, proprietary firmware permissions, or a bootable DroidXNU image.

No Motorola kernel code has been copied into DroidXNU. This review records paths and observations only.
