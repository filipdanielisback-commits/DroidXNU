# Motorola XT2135-2 kernel-source publication review

**Review date:** 2026-11-06  
**Target:** Moto G60 XT2135-2, Android 12 software build `S2RIS32.32-20-9-9-2-1`  
**Review type:** Public-source provenance check; source contents not yet audited.

## Finding

Motorola's public `kernel-msm` issue #559 is explicitly a request for the Moto G60 kernel source associated with firmware:

`XT2135-2_HANOIP_RETEU_12_S2RIS32.32-20-9-9-2-1_subsidy-DEFAULT_regulatory-XT2135-2-EUROPE_CFC.xml.zip`

The issue was closed with the `published` label. A Motorola contributor replied on 2023-11-29:

> Code released: https://github.com/MotorolaMobilityLLC/kernel-msm/releases/tag/MMI-S2RIS32.32-20-9-9-2-1

This is strong primary-source evidence that Motorola announced a matching kernel-source publication for the exact XT2135-2 software build.

## Access and verification limitation

On 2026-11-06, the linked GitHub release could not be retrieved through the public release endpoint (HTTP 404 / not found), and the repository's release listing returned no releases. The repository's default branch is `android-13-release-ttz`, which is not evidence that it matches the Android 12 build above.

Therefore this review does **not** claim that the source archive was downloaded, that its contents were inspected, or that the matching source revision is currently available. Do not substitute the repository's default branch for the named release.

## What this confirms

- The source request names the exact model XT2135-2.
- The requested firmware build is an Android 12 HANOIP RETEU build with identifier `S2RIS32.32-20-9-9-2-1`.
- A Motorola contributor explicitly stated that code was released and supplied a release-tag URL.
- The public repository is described by Motorola as Linux kernel source for MSM-based devices.

## What this does not confirm

- The precise SoC or silicon revision in this XT2135-2 unit.
- Exact board revision, memory map, CPU feature set, interrupt controller, timers, or peripheral wiring.
- That the named source release is currently downloadable or that the source archive has been inspected.
- That all required device-tree files, vendor components, or firmware interfaces are included.
- UEFI availability, boot-chain compatibility, or any XNU/iOS compatibility.

## Next safe research action

Locate an accessible, license-compatible copy of the exact Motorola release or a matching source commit using public repository metadata. Before using any code, record its exact tag/commit, top-level source contents, applicable license files, and whether its build identity matches the XT2135-2 firmware identifier above. Do not import source or binaries into DroidXNU until provenance and license review are complete.

## References

1. [Motorola kernel-msm issue #559](https://github.com/MotorolaMobilityLLC/kernel-msm/issues/559) — model and firmware request; closed with `published` label.
2. [Motorola contributor's release announcement](https://github.com/MotorolaMobilityLLC/kernel-msm/issues/559#issuecomment-1831904688) — names release tag `MMI-S2RIS32.32-20-9-9-2-1`.
3. [Announced release URL](https://github.com/MotorolaMobilityLLC/kernel-msm/releases/tag/MMI-S2RIS32.32-20-9-9-2-1) — currently not retrievable through the release endpoint at review time.
4. [Motorola kernel-msm repository](https://github.com/MotorolaMobilityLLC/kernel-msm) — public Linux kernel repository; its current default branch must not be treated as the exact Android 12 release.
