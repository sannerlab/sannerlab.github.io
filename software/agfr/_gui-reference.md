## GUI reference

### Toolbar buttons

| Button | Function |
|---|---|
| ![](img/word-image-47.png){.icon} | Focus the view on the current docking box. |
| ![](img/word-image-48.png){.icon} | Show/hide the receptor as lines. Cycles through 3 modes: the entire receptor; receptor atoms inside the docking box; hidden. |
| ![](img/word-image-49.png){.icon} | Show/hide the receptor surface. Cycles through 3 modes: surface of the entire receptor; surface of atoms inside the docking box; hidden. |
| ![](img/word-image-50.png){.icon} | Show/hide residue labels. Cycles through 3 modes: label all receptor residues; label residues with at least one side-chain atom in the box; hidden. |
| ![](img/word-image-51.png){.icon} | Show/hide the ligand. |
| ![](img/word-image-52.png){.icon} | Show/hide the ligand anchor atom: the ligand atom that AutoDockFR translates to the pocket fill points to build the initial pool of solutions for its genetic algorithm. |
| ![](img/covbutton.png){.icon} | Show/hide the atoms forming the covalent bond. |
| ![](img/word-image-54.png){.icon} | Show/hide the docking box. |
| ![](img/word-image-55.png){.icon} | Show/hide the map visualization widget (orthoslices and isocontours). |

### Docking box buttons

| Button | Function |
|---|---|
| ![](img/word-image-56.png){.icon} | Docking box encloses the receptor. |
| ![](img/word-image-57.png){.icon} | Docking box encloses the ligand. |
| ![](img/word-image-58.png){.icon} | Docking box encloses the binding-pocket fill points. |
| ![](img/word-image-59.png){.icon} | Docking box encloses receptor amino acids selected by the user. |
| ![](img/word-image-60.png){.icon} | Set the docking box manually, and set the grid spacing and smoothing factor. |

### Validity status lights

Each light has up to three states: disabled, invalid (red) and valid (green).

| Light | Function |
|---|---|
| ![](img/word-image-61.png){.icon} ![](img/word-image-62.png){.icon} | **Box**: red if the box does not overlap the receptor (no receptor atom inside the box). Never disabled; applies to every docking calculation. |
| ![](img/word-image-63.png){.icon} ![](img/word-image-64.png){.icon} ![](img/word-image-65.png){.icon} | **Pocket**: enabled unless the receptor is prepared for covalent docking. Red if none of the selected (displayed) fill points is inside the box. |
| ![](img/word-image-66.png){.icon} ![](img/word-image-67.png){.icon} ![](img/word-image-68.png){.icon} | **FR** (flexible residues): enabled only when side chains have been made flexible. Red if at least one atom of these side chains is outside the box. |
| ![](img/word-image-69.png){.icon} ![](img/word-image-70.png){.icon} ![](img/word-image-71.png){.icon} | **Cov** (covalent docking): enabled only when the covalent docking check button is checked. Turns green once the 2 receptor atoms forming the covalent bond are selected. |
