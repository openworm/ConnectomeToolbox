Data was taken from: Cook et al. 2019, Whole-animal connectomes of both Caenorhabditis elegans sexes. [Nature 571, 63–71](https://doi.org/10.1038/s41586-019-1352-7).

Three spreadsheets with these connections have been identified:

1) Original Supplementary information 5

Connectivity matrices were released in the following supplementary information file with the publication: [41586_2019_1352_MOESM9_ESM.xlsx](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-019-1352-7/MediaObjects/41586_2019_1352_MOESM9_ESM.xlsx).

**Note:** there is a slight internal consistency issue in this file - some of the male ray structural cells are named R1stL, R2stR, etc. ), but in other locations the names R1shL, R2shR, etc. are used.


2) WormWiring original adjacency matrices

On WormWiring (Emmons lab), there is a link: Original Connectome Adjacency Matrices (ref 1, SI5) [SI 5 Connectome adjacency matrices.xlsx](https://wormwiring.org/si/SI%205%20Connectome%20adjacency%20matrices.xlsx).

**Note:** there is a slight difference between this file and the original - some of the male ray structural cells R1stL, R2stR cells have been changed to R1shL, R2shR, etc. in this file.

3) WormWiring corrected adjacency matrices

There is also a file: Hermaphrodite and Male Connectomes (Adjacency Matrices), Adults (corrected July 2020) [[SI 5 Connectome adjacency matrices, corrected July 2020.xlsx](https://wormwiring.org/si/SI%205%20Connectome%20adjacency%20matrices,%20corrected%20July%202020.xlsx)].

The differences in this file are as follows: 

_Hermaphrodite gap junctions_

- Added: PVDL ↔ hmc: weight 400
- Added: PVDR ↔ hmc: weight 400
- Removed: BDUR ↔ PLMR: weight 23
- The following connections were not originally present in both directions (i.e. a fully symmetrical electrical connection was not present): 
    - DD06 ↔ PDB
    - ALA ↔ exc_gl
    - VA09 ↔ PVCR

_Male gap junctions_

- Added: DD1 ↔ MVL08: weight 2
- Removed: RIVR ↔ FLPL: weight 1
- The following connections were not originally present in both directions (i.e. a fully symmetrical electrical connection was not present): 
    - DD1 ↔ MVR08
    - R8AL ↔ R8BL
    - RIVL ↔ FLPL
    - VB6 ↔ VB7
    - VB7 ↔ VB5
    - MDR08 ↔ DD1
    
**In Connectome Toolbox, we use spreadsheet 3), and use R1stL, R2stR, etc., as these are the names used [on WormAtlas](https://www.wormatlas.org/male/rays/mainframe.htm#Celllist5).**

Additionally, we used **g1P**, not **g1p** for the name of this pharyngeal glial cell, as this is the form used in Cook et al. 2020, as well as on WormWiring. 

This file was opened in Excel and weights of selected connections were visually read from the cells on the specific sheets (e.g. hermaphrodite chemical, male gap jn symmetric), 
noting the pre and post cells and these added to the connection test YAML file, along with the total number of nonzero connections in each adjacency matrix as well as the total weights. 