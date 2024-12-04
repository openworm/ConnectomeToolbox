## Connectomes across development reveal principles of brain maturation
_Witvliet, D., Mulcahy, B., Mitchell, J.K. et al_<br>
*[Nature 596, 257–261](https://www.nature.com/articles/s41586-021-03778-8)*<br>
_Published: 4 August 2021_


!!! example "Datasets incorporated"     

    - **[Witvliet 1](Witvliet1_data.md)**
    - **[Witvliet 2](Witvliet2_data.md)**
    - **[Witvliet3](Witvliet3_data.md)** 
    - **[Witvliet 4](Witvliet4_data.md)** 
    - **[Witvliet 5](Witvliet5_data.md)** 
    - **[Witvliet 6](Witvliet6_data.md)** 
    - **[Witvliet7](Witvliet7_data.md)** 
    - **[Witvliet8](Witvliet8_data.md)**


!!! warning "Resources from publication"   

    - **[NemaNode](Resources.md#nemanode)**

**Data**

- Eight isogenic _C.elegans_ from L1 to adult
  - three L1, two L2, and one L3 worm to capture continuous connectomic changes
- Reconstructed two adults to make direct comparisons between animals of the same age and the original published connectome ([White et al. 1986](White_1986.md)).

**Brain reconstruction**

- Brain was defined as the nerve ring, ventral ganglion and neuropil anterior of the ventral sub-lateral commissures.
- Every neuron, glia and muscle was annotated for chemical synapses to generate a connectome of the brain.
- Gap junctions were partially annotated and excluded from analyses.
- Chemical synapse weight was assessed by both the number and size of synapses.

**Connection classification**

- 3,113 connections (averaging 1,292 per dataset) were assigned as stable, variable or developmentally dynamic.
- 1,647 connections (averaging 323 per dataset) had no more than two synapses in two or more datasets and were left-right asymmetric. (classed as variable).
- 1,466 connections were pooled by left-right pairs, resulting in 658 pair connections.

**Comparison with original dataset**

- As observed in the original dataset, some variability in cell body position and neurite trajectory was observed.
- Every cell was unambiguously identified in every dataset because combined anatomical features and neighbourhood for each cell is unique.
- Because individual muscles were not traced in the original, they complete this dataset by tracing through all head muscles using the EM hosted by [WormAtlas](Resources.md#wormatlas).
- Individual muscle arms were identified by their characteristic location within the brain, which were confirmed by tracing their arms back to their cell body in several datasets.

**Minimally corrected dataset (N2U, Cook et al., 2019)**

- WormAtlas hosts a wiring of N2U connectome from [Cook et al. 2019](Cook_2019.md).
- They noted errors in muscle identification and synapse annotation in this reannotation
  - corrected identity of muscle pairs (VL1-VL2, VR1-VR2, DL2-DL3, DR2-DR3, DL5-DL6, DR5-DR6, VL5-VL6, VR5-VR6)
  - muscles were not traced at all in the brain, and only one of more than 50 synapses onto muscle VR2 was annotated

**Limitations**

- Didn't include gap junctions
- Improvement in sample preparation and analysis are needed to reach the same level of confidence and throughput as they reached for chemical synaptic networks throughout development
- Analysed only one connectome at most time points
    - could not assess animal-to-animal variability at each age 