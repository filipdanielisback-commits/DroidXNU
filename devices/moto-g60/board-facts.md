# Moto G60 board facts

This file distinguishes manufacturer-confirmed identity from community-reported family information.

| Field | Current value | Confidence |
|---|---|---|
| Commercial name | Motorola Moto G60 | Manufacturer-confirmed |
| Model number | XT2135-2 | Manufacturer-confirmed |
| Motorola type identifier | MC38C | Manufacturer-confirmed |
| Internal family codename | `hanoip` | Public Android device-tree family reference; exact model mapping to verify |
| SoC | Reported Qualcomm Snapdragon 732G / SM7150 | Community-reported; verify against matching Motorola source |
| CPU architecture | ARM64/AArch64 | Not yet model-specifically verified in this repository |
| Board revision | Unknown | Unverified |
| Native UEFI support | Unknown | Do not assume |
| XNU compatibility | Unknown | No implementation or boot test exists |

## Primary references

1. Motorola EU Declaration of Conformity: [XT2135-2 Moto G60 Vision / MC38C PDF](https://en-us.support.motorola.com/ci/fattach/get/79315385/1664922506/redirect/1/filename/XT2135-2_Moto%2BG60%2BVision%2BMC38C%2BRED%2BDoC.pdf)
2. Public Android device tree: [motorola-sm6150-devs/device_motorola_hanoip](https://github.com/motorola-sm6150-devs/device_motorola_hanoip)
3. Motorola kernel source publication record: [MotorolaMobilityLLC/kernel-msm issue #559](https://github.com/MotorolaMobilityLLC/kernel-msm/issues/559)
4. Android device-tree background: [Android Open Source Project — Device tree overlays](https://source.android.com/docs/core/architecture/dto)

## Interpretation notes

- Motorola's declaration proves the commercial model and model number; it does not disclose the complete SoC or boot-chain design.
- The community device tree describes the G40 Fusion / G60 family as `hanoip`; exact variant-specific entries must be checked before applying its configuration to XT2135-2.
- A published Android/Linux kernel source tree is valuable hardware documentation, but it is not an XNU port.
- A device having an Android bootloader does not establish that it has a UEFI environment.
