# Third-party notices

MolKit (Python package `molkit`, part of MGLTools) is Copyright Michel F. Sanner and Scripps Research (formerly TSRI) and distributed under the Sannerlab MIT-like Source-Available License, version 1.0 (LICENSE.md). It includes the following software, which keeps its own copyright and license.

## PDB2PQR, with PROPKA and pdb2pka

- **Where:** `MolKit/pdb2pqr/`
- **Copyright:** © 2002–2007 Washington University in St. Louis (Nathan A. Baker, Paul Czodrowski, Todd Dolinsky, Jan H. Jensen, Jens E. Nielsen); PROPKA © 2005 Jan H. Jensen and Hui Li; `pdb2pka/substruct/Algorithms.cpp` © 2004 Nils Weskamp, © 1999–2004 Cambridge Crystallographic Data Centre, © 2000–2004 Stefan Schmitt, Daniel Kuhn and Gerhard Klebe
- **License:** GNU General Public License, version 2 or (at your option) any later version
- **License text:** `MolKit/pdb2pqr/COPYING`, `MolKit/pdb2pqr/doc/license.txt`, `MolKit/pdb2pqr/propka/LICENSE`
- **Source:** https://github.com/Electrostatics/pdb2pqr (the release included here: https://sourceforge.net/projects/pdb2pqr/)
- PDB2PQR is a separate program, included with its complete source. MolKit only finds `pdb2pqr.py` and runs it (`MolKit/APBSParameters.py`).

## Clique algorithms of pdb2pka

- **Where:** `MolKit/pdb2pqr/pdb2pka/substruct/clique/`
- **Copyright:** its authors, as part of PDB2PQR; the Bron–Kerbosch code follows Algorithm 457 of the Communications of the ACM, and `dfmax.c` is public-domain DIMACS code
- **License:** GNU Library General Public License, version 2
- **License text:** `MolKit/pdb2pqr/pdb2pka/substruct/clique/COPYING`

## PDB2PQR build files

- **Where:** `MolKit/pdb2pqr/configure`, `aclocal.m4`, `acinclude.m4`, `Makefile.in`, `config/` (and the same in `propka/`)
- **Copyright:** © Free Software Foundation, Inc. (GNU Autoconf, Automake and Libtool); `config/bootstrap*` © 1994–2000 Michael Holst; `config/install-sh` © 1991 Massachusetts Institute of Technology
- **License:** as stated in each file: the GNU General Public License with the Autoconf/Libtool exceptions, and the MIT (X11) permission notice for `install-sh`
- **License text:** the header of each file
