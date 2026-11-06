# Moto G60 board facts

This file distinguishes manufacturer-confirmed identity from model-linked source evidence and community-reported family information.

| Field | Current value | Confidence |
|---|---|---|
| Commercial name | Motorola Moto G60 | Manufacturer-confirmed |
| Model number | XT2135-2 | Manufacturer-confirmed |
| Motorola type identifier | MC38C | Manufacturer-confirmed |
| Internal family codename | hanoip | Model-linked Motorola source evidence: issue #559 names an XT2135-2 HANOIP RETEU Android 12 build and Motorola links its Hanoip source tag |
| Qualcomm platform identifier | SDMMAGPIE | Model-linked Motorola kernel device-tree source |
| Commercial SoC SKU | Unknown; Snapdragon 732G / SM7150 remains a community-reported lead | Not established by the reviewed Motorola source files |
| CPU architecture | ARMv8 / AArch64 | Model-linked ARM64 kernel config and device-tree CPU nodes |
| Board revision | Unknown | Source has EVT1, DVT1 and DVT2 overlays but does not identify this unit's revision |
| Native UEFI support | Unknown | Do not assume |
| XNU compatibility | Unknown | No implementation or boot test exists |

## Primary references

1. Motorola EU Declaration of Conformity: [XT2135-2 Moto G60 Vision / MC38C PDF](https://en-us.support.motorola.com/ci/fattach/get/79315385/1664922506/redirect/1/filename/XT2135-2_Moto%2BG60%2BVision%2BMC38C%2BRED%2BDoC.pdf)
2. Motorola source publication record: [kernel-msm issue #559](https://github.com/MotorolaMobilityLLC/kernel-msm/issues/559), which identifies the XT2135-2 HANOIP RETEU Android 12 firmware build and links the published source release.
3. Exact Motorola source tag: [MMI-S2RIS32.32-20-9-9-2-1](https://github.com/MotorolaMobilityLLC/kernel-msm/tree/MMI-S2RIS32.32-20-9-9-2-1).
4. [Hanoip configuration fragment](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/configs/vendor/ext_config/moto-sdmmagpie-hanoip.config).
5. [Hanoip DVT1 overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-dvt1-overlay.dts).
6. [SDMMAGPIE SoC device tree](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie.dtsi).
7. Public community device tree: [motorola-sm6150-devs/device_motorola_hanoip](https://github.com/motorola-sm6150-devs/device_motorola_hanoip).
8. Android device-tree background: [Android Open Source Project — Device tree overlays](https://source.android.com/docs/core/architecture/dto).

## Interpretation notes

- The Motorola declaration proves the commercial model and model number; it does not disclose the complete SoC or boot-chain design.
- The Motorola issue and tagged source provide a model-linked Hanoip software target. They do not identify the physical board revision of an individual unit.
- The reviewed source identifies the Qualcomm SDMMAGPIE platform and ARMv8 CPU nodes. It does not establish the commercial SoC SKU, so the Snapdragon 732G / SM7150 claim remains a separate community-reported lead.
- The source repository's `COPYING` file contains GPL version 2 terms; individual files may have additional or different notices. Review licenses per file before reuse.
- The matching kernel tree identifies the Qualcomm SDMMAGPIE device-tree platform and ARMv8 CPU nodes. This does not independently verify the retail SoC marketing name or silicon revision.
- A published Android/Linux kernel source tree is valuable hardware documentation, but it is not an XNU port.
- A device having an Android bootloader does not establish that it has a UEFI environment.
