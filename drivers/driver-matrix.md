# Moto G60 driver research matrix

This matrix is a research checklist, not a driver implementation or compatibility claim.

| Subsystem | Hardware identity | Public Linux reference | XNU interface needed | Status |
|---|---|---|---|---|
| Interrupt controller | Unknown | To identify from matching kernel source | Interrupt controller/platform integration | Unknown |
| Timers / clock | Unknown | To identify from matching kernel source | Clock and timer services | Unknown |
| Storage | Unknown | To identify from matching kernel source | Block/storage stack integration | Unknown |
| Display / GPU | Unknown | To identify from matching kernel source | Display and graphics services | Unknown |
| Touch | Unknown | To identify from matching kernel source | Input event interface | Unknown |
| USB | Unknown | To identify from matching kernel source | USB host/device services | Unknown |
| Wi-Fi / Bluetooth | Unknown | To identify from matching kernel source | Network and wireless integration | Unknown |
| Audio | Unknown | To identify from matching kernel source | Audio device and routing services | Unknown |
| Sensors | Unknown | To identify from matching kernel source | Sensor/input interfaces | Unknown |
| Power / thermal | Unknown | To identify from matching kernel source | Power, battery and thermal services | Unknown |

A Linux driver is a hardware reference, not an XNU driver that can be reused unchanged. For every subsystem, record exact component, board variant, source commit, driver path, license, dependencies and evidence.

Do not add vendor binaries or proprietary firmware. Do not mark a driver implemented until project-owned code exists and has been reviewed.


## Motorola HANOIP source mapping

See [docs/linux-driver-map-motorola-hanoip.md](../docs/linux-driver-map-motorola-hanoip.md) for the source-backed mapping from HANOIP device-tree declarations to Linux driver areas. It records evidence and limitations and does not claim that any driver is implemented in DroidXNU.
