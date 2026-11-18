# Third-party notices

Opengltk (Python package `opengltk`, part of MGLTools) is Copyright Michel F. Sanner and Scripps Research (formerly TSRI) and distributed under the Sannerlab MIT-like Source-Available License, version 1.0 (LICENSE.md). It includes the following software, which keeps its own copyright and license.

## JPE libplus and ccallback

- **Where:** `opengltk/ccallback.py`; `pythonplus.c`, compiled into `opengltk/extent/_gllib.so`, `_glulib.so`, `_glxlib.so`, `_glextlib.so` and `_utillib.so`
- **Copyright:** © 2001–2002 Frederic Bruno Giacometti
- **License:** Mozilla Public License, version 1.1
- **License text:** `MPL-1.1.txt`, next to this file
- **Source:** “Java-Python Extension libplus (JPE-libplus)” by Frederic Bruno Giacometti
- The source code of the compiled MPL files is `opengltk/extent/pythonplus.c`, `pythonplus.h` and `utilplus.h` of the opengltk sources.

## Virtual trackball

- **Where:** `opengltk/extent/_utillib.so` (`glTrackball`)
- **Copyright:** © 1993, 1994 Silicon Graphics, Inc. (trackball by Gavin Bell)
- **License:** Silicon Graphics permission notice
- **License text:**

```
/*
 * (c) Copyright 1993, 1994, Silicon Graphics, Inc.
 * ALL RIGHTS RESERVED
 * Permission to use, copy, modify, and distribute this software for
 * any purpose and without fee is hereby granted, provided that the above
 * copyright notice appear in all copies and that both the copyright notice
 * and this permission notice appear in supporting documentation, and that
 * the name of Silicon Graphics, Inc. not be used in advertising
 * or publicity pertaining to distribution of the software without specific,
 * written prior permission.
 *
 * THE MATERIAL EMBODIED ON THIS SOFTWARE IS PROVIDED TO YOU "AS-IS"
 * AND WITHOUT WARRANTY OF ANY KIND, EXPRESS, IMPLIED OR OTHERWISE,
 * INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY OR
 * FITNESS FOR A PARTICULAR PURPOSE.  IN NO EVENT SHALL SILICON
 * GRAPHICS, INC.  BE LIABLE TO YOU OR ANYONE ELSE FOR ANY DIRECT,
 * SPECIAL, INCIDENTAL, INDIRECT OR CONSEQUENTIAL DAMAGES OF ANY
 * KIND, OR ANY DAMAGES WHATSOEVER, INCLUDING WITHOUT LIMITATION,
 * LOSS OF PROFIT, LOSS OF USE, SAVINGS OR REVENUE, OR THE CLAIMS OF
 * THIRD PARTIES, WHETHER OR NOT SILICON GRAPHICS, INC.  HAS BEEN
 * ADVISED OF THE POSSIBILITY OF SUCH LOSS, HOWEVER CAUSED AND ON
 * ANY THEORY OF LIABILITY, ARISING OUT OF OR IN CONNECTION WITH THE
 * POSSESSION, USE OR PERFORMANCE OF THIS SOFTWARE.
 *
 * US Government Users Restricted Rights
 * Use, duplication, or disclosure by the Government is subject to
 * restrictions set forth in FAR 52.227.19(c)(2) or subparagraph
 * (c)(1)(ii) of the Rights in Technical Data and Computer Software
 * clause at DFARS 252.227-7013 and/or in similar or successor
 * clauses in the FAR or the DOD or NASA FAR Supplement.
 * Unpublished-- rights reserved under the copyright laws of the
 * United States.  Contractor/manufacturer is Silicon Graphics,
 * Inc., 2011 N.  Shoreline Blvd., Mountain View, CA 94039-7311.
 *
 * OpenGL(TM) is a trademark of Silicon Graphics, Inc.
 */
/*
 * Trackball code:
 *
 * Implementation of a virtual trackball.
 * Implemented by Gavin Bell, lots of ideas from Thant Tessman and
 *   the August '88 issue of Siggraph's "Computer Graphics," pp. 121-129.
 *
 * Vector manip code:
 *
 * Original code from:
 * David M. Ciemiewicz, Mark Grossman, Henry Moreton, and Paul Haeberli
 *
 * Much mucking with by:
 * Gavin Bell
```

- **Source:** GLUT example `progs/examples/trackball.c`, https://github.com/markkilgard/glut
- Adapted in opengltk’s `extent/dejavu.i`.

## Togl, tkdnd 2.0 and TkinterDnD2 (source repository only)

- **Where:** `Togl/`, `Togl2.0/`, `Togl2.1/`, `tkdnd2.0/`, `TkinterDnD2/` of the source repository; not in the `opengltk` package
- **Copyright:** their authors (Togl: Brian Paul, Benjamin Bederson and others; tkdnd: Georgios Petasis; TkinterDnD2: Michael Lange)
- **License:** each keeps the license stated in its folder
- **License text:** the license files in each folder
