# Moto G60 hardware research plan

**Target:** Motorola Moto G60, model XT2135-2 (type MC38C).  
**Project status:** documentation and host-side research only.

This is a research plan, not a device modification guide. Keep work to public documentation, source review, and host-side development.

## What is established

- Motorola issue #559 identifies the XT2135-2 HANOIP RETEU Android 12 firmware build, and a Motorola contributor links the published source tag `MMI-S2RIS32.32-20-9-9-2-1`. The tag contains a Hanoip-specific ARM64 kernel configuration fragment and Hanoip device-tree overlays.
- The tagged SDMMAGPIE device tree identifies the Qualcomm platform as `qcom,sdmmagpie` and CPU nodes as ARMv8. The commercial SoC SKU is still not established by these reviewed files.
- The exact source review and limitations are recorded in [docs/source-review-motorola-hanoip.md](source-review-motorola-hanoip.md).

- Motorola's EU Declaration of Conformity identifies the Moto G60 model XT2135-2 and type MC38C.
- Public Android community indexes associate the hanoip family with Moto G40 Fusion / Moto G60. This is family-level evidence; exact XT2135-2 variant mapping still needs verification.
- The public Moto Common target index is archived and labels its hanoip target as dropped. This is historical community-maintenance metadata, not proof that the hardware is unusable or that all device development has ended.
- Motorola's kernel-source issue tracker records a published source release associated with an XT2135-2 Android 12 software build.
- Community device references report a Qualcomm Snapdragon 732G / SM7150 platform for the hanoip family. This remains a model-specific verification task, not a confirmed board fact for every XT2135-2 unit.

## Research workstreams

### 1. Identity and variant mapping

- Confirm XT2135-2, type MC38C and regional suffixes from manufacturer documentation.
- Determine whether public hanoip sources explicitly list XT2135-2 or only the broader G60 family.
- Record board revision only when supported by a reliable source.
- Keep facts for XT2135-1, XT2135-2 and G40 Fusion variants separate unless a source proves they are shared.

### 2. SoC and CPU

- Locate model-matched public kernel-source metadata and board configuration.
- Verify the SoC identifier and silicon revision.
- Record CPU architecture, cores, exception-level support and required architectural features from authoritative documentation.
- Do not infer a complete XNU platform configuration from the presence of a 64-bit CPU.

### 3. Boot-chain architecture

- Document the boot stages and image formats from public documentation and source code.
- Determine whether the device exposes a UEFI protocol environment. Do not equate an Android bootloader with UEFI.
- Identify where device-tree data is supplied and how the next stage receives memory and hardware descriptions.
- Keep the current boot-menu program as a host-only mock-up until the actual platform boundary is understood.
- See docs/boot-chain-research.md for the evidence record and loader decision gate.

### 4. Hardware inventory

For each device component, record its exact controller, source evidence, Linux driver references (if any), XNU equivalent requirements, and current confidence.

The structured inventory is stored in devices/moto-g60/hardware-inventory.csv. The reviewed Linux driver areas and their evidence limitations are summarized in [linux-driver-map-motorola-hanoip.md](linux-driver-map-motorola-hanoip.md). Validate it with python3 tools/validate_hardware_inventory.py. Unknown values remain explicitly unknown until model-matched evidence is reviewed.

### 5. XNU feasibility

- Map XNU's ARM64 bootstrap and platform expert assumptions.
- Identify dependencies on Apple-specific hardware or firmware interfaces.
- Separate portable kernel code from platform-specific code.
- Record any required new platform support as an unresolved engineering problem, not as an implemented feature.
- Use docs/xnu-porting-checklist.md to track evidence and feasibility gates.

## Evidence quality

Use this order of preference:

1. Motorola documentation and Motorola-published source releases.
2. Public source trees tied to the exact device family and software build.
3. Official SoC documentation.
4. Maintained community device trees and kernel projects.
5. General specification aggregators only as leads.

A community source can guide research but must not silently upgrade a claim to manufacturer-confirmed status.

## Out of scope

- QEMU and other emulator-based testing.
- Firmware or partition changes on the phone.
- Redistributing proprietary firmware, vendor blobs, or Apple system images.
- Claiming that iOS 26 or XNU boots on the phone.
