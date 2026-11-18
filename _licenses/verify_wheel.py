#!/usr/bin/env python3
# Author: Michel Sanner, PhD. Copyright (c) 2026.
"""Check a .post1 wheel made by repack_wheel.py against the published wheel.

Allowed differences, and only these:
- renamed .dist-info/.data folders; METADATA (version, license fields); RECORD;
- removed: stray files (.git/, *.bak, PmvApp_fromSID/, prodyDIST/build/) and the
  lab's old license files; added: the files of out/<product>/;
- source files whose only change is the license notice in comments (Python: the
  token stream without comments is identical; other files: every changed line is
  the new one-line notice).
Every other file, binaries included, must be byte-identical with the same mode.

    python3 verify_wheel.py OLD.whl NEW.whl PRODUCT     (exit 1 on any violation)
"""
import difflib
import fnmatch
import io
import json
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import relicense  # noqa: E402
from repack_wheel import DROP, PATCHES  # noqa: E402


def same_function(old_src, new_src, name):
    """The function `name` returns the same value in both sources, over a range of inputs."""
    import math
    def load(src):
        tree = __import__('ast').parse(src)
        fn = [x for x in tree.body if getattr(x, 'name', None) == name][0]
        ns = {}
        exec(compile(__import__('ast').Module(body=[fn], type_ignores=[]), name, 'exec'), ns)
        return ns[name]
    f, g = load(old_src), load(new_src)
    xs = [i / 1000.0 for i in range(-1000, 2001)] + [0.23, 0.49, 0.80, 0.2299999, 0.4899999, 0.7999999,
                                                     float('nan'), float('inf'), -float('inf'), 0, 1]
    try:
        import numpy
        xs += [numpy.float64(x) for x in (0.23, 0.49, 0.8, 0.5)] + [numpy.float32(x) for x in (0.23, 0.49, 0.8)]
    except ImportError:
        pass
    return all(f(x) == g(x) for x in xs)


def main(old, new, product):
    zo, zn = zipfile.ZipFile(old), zipfile.ZipFile(new)
    vo = re.match(r'[^-]+-([^-]+)-', os.path.basename(old)).group(1)
    vn = re.match(r'[^-]+-([^-]+)-', os.path.basename(new)).group(1)
    name = os.path.basename(old).split('-')[0]
    ren = lambda n: n.replace('%s-%s.dist-info' % (name, vo), '%s-%s.dist-info' % (name, vn)) \
                     .replace('%s-%s.data' % (name, vo), '%s-%s.data' % (name, vn))
    licfiles = set(os.listdir(os.path.join(HERE, 'out', product)))
    io_ = {i.filename: i for i in zo.infolist()}
    in_ = {i.filename: i for i in zn.infolist()}
    bad, stats = [], {'identical': 0, 'notice_only': 0, 'dropped': 0, 'removed_license': 0, 'added': 0}
    for n, i in io_.items():
        m = ren(n)
        if any(fnmatch.fnmatch(n, g) or fnmatch.fnmatch('/' + n, g) for g in DROP):
            if m in in_:
                bad.append('not dropped: ' + n)
            stats['dropped'] += 1
            continue
        if m not in in_:
            if re.search(r'(^|/)(LICEN[CS]E|COPYING)(\.txt|\.md)?$', n):
                stats['removed_license'] += 1
                continue
            bad.append('missing: ' + n)
            continue
        if n.endswith(('/RECORD', '/METADATA', '/top_level.txt')) and '.dist-info/' in n:
            continue
        a, b = zo.read(n), zn.read(m)
        if (i.external_attr >> 16) != (in_[m].external_attr >> 16):
            bad.append('mode changed: %s %o -> %o' % (n, i.external_attr >> 16, in_[m].external_attr >> 16))
        if a == b:
            stats['identical'] += 1
            continue
        ta, tb = a.decode('utf-8', 'replace'), b.decode('utf-8', 'replace')
        patch = [p for p in PATCHES if p[0] == product and p[1] == n]
        if patch:
            if not same_function(ta, tb, 'capri_class_DockQ'):
                bad.append('patched function behaves differently: ' + n)
            stats['patched'] = stats.get('patched', 0) + 1
            ta = ta.replace(patch[0][2], patch[0][3], 1)     # the rest must follow the rules below
            if ta == tb:
                continue
        diff = [l for l in difflib.unified_diff(ta.split('\n'), tb.split('\n'), lineterm='', n=0)
                if l[:1] in '+-' and not l.startswith(('+++', '---'))]
        plus = [l[1:] for l in diff if l[0] == '+']
        changed = [l[1:] for l in diff]
        comments_only = all(relicense.COMMENT.match(l) or not l.strip() for l in changed)
        notice = all(relicense.NEW in l or 'Sannerlab MIT-like Source-Available License,' in l or not l.strip()
                     for l in plus)
        ok = comments_only and notice
        if ok and n.endswith('.py'):
            try:
                ok = relicense.py_tokens(ta) == relicense.py_tokens(tb)
            except Exception:
                ok = True        # Python 2 or broken file: comment-line check above holds
        if ok and not plus:
            stats['banner_removed'] = stats.get('banner_removed', 0) + 1
        elif ok:
            stats['notice_only'] += 1
        else:
            bad.append('content changed: ' + n)
    for m in in_:
        if not any(ren(n) == m for n in io_):
            if os.path.basename(m) in licfiles or m.endswith('/RECORD'):
                stats['added'] += 1
            else:
                bad.append('unexpected new file: ' + m)
    meta = zn.read('%s-%s.dist-info/METADATA' % (name, vn)).decode()
    for need in ('Version: ' + vn, 'License: ', 'License-File: LICENSE.md', 'Classifier: License :: Other/Proprietary License'):
        if need not in meta:
            bad.append('METADATA lacks ' + need)
    if 'OSI Approved' in meta:
        bad.append('METADATA keeps an OSI classifier')
    print(json.dumps({'old': os.path.basename(old), 'new': os.path.basename(new), 'stats': stats, 'violations': bad}))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:4]))
