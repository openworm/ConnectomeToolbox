## Structural Properties of the Caenorhabditis elegans Neuronal Network
_Lav R. Varshney, Beth L. Chen, Eric Paniagua, David H. Hall, Dmitri B. Chklovskii_<br>
*[PLOS Computational Biology 7(2): e1001066](https://doi.org/10.1371/journal.pcbi.1001066)*<br>
_Published: February 3, 2011_


!!! example "Datasets incorporated"   

    - **[Varshney_2011](Varshney_data.md)**

!!! warning "Resources from publication"   

    - **[MATLAB code for analysing dataset](https://github.com/lrvarshney/elegans)**

**Data Acquisition**

- Assembled wiring diagram by consolidating existing data from both published and unpublished sources

[White et al. 1986](White_1986.md) The Mind of a Worm (MOW) was the starting point

  - Extracted wiring data from diagrams, figures, tables and text
  - Connectivity of each neuron, its synaptic partners, and synaptic type was manually entered into an electronic database
  - In the ventral cord, determining this level of synaptic specification was complicated by the fact that connections were recorded by neuron class
  - Assigned proper connections to the appropriate left/right neuron by referring to White and co-worker's original laboratory notebooks and original EMs

[Durbin 1987](Durbin_1987.md) - the anterior portion of the worm

- Anterior connections needed an update as MOW did not specify the location of synapses, integration proved difficult.
- For these neurons, they obtained positional information by cross-referencing Durbin's data against original EMs and his handwritten annotations in White's laboratory notebooks.
- Only synapses located in regions addressed by Durbin were included.
- Connections in the middle and tail region of the worm were mostly unaffected by these updates.

**Differences in data and gaps**

- Hobert O and Hall DH, unpublished - differences between GFP neurons and White's work have been observed
    - anterior processes of DVB and PVT could have been mistakenly switched in MOW
    - so they reversed the connections for neurons DVB and PVT anterior to the vulva
- Reconstructions of neurons in the mid-body of the worm are incomplete
- From a combination of these published works
    - White et al 1986
    - Durbin RM 1987
    - Hall DH, Russel RL 1991
    - White et al 1976
- Wiring data for 64 neurons had large gaps or were missing entirely
    - 61 of these were motor neurons in the ventral cord
  - 2 were excretory neurons (CANL/R) that do not appear to make any synapses
    - RID is the only process in the dorsal cord that extends over the length of the animal
 
**Updates to previous data**

- Using White et al. laboratory notebooks, they identified notes for full reconstructions of 24 of the aforementioned neurons
- Partial connectivity data for the remaining 38 were also available where 22 neurons have partial/missing dorsal side connections and 6 neurons have partial ventral side connections
- 600 updates were made to the original notes and published reconstructions
    - additions of previously missed NMJs between ventral cord motor neurons and body wall muscles
- Large section on the dorsal side of the worm was never EM at high power magnification
    - produced new high power EMs of this dorsal region
    - 3 neurons (DA5, DB4, DD3) were obtained from these EMs
    - resource constraints prevented them from covering the entire dorsal gap
- reconciliation of discrepancies
    - 561 synapses for 108 neurons (49% chemical "sends", 31% chemical "receives" and 20% for electrical junctions)     
