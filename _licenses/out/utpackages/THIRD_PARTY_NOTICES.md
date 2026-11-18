# Third-party notices

The Sanner lab's part of UTpackages (Python package `utpackages`, part of MGLTools) is Copyright Michel F. Sanner and Scripps Research (formerly TSRI) and distributed under the Sannerlab MIT-like Source-Available License, version 1.0 (LICENSE.md). It includes the following software, which keeps its own copyright and license.

## UTpackages: UTblur, UTisocontour, UTmesh, UTmolderivatives, UTsdf, UTvolrend

- **Where:** `UTpackages/` (all compiled extensions)
- **Copyright:** © 2002–2005 The University of Texas at Austin (Center for Computational Visualization, Chandrajit Bajaj)
- **License:** terms of The University of Texas at Austin: free for non-commercial educational and non-commercial academic use; any other use, including commercial use, needs a license from The University of Texas at Austin
- **License text:** `UTpackages_license.txt`, next to this file
- **Source:** Center for Computational Visualization, The University of Texas at Austin (http://www.ices.utexas.edu/CCV)
- Authors named in the sources include Dan Schikore, Emilio Camahort, Anthony Thane, Lalit Karlapalem and Vinay Siddavanahalli. The source files of UTmolderivatives state the GNU Lesser General Public License 2.1 or later together with “free for academic or personal non-profit use”; those of UTvolrend and UTsdf state the GNU General Public License (rows below).

## UTvolrend volume renderer (from Volume Rover)

- **Where:** `UTpackages/UTvolrend/` (`_UTVolumeLibrary*.so`)
- **Copyright:** © 2002–2003 The University of Texas at Austin (Anthony Thane; advisor Chandrajit Bajaj)
- **License:** GNU General Public License, version 2 or (at your option) any later version, as stated in its source files; its directory also carries the terms of The University of Texas at Austin
- **License text:** `GPL-2.0.txt`, next to this file
- **Source:** Volume Rover, Center for Computational Visualization, The University of Texas at Austin

## UTsdf signed distance fields

- **Where:** `UTpackages/UTsdf/` (`_utsdf*.so`)
- **Copyright:** © 2002–2003 The University of Texas at Austin (Lalit Karlapalem; advisor Chandrajit Bajaj)
- **License:** GNU General Public License, version 2 or (at your option) any later version, as stated in its source files; its directory also carries the terms of The University of Texas at Austin
- **License text:** `GPL-2.0.txt`, next to this file
- **Source:** Center for Computational Visualization, The University of Texas at Austin

## kazlib dictionary (`dict.c`)

- **Where:** compiled into `UTpackages/UTisocontour/_isocontour*.so`
- **Copyright:** © 1997 Kaz Kylheku; modified by Anna Omelchenko (TSRI)
- **License:** kazlib free software license (notice in the file)
- **License text:**

```
/*
 * Dictionary Abstract Data Type
 * Copyright (C) 1997 Kaz Kylheku <kaz@ashi.footprints.net>
 *
 * Free Software License:
 *
 * All rights are reserved by the author, with the following exceptions:
 * Permission is granted to freely reproduce and distribute this software,
 * possibly in exchange for a fee, provided that this copyright notice appears
 * intact. Permission is also granted to adapt this software to produce
 * derivative works, as long as the modified versions carry this copyright
 * notice and additional notices stating that the work has been modified.
 * This source code may be translated into executable form and incorporated
 * into proprietary software; there is no requirement for such software to
 * contain a copyright notice related to this source.
 *
 * $Id: dict.c,v 1.2 2005/12/27 19:38:37 annao Exp $
 * $Name: rel1-1rc1 $
 */

/* This version was modified by Anna Omelchenko (TSRI) to compile it 
 * with C++ compiler:
 *  -- replaced 'new', 'template', 'delete' variables by '_new', 
 *      '_template' and '_delete' respectively.
 *  -- added type_casting for malloc().       
 */
```

- **Source:** kazlib, by Kaz Kylheku
