# Sanner Lab website

Source of https://sannerlab.github.io, built with [Quarto](https://quarto.org) (1.10.18) and
deployed by GitHub Actions. Replaced the Jekyll Lab Website Template site on 2026-10-14.

## Build and preview locally

    quarto preview          # live preview, rebuilds on save
    quarto render           # full build into _site/

Needs Python with PyYAML: `_scripts/publications.py` runs before every render and writes
`publications.qmd` from `_data/citations.yaml`.

## Publishing

Push to `main`. The `on-push` workflow:

1. **update-citations**: runs `_cite/cite.py` (Manubot), which turns the DOIs in
   `_data/sources.yaml` into `_data/citations.yaml` and commits it if it changed;
2. **build-site**: renders the site with Quarto and deploys `_site/` to the `gh-pages` branch,
   which GitHub Pages serves.

`on-schedule` runs the citation update every Monday and opens a pull request if anything changed.

## Layout

| Path | What |
|---|---|
| `_quarto.yml` | navbar, per-tool sidebars (versions), theme |
| `software/adcp/` | ADCP: `index.qmd` overview, `1.1/` and `1.0/` version pages |
| `software/*.qmd` | other tools, stubs pointing to ccsb.scripps.edu until moved |
| `_includes/` | shared snippets (version banner) |
| `_data/sources.yaml` | **add publications here** (`- id: doi:...`) |
| `adapt/` | ADapt docs, synced automatically from `sannerlab/adapt-test` (do not edit here) |
| `_cite/` | citation tool from the Greene Lab Lab Website Template (BSD-3, see `_cite/LICENSE.md`) |

ADCP content was transferred from ccsb.scripps.edu/adcp and /adcpv11 on 2026-10-14. Callouts
titled "Review note" mark problems found in the source pages, pending review.
