# XNU platform-porting research checklist

**Status: planning only. No Moto G60 XNU port is implemented.**

## Gate A — source provenance

- [x] Record the exact XNU repository, branch and commit for this first-pass review (2026-11-06; `f6217f891ac0bb64f3d375211650a4c1ff8ca1ea`).
- [ ] Record licenses and copyright notices for every file proposed for reuse.
- [x] Identify ARM64 architecture code separately from Apple platform code in [xnu-layer-separation.md](xnu-layer-separation.md).
- [ ] Record unavailable or proprietary dependencies explicitly.

## Gate B — bootstrap and platform study

- [x] Document first-pass expected entry conditions in [xnu-arm64-bootstrap-requirements.md](xnu-arm64-bootstrap-requirements.md); exact target configuration still needs selection.
- [ ] Document exception-level and CPU feature assumptions.
- [ ] Document MMU, page-table, cache and memory-allocation assumptions.
- [ ] Identify early console and diagnostic requirements.
- [x] Identify first-pass platform expert initialization boundaries in [xnu-arm64-bootstrap-requirements.md](xnu-arm64-bootstrap-requirements.md).
- [x] Identify first-pass interrupt-controller and timer interfaces; HANOIP compatibility remains unknown.
- [ ] Record unknowns rather than filling gaps with guesses.

## Gate C — Moto G60 evidence

- [ ] Verify exact XT2135-2 board and regional variant.
- [ ] Verify SoC and silicon revision from model-matched evidence.
- [ ] Establish memory map, interrupt and timer hardware.
- [ ] Establish storage and device-tree handoff requirements.
- [ ] Establish whether an EFI interface exists; do not assume one.
- [ ] Map display, touch, USB, wireless, audio and power components.
- [ ] Link every finding to a source and update the hardware inventory.

## Gate D — feasibility decision

For each required service, record available, adaptable, blocked or unknown.

- [x] Complete a preliminary service-by-service gap analysis in [xnu-platform-gap-analysis.md](xnu-platform-gap-analysis.md); many entries remain unknown.
- [ ] Identify dependencies requiring new project-owned code.
- [ ] Review licensing and redistribution constraints.
- [ ] Review whether a separate user environment is technically and legally available.
- [ ] Publish a feasibility decision with assumptions and confidence.

## Gate E — implementation review

Completing this checklist does not authorize physical-device experiments. Any later implementation proposal needs a separate design review, compatibility evidence, data-protection review and explicit project approval.

## Evidence rule

A source file, successful compilation, or menu mock-up does not demonstrate hardware support. A working claim requires a reproducible test on the exact supported configuration and a reviewed record in the compatibility document.


## First-pass bootstrap research

See [xnu-arm64-bootstrap-requirements.md](xnu-arm64-bootstrap-requirements.md) for the initial source-backed review of ARM64 entry, boot arguments, CPU startup, device-tree, SoC identification, interrupt-controller, timer and console dependencies. This is a requirements note only; no port is implemented.


## Platform-service gap analysis

See [xnu-platform-gap-analysis.md](xnu-platform-gap-analysis.md) for the preliminary service-by-service comparison between reviewed XNU requirements and Motorola HANOIP source evidence. Several core services remain unknown or unimplemented; this is not a go-ahead for loader development.
