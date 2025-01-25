import logging

from cect.ConnectomeReader import ConnectionInfo
from cect import print_

from cect.ConnectomeDataset import ConnectomeDataset

import wormneuroatlas as wa
import math
import sys

from cect.WormNeuroAtlasReader import get_all_cells


############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

LOGGER = logging.getLogger(__name__)

READER_DESCRIPTION = """Data on functional connectivity from the <b><a href="https://github.com/francescorandi/wormneuroatlas">WormNeuroAtlas package</a></b>"""

FUNCTIONAL_SYN_TYPE = "Functional"
FUNCTIONAL_SYN_CLASS = "Functional"


class WormNeuroAtlasFuncReader(ConnectomeDataset):
    """Data on functional connectivity from the **[WormNeuroAtlas package](https://github.com/francescorandi/wormneuroatlas)**"""

    def __init__(self, max_q):
        ConnectomeDataset.__init__(self)

        self.max_q = max_q

        print_(
            "Initialising WormNeuroAtlasFuncReader with max q value: %s" % self.max_q
        )

        self.atlas = wa.NeuroAtlas()

        self.all_cells = get_all_cells(self.atlas)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(conn)

    def read_data(self):
        conns = []

        dff = self.atlas.get_signal_propagation_map(strain="wt")
        q = self.atlas.get_signal_propagation_q(strain="wt")

        connected_cells = []

        for pre in self.all_cells:
            apre = self.atlas.ids_to_ai([pre])
            for post in self.all_cells:
                apost = self.atlas.ids_to_ai([post])

                connection = False

                bound = 10

                dff_ij_orig = dff[apost, apre][0]

                dff_ij = (
                    0
                    if (apost == apre or math.isnan(dff_ij_orig))
                    else max(-1 * bound, min(bound, dff_ij_orig))
                )
                # dff_ij = dff_ij_orig

                q_ij = q[apost, apre]

                num = dff_ij

                if abs(num) > -10 and q_ij < self.max_q:
                    if num < 0:
                        print_(
                            "Functional conn junc (%s (%i) -> %s (%i):\t%s (orig = %s, q = %s)"
                            % (pre, apre, post, apost, dff_ij, dff_ij_orig, q_ij)
                        )
                    synclass = FUNCTIONAL_SYN_CLASS
                    syntype = FUNCTIONAL_SYN_TYPE
                    conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                    connection = True

                if connection:
                    if pre not in connected_cells:
                        connected_cells.append(pre)
                    if post not in connected_cells:
                        connected_cells.append(post)

        return connected_cells, conns

    def read_muscle_data(self):
        neurons = []
        muscles = []
        conns = []
        return neurons, muscles, conns


def get_instance():
    return WormNeuroAtlasFuncReader(0.05)


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
            "Func conns from %s: %s"
            % (
                cell,
                my_instance.get_connections_from(
                    cell, FUNCTIONAL_SYN_CLASS, ordered_by_weight=True
                ),
            )
        )
        print(
            "Func conns to %s: %s"
            % (
                cell,
                my_instance.get_connections_to(
                    cell, FUNCTIONAL_SYN_CLASS, ordered_by_weight=True
                ),
            )
        )

    if "-nogui" not in sys.argv:
        my_instance.connection_number_plot(FUNCTIONAL_SYN_CLASS)
