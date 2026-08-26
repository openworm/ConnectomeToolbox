# -*- coding: utf-8 -*-

############################################################

#    A script to read the values of Yim et al. 2024

############################################################

from cect.readers.Yim2024DataReader import Yim2024DataReader
from cect.readers.Yim2024DataReader import CONTACTOME_FILENAME

from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

from cect.Neurotransmitters import CONTACTOME_SYN_CLASS

import os

from cect import print_


NAME = "Yim2024Contactome"

DATASET_DESCRIPTION_0 = """Reconstruction of the contactome of the dauer, a distinct developmental stage of _C. elegans_, contains a symmetric matrix measuring physical contact between pre/post cells. Every cell in the reconstructed EM volume was traced voxel by voxel; these labelled cells were then expanded until the extracellular gaps between them closed, and the area of each resulting point of contact summed. """

DATASET_DESCRIPTION = (
    DATASET_DESCRIPTION_0
    + """This connectome dataset contains normalized contact areas/weights to ease comparison to other datasets."""
)

WEIGHTS_0 = (
    "Weights are the total contact area (nm<sup>2</sup>) between a pair of cells. "
)
WEIGHTS = (
    WEIGHTS_0
    + "In this dataset, these are normalized by the standard deviation of connection weights without the top 5th percentile to remove the bias due to the big outliers"
)


READER_DESCRIPTION = (
    """Data extracted from %s, Yim et al. 2024 Dauer connectome **(Contactome; Normalized)**"""
    % get_dataset_source_on_github(CONTACTOME_FILENAME.split("/")[-1])
)


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``Yim2024DataReader`` to load data on dauer connectome

    Returns:
        (Yim2024DataReader): The initialised connectome reader
    """
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(
            get_cache_filename(__file__.split("/")[-1].split(".")[0])
        )
    else:
        return Yim2024DataReader(normalized=True, conn_filename=CONTACTOME_FILENAME)


def main():
    tdr_instance = get_instance(from_cache=False)

    # analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    print(tdr_instance.summary())

    from cect.ConnectomeView import RAW_VIEW as view
    # from cect.ConnectomeView import PHARYNX_VIEW as view
    # from cect.ConnectomeView import NEURONS_VIEW as view

    print("=======================")
    cds2 = tdr_instance.get_connectome_view(view)
    print(cds2.summary(list_pre_cells=False))

    print("Plotting view: %s" % view)
    fig, _ = cds2.to_plotly_matrix_fig(
        CONTACTOME_SYN_CLASS,
        view,
    )
    import plotly.io as pio

    pio.renderers.default = "browser"
    import sys

    if "-nogui" not in sys.argv:
        fig.show()


if __name__ == "__main__":
    main()
