# The license of each distributed package

`software/license.qmd` is the single source of the Sannerlab MIT-like Source-Available License.
These tools write the copy that each package, installer and repository carries, customized for it,
and put it into the published files. Quarto does not render this folder: its name starts with `_`.

| File | What it is |
|---|---|
| `products.tsv` | Every product: its name in a sentence, the references for Section 3, and its MSMS or exception kind. `closed` gives the MSMS License; `bundled` points to `LICENSE-MSMS.md`; `engine` excludes the CrankiteAD engine (GNU LGPL v2.0); `prody`, `utpackages`, `pyglf` and `gle` limit the license to the lab's wrappers. |
| `credits_extra.tsv` | References that are not on the license page: AutoDockTools, ProDy and ADapt. |
| `third_party.tsv` | One row per third-party component of a product. `licence_text` is `ship:FILE` (the full text in `texts/`, shipped with the package), `file:texts/FILE` (inlined), or a path inside the package. Rows whose license is "not established" name code of unknown origin; the lab claims no rights in it. |
| `texts/` | The full license texts. |
| `make_licenses.py` | Writes `out/<product>/LICENSE.md`, `THIRD_PARTY_NOTICES.md` and the shipped texts. |
| `relicense.py` | Replaces the LGPL notice in the headers of the lab's own source files with a pointer to `LICENSE.md`, and removes the lab's 2016 LGPL banner from third-party files. Comments only: the Python token stream must stay identical. |
| `repack_wheel.py`, `verify_wheel.py` | Repack a published wheel as `X.post1` with its license, and check it against the original member by member. Binaries stay byte-identical. |

To regenerate after an edit of the license page or of a table, run `python3 _licenses/make_licenses.py`.

What was done with them on 2026-11-18:
- the `.post1` wheels on https://sannerlab.github.io/pip/ (release `adcp-pip-py37` of sannerlab/downloads);
- the repacked installers of sannerlab/downloads (licence files only; the originals are archived);
- the repositories of the packages, of ADCP, ADapt, WEWoS, MSMS and of the ADCP engine (`sannerlab/Crankite_AD`, LGPL v2.0).
