# Moto G60 boot-chain research

**Status: unknown; research only.** This document does not describe a verified XT2135-2 boot procedure.

## Questions to answer from public evidence

1. Which boot stages are documented for the exact regional model?
2. Which image formats and handoff structures are expected at each stage?
3. Which stage verifies the next stage, and what is the documented trust model?
4. How are memory regions and hardware descriptions passed onward?
5. Which diagnostic interfaces are documented?
6. Is an EFI protocol environment present, or is another boot interface used?
7. Which details vary by board revision, software release or regional SKU?

## Generic concepts (not a Moto G60 claim)

Many mobile platforms have immutable early boot code followed by one or more bootloader stages and an operating-system boot image. The exact sequence, names, formats and verification behavior are platform-specific. DroidXNU must not treat this generic pattern as a verified description of XT2135-2.

## Evidence record

For each claim, record the exact model and regional variant, software build, original source URL and revision/date, relevant source file, confidence level, and differences between XT2135-1, XT2135-2 and related hanoip devices.

## Current project constraints

- No EFI loader is implemented.
- The host menu is a terminal mock-up only.
- No boot image is produced.
- No phone is connected to or modified by repository tools.
- The project does not include instructions or automation for changing bootloader, firmware or partition state.

## Decision gate

Do not design a device loader until the real boot interface, kernel entry contract, hardware-description handoff and recovery implications are understood from reliable model-matched evidence. If the platform does not expose EFI, document that finding rather than assuming an EFI application can run natively.
