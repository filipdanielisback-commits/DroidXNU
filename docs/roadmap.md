# DroidXNU development roadmap

This roadmap tracks research and implementation gates. A milestone is complete only when its evidence is committed and reviewed.

## Phase 0 — project baseline

- [x] Identify the target as Motorola Moto G60 XT2135-2.
- [x] Record Motorola's model/type declaration.
- [x] Add source provenance and confidence labels.
- [x] Remove emulator testing from project scope.
- [ ] Choose a project-wide license after reviewing all included source and contributions.

## Phase 1 — exact hardware identity

- [ ] Verify the exact XT2135-2 board revision and regional variant.
- [x] Identify the Qualcomm SDMMAGPIE platform from the model-linked Motorola device tree.
- [ ] Confirm the commercial SoC SKU and silicon revision from model-matched sources.
- [x] Corroborate the XT2135-2 HANOIP software target using Motorola issue #559 and its linked source tag.
- [ ] Inventory memory, CPU features, interrupt controller, timers and buses.
- [x] Add a structured subsystem inventory with explicit unknown/evidence states.
- [ ] Replace unknown inventory values only when model-matched evidence is reviewed.
- [ ] Record each finding in devices/moto-g60/board-facts.md and docs/compatibility.md.

## Phase 2 — public source analysis

- [x] Identify the Motorola kernel-source release linked to the XT2135-2 HANOIP RETEU Android 12 build.
- [x] Review Hanoip ARM64 config and device-tree source files without importing vendor binaries.
- [x] Record source tag, paths, provenance and license caveats in docs/research-sources.md and docs/source-review-motorola-hanoip.md.
- [x] Complete a source review note using docs/source-review-template.md.
- [x] Map visible HANOIP device-tree declarations to relevant Linux driver areas with confidence and limitation notes.

## Phase 3 — XNU feasibility study

- [x] Map first-pass XNU ARM64 bootstrap requirements in docs/xnu-arm64-bootstrap-requirements.md.
- [x] Identify first-pass platform-expert, interrupt-controller and timer dependencies; hardware compatibility remains unverified.
- [ ] Separate reusable architecture code from Apple-specific platform code.
- [ ] Write a gap analysis for every required platform service.
- [ ] Complete docs/xnu-porting-checklist.md with linked evidence.
- [ ] Decide whether the target is technically feasible before any loader implementation.

## Phase 4 — host-side engineering

- [x] Keep source inspection and configuration checks reproducible in WSL2.
- [x] Add host-side device metadata validation and unit tests.
- [x] Add a structured hardware inventory and host-side validator.
- [x] Add a Makefile entry point for repeatable validation and tests.
- [x] Add CI to run host-only checks on Python 3.11 and 3.12.
- [x] Keep the boot-menu demo clearly labelled as a mock-up.
- [ ] Run make check in a local WSL2 environment and record the result.
- [ ] Do not claim device support based on compilation alone.

## Device experimentation gate

No physical-device experiment is part of the current roadmap. Any future proposal requires a complete technical review, clear recovery plan, verified model-specific compatibility, and explicit project approval before it is considered.

## Explicitly out of scope

- QEMU and emulator test benches.
- Unverified bootloader or partition modifications.
- Proprietary operating-system images, firmware, or private keys.
- Claims that iOS 26 or XNU currently boots on the Moto G60.
