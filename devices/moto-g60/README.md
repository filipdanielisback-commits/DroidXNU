# Motorola Moto G60 — XT2135-2

**Port status: research only. No bootable port exists.**

Motorola's EU declaration identifies model XT2135-2 as the Moto G60, type MC38C. A public Android device tree covers the Moto G40 Fusion / Moto G60 family under the codename `hanoip`. That family-level reference is useful, but the exact XT2135-2 regional mapping and hardware revision still need confirmation.

## Project target

- Device: Motorola Moto G60
- Model: XT2135-2
- Type identifier in Motorola declaration: MC38C
- Reported family codename: `hanoip` (exact variant mapping to verify)
- Reported SoC family: Qualcomm Snapdragon 732G / SM7150 (not yet verified against model-specific Motorola source)
- Host development baseline: Windows + WSL2
- Host memory planning target: 6 GB
- Bootloader state requested by project: unlocked

These are project planning details and research leads, not proof of hardware compatibility or a recommendation to modify a phone.

## Research checklist

- [x] Confirm the exact commercial model name and model number from Motorola documentation.
- [ ] Confirm exact board name, revision and regional variant mapping.
- [ ] Confirm SoC model and silicon revision from model-specific evidence.
- [ ] Record CPU architecture and supported exception levels.
- [ ] Review public device-tree and kernel-source references.
- [ ] Document boot chain and supported image formats from public sources.
- [ ] Identify interrupt controller, timer and memory layout.
- [ ] Identify storage, display, touch, USB, audio and power components.
- [ ] Map each component to available public documentation.
- [ ] Record unknowns rather than guessing.

See [board facts](board-facts.md), [hardware research](../../docs/hardware-research.md), and [compatibility.md](../../docs/compatibility.md).

## Data handling

Do not add proprietary firmware, private keys, device credentials, or personal logs here. Keep this directory limited to original notes, public references, and project-owned configuration.
