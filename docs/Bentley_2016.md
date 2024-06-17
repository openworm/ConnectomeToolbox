## The Multilayer Connectome of Caenorhabditis elegans
*Barry Bentley, Robyn Branicky, Christopher L. Barnes, Yee Lian Chew, Eviatar Yemini, Edward T. Bullmore, Petra E. Vértes , William R. Schafer* <br> *Published: December 16, 2016* <br>*Citation: Bentley B, Branicky R, Barnes CL, Chew YL, Yemini E, Bullmore ET, et al. (2016) The Multilayer Connectome of Caenorhabditis elegans. PLoS Comput Biol 12(12): e1005283. https://doi.org/10.1371/journal.pcbi.1005283*


**Abstract:**
- Extrasynaptic modulation (monoamines and peptides) influence neural circuits
- This paper presents a draft monoamine connectome and a partial neuropeptide connectome, based on new and published expression data for biosynthetic genes and receptors

**Introduction**
- A full understanding of neural connectivity requires a detailed mapping of these extrasynaptic pathways
- Monoaminergic systems play diverse roles in regulating behaviour and so extrasynaptic monoamine interactions must also be mapped, not just the network of wired chemical synapses and gap junctions
- Neuropeptides are widely used as neuromodulators in the C.elegans nervous system, with over 250 known or predicted neuropeptides from at least 122 precursor genes and over 100 putative peptide receptors

**Materials & Methods**
- Full hermaphrodite C.elegans connectome, containing all 302 neurons
- Network was composed from somatic connectome of White et al, updates and released by Chklovskii lab
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1001066
  - https://www.pnas.org/doi/full/10.1073/pnas.0506806103
- Pharyngeal network of Albertson and Thomson made available by the Cybernetic C.elegans Program
  - (CCeP:http://ims.dse.ibaraki.ac.jp/ccep/)
- Functional classifications referred (i.e. sensory neuron, interneuron, motor neuron) are based on the classification scheme used in WormAtlas

**Monoamine network construction**
- A literature search was performed to identify genes known to be receptors, transporters or synthetic enzymes of monoamines
- A further search was performed to collect cell-level expression data for the monoamine associated genes identified in the previous step
- Search was assisted with WormBase databases and WormWeb (http://www.wormbase.org/)
- Neurons expressing multiple receptors for a single monoamine receive a single edge from each sending neuron
- Reciprocal connections between nodes are considered as 2 separate unidirectional connections

**Neuropeptide network construction**
- Constructed from published expression data for peptides and receptors using similar methods for the monoamines
- Only those systems were included for which sufficient expression and ligand-receptor interaction data in the literature (biologically plausible EC50 values)
- 15 neuropeptides and 12 receptors were matched and included
