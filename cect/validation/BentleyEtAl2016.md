Data from: The Multilayer Connectome of Caenorhabditis elegans, Bentley et al. 2016, [PLoS Comput Biol 12(12): e1005283](https://doi.org/10.1371/journal.pcbi.1005283)

Connectivity was originally released in supplementary information: [S1 Dataset](https://doi.org/10.1371/journal.pcbi.1005283.s004) ("Included are edge lists for monoamine and neuropeptide networks").

The contents of this zip file were extracted and the 2 files [edge_lists/edgelist_MA.csv](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/edgelist_MA.csv) and [edge_lists/edgelist_NP.csv](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/edgelist_NP.csv) were added to our repository and used in the monoaminergic and peptidergic DataReaders respectively. 

For the validation tests below, specific connections between pre and postsynaptic cells were read out from the edgelist_MA.csv and edgelist_NP.csv files above and a weight of 1 was added to the connection test YAML file for these. 
