## Brain-wide representations of behavior spanning multiple timescales and states in C. elegans
_Adam A. Atanas, Jungsoo Kim, Ziyu Wang, Eric Bueno, McCoy Becker, Di Kang, Jungyeon Park, Talya S. Kramer, Flossie K. Wan, Saba Baskoylu, Ugur Dag, Elpiniki Kalogeropoulou, Matthew A. Gomes, Cassi Estrem, Netta Cohen, Vikash K. Mansinghka, and Steven W. Flavell_ <br>
_[Cell, Volume 186, Issue 19, 2023, Pages 4134-4151.e31, ISSN 0092-8674]( https://doi.org/10.1016/j.cell.2023.07.035)_ <br> _Published: September 14, 2023_


!!! warning "Resources from publication"   

    - **[WormWideWeb](Resources.md#wormwideweb)**

- For quantitative analysis, the two adult datasets from [Witvliet et al. 2021](Witvliet_2021.md) were averaged.
- Self looping and single synapse edges were excluded.
- For the pharyngeal circuit analysis, the connectome from the original [White et al. 1986](White_1986.md) was used as the Witvliet connectome only covers the head ganglion.
- For the 2D embedding of the connectome (the sensorimotor layer and the graph eigenvector; see below), the [White et al. 1986](White_1986.md) connectome was used to replicate the embedding previously used in the field.

**_2D embedding of the connectome_**

- The 2D embedding of connectome as performed by determining the sensorimotor layer (referred to as processing depth in the original paper) for each neuron and the 2nd eigenvector of the Laplacian of the graph. See [Varshney et al. 2011](Varshney_2011.md) for the exact methods in determining those values.

