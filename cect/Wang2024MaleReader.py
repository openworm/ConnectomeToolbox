# -*- coding: utf-8 -*-

############################################################

#    A script to read the neurotransmitter atlas values from Wang et al. 2024.

############################################################


from cect.Wang2024Reader import Wang2024Reader
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

from cect.ConnectomeReader import analyse_connections
from cect import print_

import os
import pprint as pp


READER_DESCRIPTION = "???"


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[1]))
    else:
        global READER_DESCRIPTION
        inst = Wang2024Reader(sex="Male")
        READER_DESCRIPTION = inst.reader_description
        return inst


def main():
    tdr_instance = get_instance(from_cache=False)

    print(tdr_instance.summary(list_pre_cells=True))
    print(tdr_instance.reader_description)
    quit()

    pp.pprint(tdr_instance.all_neurotransmitters)
    quit()

    cells, neuron_conns = tdr_instance.read_data()

    neurons2muscles, muscles, muscle_conns = tdr_instance.read_muscle_data()

    analyse_connections(
        cells,
        neuron_conns,
        neurons2muscles,
        muscles,
        muscle_conns,
        print_details_on=["ADFL"],
    )

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    """
    
    from cect.ConnectomeView import COOK_FIG3_VIEW as 
    from cect.ConnectomeView import LOCOMOTION_3_VIEW as view
    from cect.ConnectomeView import LOCOMOTION_1_VIEW as view
    """
    # from cect.ConnectomeView import SOCIAL_VIEW as view
    # from cect.ConnectomeView import LOCOMOTION_2_VIEW as view
    from cect.ConnectomeView import RAW_VIEW as view
    # from cect.ConnectomeView import NEURONS_VIEW as view

    cds2 = tdr_instance.get_connectome_view(view)

    print(cds2.summary(list_pre_cells=True))

    # fig = cds2.to_plotly_hive_plot_fig(list(view.synclass_sets.keys())[0], view)

    """
    fig = cds2.to_plotly_graph_fig(list(view.synclass_sets.keys())[0], view)
    """

    from cect.Cells import GLUTAMATE

    fig, _ = cds2.to_plotly_matrix_fig(
        GLUTAMATE,
        view,
    )
    import plotly.io as pio

    pio.renderers.default = "browser"
    import sys

    if "-nogui" not in sys.argv:
        fig.show()


if __name__ == "__main__":
    main()
