# Contributing to DroidXNU

Thanks for your interest. This project is at the research stage, so careful documentation is as valuable as code.

## Before opening a change

- Read the README and the relevant documents under `docs/`.
- Keep claims aligned with actual test evidence.
- Prefer small, reviewable changes.
- Include exact source provenance and license information for imported material.
- Never add proprietary firmware, system images, keys, credentials, or private logs.

## Code expectations

- Explain what a change does and what it does not do.
- Add host-side tests where practical.
- Do not add device-writing, flashing, partition-editing, or boot-chain modification behavior without a separately reviewed design and explicit maintainer approval.
- Keep experimental device work disabled by default.
- Do not claim a successful compile means the phone is supported.

## Reporting compatibility

A hardware feature must include the device revision, test environment, reproducible test, expected result, actual result, and relevant logs with personal identifiers removed.

## Licensing

Do not submit third-party source without identifying its origin and license. The project-wide license is not yet selected; see [docs/licensing.md](docs/licensing.md).
