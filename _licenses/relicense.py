#!/usr/bin/env python3
# Author: Michel Sanner, PhD. Copyright (c) 2026.
"""Replace the GNU LGPL notice in the headers of the Sanner lab's own source files
with a pointer to the Sannerlab license.

The MGLTools-era files carry this block (with "##", "#", " *" or "//" in front):

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    ...
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

It becomes one line, "Distributed under the Sannerlab MIT-like Source-Available
License 1.0; see LICENSE.md.", with the same comment prefix. Copyright lines
("(C) Copyrights Dr. Michel F. Sanner and TSRI 2016") stay as they are.

A file is left untouched, and listed, when it names a copyright holder outside
the lab, holds more than one license block (third-party code that was stamped),
or matches a --skip pattern (the third-party paths of THIRD_PARTY_NOTICES).
Only comment lines change: for Python files the token stream without comments
must be identical before and after, or the file is left untouched.

    python3 relicense.py TREE [--skip GLOB ...] [--dry-run]
Prints a JSON summary: changed, skipped (with reasons), unchanged counts.
"""
import argparse
import fnmatch
import io
import json
import os
import re
import sys
import tokenize

NEW = 'Distributed under the Sannerlab MIT-like Source-Available License 1.0; see LICENSE.md.'
START = re.compile(r'This (library|program) is free software; you can redistribute it')
END = re.compile(r'(Franklin Street|Temple Place|License along with this (library|program)[;.]?\s*$|<https?://www\.gnu\.org/licenses/>)')
PREFIX = re.compile(r'^(\s*(?:#+|\*|//|/\*+)?\s?)')
COMMENT = re.compile(r'^\s*(#|\*|//|/\*)')
LAB = re.compile(r'Sanner|TSRI|TRSI|Scripps|Huey|Lindstrom|Morris|Stoffler|Coon|Gillet|Omelchenko|'
                 r'Yuqi|Ravindranath|Shanker|Dallakyan|Vareille|Goodsell|Olson|Forli|Yong Zhao|Y\. Zhao|<year>|<name of author>',
                 re.I)
HOLDER = re.compile(r'copyright\s*(?:\(c\)|©)?\s*:?\s*(?:\(c\))?\s*\d{4}[^\n]*|\(c\)\s*\d{4}[^\n]*', re.I)
EXTS = ('.py', '.pyx', '.pxd', '.c', '.h', '.cc', '.cpp', '.cxx', '.hh', '.hpp', '.i', '.f', '.tcl', '.sh')
# the LGPL banner stamped on every MGLTools file in 2016, third-party files included
BANNER = re.compile(r'^#{20,}[ \t]*\r?\n(?:##[^\n]*\n)*?##[ \t]*This library is free software;[^\n]*\n'
                    r'(?:##[^\n]*\n)*?##[ \t]*\(C\) Copyrights Dr\. Michel F\. Sanner and TSRI \d{4}[^\n]*\n'
                    r'(?:##[ \t]*\r?\n)?#{20,}[ \t]*\r?\n(?:[ \t]*\r?\n)?', re.M)
# lab files whose third-party "Copyright" string is data they write, not their authorship
DATA_HOLDER = ['*/tablemaker.py']
# other sentences about the old license, in comments
EXTRA = [('while MGLTools2 is under the GNU Lesser Public License,',
          'while MGLTools2 is under the Sannerlab MIT-like Source-Available License,')]


def third_party_holders(text):
    out = []
    for m in HOLDER.finditer(text):
        a = text.rfind('\n', 0, m.start()) + 1          # the whole line: "Copyright TSRI (C) 2006"
        s = text[a:m.end()]
        if not LAB.search(s):
            out.append(m.group(0).strip()[:80])
    return out


def py_tokens(text):
    toks = []
    for t in tokenize.generate_tokens(io.StringIO(text).readline):
        if t.type in (tokenize.COMMENT, tokenize.NL, tokenize.NEWLINE, tokenize.INDENT,
                      tokenize.DEDENT, tokenize.ENCODING):
            continue
        toks.append((t.type, t.string))
    return toks


def rewrite(text):
    """(new_text, n_blocks) for one file's text."""
    lines = text.split('\n')
    out, i, n = [], 0, 0
    while i < len(lines):
        l = lines[i]
        if START.search(l) and COMMENT.match(l):
            j = i
            while j < len(lines) and j - i < 25 and not END.search(lines[j]):
                j += 1
            if j < len(lines) and END.search(lines[j]) and all(COMMENT.match(x) or not x.strip() for x in lines[i:j + 1]):
                prefix = PREFIX.match(l).group(1)
                out.append(prefix + NEW)
                n += 1
                i = j + 1
                continue
        out.append(l)
        i += 1
    new = '\n'.join(out)
    for a, b in EXTRA:
        new = new.replace(a, b)
    return new, n


def strip_banner(path, text, raw, dry):
    """Remove the lab's LGPL banner from a third-party file; True if removed."""
    new = BANNER.sub('', text, count=1)
    if new == text:
        return False
    if path.endswith('.py'):
        try:
            if py_tokens(text) != py_tokens(new):
                return False
        except (tokenize.TokenError, IndentationError, SyntaxError):
            pass
    if not dry:
        enc = 'utf-8'
        try:
            raw.decode('utf-8')
        except UnicodeDecodeError:
            enc = 'latin-1'
        with open(path, 'wb') as fh:
            fh.write(new.encode(enc))
    return True


def run(tree, skip=(), dry=False):
    res = {'changed': [], 'skipped': {}, 'unchanged': 0, 'banner_removed': []}
    for root, dirs, files in os.walk(tree):
        dirs[:] = [d for d in dirs if d != '.git']
        for f in files:
            path = os.path.join(root, f)
            rel = os.path.relpath(path, tree)
            if not f.endswith(EXTS):
                continue
            raw = open(path, 'rb').read()
            try:
                text = raw.decode('utf-8')
            except UnicodeDecodeError:
                text = raw.decode('latin-1')
            nblocks = len([1 for l in text.split('\n') if START.search(l)])
            if not nblocks and not any(a in text for a, _ in EXTRA):
                res['unchanged'] += 1
                continue
            why = None
            if any(fnmatch.fnmatch(rel, g) for g in skip):
                why = 'third-party path'
            elif third_party_holders(text) and not any(fnmatch.fnmatch('/' + rel, g) for g in DATA_HOLDER):
                why = 'third-party holder: ' + '; '.join(third_party_holders(text)[:2])
            elif nblocks > 1:
                why = '%d license blocks' % nblocks
            if why:
                res['skipped'][rel] = why
                if strip_banner(path, text, raw, dry):
                    res['banner_removed'].append(rel)
                continue
            new, n = rewrite(text)
            if new == text:
                res['skipped'][rel] = 'license block not recognized'
                continue
            if f.endswith('.py'):
                try:
                    same = py_tokens(text) == py_tokens(new)
                except (tokenize.TokenError, IndentationError, SyntaxError):
                    same = None
                if same is False:
                    res['skipped'][rel] = 'code would change'
                    continue
            if not dry:
                enc = 'utf-8'
                try:
                    raw.decode('utf-8')
                except UnicodeDecodeError:
                    enc = 'latin-1'
                with open(path, 'wb') as fh:
                    fh.write(new.encode(enc))
            res['changed'].append(rel)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tree')
    ap.add_argument('--skip', nargs='*', default=[])
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    r = run(a.tree, a.skip, a.dry_run)
    print(json.dumps({'changed': len(r['changed']), 'unchanged': r['unchanged'],
                      'banner_removed': r['banner_removed'], 'skipped': r['skipped']}, indent=1))


if __name__ == '__main__':
    main()
