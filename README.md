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

## Posting news

1. Copy a post in `news/posts/` to `news/posts/YYYY-MM-DD-short-name.qmd`.
2. Set its front matter:
   - `title`;
   - `date`;
   - `description`: one sentence, shown on the home page and in link previews on Bluesky and
     LinkedIn;
   - `image`: for a software release, the tool's icon (`../../images/tools/<tool>.jpg`).
3. Write the body: what changed, plus links to the download and release-notes pages. Keep the
   last line, `{{< include /_includes/follow-bluesky.md >}}`: it adds the "Follow the Sanner Lab
   on Bluesky" box.
4. Push. The home page shows the 3 newest posts, `news/index.qmd` lists all of them, and the
   RSS feed (`news/index.xml`) updates.
5. Once the site is deployed, paste the post's URL into a Bluesky post and a LinkedIn post. Both
   build the preview card from the post's title, description and image.

## Layout

| Path | What |
|---|---|
| `_quarto.yml` | navbar, per-tool sidebars (versions), theme |
| `software/adcp/` | ADCP: `index.qmd` overview, `1.1/` and `1.0/` version pages |
| `software/*.qmd` | other tools; their installers and data are in the releases of `sannerlab/downloads` |
| `news/` | News page (`index.qmd`, with RSS feed) and one file per post in `posts/` |
| `_includes/` | shared snippets (version banner, home-page news template `news-latest.ejs`) |
| `_data/sources.yaml` | **add publications here** (`- id: doi:...`) |
| `adapt/` | ADapt docs, synced automatically from `sannerlab/adapt-test` (do not edit here) |
| `wewos/` | WEWoS docs, synced automatically from `sannerlab/WEWoS` (do not edit here) |
| `_cite/` | citation tool from the Greene Lab Lab Website Template (BSD-3, see `_cite/LICENSE.md`) |

Downloads (installers, tutorial data, PDFs) are attached to the releases of
[sannerlab/downloads](https://github.com/sannerlab/downloads/releases); the ADCP 1.1 Python packages
are served as a pip index by [sannerlab/pip](https://github.com/sannerlab/pip).
