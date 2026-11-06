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
| Exact board identifier | Unknown | Identify from trustworthy device documentation |
| Exact SoC revision | Unknown | Verify XT2135-2 mapping |
| CPU / ARM64 details | Unknown | Record CPU implementer, cores and architectural features |
| Memory map | Unknown | Requires reliable board-level information |
| Boot chain / EFI availability | Unknown | Determine whether native EFI exists or a separate platform layer is needed |
| Interrupt controller | Unknown | Research SoC documentation |
| Timer / clock sources | Unknown | Research SoC documentation |
| Serial console | Unknown | Identify safe diagnostic path |
| Storage controller | Unknown | Research; no writes planned |
| Display / GPU | Unknown | Research controller and available documentation |
| Touch | Unknown | Identify controller and protocol |
| USB | Unknown | Research controller and host/device mode |
| Wi-Fi / Bluetooth | Unknown | Identify chip and licensing/documentation constraints |
| Audio | Unknown | Research codec and routing |
| Power / thermal management | Unknown | Research before any hardware testing |
| XNU boot | Unknown | No port or bootable image exists |
| User space | Unknown | No compatible user space is included |

## Test record template

For every future test, record:

- Date and project commit:
- Device model / board revision:
- Host OS and tool versions:
- Test environment (QEMU or physical device):
- Exact test command or procedure:
- Expected result:
- Actual result:
- Logs and artifact hashes:
- Data-safety / recovery review:
- Reviewer:

Do not report a feature as working based only on a successful compile.
