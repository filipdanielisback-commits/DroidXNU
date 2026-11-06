# Motorola kernel source review: Moto G60 / HANOIP

**Review date:** 2026-11-06  
**Scope:** Public Motorola kernel source metadata and selected device-specific configuration/device-tree files. This is a source review only; no kernel was built and no device was accessed.

## Result

<badge>Strong device-family evidence</badge>

Motorola's public `kernel-msm` repository contains a published tag named `MMI-S2RIS32.32-20-9-9-2-1`. The tag annotation says "Hanoip push for Android 12". Motorola issue #559 is a request for the Moto G(60) kernel source for build `S2RIS32.32-20-9-9-2-1`; the request names the firmware package `XT2135-2_HANOIP_RETEU_12_S2RIS32.32-20-9-9-2-1...`. A Motorola contributor replied that the code was released under the matching tag.

This is a strong match between the XT2135-2 Moto G60 firmware build and Motorola's HANOIP kernel source release. It is not proof that every HANOIP-family board file applies unchanged to every XT2135-2 regional/hardware revision.

## Files inspected

All paths below are in the tagged Motorola source tree at commit `f6673a1302e3b9ca84c54e956ad4075d676fdf59`.

| File | What it establishes | What it does not establish |
|---|---|---|
| `arch/arm64/configs/vendor/ext_config/moto-sdmmagpie-hanoip.config` | Motorola-specific HANOIP kernel configuration exists; it enables `CONFIG_HANOIP_DTB`. | A complete CPU feature inventory or XNU compatibility. |
| `arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-common-overlay.dtsi` | HANOIP common overlay includes Motorola SDMMAGPIE common, audio, panel, battery/thermal, sensor, touchscreen and audio overlays; configures NFC-related GPIO/I²C and disables a DisplayPort node. | A complete standalone board description or proof that these settings can be reused by XNU. |
| `arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-sensor-overlay.dtsi` | HANOIP sensor overlay describes a Semtech SX933x device on an I²C bus and associated GPIO/regulator references. | Full sensor inventory or confirmation of the exact sensor fitted in every XT2135-2 unit. |
| `arch/arm64/boot/dts/qcom/sdmmagpie-moto-base.dtsi` | The Motorola base DTSI includes the SDMMAGPIE SoC description and memory/reserved-memory adjustments. | The phone's complete physical memory map at runtime. |

## Findings

1. **Architecture evidence:** the device-specific files are under `arch/arm64`, so this source release is for an ARM64 kernel target. This is strong platform evidence, but the exact CPU feature set still needs model-specific documentation.
2. **Platform naming:** the device configuration and overlays use the names `HANOIP` and `SDMMAGPIE`.
3. **Peripheral evidence:** the inspected overlay describes NFC, touch, display, audio, battery/thermal and sensor integration points. These are useful leads for the driver matrix.
4. **Device-tree role:** these files are Linux device-tree configuration and overlays. They are not EFI tables, an EFI implementation, or XNU platform drivers.
5. **Licensing:** the inspected DTSI files contain GPL-2.0-only notices. The repository's top-level GitHub license metadata is `NOASSERTION`; each file must be reviewed individually before any reuse. This review records references only and copies no Motorola source code into DroidXNU.

## Not established

- The exact SoC marketing name and silicon revision for every XT2135-2 variant.
- A complete XT2135-2 board-specific DTS and all device-tree overlays actually selected by the firmware build.
- Boot ROM, bootloader, secure-boot, image-format or EFI protocol behavior.
- Whether the boot chain can load a non-Android kernel.
- XNU support for SDMMAGPIE/HANOIP, or any usable Apple driver for these components.
- A working kernel build or boot on the Moto G60.

## Next source-review tasks

- Identify the exact DTS/DTBO composition selected by the XT2135-2 firmware build from public metadata.
- Compare HANOIP device-tree names against the community device tree, recording where the mapping is direct and where it is only family-level.
- Review source licensing before considering any code import.
- Continue boot-chain research separately; do not infer UEFI from the existence of ARM64 Linux source.

## References

- [Motorola kernel-msm repository](https://github.com/MotorolaMobilityLLC/kernel-msm)
- [Motorola source request #559](https://github.com/MotorolaMobilityLLC/kernel-msm/issues/559)
- [Motorola HANOIP Android 12 source tag](https://github.com/MotorolaMobilityLLC/kernel-msm/tree/MMI-S2RIS32.32-20-9-9-2-1)
- [Tagged source commit](https://github.com/MotorolaMobilityLLC/kernel-msm/commit/f6673a1302e3b9ca84c54e956ad4075d676fdf59)
- [HANOIP kernel configuration](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/configs/vendor/ext_config/moto-sdmmagpie-hanoip.config)
- [HANOIP common overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-common-overlay.dtsi)

## Device-tree build selection evidence

The tagged kernel tree's `arch/arm64/boot/dts/qcom/Makefile` associates `CONFIG_HANOIP_DTB` with three HANOIP overlay outputs:

- `sdmmagpie-hanoip-evt1-overlay.dtbo`
- `sdmmagpie-hanoip-dvt1-overlay.dtbo`
- `sdmmagpie-hanoip-dvt2-overlay.dtbo`

The Makefile sets each overlay's base to `sdmmagpie-hanoi-base.dtb`. The base file `sdmmagpie-hanoi-base.dts` includes `sdmmagpie-moto-base.dtsi`. The HANOIP common overlay includes the HANOIP sensor overlay plus shared display, audio, battery/thermal and touchscreen overlay files.

This establishes the source tree's candidate base/overlay relationships. It does **not** identify which hardware revision or DTBO combination was selected for the XT2135-2 European firmware build. The exact selected DTBO remains unknown without build-specific product configuration or authoritative firmware metadata.

## Cross-check against the community HANOIP Android device tree

The public [motorola-sm6150-devs/device_motorola_hanoip](https://github.com/motorola-sm6150-devs/device_motorola_hanoip) repository describes itself as an Android device tree for the Moto G40 Fusion / Moto G60 family. Its inspected `BoardConfig.mk` records:

- `TARGET_ARCH := arm64`, `TARGET_ARCH_VARIANT := armv8-2a-dotprod`, and `TARGET_CPU_VARIANT := cortex-a76`.
- A secondary 32-bit ARM target with `cortex-a55`.
- `TARGET_BOARD_PLATFORM := sm6150`.
- Kernel configuration fragments including `vendor/ext_config/moto-sdmmagpie-hanoip.config`.
- A separate DTBO image and a boot image containing a DTB.

This corroborates ARM64 and the HANOIP family association, and shows the Android build's declared platform and kernel configuration inputs. However, the community board config's `sm6150` label and Motorola's `SDMMAGPIE` source naming are not enough on their own to identify the exact silicon part. The earlier Snapdragon 732G / SM7150 label remains an unverified family-level lead, not a confirmed XT2135-2 fact.

The community device tree is a different source project from Motorola's kernel release. Its README identifies the project as Apache-2.0; inspect each file's headers before reuse. Motorola's inspected device-tree files carry GPL-2.0-only notices. Do not mix or copy files until a file-by-file license review is complete.

### Updated conclusion

The source evidence supports **ARM64 + HANOIP family + SDMMAGPIE-named Motorola kernel DTS/overlays**. The exact XT2135-2 silicon identity and exact DTBO selected by the European firmware build remain open questions.
