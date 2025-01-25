############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

from cect.WormNeuroAtlasExtSynReader import WormNeuroAtlasExtSynReader
from cect.Cells import PEPTIDERGIC_SYN_CLASS

import logging
import sys


LOGGER = logging.getLogger(__name__)

READER_DESCRIPTION = """Data on peptidergic connectivity from the <b><a href="https://github.com/francescorandi/wormneuroatlas">WormNeuroAtlas package</a></b>"""


def get_instance():
    """Uses ``WormNeuroAtlasExtSynReader`` to load data on peptidergic connectivity using the **[WormNeuroAtlas package](https://github.com/francescorandi/wormneuroatlas)**

    Returns:
        WormNeuroAtlasExtSynReader: The initialised connectome reader
    """
    return WormNeuroAtlasExtSynReader(PEPTIDERGIC_SYN_CLASS)


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data

if __name__ == "__main__":
    syn_class_to_test = PEPTIDERGIC_SYN_CLASS

    cells, neuron_conns = my_instance.read_data()
    print("Loaded %s connections" % len(neuron_conns))

    # from cect.ConnectomeReader import analyse_connections
    # analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    to_test = ["ADAL", "MCL", "M5"]

    for cell in to_test:
        my_instance.atlas.all_about(cell)

        print(
            "MA conns from %s: %s"
            % (
                cell,
                my_instance.get_connections_from(
                    cell, syn_class_to_test, ordered_by_weight=True
                ),
            )
        )
        print(
            "MA conns to %s: %s"
            % (
                cell,
                my_instance.get_connections_to(
                    cell, syn_class_to_test, ordered_by_weight=True
                ),
            )
        )

    if "-nogui" not in sys.argv:
        my_instance.connection_number_plot(syn_class_to_test)
