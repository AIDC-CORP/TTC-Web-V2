# TTC Company Profile — English Edition 2026

This directory contains the 36-page English edition of the TTC company profile.

## Deliverables

- `05-company-profile-en.pdf` — final 36-page A4 profile.
- `05-company-profile-en.tex` — approved English source preserving the
  Vietnamese master layout page by page.
- `build_english_profile.py` — compile and 36-page validation command.
- `generate_from_original.py` — controlled utility used to derive the English
  source from the Vietnamese master.

## Rebuild

From the repository root:

```bash
python3 sales-kit/05-company-profile-en/build_english_profile.py
```

The builder compiles the document twice and fails if the result is not exactly
36 pages. It does not regenerate or overwrite the approved English source.

## English-release typography and branding

- Supporting copy has a 6.5 pt minimum; headings and body copy retain the
  hierarchy of the Vietnamese master without miniature translated text.
- The cover and back cover use an English TTC lock-up built from the official
  symbol plus live English type, so the Vietnamese descriptor embedded in the
  source raster is not shown.
- Vietnamese labels baked into selected project renders are masked with concise
  English captions while the underlying project imagery remains in place.

## Release control

Before external issue, update the controlled legal dossier used alongside the profile: enterprise registration, construction capability schedules, ISO certificates, project references and approved corporate relationships.
