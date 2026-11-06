# Host-side development workflow

This workflow keeps development reproducible and separate from the physical phone.

## Inspect the project

Read the README, roadmap, compatibility, licensing and research-source documents. Check the exact device model and confidence level of any hardware claim before changing it.

## Make a small change

- Keep one logical change per commit where practical.
- Link upstream sources and exact revisions.
- Preserve upstream license notices.
- Add or update tests for host-side code.
- Mark scaffolding and placeholders clearly.
- Do not add proprietary or personal data.

## Run host checks

```sh
make check
```

These commands inspect repository files only. They do not communicate with the phone.

## Review the result

- Confirm tests actually ran and record their output.
- Check the diff for accidental binaries, keys, firmware or local files.
- Update the roadmap only when acceptance evidence exists.
- Update compatibility status only with model-matched, reproducible evidence.

## Report status honestly

An implementation is not tested merely because it exists. A host test is not a device test. A compile is not a successful boot.

## Not part of this workflow

This workflow does not authorize device flashing, partition modification, bootloader changes or experiments on a daily-use phone.
