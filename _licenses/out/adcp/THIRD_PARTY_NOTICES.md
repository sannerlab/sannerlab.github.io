# Third-party notices

ADCP (Python package `adcp`) is Copyright Michel F. Sanner and Scripps Research (formerly TSRI) and distributed under the Sannerlab MIT-like Source-Available License, version 1.0 (LICENSE.md). It includes the following software, which keeps its own copyright and license.

## CrankiteAD docking engine

- **Where:** `ADCP/CrankiteAD_Linux-x86_64_1.1` (executable) and its Ramachandran table `ADCP/data/ramaprob.data`
- **Copyright:** © 2003–2010 Alexei Podtelezhnikov; © 2007–2013 Nikolas Burkoff, Csilla Varnai and David Wild; © 2019–present Michel F. Sanner
- **License:** GNU Library General Public License, version 2.0, with the agreement of CRANKITE's authors
- **License text:** `COPYING.LESSER`, next to this file
- **Source:** https://github.com/sannerlab/Crankite_AD (tag `adcp-1.1-engine` is the source of the engine of adcp 0.0.25, ADCP 1.1); the alpha releases list the engine's source commit in `ADCP/BUILD_INFO.txt` and ship its source archive with the installer
- The engine derives from CRANKITE: Podtelezhnikov, A. A.; Wild, D. L. *Source Code Biol. Med.* **2008**, 3, 12. It runs as a separate program, started by `runADCP.py`.

## OpenMM implicit-solvent parameter files

- **Where:** `ADCP/data/openMMff/openmm7.7/implicit/*.xml`
- **Copyright:** © 2008–2022 Stanford University and the Authors
- **License:** MIT License
- **License text:**

```
Portions copyright (c) 2008-2022 Stanford University and the Authors.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS, CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
USE OR OTHER DEALINGS IN THE SOFTWARE.
```

- **Source:** https://github.com/openmm/openmm (OpenMM 7.7)

## SwissSidechain rotamer data

- **Where:** `ADCP/data/rotamers/SWISS_ROTAMER_LIST.dat`, `ADCP/data/rotamers/swiss*.lib`, `ADCP/data/openMMff/swiss_ff.xml`
- **Copyright:** the lab's files are made from the SwissSidechain library, © SIB Swiss Institute of Bioinformatics
- **License:** the terms of SwissSidechain
- **License text:** https://www.swisssidechain.ch
- **Source:** https://www.swisssidechain.ch
- Gfeller, D.; Michielin, O.; Zoete, V. SwissSidechain: a molecular and structural database of non-natural sidechains. *Nucleic Acids Res.* **2013**, 41, D327–D332.

## 2010 Backbone-Dependent Rotamer Library

- **Where:** `ADCP/data/rotamers/bbdep_20260812.lib` (adcp 0.0.26a1 and later)
- **Copyright:** © Fox Chase Cancer Center (Maxim V. Shapovalov and Roland L. Dunbrack, Jr.)
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **License text:** `CC-BY-4.0.txt`, next to this file
- **Source:** https://dunbrack.fccc.edu/lab/bbdep2010 (read from the copy `dun2010bbdep.bin` distributed with FASPR, https://github.com/tommyhuangthu/FASPR, MIT License, © 2020 Xiaoqiang Huang)
- Contains information from the 2010 Backbone-Dependent Rotamer Library (https://dunbrack.fccc.edu/bbdep2010), which is made available under the license at https://dunbrack.fccc.edu/bbdep2010/license/bbdep2010_license.txt. Changed by the Sanner lab: written in the CrankiteAD rotamer-library format, with backbone-marginal rotamer probabilities and the phi/psi probability tables. Shapovalov, M. V.; Dunbrack, R. L., Jr. *Structure* **2011**, 19, 844–858.
