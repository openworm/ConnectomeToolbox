An updated version of the White et al. 1986 wiring data, as presented in Varshney et al. 2011, Structural Properties of the Caenorhabditis elegans Neuronal Network. [PLOS Computational Biology 7(2): e1001066](https://doi.org/10.1371/journal.pcbi.1001066).

The file [NeuronConnect.xls](https://www.wormatlas.org/images/NeuronConnect.xls), referenced in the paper ("The collected data is available from the WormAtlas"), which is also available [here](https://wormwiring.org/), has been copied into our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/NeuronConnect.xls), and used in our DataReader.

The spreadsheet above contained a single sheet, with a list of presynaptic cells, postsynaptic cells, synapse numbers, and types of synapse (S, Sp, R, Rp, EJ, NMJ). See [here](https://www.wormatlas.org/neuronalwiring.html#Connectivitydata) for full details. This file was opened in Excel and weights of selected connections were visually read from the cells (summing entries for S and Sp where both were present), noting the pre and post cells and added to the connection test YAML file. 

