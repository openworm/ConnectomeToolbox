Data on the dauer connectivity, comprising both directed synaptic connections and contact area matrices, was obtained from the supplementary information of:
[Nature Communications, 15:1546](https://www.nature.com/articles/s41467-024-45943-3).

Two distinct types of connection information are used from this paper:

A) **Synaptic connectivity** (Supplementary Data 3). A directed matrix, with rows presynaptic and columns postsynaptic. Presynaptic active zones were detected by a convolutional neural network, reconstructed in 3D and proofread; postsynaptic partners and each partner's share of an active zone were assigned by simulating neurotransmitter diffusion. Weights are the summed volume (nm³) of active zone material attributed to a pre/post pair.

B) **Contact area** (Supplementary Data 6). A symmetric matrix, as physical apposition has no pre/post polarity, measured from the volumetric segmentation rather than from synapses. Weights are the summed area (nm²) of contact between two cells.

Both are available as raw values and normalised by the standard deviation of weights excluding the top 5th percentile, the latter easing comparison with other datasets. 

Supplementary Data 3 in the paper links to file [41467_2024_45943_MOESM6_ESM.xlsx](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-024-45943-3/MediaObjects/41467_2024_45943_MOESM6_ESM.xlsx). This file has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/41467_2024_45943_MOESM6_ESM.xlsx).

Supplementary Data 6 in the paper links to file [41467_2024_45943_MOESM9_ESM.xlsx](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-024-45943-3/MediaObjects/41467_2024_45943_MOESM9_ESM.xlsx). This file has been added to our repository [here](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/data/41467_2024_45943_MOESM9_ESM.xlsx).


Both of the Supplementary Data 3 & 6 spreadsheets contained sheets named "Dauer" and one named "Dauer_normalized", from where the values for the non normalized/normalized (respectively) synaptic weights/contact areas of connections were read.

Each file was opened in Excel and weights of selected connections were visually read from the spreadsheet cells, noting the pre and post cells, and the values were added to the connection test yaml file for validation below. 

