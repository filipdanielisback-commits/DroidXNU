# XNU porting status

**Status: research only.**

No XNU source has been imported, patched or built by this repository. This directory is a planning area, not a kernel tree.

| Work item | Status |
|---|---|
| Identify upstream XNU source | Research reference recorded |
| Pin exact upstream revision | Not done |
| Review file-level licenses | Not done |
| Identify ARM64 bootstrap assumptions | Not done |
| Identify Moto G60 platform entry contract | Unknown |
| Implement platform expert | Not implemented |
| Implement interrupt/timer support | Not implemented |
| Build an XNU kernel | Not demonstrated |
| Boot on Moto G60 | Not demonstrated |

## Before adding kernel code

1. Complete the source review template for the selected XNU revision.
2. Record the exact upstream commit and applicable license.
3. Map architecture-generic code separately from Apple platform code.
4. Complete the XNU porting checklist.
5. Complete the device-specific hardware inventory and boot-chain evidence.
6. Document every required platform service and its feasibility.

Keep project-owned changes separate from pristine upstream source. Preserve provenance and make patches reviewable. Do not present an unmodified upstream checkout as a DroidXNU port.

This file does not claim that XNU compiles for the target, that a kernel entry point is known, or that the phone can boot an experimental kernel.
