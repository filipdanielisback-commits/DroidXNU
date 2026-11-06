# Research Toolkit

The DroidXNU Research Toolkit produces a repeatable snapshot of the project's recorded research state.

## Commands

From the repository root:

```sh
make check
make report
make report-html
```

- `make check` validates device and hardware metadata and runs host-side unit tests.
- `make report` writes `build/research-report.md`.
- `make report-html` writes both Markdown and an escaped, dependency-free HTML report under `build/`.

The generated `build/` directory is ignored by Git; reports can be regenerated at any time.

## Inputs

- `devices/moto-g60/hardware-inventory.csv`: subsystem facts, evidence references, and open questions.
- `docs/research-sources.json`: curated source metadata with explicit support and limitation statements.

The JSON source register complements `docs/research-sources.md`. When adding a source, update both registers and preserve the distinction between manufacturer evidence, upstream sources, and community-reported material.

## Scope and limitations

This is a local, deterministic metadata report generator. It does not fetch URLs, inspect upstream source code, verify that links are live, probe hardware, access a phone, build a kernel, or test bootability. A listed reference is a research lead, not automatic proof of a claim. All unknowns remain visible rather than being filled with guesses.

No proprietary firmware, vendor blobs, operating-system images, keys, or personal device data are included.
