Data from White et al. 1986, The Structure of the Nervous System of the Nematode Caenorhabditis elegans, [Phil. Trans. R. Soc. Lond. B3141–340](https://royalsocietypublishing.org/doi/10.1098/rstb.1986.0056) (also on [WormAtlas](https://wormatlas.org/MoW_built0.92/MoW.html)).

As described on [WormAtlas](https://www.wormatlas.org/neuronalwiring.html), the primary structured dataset describing this connectivity is the **neurodata.txt** file which was compiled by Richard Durbin in his thesis (Studies on the Development and Organisation of the Nervous System of Caenorhabditis elegans.
University of Cambridge; 1987). This (and the [Readme](https://www.wormatlas.org/neurodata_readme.txt) describing it) can be found [on WormAtlas](https://www.wormatlas.org/neurodata.txt). 

The **neurodata.txt** file describes reconstructed connectivity for 2 animals: an N2U (adult hermaphrodite) and JSH (which Durbin described as an L4 male, it is now believed that this animal was an L4 hermaphrodite). This file has been copied into our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/neurodata.txt).

We noted however a small number of minor issues (described below) that were found in the original data file. 
These updates were incorporated in cect by using an updated version of this file (**neurodata_updated.txt**, in our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/neurodata_updated.txt)), as opposed to being fixed in the source of our Python reader (DurbinDataReader), for clarity. 
The issues are: 

**Issue 1)** Line 2 in the original file (ADAL ADAR Gap_junction 1) was missing JSH or N2U, and so assuming N2U as "ADAL ADAR Gap_junction JSH 2" was already present.

**Issue 2)** While most gap junction connections contained both A->B and B->A connections, some were missing the reverse connection. The missing connections have been included at the top of the updated file.

**Issue 3)** One gap junction connection had a different weight for the A->B and B->A connections (RIML<->AVAR). Updated the weight to be the same for both directions, using the larger of the two weights.

This file is the source of two of our readers below, **DurbinJSHDataReader** and **DurbinN2UDataReader**. A third, **White_whole**, is effectively the same as the Varshney et al. 2011 dataset (**VarshneyDataReader**), apart from also containing the connections to/from the pharynx. See the **VarshneyDataReader** description for how that dataset builds on the JSH and N2U data. 

This **White_whole** dataset was obtained from a file in the WormNeuroAtlas source code ([here](https://github.com/francescorandi/wormneuroatlas/blob/main/wormneuroatlas/data/aconnectome_white_1986_whole.csv)), and copied to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/aconnectome_white_1986_whole.csv).

Note: this dataset contained 3 electrical connections not present in the Varshney dataset: PLML <-> BDUL, PLMR <-> BDUR, RID <-> RID, all of weight 1.
