## The Multilayer Connectome of _Caenorhabditis elegans_

*Barry Bentley, Robyn Branicky, Christopher L. Barnes, Yee Lian Chew, Eviatar Yemini, Edward T. Bullmore, Petra E. Vértes , William R. Schafer* <br>*[PLoS Comput Biol 12(12): e1005283](https://doi.org/10.1371/journal.pcbi.1005283)*<br> *Published: December 16, 2016* 


!!! example "Datasets incorporated"     

    - **[Bentley et al. 2016 Monoaminergic](Bentley2016_MA_data_graph.md)**
    - **[Bentley et al. 2016 Peptidergic](Bentley2016_PEP_data_graph.md)**

**Abstract:**

- Extrasynaptic modulation (monoamines and peptides) influence neural circuits.
- This paper presents a draft monoamine connectome and a partial neuropeptide connectome, based on new and published expression data for biosynthetic genes and receptors.

**Introduction**

- A full understanding of neural connectivity requires a detailed mapping of these extrasynaptic pathways.
- Monoaminergic systems play diverse roles in regulating behaviour and so extrasynaptic monoamine interactions must also be mapped, not just the network of wired chemical synapses and gap junctions.
- Neuropeptides are widely used as neuromodulators in the _C. elegans_ nervous system, with over 250 known or predicted neuropeptides from at least 122 precursor genes and over 100 putative peptide receptors.

**Materials & Methods**

- Full hermaphrodite _C. elegans_ connectome, containing all 302 neurons.
- Network was composed from somatic connectome of [White et al. 1986](White_1986.md), updates and released by Chklovskii lab ([Varshney et al. 2011](Varshney_2011.md)).
- Pharyngeal network of [Albertson & Thomson 1976](Albertson_1976.md) made available by the Cybernetic _C. elegans_s Program [CCeP](http://ims.dse.ibaraki.ac.jp/ccep/).
- Functional classifications referred (i.e. sensory neuron, interneuron, motor neuron) are based on the classification scheme used in [WormAtlas](Resources.md#wormatlas).

**Monoamine network construction**

- A literature search was performed to identify genes known to be receptors, transporters or synthetic enzymes of monoamines
- A further search was performed to collect cell-level expression data for the monoamine associated genes identified in the previous step.
- Search was assisted with the [WormBase](Resources.md#wormbase) databases and [WormWeb](Resources.md#wormweb). 
- Neurons expressing multiple receptors for a single monoamine receive a single edge from each sending neuron.
- Reciprocal connections between nodes are considered as 2 separate unidirectional connections.

**Neuropeptide network construction**

- Constructed from published expression data for peptides and receptors using similar methods for the monoamines.
- Only those systems were included for which sufficient expression and ligand-receptor interaction data in the literature (biologically plausible EC50 values).
- 15 neuropeptides and 12 receptors were matched and included.
