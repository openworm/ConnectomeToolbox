# -*- coding: utf-8 -*-

############################################################

#    A script to read the values of Yim et al. 2024

############################################################

from cect.readers.Yim2024DataReader import Yim2024DataReader
from cect.readers.Yim2024DataReader import CONTACTOME_FILENAME
from cect.readers.Yim2024ContactomeDataReader import DATASET_DESCRIPTION_0
from cect.readers.Yim2024ContactomeDataReader import WEIGHTS_0

from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

from cect.Neurotransmitters import CONTACTOME_SYN_CLASS

import os

from cect import print_


NAME = "Yim2024ContactomeNonNorm"

DATASET_DESCRIPTION = DATASET_DESCRIPTION_0
WEIGHTS = WEIGHTS_0


READER_DESCRIPTION = (
    """Data extracted from %s, Yim et al. 2024 Dauer connectome **(Contactome; Non-normalized)**"""
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
        return Yim2024DataReader(normalized=False, conn_filename=CONTACTOME_FILENAME)


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
