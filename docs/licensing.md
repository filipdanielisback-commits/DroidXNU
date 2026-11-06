# Licensing and source provenance

This file is a project policy note, not legal advice.

## Current policy

No project-wide license has been selected yet. Until the maintainers choose one, contributors should not assume that all DroidXNU files may be redistributed under MIT or another blanket license.

## XNU

Apple publishes XNU source under the Apple Public Source License (APSL). Before importing or modifying any XNU files:

1. Read the license text in the exact upstream revision.
2. Preserve copyright and license notices.
3. Record the exact source URL, branch/tag and commit.
4. Keep modified-file and source-disclosure obligations in view.
5. Do not combine files under incompatible terms without review.

Upstream reference: https://github.com/apple-oss-distributions/xnu

## Other sources

For every third-party file, record:

- Original project and exact URL.
- Version, tag or commit.
- Copyright holder.
- License identifier and license-file path.
- Local modifications.
- Required notices and redistribution conditions.

Do not copy HakiOS source or other third-party code merely because it is public. Study its public documentation and implement independent code unless the relevant license and provenance have been reviewed.

## Never commit

- Proprietary iOS or other vendor system images.
- Phone firmware blobs unless redistribution rights are clear and explicitly approved.
- Private keys, signing keys, certificates, tokens or passwords.
- Personal device logs containing identifiers or private information.

## Project identity

DroidXNU is an independent research project. It is not affiliated with or endorsed by Apple or Motorola. Product and company names are used only to identify technologies and target hardware.
