# Redirects for the retired ccsb.scripps.edu software subsites

The Sanner Lab software pages that were on ccsb.scripps.edu now live on
https://sannerlab.github.io/software/, and their files on
https://github.com/sannerlab/downloads/releases. The rules here send every old address to its
new equivalent, so links in papers, bookmarks and old install scripts keep working.

Covered paths on `ccsb.scripps.edu`:

| Old path | Goes to |
|---|---|
| `/adcp/`, `/adcpv11/`, `/adfr/`, `/agfr/`, `/autosite/`, `/mgltools/`, `/msms/` (WordPress subsites) | each page → its new page; anything else → the tool's overview page |
| `/<subsite>/download/<id>/` and `/download/<id>/` (download links) | the same file on GitHub |
| `/<subsite>/wp-content/uploads/…` files that pages linked to (tutorial data, PDFs) | the same file on GitHub |
| `/mamba/scripts/`, `/mamba/examples/` (ADCP 1.1 install scripts and examples) | the same files on GitHub |
| `/mamba/pip/py37/…` (ADCP 1.1 Python packages, current versions) | the files on GitHub, and the pip index https://sannerlab.github.io/pip/py37/ |

`/mamba/` is a plain folder, not part of WordPress, but it needs the same rules.

## Files

| File | What it is |
|---|---|
| `ccsb-redirects.conf` | the Apache rules (mod_rewrite, 301 redirects); generated, don't edit |
| `redirects.tsv` | the old → new table the rules are made from (190 rows) |
| `make_conf.py` | regenerates `ccsb-redirects.conf` from `redirects.tsv` |
| `check_redirects.py` | checks the rules and targets; `--live` checks the deployed server |

## Deploying (for the network team)

1. Add the contents of `ccsb-redirects.conf` to the `ccsb.scripps.edu` `<VirtualHost>` (they then
   run before WordPress's rewrite rules), or at the very top of the site's `.htaccess`, before the
   WordPress block. They need `mod_rewrite`, which WordPress already uses.
2. Reload Apache, then run `python3 check_redirects.py --live`; it should report 0 problems.
3. Delete the WordPress subsites. The rules let `wp-admin` and `wp-login.php` through until then.

The redirects keep working as long as the `ccsb.scripps.edu` host name exists.

## Changing a redirect

Edit `redirects.tsv`, run `python3 make_conf.py`, then `python3 check_redirects.py`, and send the
new `ccsb-redirects.conf` to the network team.
