# Korpusaro: a register of source-text corpora

A register of corpora for historical text research: what each one holds, which period and languages it covers, under what
licence, and whether it can be downloaded. It currently lists **518 corpora** (52 with a drawn geographic and
chronological extent) and **84,227 individual works**. Browse it at **https://sypian.ski/korpusaro/**.

## Files

| File | What it is |
|---|---|
| [`data/corpusorum.csv`](data/corpusorum.csv) | One row per corpus; multiple values separated by `; `. |
| [`data/corpusorum.json`](data/corpusorum.json) | The same records with lists as arrays and the drawn extent as a GeoJSON Feature. |
| [`data/works.csv.gz`](data/works.csv.gz) | The works listed so far (84,227 rows, gzip-compressed CSV): author, title, language, dates, genre, address. Joins to the corpora on `corpus_id`. |
| [`FIELDS.md`](FIELDS.md) | What each field means. |
| [`CHANGELOG.md`](CHANGELOG.md), [`data/changelog.json`](data/changelog.json) | What changed, and when. |
| [`tools/build_sqlite.py`](tools/build_sqlite.py) | Builds a SQLite database from the files above (standard library only): `python3 tools/build_sqlite.py`. |

The same files are served at `https://sypian.ski/korpusaro/export/`. This repository is a mirror that keeps their history.

## Use with an LLM agent

The site has a ready prompt ("Give it to your LLM agent") that says where the data is and how to read the licence fields.
The corpus `id` is stable; keep it with every reference.

## Corrections and missing corpora

Found a mistake, or a corpus we should list? Any of these works, and a person reads every suggestion:

1. Open an [issue](../../issues/new/choose) with the form for a correction or a new corpus.
2. Use the "Suggest a correction" button on the corpus page at https://sypian.ski/korpusaro/.
3. Send it from a program: `POST https://sypian.ski/korpusaro/api/suggest` (JSON, with a small proof of work; described in [`openapi.json`](https://sypian.ski/korpusaro/openapi.json)).

Nothing in the register changes until a maintainer accepts a suggestion.

## Licence

The register (the compilation, the descriptions and the changelog) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The register describes corpora that belong to other people. Each corpus keeps its own licence, recorded in its
`license` and `license_status` fields; listing a corpus here does not grant any rights to its texts.
`license_status`: `open` = an open licence; `free_access` = free to read, no licence stated, so reuse is not granted;
`restricted` = non-commercial or other limits; `not_stated` and `to_check` = unknown, never treat as free.

Numbers (`n_works`, `n_authors`) are estimates, and periods and extents are drafts drawn from the sources' own descriptions.
The register is not exhaustive.

Generated 2026-11-21 from the maintainers' working copy; do not edit the files here by hand.
