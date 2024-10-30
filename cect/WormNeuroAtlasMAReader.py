############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

from cect.WormNeuroAtlasExtSynReader import WormNeuroAtlasExtSynReader
from cect.Cells import MONOAMINERGIC_SYN_CLASS

import logging
import sys


LOGGER = logging.getLogger(__name__)

READER_DESCRIPTION = """Data extracted from the **WormNeuroAtlas package** for monoaminergic connectivity"""


def get_instance():
    return WormNeuroAtlasExtSynReader(MONOAMINERGIC_SYN_CLASS)


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data

if __name__ == "__main__":
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
                    cell, MONOAMINERGIC_SYN_CLASS, ordered_by_weight=True
                ),
            )
        )
        print(
            "MA conns to %s: %s"
            % (
                cell,
                my_instance.get_connections_to(
                    cell, MONOAMINERGIC_SYN_CLASS, ordered_by_weight=True
                ),
            )
        )

    if "-nogui" not in sys.argv:
        my_instance.connection_number_plot(MONOAMINERGIC_SYN_CLASS)
