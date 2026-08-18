# Validation status of Data Readers

## WhiteEtAl1986

Data from White et al. 1986, The Structure of the Nervous System of the Nematode Caenorhabditis elegans, [Phil. Trans. R. Soc. Lond. B3141–340](https://royalsocietypublishing.org/doi/10.1098/rstb.1986.0056) (also on [WormAtlas](https://wormatlas.org/MoW_built0.92/MoW.html)).

As described on [WormAtlas](https://www.wormatlas.org/neuronalwiring.html), the primary structured dataset describing this connectivity is the **neurodata.txt** file which was compiled by Richard Durbin in his 1987 thesis. This (and the [Readme](https://www.wormatlas.org/neurodata_readme.txt) describing it) can be found [on WormAtlas](https://www.wormatlas.org/neurodata.txt). 

The **neurodata.txt** file describes reconstructed connectivity for 2 animals: an N2U (adult hermaphrodite) and JSH (which Durbin described as an L4 male, it is now believed that this animal was an L4 hermaphrodite). This file been copied into our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/neurodata.txt).

However, an [updated version of this file](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/neurodata_updated.txt) was used in the DurbinDataReader in cect, as the following minor issues were found in the file, and these were incorporated in the data source, as opposed to the Python reader, for clarity:

**Issue 1)** Line 2 in the original file (ADAL ADAR Gap_junction 1) was missing JSH or N2U, and so assuming N2U as "ADAL ADAR Gap_junction JSH 2" was already present.
**Issue 2)** While most gap junction connections contained both A->B and B->A connections, but some were missing the reverse connection. The missing connections at the top of the file.
**Issue 3)** One gap junction connection had a different weight for the A->B and B->A connections (RIML<->AVAR). Updated the weight to be the same for both directions, using the larger of the two weights.

The "White Whole" dataset is effectively the same as the Varshney et al. 2011 dataset, apart from also containing the connections to/from the pharynx. This dataset was obtained from the [WormNeuroAtlas source code](https://github.com/francescorandi/wormneuroatlas/blob/main/wormneuroatlas/data/aconnectome_white_1986_whole.csv), and copied to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/aconnectome_white_1986_whole.csv).

Note: this dataset contained 3 electrical connections not present in the Varshney dataset: PLML <-> BDUL, PLMR <-> BDUR, RID <-> RID, all of weight 1



### Validation tests for [DurbinJSHDataReader](WhiteJSH_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADAL | AVBR | 5 | Yes |
| ADFR | AIZR | 10 | Yes |
| DVC | RIGL | 8 | Yes |
| RMDDR | RMDVL | 10 | Yes |

Expected number of nonzero connection weights: **1350** (matches)

Expected total weight of connections: **4000** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AVAR | 2 | Yes |
| RMED | IL1VL | 2 | Yes |
| CEPDL | OLQDL | 4 | Yes |
| AVAL | SABD | 2 | Yes |
| SABD | AVAL | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **586** (matches)

Expected total weight of connections: **1546** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [DurbinN2UDataReader](WhiteN2U_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADAL | AVBR | 7 | Yes |
| ADFR | AIZR | 8 | Yes |
| DVC | RIGL | 5 | Yes |
| RMDDR | RMDVL | 12 | Yes |

Expected number of nonzero connection weights: **1486** (matches)

Expected total weight of connections: **4056** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AVAR | 1 | Yes |
| RMED | IL1VL | 1 | Yes |
| CEPDL | OLQDL | 1 | Yes |
| VA2 | PLNR | 1 | Yes |
| PLNR | VA2 | 1 | Yes |
| DVC | VD1 | 2 | Yes |
| VD1 | DVC | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **556** (matches)

Expected total weight of connections: **692** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [White_whole](White_whole_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AS5 | 3 | Yes |
| ADAL | AVBR | 7 | Yes |
| ADFR | AIZR | 8 | Yes |
| DVC | RIGL | 5 | Yes |
| RMDDR | RMDVL | 12 | Yes |
| VD3 | BWM | 23 | Yes |
| URADR | BWM | 7 | Yes |
| IL1DL | BWM | 5 | Yes |

Expected number of nonzero connection weights: **2386** (matches)

Expected total weight of connections: **7943** (matches)

Expected number of cells: **309** (matches)

#### Chemical connections

**Note:** only cells/connections in ConnectomeView: **NonpharyngealH** included (All **hermaphrodite** neurons except those in the pharynx)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AS5 | 3 | Yes |
| ADAL | AVBR | 7 | Yes |
| ADFR | AIZR | 8 | Yes |
| DVC | RIGL | 5 | Yes |
| RMDDR | RMDVL | 12 | Yes |

Expected number of nonzero connection weights: **2194** (matches)

Expected total weight of connections: **6394** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AVAR | 5 | Yes |
| RMED | IL1VL | 1 | Yes |
| CEPDL | OLQDL | 1 | Yes |
| PDER | PDEL | 3 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **1144** (matches)

Expected total weight of connections: **1928** (matches)

#### Electrical connections

**Note:** only cells/connections in ConnectomeView: **NonpharyngealH** included (All **hermaphrodite** neurons except those in the pharynx)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AVAR | 5 | Yes |
| RMED | IL1VL | 1 | Yes |
| CEPDL | OLQDL | 1 | Yes |
| PDER | PDEL | 3 | Yes |

Expected number of nonzero connection weights: **1036** (matches)

Expected total weight of connections: **1782** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## VarshneyEtAl2011

An updated version of the White et al. 1986 wiring data, as presented in Varshney et al. 2011, Structural Properties of the Caenorhabditis elegans Neuronal Network. [PLOS Computational Biology 7(2): e1001066](https://doi.org/10.1371/journal.pcbi.1001066).

The file [NeuronConnect.xls](https://www.wormatlas.org/images/NeuronConnect.xls), referenced in the paper ("The collected data is available from the WormAtlas"), which is also available [here](https://wormwiring.org/), has been copied into our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/NeuronConnect.xls), and used in our DataReader.

The spreadsheet above contained a single sheet, with a list of presynaptic cells, postsynaptic cells, synapse numbers, and types of synapse (S, Sp, R, Rp, EJ, NMJ). See [here](https://www.wormatlas.org/neuronalwiring.html#Connectivitydata) for full details. This file was opened in Excel and weights of selected connections were visually read from the cells (summing entries for S and Sp where both were present), noting the pre and post cells and added to the connection test yaml file. 




### Validation tests for [VarshneyDataReader](Varshney_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AS5 | 3 | Yes |
| ADAL | AVBR | 7 | Yes |
| ADFR | AIZR | 8 | Yes |
| DVC | RIGL | 5 | Yes |
| RMDDR | RMDVL | 12 | Yes |
| VD3 | BWM | 23 | Yes |
| URADR | BWM | 7 | Yes |
| IL1DL | BWM | 5 | Yes |

Expected number of nonzero connection weights: **2309** (matches)

Expected total weight of connections: **7804** (matches)

#### Chemical connections

**Note:** only cells/connections in ConnectomeView: **NonpharyngealH** included (All **hermaphrodite** neurons except those in the pharynx)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AS5 | 3 | Yes |
| ADAL | AVBR | 7 | Yes |
| ADFR | AIZR | 8 | Yes |
| DVC | RIGL | 5 | Yes |
| RMDDR | RMDVL | 12 | Yes |

Expected number of nonzero connection weights: **2194** (matches)

Expected total weight of connections: **6394** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AVAR | 5 | Yes |
| RMED | IL1VL | 1 | Yes |
| CEPDL | OLQDL | 1 | Yes |
| PDER | PDEL | 3 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **1031** (matches)

Expected total weight of connections: **1777** (matches)

#### Electrical connections

**Note:** only cells/connections in ConnectomeView: **NonpharyngealH** included (All **hermaphrodite** neurons except those in the pharynx)

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVAL | AVAR | 5 | Yes |
| RMED | IL1VL | 1 | Yes |
| CEPDL | OLQDL | 1 | Yes |
| PDER | PDEL | 3 | Yes |

Expected number of nonzero connection weights: **1031** (matches)

Expected total weight of connections: **1777** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## BentleyEtAl2016

Data from: The Multilayer Connectome of Caenorhabditis elegans, Bentley et al. 2016, [PLoS Comput Biol 12(12): e1005283](https://doi.org/10.1371/journal.pcbi.1005283)

Connectivity was originally released in supplementary information: [S1 Dataset](https://doi.org/10.1371/journal.pcbi.1005283.s004) ("Included are edge lists for monoamine and neuropeptide networks").

The contents of this zip file were extracted and the 2 files [edge_lists/edgelist_MA.csv](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/edgelist_MA.csv) and [edge_lists/edgelist_NP.csv](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/edgelist_NP.csv) were added to our repository and used in the monoaminergic and peptidergic DataReaders respectively. 

For the validation tests below, specific connections between pre and postsynaptic cells were read out from the edgelist_MA.csv and edgelist_NP.csv files above and a weight of 1 was added to the connection test yaml file for these. 



### Validation tests for [Bentley2016MAReader](Bentley2016_MA_data.md) 


#### Dopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| CEPDR | ALNR | 1 | Yes |
| ADER | VA11 | 1 | Yes |
| PDEL | SIBDR | 1 | Yes |
| ADEL | CANL | 1 | Yes |
| CEPDR | CANL | 1 | Yes |

Expected number of nonzero connection weights: **1176** (matches)

#### Tyramine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIML | IL1DL | 1 | Yes |
| RIML | PVT | 1 | Yes |
| RIMR | AFDL | 1 | Yes |
| RIML | CANL | 1 | Yes |

Expected number of nonzero connection weights: **228** (matches)

#### Octopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RICL | PHAL | 1 | Yes |
| RICL | ADEL | 1 | Yes |
| RICR | SIAVL | 1 | Yes |

Expected number of nonzero connection weights: **56** (matches)

#### Serotonin connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADFR | M2R | 1 | Yes |
| NSMR | AIBL | 1 | Yes |
| HSNL | M3L | 1 | Yes |

Expected number of nonzero connection weights: **492** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [Bentley2016PepReader](Bentley2016_Pep_data.md) 


#### Peptidergic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AIAL | AIAR | 1 | Yes |
| RMER | OLQVR | 1 | Yes |
| M3R | RIVR | 1 | Yes |
| FLPR | IL2R | 1 | Yes |
| VD9 | PVWR | 1 | Yes |

Expected number of nonzero connection weights: **7078** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## CookEtAl2019

Data was taken from: Cook et al. 2019, Whole-animal connectomes of both Caenorhabditis elegans sexes. [Nature 571, 63–71](https://doi.org/10.1038/s41586-019-1352-7).

Three spreadsheets with these connections have been identified:

1) Original Supplementary information 5

Connectivity matrices were released in the following supplementary information file with the publication: [41586_2019_1352_MOESM9_ESM.xlsx](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-019-1352-7/MediaObjects/41586_2019_1352_MOESM9_ESM.xlsx).

**Note:** there is a slight internal consistency issue this file - some of the male ray structural cells are named R1stL, R2stR, etc. ), but in other locations the names R1shL, R2shR, etc. are used.


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
noting the pre and post cells and these added to the connection test yaml file, along with the total number of nonzero connections in each adjacency matrix as well as the total weights. 


### Validation tests for [Cook2019HermReader](Cook2019Herm_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 6 | Yes |
| SMBDL | SDQR | 18 | Yes |
| VC2 | PVT | 6 | Yes |
| DB4 | MDL13 | 4 | Yes |
| RIMR | MDL05 | 15 | Yes |
| M1 | g1P | 5 | Yes |
| I6 | g1P | 2 | Yes |

Expected number of nonzero connection weights: **4879** (matches)

Expected total weight of connections: **28113** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| M4 | pm5VL | 1 | Yes |
| g1AL | M4 | 7 | Yes |
| PLNL | PHCL | 2 | Yes |
| PVDL | ALA | 250 | Yes |
| PVDL | hmc | 400 | Yes |
| PVDR | hmc | 400 | Yes |
| DD6 | PDB | 2 | Yes |
| PDB | DD6 | 2 | Yes |
| ALA | exc_gl | 1 | Yes |
| exc_gl | ALA | 1 | Yes |
| BDUL | PLML | 0 | Yes |
| RMDVR | SMDVR | 8 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **2883** (matches)

Expected total weight of connections: **23313** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [Cook2019MaleReader](Cook2019Male_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 6 | Yes |
| SMBDL | SDQR | 18 | Yes |
| R7BL | PDC | 34 | Yes |
| DB4 | MDL13 | 4 | Yes |
| RIMR | MDL05 | 15 | Yes |
| CEPDR | RMHL | 6 | Yes |
| URBL | OLLL | 4 | Yes |
| R9BR | R7stR | 2 | Yes |

Expected number of nonzero connection weights: **5306** (matches)

Expected total weight of connections: **45959** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| M4 | pm5VL | 1 | Yes |
| g1AL | M4 | 7 | Yes |
| CANL | exc_cell | 200 | Yes |
| PVDL | ALA | 250 | Yes |
| URBL | IL2L | 17 | Yes |
| DD1 | MVL08 | 2 | Yes |
| RIVR | FLPL | 0 | Yes |
| DD1 | MVR08 | 2 | Yes |
| R8AL | R8BL | 5 | Yes |
| RIVL | FLPL | 1 | Yes |
| VB6 | VB7 | 5 | Yes |
| VB7 | VB5 | 1 | Yes |
| MDR08 | DD1 | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **3482** (matches)

Expected total weight of connections: **31702** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## CookEtAl2020

Data was taken from Cook et al. 2020, The connectome of the Caenorhabditis elegans pharynx, [J Comp Neurol. 2020; 528: 2767–2784](https://onlinelibrary.wiley.com/doi/10.1002/cne.24932).

The connectivity data was released in 2 CSV files in the supplementary information for that paper:

- [cne24932-sup-0004-Supinfo4.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0004-Supinfo4.csv) described as "Complete edge list for pharyngeal reconstruction."

- [cne24932-sup-0005-Supinfo5.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0005-Supinfo5.csv) described as "Inferred gap junction connectivity between end-organs". These connections have been included and some of these tested below also. 

These files were opened in Apple Numbers, and the weights (numbers of connections between pairs of cells, electrical or chemical) were read off, to provide checks listed below. 

**Validation issue: Repeated connections**

There were multiple entries in [cne24932-sup-0004-Supinfo4.csv](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fcne.24932&file=cne24932-sup-0004-Supinfo4.csv) for the same pair of cells and the same type of connection. Where there are multiple lines of this type, the weights in the new line have been appended to the existing weight. 

This is a summary of the connections which were repeated: 

> Existing connection at (14,14) (M4->M4, Chemical), was: 15.0, new conn weight: 15.0, appended weight is: 30.000000
>
> Existing connection at (17,30) (I4->NSMR, Chemical), was: 2.0, new conn weight: 13.5, appended weight is: 15.500000
>
> Existing connection at (37,15) (NSML->pm5D, Chemical), was: 29.0, new conn weight: 9.0, appended weight is: 38.000000
>
> Existing connection at (30,31) (NSMR->bm, Chemical), was: 50.0, new conn weight: 11.0, appended weight is: 61.000000
>
> Existing connection at (30,15) (NSMR->pm5D, Chemical), was: 1.0, new conn weight: 8.5, appended weight is: 9.500000
>
> Existing connection at (30,32) (NSMR->M3R, Chemical), was: 15.0, new conn weight: 7.5, appended weight is: 22.500000
>
> Existing connection at (37,18) (NSML->pm5VL, Chemical), was: 58.0, new conn weight: 5.0, appended weight is: 63.000000
>
> Existing connection at (17,18) (I4->pm5VL, Chemical), was: 6.0, new conn weight: 4.5, appended weight is: 10.500000
>
> Existing connection at (37,31) (NSML->bm, Chemical), was: 78.0, new conn weight: 5.0, appended weight is: 83.000000
>
> Existing connection at (17,34) (I4->M2L, Chemical), was: 1.0, new conn weight: 4.0, appended weight is: 5.000000
>
> Existing connection at (32,8) (M3R->g1AR, Chemical), was: 1.0, new conn weight: 1.5, appended weight is: 2.500000
>
> Existing connection at (6,14) (I5->M4, Chemical), was: 8.0, new conn weight: 18.5, appended weight is: 26.500000
>
> Existing connection at (6,30) (I5->NSMR, Chemical), was: 3.0, new conn weight: 17.5, appended weight is: 20.500000
>
> Existing connection at (37,16) (NSML->pm5VR, Chemical), was: 3.0, new conn weight: 7.0, appended weight is: 10.000000
>
> Existing connection at (37,38) (NSML->M3L, Chemical), was: 14.0, new conn weight: 6.5, appended weight is: 20.500000
>
> Existing connection at (6,16) (I5->pm5VR, Chemical), was: 8.0, new conn weight: 3.5, appended weight is: 11.500000
>
> Existing connection at (25,41) (I1R->I2R, Chemical), was: 5.0, new conn weight: 3.0, appended weight is: 8.000000
>
> Existing connection at (9,15) (M1->pm5D, Chemical), was: 3.0, new conn weight: 1.0, appended weight is: 4.000000
>
> Existing connection at (6,8) (I5->g1AR, Chemical), was: 4.0, new conn weight: 1.0, appended weight is: 5.000000
>
> Existing connection at (6,7) (I5->g1AL, Chemical), was: 7.0, new conn weight: 1.0, appended weight is: 8.000000
>
> Existing connection at (33,27) (I1L->I2L, Chemical), was: 10.0, new conn weight: 1.0, appended weight is: 11.000000
>
> Existing connection at (14,6) (M4->I5, Chemical), was: 1.0, new conn weight: 0.5, appended weight is: 1.500000
>
> Existing connection at (36,14) (I6->M4, Chemical), was: 3.0, new conn weight: 9.5, appended weight is: 12.500000
>
> Existing connection at (36,37) (I6->NSML, Chemical), was: 13.0, new conn weight: 8.0, appended weight is: 21.000000
>
> Existing connection at (35,16) (M2R->pm5VR, Chemical), was: 9.0, new conn weight: 3.0, appended weight is: 12.000000
>
> Existing connection at (34,7) (M2L->g1AL, Chemical), was: 2.0, new conn weight: 3.0, appended weight is: 5.000000
>
> Existing connection at (42,43) (MCL->mc2V, Chemical), was: 10.0, new conn weight: 2.5, appended weight is: 12.500000
>
> Existing connection at (9,23) (M1->I3, Chemical), was: 6.0, new conn weight: 1.0, appended weight is: 7.000000
>
> Existing connection at (9,27) (M1->I2L, Chemical), was: 2.0, new conn weight: 1.0, appended weight is: 3.000000
>
> Existing connection at (25,9) (I1R->M1, Chemical), was: 2.0, new conn weight: 1.0, appended weight is: 3.000000
>
> Existing connection at (25,23) (I1R->I3, Chemical), was: 5.0, new conn weight: 1.0, appended weight is: 6.000000
>
> Existing connection at (32,14) (M3R->M4, Chemical), was: 1.0, new conn weight: 1.0, appended weight is: 2.000000
>
> Existing connection at (36,30) (I6->NSMR, Chemical), was: 3.0, new conn weight: 1.0, appended weight is: 4.000000
>
> Existing connection at (36,15) (I6->pm5D, Chemical), was: 14.0, new conn weight: 1.0, appended weight is: 15.000000
>
> Existing connection at (14,17) (M4->I4, Chemical), was: 4.0, new conn weight: 0.5, appended weight is: 4.500000
>
> Existing connection at (9,19) (M1->g1P, Chemical), was: 4.0, new conn weight: 0.5, appended weight is: 4.500000
>
> Existing connection at (0,0) (M5->M5, GapJunction), was: 1.0, new conn weight: 1.0, appended weight is: 2.000000
>
> Existing connection at (14,14) (M4->M4, GapJunction), was: 1.0, new conn weight: 1.0, appended weight is: 2.000000
>
> Existing connection at (60,49) (mc1DR->pm4VR, GapJunction), was: 3.0, new conn weight: 3.0, appended weight is: 6.000000
>
> Existing connection at (49,60) (pm4VR->mc1DR, GapJunction), was: 3.0, new conn weight: 3.0, appended weight is: 6.000000


### Validation tests for [Cook2020DataReader](Cook2020_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 8 | Yes |
| I1R | I2L | 1 | Yes |
| RIPL | pm3VL | 4 | Yes |
| I5 | g1AR | 5 | Yes |
| I5 | g1AL | 8 | Yes |
| I6 | g1P | 2 | Yes |

Expected number of nonzero connection weights: **259** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| M4 | pm5VL | 1 | Yes |
| e2DR | e3D | 2 | Yes |
| g1AL | M3L | 2 | Yes |
| pm1 | pm2VL | 3 | Yes |
| mc1V | pm3VL | 3 | Yes |
| mc3V | pm7VL | 3 | Yes |
| mc3DR | pm8 | 3 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **246** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## Brittin2021

Data taken from: A multi-scale brain map derived from whole-brain volumetric reconstructions, 
Christopher A. Brittin, Steven J. Cook, David H. Hall, Scott W. Emmons & Netta Cohen, [Nature 591, 105–110, 2021](https://www.nature.com/articles/s41586-021-03284-x).

Supplementary data file 3 ([41586_2021_3284_MOESM5_ESM.xlsx](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03284-x/MediaObjects/41586_2021_3284_MOESM5_ESM.xlsx)) 
containing the M<sup>δ</sup>, C<sup>δ</sup> and G<sup>δ</sup> reference graphs was downloaded and used in the BrittinDataReader.

The M<sup>4</sup> graph is the example used in Connectome Toolbox. Values for the contact area/weights in tab M, with delta = 4 were used for this, and the values below were read from the spreadsheet.




### Validation tests for [BrittinDataReader](Brittin2021_data.md) 


#### Contact connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADAL | ADLL | 11319.5 | Yes |
| ADLL | ADAL | 11319.5 | Yes |
| ADLR | ADAR | 11319.5 | Yes |
| ADLR | ADAR | 11319.5 | Yes |
| ADAR | ADLR | 11319.5 | Yes |
| RID | RICL | 10043.5 | Yes |
| RICL | RID | 10043.5 | Yes |
| RICR | RID | 10043.5 | Yes |
| RIAR | SIBVR | 5114.25 | Yes |
| AQR | RIAL | 2010.75 | Yes |
| AQR | RIAR | 2010.75 | Yes |
| RIAR | AQR | 2010.75 | Yes |
| RIAL | AQR | 2010.75 | Yes |

Expected number of nonzero connection weights: **3850** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## WitvlietEtAl2021

Data on neuronal connectivity at different developmental stages of C. elegans from: Connectomes across development reveal principles of brain maturation
[Witvliet et al. Nature 2021](https://www.nature.com/articles/s41586-021-03778-8). 

While the paper's supplementary information contained connectivity matrices ([here](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03778-8/MediaObjects/41586_2021_3778_MOESM4_ESM.xlsx)), these only contain the chemical connections. 

The 8 spreadsheet files (witvliet_2020_1 L1.xlsx, witvliet_2020_2 L1.xlsx, ..., witvliet_2020_8 adult.xlsx) hosted on [WormWiring](https://wormwiring.org/pages/witvliet.html), also contain electrical connectivity, and are saved to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data), and used for the readers.

The chemical connection weights below were read from the supplementary information spreadsheet, and the electrical connection weights were taken from the WormWiring spreadsheet.





### Validation tests for [WitvlietDataReader1](Witvliet1_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AWAL | AWBL | 2 | Yes |
| AINR | AUAL | 2 | Yes |
| RIAL | RMDVR | 6 | Yes |

Expected number of nonzero connection weights: **775** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASHL | ADAL | 9 | Yes |
| RMDR | SMDVR | 1 | Yes |
| IL1R | IL1VR | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **164** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [WitvlietDataReader2](Witvliet2_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADLR | ASKR | 4 | Yes |
| AUAL | RIBL | 3 | Yes |
| AWBL | AIZL | 2 | Yes |

Expected number of nonzero connection weights: **986** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AVJR | RIS | 1 | Yes |
| OLLL | OLLR | 2 | Yes |
| RIH | RIR | 1 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **246** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [WitvlietDataReader3](Witvliet3_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADLR | ASKR | 4 | Yes |
| FLPR | FLPL | 3 | Yes |
| RIVL | GLRVR | 2 | Yes |

Expected number of nonzero connection weights: **1012** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| OLLR | RIGR | 1 | Yes |
| OLLL | OLLR | 2 | Yes |
| SMDDL | SMDDR | 1 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **186** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [WitvlietDataReader4](Witvliet4_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AWCR | AWCL | 5 | Yes |
| RIML | MDR04 | 2 | Yes |
| RIVL | MVR07 | 1 | Yes |

Expected number of nonzero connection weights: **1136** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ALML | AVDR | 2 | Yes |
| AVER | URYVL | 1 | Yes |
| SMDDL | SMDDR | 1 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **415** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [WitvlietDataReader5](Witvliet5_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADLR | ASHR | 3 | Yes |
| ALNR | SAAVR | 2 | Yes |
| BAGR | RIBL | 13 | Yes |

Expected number of nonzero connection weights: **1515** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADAR | ASHR | 2 | Yes |
| ADLL | CEPshVL | 1 | Yes |
| OLQVL | RIGL | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **578** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [WitvlietDataReader6](Witvliet6_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASER | ASEL | 1 | Yes |
| ASKR | AIAR | 18 | Yes |
| ALML | CEPVL | 3 | Yes |

Expected number of nonzero connection weights: **1525** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AIZR | AWCL | 2 | Yes |
| BAGR | RIR | 1 | Yes |
| DVA | OLQVL | 1 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **426** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [WitvlietDataReader7](Witvliet7_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| AQR | BAGR | 4 | Yes |
| ALNR | SAAVR | 11 | Yes |
| CEPDL | OLLL | 7 | Yes |

Expected number of nonzero connection weights: **2202** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADAL | PVQL | 2 | Yes |
| SIAVL | SMDVR | 1 | Yes |
| SAADL | SMBDL | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **576** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [WitvlietDataReader8](Witvliet8_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASER | AWCR | 9 | Yes |
| ALNL | SAAVL | 10 | Yes |
| ALML | BDUL | 9 | Yes |

Expected number of nonzero connection weights: **2186** (matches)

#### Electrical connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADFL | AIAL | 3 | Yes |
| AFDR | AIZR | 1 | Yes |
| PVT | RIBL | 2 | Yes |

Electrical synapse. Symmetric connectivity matrix: **True**

Expected number of nonzero connection weights: **612** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## RandiEtAl2023

Functional connectivity data of _C. elegans_ from: Randi et al. 2023, Neural signal propagation atlas of _Caenorhabditis elegans_, [Nature 623, 406–414 (2023)](https://doi.org/10.1038/s41586-023-06683-4).

We used the [WormNeuroAtlas package](https://github.com/francescorandi/wormneuroatlas) as discussed in the paper to provide the signal propagation map values. 
The method _get_signal_propagation_map()_ specifying the wildtype data (strain="wt") was used to get the post-stimulus calcium response amplitude (⟨ΔF/F₀⟩ₜ) matrix, while 
_get_signal_propagation_q()_ was used to get the q-values (the false discovery rate, i.e. the probability that a neuron pair declared "functionally connected" is actually a false positive). We used a q_max = 0.05 and just added that to the adjacency matrix used in this example.

We obtained the validation values below by calling the above functions and printing the value in the signal propagation for specific connections, checking q < 0.05. 


### Validation tests for [WormNeuroAtlasFuncReader](Randi2023_data.md) 


#### Functional connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASER | ASHL | 0 | Yes |
| I1L | MI | -0.12525142862743782 | Yes |
| MCR | M2R | 1.1917423178652604 | Yes |
| AVBR | AVEL | -0.14791430582009063 | Yes |
| AVEL | AVEL | 0 | Yes |

Expected number of nonzero connection weights: **1150** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## RipollSanchezEtAl2023

Data on neuropeptidergic signalling has been taken from: Ripoll-Sánchez et al. 2023, The neuropeptidergic connectome of C. elegans. [Neuron, Volume 111, Issue 22, 2023, Pages 3570-3589.e5](https://doi.org/10.1016/j.neuron.2023.09.043). 

There is a GitHub repository referenced in the paper: [https://github.com/LidiaRipollSanchez/Neuropeptide-Connectome](https://github.com/LidiaRipollSanchez/Neuropeptide-Connectome). 
There are 3 different models used for the neuropeptidergic connectome (short-, medium- and long-range), and the following files have been used in Connectome Toolbox as the source of these models:

- [01022024_neuropeptide_connectome_short_range_model.csv](https://github.com/LidiaRipollSanchez/Neuropeptide-Connectome/blob/main/Adjacency%20matrices%20for%20networks/01022024_neuropeptide_connectome_short_range_model.csv)
- [01022024_neuropeptide_connectome_mid_range_model.csv](https://github.com/LidiaRipollSanchez/Neuropeptide-Connectome/blob/main/Adjacency%20matrices%20for%20networks/01022024_neuropeptide_connectome_mid_range_model.csv)
- [01022024_neuropeptide_connectome_long_range_model.csv](https://github.com/LidiaRipollSanchez/Neuropeptide-Connectome/blob/main/Adjacency%20matrices%20for%20networks/01022024_neuropeptide_connectome_long_range_model.csv)

For each of these CSV files, the file was opened in Apple Numbers, and the weights (numbers of matched peptides expressed in pre cell with corresponding receptor in post cell) read off, to provide checks listed below. 


### Validation tests for [RipollSanchezShortRangeReader](RipollSanchezShortRange_data.md) 


#### Peptidergic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I3 | I5 | 3 | Yes |
| URBL | RMDDL | 4 | Yes |
| RIVR | HSNL | 6 | Yes |

Expected number of nonzero connection weights: **31417** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [RipollSanchezMidRangeReader](RipollSanchezMidRange_data.md) 


#### Peptidergic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| PVR | I3 | 6 | Yes |
| SABVL | VC1 | 1 | Yes |
| RIR | AVKR | 5 | Yes |

Expected number of nonzero connection weights: **40425** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [RipollSanchezLongRangeReader](RipollSanchezLongRange_data.md) 


#### Peptidergic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I3 | I5 | 3 | Yes |
| URBL | RMDDL | 4 | Yes |
| RIVR | HSNL | 6 | Yes |
| PVR | I3 | 6 | Yes |
| SABVL | VC1 | 1 | Yes |
| RIR | AVKR | 5 | Yes |
| VC4 | I4 | 1 | Yes |
| ALA | HSNR | 11 | Yes |

Expected number of nonzero connection weights: **53558** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## YimEtAl2024

Data on the dauer connectivity was obtained from the supplementary information of: Yim et al. 2024, Comparative connectomics of dauer reveals developmental plasticity
[Nature Communications, 15:1546](https://www.nature.com/articles/s41467-024-45943-3).

Supplementary Data 3 links to file [41467_2024_45943_MOESM6_ESM.xlsx](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-024-45943-3/MediaObjects/41467_2024_45943_MOESM6_ESM.xlsx).

This file has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/41467_2024_45943_MOESM6_ESM.xlsx).

#### Contactome based/non-normalised data

The spreadsheet above contained a sheet named "Dauer", from where the values for the contact area of connections were read. 
This file was opened in Excel and weights of selected connections were visually read from the cells, noting the pre and post cells and added to the connection test yaml file. 

### Normalised data

The spreadsheet above contained a sheet named "Dauer_normalized", from where the values for the "normalized" connections were read. 
This file was opened in Excel and weights of selected connections were visually read from the cells, noting the pre and post cells and added to the connection test yaml file. 


### Validation tests for [Yim2024NonNormDataReader](Yim2024NonNorm_data.md) 


#### Contact connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIH | CEPshDL | 7464.984227 | Yes |
| PVNL | ALMR | 97686.4 | Yes |
| URYDR | URADR | 33663.09403 | Yes |

Expected number of nonzero connection weights: **2198** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [Yim2024DataReader](Yim2024_data.md) 


#### Chemical synaptic connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ADFR | AFDR | 0.428024049927915 | Yes |
| SMBDL | RMED | 6.01978135910464 | Yes |
| ASHL | RIPL | 1.20804164634321 | Yes |

Expected number of nonzero connection weights: **2198** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



## WangEtAl2024

This reader combines neurotransmitter expression values from: Wang et al. 2024 (A neurotransmitter atlas of C. elegans males and hermaphrodites, [eLife 13:RP95402](https://doi.org/10.7554/eLife.95402.3)) with basic anatomical connectivity information from Cook et al. 2019, and monoaminergic receptor expression information from Bentley et al 2016.

[Supplementary file 2](https://cdn.elifesciences.org/articles/95402/elife-95402-supp2-v1.xlsx) in that publication contains the expression patterns of neurotransmitter pathway genes in hermaphrodites.
    
This has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/elife-95402-supp2-v1.xlsx). 


[Supplementary file 3](https://cdn.elifesciences.org/articles/95402/elife-95402-supp3-v1.xlsx) contains the expression patterns of neurotransmitter pathway genes in male-specific neurons.

This has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/elife-95402-supp3-v1.xlsx).

These files were used to identify potential presynaptic cells for each neurotransmitter, and then validation tests were added towards known connected anatomical (or monoaminergic) postsynaptic targets of these. 

    


### Validation tests for [Wang2024HermReader](Wang2024Herm_data.md) 


#### Acetylcholine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 1 | Yes |
| SMBDL | SDQR | 1 | Yes |
| VC2 | PVT | 1 | Yes |
| DB4 | MDL13 | 1 | Yes |
| M1 | g1P | 1 | Yes |

Expected number of nonzero connection weights: **2756** (matches)

Expected total weight of connections: **2756** (matches)

#### Glutamate connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIMR | MDL05 | 1 | Yes |
| PHBR | AVAR | 1 | Yes |
| URYDL | OLQDL | 1 | Yes |
| PVR | IL1DR | 1 | Yes |

Expected number of nonzero connection weights: **1334** (matches)

Expected total weight of connections: **1334** (matches)

#### Betaine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASIL | AIBL | 1 | Yes |
| NSMR | pm5VR | 1 | Yes |
| RIR | AQR | 1 | Yes |

Expected number of nonzero connection weights: **150** (matches)

Expected total weight of connections: **150** (matches)

#### GABA connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIBL | CEPVL | 1 | Yes |
| VD10 | MVR20 | 1 | Yes |
| SMDDL | SIBDL | 1 | Yes |

Expected number of nonzero connection weights: **506** (matches)

Expected total weight of connections: **506** (matches)

#### Dopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| CEPVL | AIMR | 1 | Yes |
| PDEL | RICR | 1 | Yes |
| ADEL | DD4 | 1 | Yes |

Expected number of nonzero connection weights: **1176** (matches)

Expected total weight of connections: **1176** (matches)

#### Serotonin connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| HSNL | PVQL | 1 | Yes |
| NSML | VD3 | 1 | Yes |
| ADFR | RID | 1 | Yes |

Expected number of nonzero connection weights: **492** (matches)

Expected total weight of connections: **492** (matches)

#### Tyramine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIMR | RMEV | 1 | Yes |
| RIMR | SIADL | 1 | Yes |
| RIML | VD5 | 1 | Yes |

Expected number of nonzero connection weights: **228** (matches)

Expected total weight of connections: **228** (matches)

#### Octopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RICR | ASIL | 1 | Yes |
| RICL | SIAVR | 1 | Yes |
| RICL | PVQL | 1 | Yes |

Expected number of nonzero connection weights: **56** (matches)

Expected total weight of connections: **56** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_




### Validation tests for [Wang2024MaleReader](Wang2024Male_data.md) 


#### Acetylcholine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| I1R | I2R | 1 | Yes |
| SMBDL | SDQR | 1 | Yes |
| VC2 | PVT | 1 | Yes |
| DB4 | MDL13 | 1 | Yes |
| M1 | g1P | 1 | Yes |

Expected number of nonzero connection weights: **3889** (matches)

Expected total weight of connections: **3889** (matches)

#### Glutamate connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIMR | MDL05 | 1 | Yes |
| CP05 | AVG | 1 | Yes |
| R9AL | HOB | 1 | Yes |

Expected number of nonzero connection weights: **1722** (matches)

Expected total weight of connections: **1722** (matches)

#### Betaine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| ASIL | AIBL | 1 | Yes |
| NSMR | pm5VR | 1 | Yes |
| RIR | AQR | 1 | Yes |

Expected number of nonzero connection weights: **150** (matches)

Expected total weight of connections: **150** (matches)

#### GABA connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIBL | CEPVL | 1 | Yes |
| VD10 | MVR20 | 1 | Yes |
| SMDDL | SIBDL | 1 | Yes |

Expected number of nonzero connection weights: **691** (matches)

Expected total weight of connections: **691** (matches)

#### Dopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| CEPVL | AIMR | 1 | Yes |
| PDEL | RICR | 1 | Yes |
| ADEL | DD4 | 1 | Yes |

Expected number of nonzero connection weights: **1176** (matches)

Expected total weight of connections: **1176** (matches)

#### Serotonin connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| HSNL | PVQL | 1 | Yes |
| NSML | VD3 | 1 | Yes |
| ADFR | RID | 1 | Yes |

Expected number of nonzero connection weights: **492** (matches)

Expected total weight of connections: **492** (matches)

#### Tyramine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RIMR | RMEV | 1 | Yes |
| RIMR | SIADL | 1 | Yes |
| RIML | VD5 | 1 | Yes |

Expected number of nonzero connection weights: **228** (matches)

Expected total weight of connections: **228** (matches)

#### Octopamine connections

| Pre      | Post | Expected weight | Match |
|----------|------|-----------------|-------|
| RICR | ASIL | 1 | Yes |
| RICL | SIAVR | 1 | Yes |
| RICL | PVQL | 1 | Yes |

Expected number of nonzero connection weights: **56** (matches)

Expected total weight of connections: **56** (matches)

_Validation **PASSED** on 2026-08-18 with cect v0.3.3_



