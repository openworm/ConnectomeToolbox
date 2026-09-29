############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

from cect.readers.WormNeuroAtlasExtSynReader import WormNeuroAtlasExtSynReader
from cect.Neurotransmitters import MONOAMINERGIC_SYN_GENERAL_CLASS
from cect.Neurotransmitters import DOPAMINE
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

import logging
import sys


LOGGER = logging.getLogger(__name__)

NAME = "Bentley2016_MAwna"

READER_DESCRIPTION = """Data on monoaminergic connectivity from the <b><a href="https://github.com/francescorandi/wormneuroatlas">WormNeuroAtlas package</a></b>"""

DATASET_DESCRIPTION = """Data on monoaminergic connectivity from Bentley et al. 2016 (i.e. dopaminergic, tyraminergic, octopaminergic & serotonergic extrasynaptic transmission), accessed via the WormNeuroAtlas package"""

WEIGHTS = "Adjacency matrices are binary and directed; a weight of 1 between neurons A and B signifies that cell A expresses a biosynthetic enzyme or transporter for the specific monoamine and neuron B expresses a cognate receptor for that monoamine."


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WormNeuroAtlasExtSynReader`` to load data on monoaminergic connectivity using the **[WormNeuroAtlas package](https://github.com/francescorandi/wormneuroatlas)**

    Returns:
        (WormNeuroAtlasExtSynReader): The initialised connectome reader
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
        try:
            return WormNeuroAtlasExtSynReader(MONOAMINERGIC_SYN_GENERAL_CLASS)
        except Exception as e:
            print(
                "Problem loading WormNeuroAtlas data. Can be caused by WormBase url not working. Defaulting to loading from cache... Issue: %s"
                % str(e)
            )
            return get_instance(from_cache=True)


if __name__ == "__main__":
    my_instance = get_instance(from_cache=True)
    cells, neuron_conns = my_instance._read_data()
    print("Loaded %s connections" % len(neuron_conns))

    # from cect.ConnectomeReader import analyse_connections
    # analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    to_test = ["ADEL", "RIML", "CEPVR"]

    synclass = DOPAMINE  # or 'Tyramine', 'Octopamine', 'Serotonin'

    for cell in to_test:
        # my_instance.atlas.all_about(cell)

        print(
            "MA conns from %s:\n%s"
            % (
                cell,
                "\n".join(
                    [
                        f"   {c}:  \t{float(w)}"
                        for c, w in my_instance.get_connections_from(
                            cell, synclass, ordered_by_weight=True
                        ).items()
                    ]
                ),
            )
        )

        print(
            "MA conns to %s:\n%s"
            % (
                cell,
                "\n".join(
                    [
                        f"   {c}:  \t{float(w)}"
                        for c, w in my_instance.get_connections_to(
                            cell, synclass, ordered_by_weight=True
                        ).items()
                    ]
                ),
            )
        )

    if "-nogui" not in sys.argv:
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

        fig.show()
