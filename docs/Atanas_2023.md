## Brain-wide representations of behavior spanning multiple timescales and states in C. elegans
_Adam A. Atanas, Jungsoo Kim, Ziyu Wang, Eric Bueno, McCoy Becker, Di Kang, Jungyeon Park, Talya S. Kramer, Flossie K. Wan, Saba Baskoylu, Ugur Dag, Elpiniki Kalogeropoulou, Matthew A. Gomes, Cassi Estrem, Netta Cohen, Vikash K. Mansinghka, and Steven W. Flavell_ 

_Cell, Volume 186, Issue 19, 2023, Pages 4134-4151.e31, ISSN 0092-8674_ <br> _Published: September 14, 2023 https://doi.org/10.1016/j.cell.2023.07.035_

- For quantitative analaysis, the two adult datasets from Witvliet et al were averaged. (https://www.nature.com/articles/s41586-021-03778-8)
- Self looping and single synapse edges were excluded
- For the pharyngeal circuit analysis, the connectome from the original White et al was used as the Witvliet connectome only covers the head ganglion.
- For the 2D embedding of the connectome (the sensorimotor layer and the graph eigenvector; see below), the White et al connectome was used to replicate the embedding previouslt used in the field.

**_2D embedding of the connectome_**
- The 2D embedding of connectome as performed by determining the sensorimotor layer (referred to as processing depth in the original paper) for each neuron and the 2nd eigenvector of the Laplacian of the graph. See Varshney et al for the exact methods in determining those values.

- Need to add new datasets from www.WormWideWeb.org
