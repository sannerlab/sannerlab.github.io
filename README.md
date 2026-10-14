# Sanner Lab website (Quarto prototype)

Branch `quarto`: a rebuild of https://sannerlab.github.io in [Quarto](https://quarto.org),
following Michel's plan (menu Home · Lab · Software · Publications · Contact; per-tool pages with
versions). The live site is still the Jekyll site on `main`.

## Build and preview

    quarto preview          # live preview, rebuilds on save
    quarto render           # full build into _site/

`_scripts/publications.py` runs before every render and writes `publications.qmd` from
`_data/citations.yaml` (copied from the Jekyll site; add DOIs to `_data/sources.yaml`).

## Layout

| Path | What |
|---|---|
| `_quarto.yml` | navbar, ADCP sidebar (versions), theme |
| `software/adcp/` | ADCP pilot: `index.qmd` overview, `1.1/` and `1.0/` version pages |
| `software/*.qmd` | other tools, stubs pointing to ccsb.scripps.edu until moved |
| `_includes/` | shared snippets (version banner) |
| `adapt/` | ADapt docs, copied as static files from `main` |

Content transferred from ccsb.scripps.edu/adcp and /adcpv11 on 2026-10-14. Callouts titled
"Review note (prototype only)" mark problems found in the source pages; remove them before going
live.
