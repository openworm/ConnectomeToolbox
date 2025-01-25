import logging

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeDataset import ConnectomeDataset
from cect.Cells import EXTRASYNAPTIC_SYN_TYPE
from cect.Cells import MONOAMINERGIC_SYN_CLASS
from cect.Cells import PEPTIDERGIC_SYN_CLASS

from cect import print_

import wormneuroatlas as wa
import sys

from cect.WormNeuroAtlasReader import get_all_cells


############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

LOGGER = logging.getLogger(__name__)

READER_DESCRIPTION = """Data on extrasynaptic connectivity from the <b><a href="https://github.com/francescorandi/wormneuroatlas">WormNeuroAtlas package</a></b>"""


class WormNeuroAtlasExtSynReader(ConnectomeDataset):
    def __init__(self, synclass):
        ConnectomeDataset.__init__(self)

        self.synclass = synclass

        print_(
            "Initialising WormNeuroAtlasExtSynReader for syn class %s" % self.synclass
        )

        self.atlas = wa.NeuroAtlas()

        self.all_cells = get_all_cells(self.atlas)

        cells, neuron_conns = self.read_data()

        for conn in neuron_conns:
            self.add_connection_info(conn)

    def read_data(self):
        conns = []

        if self.synclass == MONOAMINERGIC_SYN_CLASS:
            connectome = self.atlas.get_monoaminergic_connectome()
            syntype = EXTRASYNAPTIC_SYN_TYPE

        if self.synclass == PEPTIDERGIC_SYN_CLASS:
            connectome = self.atlas.get_peptidergic_connectome()
            syntype = EXTRASYNAPTIC_SYN_TYPE

        connected_cells = []

        for pre in self.all_cells:
            apre = self.atlas.ids_to_ai([pre])
            for post in self.all_cells:
                apost = self.atlas.ids_to_ai([post])

                connection = False

                weight = connectome[apost, apre][0]

                if weight != 0:
                    # print_( "%s conn (%s (%i) -> %s (%i):\t%s " % (self.synclass, pre, apre, post, apost, weight)       )

                    conns.append(
                        ConnectionInfo(pre, post, weight, syntype, self.synclass)
                    )
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


if __name__ == "__main__":
    syn_class_to_test = PEPTIDERGIC_SYN_CLASS

    my_instance = WormNeuroAtlasExtSynReader(syn_class_to_test)
    cells, neuron_conns = my_instance.read_data()
    print("Loaded %s connections" % len(neuron_conns))

    # from cect.ConnectomeReader import analyse_connections
    # analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    to_test = ["RIMR"]

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
