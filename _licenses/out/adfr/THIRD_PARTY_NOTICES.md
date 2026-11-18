# Third-party notices

ADFR (Python package `adfr`) is Copyright Michel F. Sanner and Scripps Research (formerly TSRI) and distributed under the Sannerlab MIT-like Source-Available License, version 1.0 (LICENSE.md). It includes the following software, which keeps its own copyright and license.

## AutoGrid 4

- **Where:** `bin/autogrid4` of the environment (wheel: `adfr-*.data/data/bin/autogrid4`)
- **Copyright:** © 1989–2020 The Scripps Research Institute (Garrett M. Morris, Ruth Huey, David S. Goodsell, Arthur J. Olson). AutoGrid is a trademark of The Scripps Research Institute
- **License:** GNU General Public License, version 2 or (at your option) any later version
- **License text:** `GPL-2.0.txt`, next to this file
- **Source:** https://github.com/ccsb-scripps/AutoGrid (this executable is AutoGrid 4.2.7.x.2020-07-06, built from the MGLTools CVS tree of AutoGrid)
- AutoGrid is a separate program; ADFR and AGFR run it to compute affinity maps.

## AutoDock 4.1 force-field parameters

- **Where:** `ADFR/Data/AD4.1_bound.dat`
- **Copyright:** © 1989–2007 Garrett M. Morris, David S. Goodsell, Ruth Huey, Arthur J. Olson. AutoDock is a trademark of The Scripps Research Institute
- **License:** GNU General Public License, version 2 or (at your option) any later version
- **License text:** `GPL-2.0.txt`, next to this file
- **Source:** AutoDock 4, https://autodock.scripps.edu
- Huey, R.; Morris, G. M.; Olson, A. J.; Goodsell, D. S. *J. Comput. Chem.* **2007**, 28, 1145–1152.

## reduce 3.23 and its hetero-group dictionary

- **Where:** `bin/reduce` and `bin/reduce_wwPDB_het_dict.txt` of the environment (wheel: `adfr-*.data/data/bin/reduce`, `adfr-*.data/scripts/reduce_wwPDB_het_dict.txt`)
- **Copyright:** © 1997–2013 J. Michael Word (Richardson Laboratory, Duke University); `libpdb` © 1992 The Regents of the University of California
- **License:** the reduce notice (redistribution and modification are permitted provided the notice is kept unchanged and modified versions are also available for free), and the University of California notice for `libpdb`
- **License text:**

```
reduce 3.23 (05/21/2013), source: https://github.com/rlabduke/reduce, commit 81b5b32.
Notices copied verbatim from that commit.

== reduce_src/reduce.cpp (and the other reduce and toolclasses sources) ==

// **************************************************************
// NOTICE: This is free software and the source code is freely
// available. You are free to redistribute or modify under the
// conditions that (1) this notice is not removed or modified
// in any way and (2) any modified versions of the program are
// also available for free.
//               ** Absolutely no Warranty **
// Copyright (C) 1999-2013 J. Michael Word
// **************************************************************

== libpdb/pdb++.h (and the other libpdb sources) ==

// with Modifications by J. Michael Word, Duke University
//
//	Copyright (c) 1992 The Regents of the University of California.
//	All rights reserved.
//
//	Redistribution and use in source and binary forms are permitted
//	provided that the above copyright notice and this paragraph are
//	duplicated in all such forms and that any documentation,
//	advertising materials, and other materials related to such
//	distribution and use acknowledge that the software was developed
//	by the University of California, San Francisco.  The name of the
//	University may not be used to endorse or promote products derived
//	from this software without specific prior written permission.
//	THIS SOFTWARE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
//	IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
//	WARRANTIES OF MERCHANTIBILITY AND FITNESS FOR A PARTICULAR PURPOSE.
//
//	Based on Brookhaven National Laboratory Protein Data Bank, Feb 1992
//
```

- **Source:** https://github.com/rlabduke/reduce (version 3.23 is commit 81b5b32, 21 May 2013)
- reduce is a separate program, run by AGFR to add hydrogen atoms: Word, J. M. et al. *J. Mol. Biol.* **1999**, 285, 1735–1747. The dictionary is a reduce dictionary made from the wwPDB Chemical Component Dictionary. Releases of reduce since September 2026 are under the Apache License 2.0.

## NLopt 2.5.0 (nonlinear optimization library)

- **Where:** `lib/libnlopt.so.0` of the environment (wheel: `adfr-*.data/data/lib/libnlopt.so.0`)
- **Copyright:** © 2007–2014 Massachusetts Institute of Technology (Steven G. Johnson); its Luksan routines © 2007 Ladislav Luksan and Jan Vlcek; its other algorithms © their authors (M. J. D. Powell; Jean-Sébastien Roy; North Carolina State University; Carlos Henrique da Silva Santos; Dieter Kraft, ACM, Enthought and the SciPy developers), as listed in the license file
- **License:** GNU Lesser General Public License, version 2.1 or (at your option) any later version, for the compiled library (because of its Luksan routines); the other parts are under the MIT License or the permissive notices reproduced in the license file
- **License text:** `NLopt-2.5.0-LICENSE.txt`, next to this file
- **Source:** https://github.com/stevengj/nlopt (tag v2.5.0)
- Built without the StoGO and AGS algorithms. `ADFRcc/_adfrcc.so` (package adfrcc) loads it at run time; any compatible NLopt library can replace it.

## Backbone-independent rotamer library (2002)

- **Where:** `ADFR/Data/bbind02.May.lib`
- **Copyright:** Roland L. Dunbrack, Jr., Fox Chase Cancer Center (May 2002)
- **License:** none stated: the Dunbrack lab published the library as freely available and asked users to cite Dunbrack and Cohen (1997)
- **Source:** http://dunbrack.fccc.edu/bbdep/ (file `bbind02.May.lib.gz`)
- Dunbrack, R. L., Jr.; Cohen, F. E. *Protein Sci.* **1997**, 6, 1661–1681.

## Tables made from the Protein Data Bank

- **Where:** `ADFR/PDBChemComp.py`, `ADFR/PDBLigDicts.py`
- **Copyright:** data of the PDB archive and its Chemical Component Dictionary, wwPDB
- **License:** CC0 1.0 Universal public domain dedication
- **License text:** https://www.wwpdb.org/about/usage-policies
- **Source:** https://www.wwpdb.org

## Statistics functions of ScientificPython

- **Where:** `ADFR/ga_util.py` (`moment`, `mean`, `weightedMean`, `variance`, `standardDeviation`, `median`, `mode`, `normalizedMoment`)
- **Copyright:** Konrad Hinsen (ScientificPython, `Scientific.Statistics`)
- **License:** not established: depends on the ScientificPython version copied (permissive notice until about 2.4.9; CeCILL from about 2.4.10, CeCILL-C from 2.7.9); the file does not say
- **Source:** https://github.com/khinsen/ScientificPython
- Comment in the file: “taken from MMTK / Scientific.Statistics.__init__.py”. Its origin or license could not be established; the Sanner lab claims no rights in it.
