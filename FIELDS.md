# Korpusaro: register of source-text corpora

Generated 2026-11-21T22:42:14. 518 corpora, 52 with a drawn geographic and chronological extent.

- `corpusorum.csv`: one row per corpus; multiple values separated by `; `.
- `corpusorum.json`: the same records with lists as arrays and the drawn extent as a GeoJSON Feature (`extent`).
- `changelog.json` and `changelog.atom`: what changed between rebuilds (corpora added or removed; changes in licence, access, availability flag, download addresses, source address, number of works and authors), newest first.
- Found a mistake or a missing corpus? `POST /api/suggest` (JSON, described in `openapi.json`) or the “Suggest a correction” button on the site. Suggestions are read by a person; nothing changes until a maintainer accepts it. The endpoint asks for a small proof of work (`GET /api/challenge`).

Extents are drafts drawn from the sources' own descriptions; see `extent_status` and the confidence fields.

| field | meaning |
|---|---|
| `id` | stable identifier of the corpus |
| `name` | full name |
| `short_name` | short name used in lists |
| `subtitle` | the part of the full name not in short_name |
| `type` | kind of resource (corpus, digital_library, dataset, source_edition, study, archive, …) |
| `parent_id` | id of the larger corpus this one belongs to |
| `platform` | hosting platform |
| `languages` | ISO 639-3 language codes |
| `regions` | regions (registry vocabulary) |
| `area` | geographic area(s) covered |
| `topic` | what the texts are |
| `date_range` | period as stated by the source |
| `year_from` | first year covered (negative = BCE) |
| `year_to` | last year covered |
| `url` | main website |
| `additional_urls` | other relevant addresses |
| `author_editor` | authors or editors of the corpus |
| `curator` | who maintains it |
| `institution` | hosting or responsible institution |
| `license` | licence or terms of use as stated by the source |
| `license_status` | open, free_access, restricted, not_stated, to_check, not_applicable |
| `license_scope` | what the licence covers |
| `license_evidence_url` | where the licence is stated |
| `license_checked` | date the licence was checked |
| `access` | open, registration, subscription, restricted, unknown |
| `access_method` | how the texts can be reached |
| `format` | file formats |
| `format_class` | format classes (TEI-XML, PDF, text, images, …) |
| `n_works` | number of works (texts) |
| `n_authors` | number of authors |
| `downloadable` | yes, partial, no, unknown |
| `download_kind` | how the files are offered (git, zip, zenodo, per-file, dump, api, html-only, unknown) |
| `download_url` | direct address to get the files, where one exists |
| `bulk_download` | yes, no, unknown (a single bulk file or repository) |
| `bulk_url` | address of the bulk download, where one exists |
| `availability` | flag: empty = normal entry; unreachable = the source could not be reached or verified; duplicate = the same material is also in another listed corpus; superseded = replaced by another resource |
| `superseded_by` | id(s) of the listed corpus that holds the same material or replaced this resource (see availability) |
| `checked_on` | date the entry was last checked |
| `extent_year_from` | start of the drawn extent (negative = BCE) |
| `extent_year_to` | end of the drawn extent |
| `extent_status` | status of the drawn extent (draft, …) |
| `extent_confidence_geo` | confidence in the drawn area |
| `extent_confidence_years` | confidence in the extent years |
