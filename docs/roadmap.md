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
- [ ] Confirm the SoC and silicon revision from model-matched sources.
- [ ] Confirm the `hanoip` family mapping for this exact variant.
- [ ] Inventory memory, CPU features, interrupt controller, timers and buses.
- [ ] Record each finding in `devices/moto-g60/board-facts.md` and `docs/compatibility.md`.

## Phase 2 — public source analysis

- [ ] Identify the Motorola kernel-source release matching the target software build.
- [ ] Review device-tree and board configuration files without importing vendor binaries.
- [ ] Record source tags/commits and licenses in `docs/research-sources.md`.
- [ ] Map relevant Linux hardware drivers to the hardware inventory.

## Phase 3 — XNU feasibility study

- [ ] Map XNU ARM64 bootstrap requirements.
- [ ] Identify platform-expert and interrupt/timer dependencies.
- [ ] Separate reusable architecture code from Apple-specific platform code.
- [ ] Write a gap analysis for every required platform service.
- [ ] Decide whether the target is technically feasible before any loader implementation.

## Phase 4 — host-side engineering

- [ ] Keep source inspection and configuration checks reproducible in WSL2.
- [x] Add host-side metadata validation and unit tests (4 tests pass locally).
- [x] Keep the boot-menu demo clearly labelled as a mock-up.
- [ ] Do not claim device support based on compilation alone.

## Device experimentation gate

No physical-device experiment is part of the current roadmap. Any future proposal requires a complete technical review, clear recovery plan, verified model-specific compatibility, and explicit project approval before it is considered.

## Explicitly out of scope

- QEMU and emulator test benches.
- Unverified bootloader or partition modifications.
- Proprietary operating-system images, firmware, or private keys.
- Claims that iOS 26 or XNU currently boots on the Moto G60.
