# XNU platform-porting research checklist

**Status: planning only. No Moto G60 XNU port is implemented.**

## Gate A — source provenance

- [ ] Record the exact XNU repository, branch/tag, commit and retrieval date.
- [ ] Record licenses and copyright notices for every file proposed for reuse.
- [ ] Identify ARM64 architecture code separately from Apple platform code.
- [ ] Record unavailable or proprietary dependencies explicitly.

## Gate B — bootstrap and platform study

- [ ] Document the expected entry conditions for the selected XNU ARM64 configuration.
- [ ] Document exception-level and CPU feature assumptions.
- [ ] Document MMU, page-table, cache and memory-allocation assumptions.
- [ ] Identify early console and diagnostic requirements.
- [ ] Identify platform expert initialization boundaries.
- [ ] Identify interrupt-controller and timer interfaces.
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

- [ ] Complete a service-by-service gap analysis.
- [ ] Identify dependencies requiring new project-owned code.
- [ ] Review licensing and redistribution constraints.
- [ ] Review whether a separate user environment is technically and legally available.
- [ ] Publish a feasibility decision with assumptions and confidence.

## Gate E — implementation review

Completing this checklist does not authorize physical-device experiments. Any later implementation proposal needs a separate design review, compatibility evidence, data-protection review and explicit project approval.

## Evidence rule

A source file, successful compilation, or menu mock-up does not demonstrate hardware support. A working claim requires a reproducible test on the exact supported configuration and a reviewed record in the compatibility document.
