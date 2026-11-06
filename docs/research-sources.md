# Research source register

This register tracks public references used by DroidXNU. It records what each source supports and what it does not prove.

| Source | Type | Supports | Does not prove |
|---|---|---|---|
| [Motorola XT2135-2 declaration](https://en-us.support.motorola.com/ci/fattach/get/79315385/1664922506/redirect/1/filename/XT2135-2_Moto%2BG60%2BVision%2BMC38C%2BRED%2BDoC.pdf) | Manufacturer document | Moto G60 model XT2135-2, type MC38C | SoC, board revision, UEFI, XNU support |
| [hanoip Android device tree](https://github.com/motorola-sm6150-devs/device_motorola_hanoip) | Public community source | Android device-tree work for Moto G40 Fusion / Moto G60 family | Exact compatibility of every variant or XNU support |
| [Moto Common target index](https://github.com/moto-common/android_device_motorola_targets) | Public community target index (archived 2026-04-04) | Lists hanoip for Moto G40 Fusion / Moto G60; records target as dropped in that index | Exact XT2135-2 board revision, current support, or XNU feasibility |
| [Motorola kernel-msm issue #559](https://github.com/MotorolaMobilityLLC/kernel-msm/issues/559) | Motorola source publication record | Motorola contributor points to a published source release for an XT2135-2 build | That source is sufficient to boot XNU |
| [Android device-tree documentation](https://source.android.com/docs/core/architecture/dto) | Official Android documentation | General purpose and use of DT/DTBO in Android boot flows | Exact Moto G60 device-tree contents |
| [Apple XNU source](https://github.com/apple-oss-distributions/xnu) | Apple open-source repository | Source for the XNU kernel | A ready-made third-party Moto G60 platform port |
| [Apple distribution-iOS branch](https://github.com/apple-oss-distributions/distribution-iOS/tree/ios-260) | Apple source tree supplied for research | Material to inspect under its own repository and file licenses | A complete, installable iOS 26 image for Moto G60 |
| [HakiOS reference](https://github.com/oosexgang/hakios-xnu-kernel) | Independent research project | Example of a layered XNU research repository | A compatible implementation to copy or proof of Moto G60 support |

## Citation and provenance rules

- Link to the original source, not a rehosted copy.
- Record the exact branch, tag, release or commit when source code is reviewed.
- Preserve upstream copyright and license notices.
- Do not copy code until its license and compatibility with this repository are reviewed.
- Mark third-party device information as community-reported unless confirmed by Motorola or a model-matched primary source.
- Do not commit proprietary firmware, vendor blobs, private keys, credentials or Apple system images.
