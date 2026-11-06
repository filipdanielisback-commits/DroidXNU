# Moto G60 hardware research plan

**Target:** Motorola Moto G60, model XT2135-2 (type MC38C).  
**Project status:** documentation and host-side research only.

This document is a research plan, not a device modification guide. Keep work to public documentation, source review, and host-side development.

## What is established

- Motorola's EU Declaration of Conformity identifies the Moto G60 model XT2135-2 and type MC38C.
- A public Android device-tree repository describes support for the Moto G40 Fusion / Moto G60 family using the codename `hanoip`.
- Motorola's kernel-source issue tracker records a published source release associated with an XT2135-2 Android 12 software build.
- Community device references report a Qualcomm Snapdragon 732G / SM7150 platform for the hanoip family. This remains a model-specific verification task, not a confirmed board fact for every XT2135-2 unit.

## Research workstreams

### 1. Identity and variant mapping

- Confirm XT2135-2, type MC38C and regional suffixes from manufacturer documentation.
- Determine whether the public `hanoip` device tree explicitly lists XT2135-2 or only the broader G60 family.
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

### 4. Hardware inventory

For each device component, record its exact controller, source evidence, Linux driver references (if any), XNU equivalent requirements, and current confidence:

- DRAM and memory map
- interrupt controller and timers
- storage and filesystem access
- display, GPU and panel
- touch controller
- USB controller
- Wi-Fi and Bluetooth
- audio codec and routing
- sensors
- power, charging and thermal management

### 5. XNU feasibility

- Map XNU's ARM64 bootstrap and platform expert assumptions.
- Identify dependencies on Apple-specific hardware or firmware interfaces.
- Separate portable kernel code from platform-specific code.
- Record any required new platform support as an unresolved engineering problem, not as an implemented feature.

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
