############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

from cect.WormNeuroAtlasExtSynReader import WormNeuroAtlasExtSynReader
from cect.Cells import MONOAMINERGIC_SYN_GENERAL_CLASS
from cect.Cells import DOPAMINE
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

import logging
import sys


LOGGER = logging.getLogger(__name__)

READER_DESCRIPTION = """Data on monoaminergic connectivity from the <b><a href="https://github.com/francescorandi/wormneuroatlas">WormNeuroAtlas package</a></b>"""


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WormNeuroAtlasExtSynReader`` to load data on monoaminergic connectivity using the **[WormNeuroAtlas package](https://github.com/francescorandi/wormneuroatlas)**

    Returns:
        WormNeuroAtlasExtSynReader: The initialised connectome reader
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
        return WormNeuroAtlasExtSynReader(MONOAMINERGIC_SYN_GENERAL_CLASS)


if __name__ == "__main__":
    my_instance = get_instance(from_cache=False)
    cells, neuron_conns = my_instance._read_data()
    print("Loaded %s connections" % len(neuron_conns))

    # from cect.ConnectomeReader import analyse_connections
    # analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    to_test = ["ADAL", "MCL", "RIML"]

    synclass = "dopamine"  # or 'Tyramine', 'Octopamine', 'Serotonin'

    for cell in to_test:
        # my_instance.atlas.all_about(cell)

        print(
            "MA conns from %s: %s"
            % (
                cell,
                my_instance.get_connections_from(
                    cell, synclass, ordered_by_weight=True
                ),
            )
        )
        print(
            "MA conns to %s: %s"
            % (
                cell,
                my_instance.get_connections_to(cell, synclass, ordered_by_weight=True),
            )
        )

    print(my_instance.summary())

    # from cect.ConnectomeView import RAW_VIEW as view
    from cect.ConnectomeView import NEURONS_VIEW as view

    cds2 = my_instance.get_connectome_view(view)

    print(cds2.summary())

    fig = cds2.to_plotly_graph_fig(DOPAMINE, view)
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
