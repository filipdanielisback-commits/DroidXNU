# HANOIP Linux driver and hardware-description map

**Source:** Motorola `kernel-msm` tag `MMI-S2RIS32.32-20-9-9-2-1`  
**Reviewed target link:** XT2135-2 HANOIP RETEU Android 12 build, recorded in Motorola issue #559  
**Scope:** source-path and device-tree metadata mapping only. No code imported, no kernel built, no device queried.

This map connects visible Hanoip device-tree declarations to likely Linux driver areas in the same source tree. It is a research index, not proof that every listed node is enabled in every retail variant or that a Linux driver can be reused by XNU.

| Subsystem | Reviewed device-tree evidence | Linux driver area to inspect | Confidence / limitation |
|---|---|---|---|
| CPU / platform | `sdmmagpie.dtsi`: SDMMAGPIE compatible, ARMv8 CPU nodes, PSCI | `arch/arm64/`, `drivers/firmware/psci/`, Qualcomm SoC support | Model-linked platform evidence; not an XNU bootstrap recipe |
| Interrupts / GPIO | SoC DTS includes ARM GIC bindings and Qualcomm TLMM GPIO references | `drivers/irqchip/`, `drivers/pinctrl/qcom/`, `drivers/gpio/` | Bindings and references found; exact interrupt topology and initialization need full review |
| I2C / SPI | SoC aliases for QUPv3 I2C and SPI; Hanoip sensor and NFC nodes | `drivers/i2c/busses/`, `drivers/spi/`, Qualcomm QUP support | Bus instances are described; XNU needs its own controller/platform integration |
| Storage | SoC aliases describe eMMC, SD card and UFS nodes | `drivers/mmc/host/`, `drivers/ufs/host/` | DTS describes controller roles; exact retail storage population still needs confirmation |
| Display / panel | Hanoip common overlay includes `hanoi-panel.dtsi`; panel fragment names Tianma ILI7807S 678 1080x2460 video panel and DSI | `drivers/gpu/drm/msm/`, Qualcomm DSI / panel support | Specific panel appears in this software configuration; physical panel variant may differ |
| Touch | `sdmmagpie-hanoi-touchscreen.dtsi` declares `tchip,ilitek` on QUPv3 SPI | `drivers/input/touchscreen/` | Device-tree declaration only; controller revision and exact production variant unverified |
| NFC | Hanoip common overlay declares `qcom,nq-nci` on QUPv3 I2C | `drivers/nfc/` and Qualcomm / NQ integration | NFC node present in common overlay; physical component population not independently verified |
| Sensors | Hanoip sensor overlay declares Semtech SX933x on QUPv3 I2C | `drivers/iio/`, `drivers/input/misc/` (depending on upstream binding) | DTS identifies a SAR/proximity-related device node; don't generalize to the full sensor suite |
| Audio | Hanoip audio overlay references WCD937x codec, Qualcomm MI2S, Awinic AW882xx smart amplifier | `sound/soc/`, Qualcomm audio DSP / codec drivers | Audio graph and components are described in this source configuration; board-level routing needs review |
| Battery / charging / thermal | `hanoi_battery_thermal_overlay.dtsi` references PM6150 charger, gauge, ADC thermal zones and battery-data includes | `drivers/power/supply/`, `drivers/thermal/`, Qualcomm PMIC support | Configuration-specific battery data; not proof of exact battery vendor or pack in every unit |
| USB | SoC tree and kernel source include Qualcomm USB support; Hanoip overlay details require deeper node-by-node pass | `drivers/usb/`, Qualcomm DWC3 / PHY support | Not enough evidence in the reviewed Hanoip fragments to assert exact port role or external connector behavior |
| Wi-Fi / Bluetooth | Not fully mapped in the Hanoip overlays reviewed for this note | Qualcomm WLAN / Bluetooth subsystems | Keep unknown until exact board configuration and firmware dependencies are reviewed |
| Boot / firmware handoff | SoC DTS has Android firmware / vbmeta metadata and reserved-memory declarations; this is not UEFI evidence | `drivers/firmware/`, Qualcomm boot / SCM interfaces | Does not establish UEFI, bootloader handoff contract, or a safe alternate boot path |

## Important interpretation

- A device-tree node names a device or interface for the Linux kernel. It does not prove that a driver is loaded, that the component is physically populated in every retail unit, or that an XNU equivalent exists.
- Linux driver paths are investigation leads. Do not copy source into DroidXNU until the exact file license, dependencies, and architectural fit have been reviewed.
- The kernel repository's root `COPYING` file contains GPL version 2 terms, while individual source files may carry their own notices. Review per file.
- No vendor firmware, binary blobs, calibration data, or proprietary images are included in this project.
- The source release is tied to a HANOIP RETEU Android 12 build. It does not identify the exact physical EVT/DVT/PVT revision of an individual phone.

## Primary source files

- [SDMMAGPIE base device tree](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie.dtsi)
- [HANOIP common overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-common-overlay.dtsi)
- [HANOIP sensor overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoip-sensor-overlay.dtsi)
- [HANOI panel description](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/hanoi-panel.dtsi)
- [HANOI touchscreen description](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoi-touchscreen.dtsi)
- [HANOI audio overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/sdmmagpie-hanoi-audio-overlay.dtsi)
- [HANOI battery and thermal overlay](https://github.com/MotorolaMobilityLLC/kernel-msm/blob/MMI-S2RIS32.32-20-9-9-2-1/arch/arm64/boot/dts/qcom/hanoi_battery_thermal_overlay.dtsi)
