# -*- coding: utf-8 -*-

############################################################

#    A script to read NeuroML files containing C. elegans based connectomes.

############################################################


from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT
from cect import print_
from cect.NeuroMLDataReader import NeuroMLDataReader

import os

file_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
filename = "%sWorm2D.net.nml" % file_location

READER_DESCRIPTION = """Data extracted from a NeuroML file based on <b><a href="https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2021.572339/full">Olivares et al. 2021</a></b>"""


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``NeuroMLDataReader`` to load data from the NeuroML model

    Returns:
        NeuroMLDataReader: The initialised connectome reader
    """
    if (
        from_cache and False
    ):  ####################################################################################################### TODO Remove!
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[1]))
    else:
        return NeuroMLDataReader(filename)


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


if __name__ == "__main__":
    tdr_instance = get_instance()
    cells, neuron_conns = tdr_instance.read_data()

    neurons2muscles, muscles, muscle_conns = tdr_instance.read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    print(tdr_instance.summary())

    """
    
    from cect.ConnectomeView import NEURONS_VIEW as view
    from cect.ConnectomeView import COOK_FIG3_VIEW as 
    from cect.ConnectomeView import LOCOMOTION_3_VIEW as view
    from cect.ConnectomeView import LOCOMOTION_1_VIEW as view
    """
    # from cect.ConnectomeView import SOCIAL_VIEW as view
    # from cect.ConnectomeView import LOCOMOTION_2_VIEW as view
    from cect.ConnectomeView import RAW_VIEW as view

    cds2 = tdr_instance.get_connectome_view(view)

    print(cds2.summary())

    # fig = cds2.to_plotly_hive_plot_fig(list(view.synclass_sets.keys())[0], view)

    fig = cds2.to_plotly_graph_fig(list(view.synclass_sets.keys())[0], view)
    """

    fig, _ = cds2.to_plotly_matrix_fig(
        list(view.synclass_sets.keys())[2],
        view,
    )
   """
    import plotly.io as pio

    pio.renderers.default = "browser"
    import sys

    if "-nogui" not in sys.argv:
        fig.show()
