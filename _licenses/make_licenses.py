#!/usr/bin/env python3
# Author: Michel Sanner, PhD. Copyright (c) 2026.
"""Write the Sannerlab license of each distributed product, customized for it.

The text comes from software/license.qmd, the license page of the website, which
is the single source:
- the introduction names only the product;
- the MSMS non-commercial clause is kept only for products that ship MSMS;
- Section 3 (Credits) keeps only the product's references;
- Sections 1-2 and 4-13 are copied as they are.

products.tsv lists the products; credits_extra.tsv holds the references that
are not on the license page; third_party.tsv the third-party components of each
product, from which THIRD_PARTY_NOTICES.md is written.

    python3 _licenses/make_licenses.py [product ...]     # default: all
Output: _licenses/out/<product>/LICENSE.md and THIRD_PARTY_NOTICES.md
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
PAGE = os.path.join(SITE, 'software', 'license.qmd')
URL = 'https://sannerlab.github.io/software/license.html'

# the exceptions a product may carry (products.tsv, column "exception")
EXCEPTIONS = {
    'engine': (
        'The CrankiteAD docking engine of ADCP ({path}) is not covered by this License. It derives '
        'from CRANKITE (Podtelezhnikov and Wild, 2008) and, like ADCP since 2019, it is distributed '
        'under the GNU Library General Public License, version 2.0, with the agreement of '
        "CRANKITE's authors: see THIRD_PARTY_NOTICES.md for its copyright holders and where its "
        'source is.'),
    'utpackages': (
        'The libraries this package wraps (UTblur, UTisocontour, UTmesh, UTmolderivatives, UTsdf, '
        'UTvolrend) were written at The University of Texas at Austin and keep their own terms: free '
        'for non-commercial educational or academic use only, and parts of them under the GNU GPL '
        '(see THIRD_PARTY_NOTICES.md). This License applies only to the Sanner lab\'s Python wrappers.'),
    'pyglf': (
        'GLF 1.4 and its fonts, which this package wraps, are by Roman Podobedov and are free for '
        'non-commercial use only; commercial use needs his permission (see THIRD_PARTY_NOTICES.md). '
        'This License applies only to the Sanner lab\'s Python wrapper.'),
    'gle': (
        'GLE 3.1.0, the library this package wraps, is by Linas Vepstas and keeps its own license '
        '(see THIRD_PARTY_NOTICES.md). This License applies only to the Sanner lab\'s Python wrapper.'),
    'prody': (
        'This package is a modified copy of ProDy, which is Copyright its authors (Ahmet Bakan, '
        'Ivet Bahar and the Bahar lab, University of Pittsburgh) and distributed under the MIT '
        'License. This License applies only to the changes made in the Sanner lab; ProDy itself '
        'keeps its MIT License (see THIRD_PARTY_NOTICES.md).'),
}

SUPERSEDES = (
    'Where a file of {name} written in the Sanner lab (copyright Michel F. Sanner, TSRI or Scripps '
    'Research) states another license (the GNU LGPL, the BSD, MIT or Mozilla licenses, or the '
    'MGLTools software license agreement), this License replaces that statement for the copies '
    'distributed with this License. Third-party components keep their own licenses: see '
    'THIRD_PARTY_NOTICES.md and Section 6.')


def cap(s):
    return s[:1].upper() + s[1:]


def read_tsv(name):
    with open(os.path.join(HERE, name), newline='') as fh:
        rows = [r for r in csv.reader(fh, delimiter='\t') if r and not r[0].startswith('#')]
    head, rows = rows[0], rows[1:]
    return [dict(zip(head, r + [''] * (len(head) - len(r)))) for r in rows]


def parse_page():
    """(msms_callout, body_before_credits, credits{key: bullet}, credits_intro, body_after)."""
    text = open(PAGE, encoding='utf-8').read()
    text = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.S)       # front matter
    head, body = text.split('\n---\n', 1)
    m = re.search(r'::: \{\.callout-important\}\n## (.*?)\n\n(.*?)\n:::', head, re.S)
    callout = '> **%s**\n>\n' % m.group(1) + '\n'.join('> ' + l if l else '>' for l in m.group(2).split('\n'))
    i = body.index('## 3. Credits')
    j = body.index('## 4.')
    before, credits, after = body[:i], body[i:j], body[j:]
    paras = credits.split('\n\n')
    intro = paras[0] + '\n\n' + paras[1]          # heading + "The licensee will acknowledge ..."
    bullets = {}
    for b in re.split(r'\n(?=- \*\*)', '\n\n'.join(paras[2:]).strip()):
        k = re.match(r'- \*\*(.+?):\*\*', b).group(1)
        bullets[k] = b.strip()
    return callout, before.strip('\n'), intro, bullets, after.rstrip() + '\n'


MSMS_INTRO = (
    'MSMS is closed-source software, distributed in executable form only: the MSMS program, and '
    'the MSLIB library through which ADFRsuite, MGLTools and other programs compute molecular '
    'surfaces. {name} is licensed under the terms below. They are those of the Sannerlab MIT-like '
    'Source-Available License, version 1.0 ({url}), except Sections 1, 5 and 12, which are '
    'specific to MSMS.')

MSMS_S1 = """## 1. Grant of License

Subject to the conditions, limitations, and exclusions set forth in this License, permission is
hereby granted, free of charge, to students, faculty and staff of universities and of other
non-profit academic or research institutions to install, execute and reproduce the Software for
their research and teaching ("Academic Use"), and to publish the results they obtain with it.

Any other use, including any use by or on behalf of a commercial entity, requires a separate
commercial license from the copyright holder: contact
[Dr. Michel Sanner](mailto:sanner@scripps.edu).

No right is granted to decompile, reverse-engineer, modify or create derivative works of the
Software, or to distribute, sublicense, sell or otherwise transfer copies of it, except as the
copyright holder authorizes in writing.

No rights are granted to Excluded Persons or Excluded Organizations.

"""

MSMS_S5 = """## 5. Copies and Attribution

Copies made under Section 1 must keep the copyright notice and this License. The restrictions
applicable to Excluded Persons and Excluded Organizations apply to every copy.

"""

MSMS_S12 = """## 12. License Classification

This License is a proprietary license for closed-source software. It is not an open-source
license.

"""

BUNDLED = (
    '> **MSMS**\n>\n'
    '> The MSMS program and the MSLIB library included in {name} are closed-source software under '
    'their own license, the MSMS License (LICENSE-MSMS.md): free for academic use; commercial use '
    'needs a commercial license from [Dr. Michel Sanner](mailto:sanner@scripps.edu).')


def replace_section(text, num, new):
    i = text.index('## %d. ' % num)
    j = text.index('## %d. ' % (num + 1))
    return text[:i] + new + text[j:]


def license_text(p, page, extra):
    callout, before, intro, bullets, after = page
    name = p['name']
    allc = dict(bullets)
    allc.update(extra)
    keys = [k.strip() for k in p['credits'].split(',') if k.strip()]
    missing = [k for k in keys if k not in allc]
    if missing:
        raise SystemExit('%s: no reference for %s' % (p['id'], missing))
    if p['msms'] == 'closed':
        out = ['# MSMS License', '', MSMS_INTRO.format(name=name, url=URL), '']
        out += ['Questions about the license: contact [Dr. Michel Sanner](mailto:sanner@scripps.edu).',
                '', '---', '', replace_section(before + '\n\n', 1, MSMS_S1).rstrip('\n'), '', intro, '']
        out += [allc[k] for k in keys]
        tail = replace_section(replace_section(after, 5, MSMS_S5), 12, MSMS_S12)
        out += ['', tail.replace('**End of License — Version 1.0**', '**End of License — MSMS License, based on the Sannerlab License Version 1.0**')]
        return '\n'.join(out)
    out = ['# Sannerlab MIT-like Source-Available License, version 1.0', '',
           '%s is distributed under the **Sannerlab MIT-like Source-Available License, version 1.0**, '
           'as published at %s and reproduced below for %s. Section 3 lists what to cite for it.'
           % (cap(name), URL, name), '']
    if p.get('exception'):
        kind, _, path = p['exception'].partition(':')
        out += [EXCEPTIONS[kind].format(path=path or 'its CrankiteAD executable'), '']
    out += [SUPERSEDES.format(name=name), '']
    if p['msms'] == 'bundled':
        out += [BUNDLED.format(name=name), '']
    out += ['Questions about the license: contact [Dr. Michel Sanner](mailto:sanner@scripps.edu).',
            '', '---', '', before, '', intro, '']
    out += [allc[k] for k in keys]
    out += ['', after]
    return '\n'.join(out)


def notices_text(p, rows):
    name = p['name']
    mine = [r for r in rows if r['product'] == p['id']]
    if p.get('exception') in ('prody', 'utpackages', 'pyglf', 'gle'):
        name = "the Sanner lab's part of " + name
    out = ['# Third-party notices', '',
           '%s is Copyright Michel F. Sanner and Scripps Research (formerly TSRI) and distributed '
           'under the Sannerlab MIT-like Source-Available License, version 1.0 (LICENSE.md). It '
           'includes the following software, which keeps its own copyright and license.' % cap(name), '']
    if not mine:
        out += ['None: %s includes no third-party code.' % name, '']
    shipped = []
    for r in mine:
        out += ['## ' + r['component'], '']
        out += ['- **Where:** ' + r['path']]
        out += ['- **Copyright:** ' + r['copyright']]
        out += ['- **License:** ' + r['licence']]
        if r['licence_text'].startswith('ship:'):
            f = r['licence_text'][5:]
            shipped.append(f)
            out += ['- **License text:** `%s`, next to this file' % f]
        elif r['licence_text'].startswith('file:'):
            text = open(os.path.join(HERE, r['licence_text'][5:]), encoding='utf-8').read().rstrip()
            out += ['- **License text:**', '', '```', text, '```', '']
        elif r['licence_text']:
            out += ['- **License text:** ' + r['licence_text']]
        if r['source']:
            out += ['- **Source:** ' + r['source']]
        if r['note']:
            out += ['- ' + r['note']]
        out += ['']
    return '\n'.join(out), shipped


def main(ids):
    page = parse_page()
    extra = dict((r['key'], r['bullet']) for r in read_tsv('credits_extra.tsv'))
    products = read_tsv('products.tsv')
    tp = read_tsv('third_party.tsv')
    known = set(p['id'] for p in products)
    bad = [i for i in ids if i not in known] + sorted(set(r['product'] for r in tp) - known)
    if bad:
        raise SystemExit('unknown products: %s' % bad)
    for p in products:
        if ids and p['id'] not in ids:
            continue
        d = os.path.join(HERE, 'out', p['id'])
        os.makedirs(d, exist_ok=True)
        for f in os.listdir(d):                      # start clean: shipped texts change
            os.remove(os.path.join(d, f))
        with open(os.path.join(d, 'LICENSE.md'), 'w', encoding='utf-8') as fh:
            fh.write(license_text(p, page, extra))
        text, shipped = notices_text(p, tp)
        with open(os.path.join(d, 'THIRD_PARTY_NOTICES.md'), 'w', encoding='utf-8') as fh:
            fh.write(text)
        for f in sorted(set(shipped)):
            with open(os.path.join(HERE, 'texts', f), 'rb') as src, open(os.path.join(d, f), 'wb') as dst:
                dst.write(src.read())
        print('wrote', os.path.relpath(d, SITE))


if __name__ == '__main__':
    main(sys.argv[1:])
