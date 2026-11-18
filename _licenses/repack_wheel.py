#!/usr/bin/env python3
# Author: Michel Sanner, PhD. Copyright (c) 2026.
"""Repack a published wheel as a .post1 release that carries its Sannerlab license.

Changes, and nothing else:
- version X -> X.post1 (the .dist-info and .data folders are renamed);
- METADATA: License and License-File fields, and the classifier
  "License :: Other/Proprietary License" instead of the OSI one;
- the old license files of the lab (PyPA MIT sample, BSD-2 "sannerlab", MGLTools
  agreement) are replaced by out/<product>/* (LICENSE.md, THIRD_PARTY_NOTICES.md
  and the full license texts it ships), in the .dist-info and in each top-level
  package folder;
- relicense.py rewrites the LGPL notice of the lab's own source files;
- stray files are left out: .git/ folders, *.bak, PmvApp_fromSID/, prodyDIST/build/.
Binaries and every other file are byte-identical; verify.py checks it.

    python3 repack_wheel.py WHEEL OUTDIR PRODUCT [--wheel-cli PATH]
"""
import argparse
import csv
import fnmatch
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import relicense  # noqa: E402

DROP = ['*/.git/*', '*.bak', 'PmvApp_fromSID/*', 'prodyDIST/*']
LAB_LICENSE = re.compile(r'The Python Packaging Authority|BSD 2-Clause License\s+Copyright \(c\) 2022, sannerlab|'
                         r'This software is copyrighted by Michel F\. Sanner')
# code replaced while repacking: (product, path, old text, new text)
DOCKQ_OLD = """def capri_class_DockQ(DockQ):
    # function implemented by Bjorn Wallner see
    # https://github.com/bjornwallner/DockQ
    (c1,c2,c3)=(0.23,0.49,0.80)
    if(DockQ < c1):
        return 'Incorrect'
    elif(DockQ >= c1 and DockQ < c2):
        return 'Acceptable'
    elif(DockQ >= c2 and DockQ < c3):
        return 'Medium'
    elif(DockQ >= c3):
        return 'High'
    else:
        return 'Undef'
"""
DOCKQ_NEW = """def capri_class_DockQ(DockQ):
    # CAPRI quality class of a DockQ score, with the thresholds published with DockQ:
    # Basu, S.; Wallner, B. DockQ: a quality measure for protein-protein docking models.
    # PLoS One 2016, 11 (8), e0161879. (A score that is not a number is 'Undef'.)
    if DockQ >= 0.80:
        return 'High'
    if DockQ >= 0.49:
        return 'Medium'
    if DockQ >= 0.23:
        return 'Acceptable'
    if DockQ < 0.23:
        return 'Incorrect'
    return 'Undef'
"""
PATCHES = [('adcp', 'ADCP/dockq.py', DOCKQ_OLD, DOCKQ_NEW)]
LICENSE_NAME = {'closed': 'MSMS License (closed source; free for academic use; commercial use needs a license)'}


def third_party_globs(product):
    """--skip globs from the paths of the product's rows in third_party.tsv."""
    globs = []
    with open(os.path.join(HERE, 'third_party.tsv'), newline='') as fh:
        rows = [r for r in csv.reader(fh, delimiter='\t') if r and not r[0].startswith('#')]
    for r in rows[1:]:
        if r[0] != product:
            continue
        for p in re.findall(r'`([^`]+)`', r[2]):
            p = p.split(' ')[0]
            globs.append(p + '*' if p.endswith('/') else p)
    return globs


def product_row(product):
    with open(os.path.join(HERE, 'products.tsv'), newline='') as fh:
        rows = [r for r in csv.reader(fh, delimiter='\t') if r and not r[0].startswith('#')]
    head = rows[0]
    for r in rows[1:]:
        if r[0] == product:
            return dict(zip(head, r + [''] * len(head)))
    raise SystemExit('no product %s' % product)


def edit_metadata(path, version, licfiles, closed):
    text = open(path, encoding='utf-8').read()
    head, sep, body = text.partition('\n\n')
    lines = [l for l in head.split('\n')
             if not l.startswith(('License:', 'License-File:', 'Classifier: License ::'))]
    lines = ['Version: ' + version if l.startswith('Version:') else l for l in lines]
    lic = LICENSE_NAME['closed'] if closed else 'Sannerlab MIT-like Source-Available License 1.0'
    i = next(k for k, l in enumerate(lines) if l.startswith('Version:')) + 1
    while i < len(lines) and lines[i].startswith(('Summary:', 'Home-page:', 'Author', 'Maintainer')):
        i += 1
    lines[i:i] = ['License: ' + lic]
    lines.append('Classifier: License :: Other/Proprietary License')
    lines += ['License-File: ' + f for f in licfiles]
    open(path, 'w', encoding='utf-8').write('\n'.join(lines) + sep + body)


def repack(wheel, outdir, product, wheel_cli):
    p = product_row(product)
    lic = os.path.join(HERE, 'out', product)
    licfiles = sorted(os.listdir(lic))
    tmp = tempfile.mkdtemp(prefix='repack-', dir=outdir)
    try:
        subprocess.run([wheel_cli, 'unpack', '-d', tmp, wheel], check=True, stdout=subprocess.DEVNULL)
        (root,) = [os.path.join(tmp, d) for d in os.listdir(tmp)]
        di = [d for d in os.listdir(root) if d.endswith('.dist-info')][0]
        name, version = di[:-len('.dist-info')].rsplit('-', 1)
        newv = version + '.post1'
        report = {'dropped': [], 'removed_licenses': [], 'relicense': None}
        # stray files
        for dp, dns, fns in os.walk(root, topdown=False):
            for f in fns:
                rel = os.path.relpath(os.path.join(dp, f), root)
                if any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch('/' + rel, g) for g in DROP):
                    os.remove(os.path.join(dp, f))
                    report['dropped'].append(rel)
            if not os.listdir(dp) and dp != root:
                os.rmdir(dp)
        # replaced code
        report['patched'] = []
        for prod, rel, old, new in PATCHES:
            fp = os.path.join(root, rel)
            if prod == product and os.path.exists(fp):
                t = open(fp, encoding='utf-8').read()
                if old in t:
                    open(fp, 'w', encoding='utf-8').write(t.replace(old, new, 1))
                    report['patched'].append(rel)
        # the lab's old license files
        tops = [l.strip() for l in open(os.path.join(root, di, 'top_level.txt')) if l.strip()] \
            if os.path.exists(os.path.join(root, di, 'top_level.txt')) else []
        kept = [t for t in tops if os.path.isdir(os.path.join(root, t)) or os.path.isfile(os.path.join(root, t + '.py'))]
        if kept != tops:                       # a dropped top-level folder (prodyDIST)
            open(os.path.join(root, di, 'top_level.txt'), 'w').write(''.join(t + '\n' for t in kept))
        tops = [t for t in kept if os.path.isdir(os.path.join(root, t))]
        for d in [di] + tops:
            for f in os.listdir(os.path.join(root, d)):
                fp = os.path.join(root, d, f)
                if os.path.isfile(fp) and re.match(r'^(LICEN[CS]E|COPYING)(\.txt|\.md)?$', f):
                    txt = open(fp, encoding='utf-8', errors='replace').read()
                    if d == di or LAB_LICENSE.search(txt):
                        os.remove(fp)
                        report['removed_licenses'].append(os.path.join(d, f))
        # source headers
        r = relicense.run(root, skip=third_party_globs(product) + [di + '/*'])
        report['relicense'] = {'changed': len(r['changed']), 'skipped': r['skipped'],
                               'banner_removed': r['banner_removed']}
        # new license files
        for d in [di] + tops:
            for f in licfiles:
                shutil.copyfile(os.path.join(lic, f), os.path.join(root, d, f))
        edit_metadata(os.path.join(root, di, 'METADATA'), newv, licfiles, p['msms'] == 'closed')
        # rename .dist-info / .data
        for suffix in ('.dist-info', '.data'):
            old = os.path.join(root, '%s-%s%s' % (name, version, suffix))
            if os.path.isdir(old):
                os.rename(old, os.path.join(root, '%s-%s%s' % (name, newv, suffix)))
        subprocess.run([wheel_cli, 'pack', '-d', outdir, root], check=True, stdout=subprocess.DEVNULL)
        out = os.path.join(outdir, '%s-%s-py3-none-any.whl' % (name, newv))
        report['wheel'] = out
        return report
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('wheel')
    ap.add_argument('outdir')
    ap.add_argument('product')
    ap.add_argument('--wheel-cli', default='wheel')
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    import json
    print(json.dumps(repack(os.path.abspath(a.wheel), os.path.abspath(a.outdir), a.product, a.wheel_cli), indent=1))


if __name__ == '__main__':
    main()
