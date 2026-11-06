# Compatibility status

Status vocabulary:

- **Unknown** — not researched or not verified.
- **Researched** — credible documentation collected, no implementation claim.
- **Implemented** — project code exists, but may not work on target hardware.
- **Tested** — a reproducible test was run; record exact setup and result.
- **Unsupported** — known not to work or intentionally out of scope.

## Moto G60 (XT2135-2)

| Area | Status | Evidence / next step |
|---|---|---|
| Product identity | Researched | Motorola declaration identifies Moto G60, model XT2135-2 (MC38C) |
| Device-family codename | Researched | Public Android device tree covers Moto G40 Fusion / Moto G60 as `hanoip`; confirm exact variant mapping |
| SoC family | Researched | Snapdragon 732G / SM7150 is reported by community device references; verify against Motorola source and exact model |
| CPU / ARM64 details | Unknown | Record CPU implementer, cores and architectural features from reliable model-specific data |
| Board revision | Unknown | Find exact hardware revision and board configuration |
| Memory map | Unknown | Requires reliable board-level information |
| Boot chain / EFI availability | Unknown | Determine actual boot stages and image formats; do not assume native UEFI |
| Interrupt controller | Unknown | Research SoC documentation and public kernel source |
| Timer / clock sources | Unknown | Research SoC documentation and public kernel source |
| Serial diagnostics | Unknown | Identify documentation for safe, non-invasive diagnostics |
| Storage controller | Unknown | Research only; no writes planned |
| Display / GPU | Unknown | Research controller and available documentation |
| Touch | Unknown | Identify controller and protocol |
| USB | Unknown | Research controller and host/device mode |
| Wi-Fi / Bluetooth | Unknown | Identify chip and licensing/documentation constraints |
| Audio | Unknown | Research codec and routing |
| Power / thermal management | Unknown | Research before any hardware testing |
| XNU boot | Unknown | No port or bootable image exists |
| User space | Unknown | No compatible user space is included |

## Test record template

For every future research observation or test, record:

- Date and project commit:
- Device model / board revision:
- Host OS and tool versions:
- Research method (public-source review / host-only test / device observation):
- Exact source or procedure:
- Expected result:
- Actual result:
- Logs and artifact hashes (redact personal data):
- Data-safety review:
- Reviewer:

Do not report a feature as working based only on a successful compile. Do not perform partition writes or firmware changes as part of this research phase.
