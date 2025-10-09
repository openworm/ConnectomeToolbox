import logging

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeDataset import ConnectomeDataset
from cect.Cells import EXTRASYNAPTIC_SYN_TYPE
from cect.Cells import MONOAMINERGIC_SYN_GENERAL_CLASS
from cect.Cells import MONOAMINERGIC_SYN_CLASSES
from cect.Cells import PEPTIDERGIC_SYN_CLASS

from cect import print_

import sys

from cect.WormNeuroAtlasReader import get_all_cells


############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

LOGGER = logging.getLogger(__name__)

READER_DESCRIPTION = """Data on extrasynaptic connectivity from the <b><a href="https://github.com/francescorandi/wormneuroatlas">WormNeuroAtlas package</a></b>"""


class WormNeuroAtlasExtSynReader(ConnectomeDataset):
    def __init__(self, mono_or_pep):
        ConnectomeDataset.__init__(self)

        self.mono_or_pep = mono_or_pep

        print_("Initialising WormNeuroAtlasExtSynReader for %s" % self.mono_or_pep)

        import wormneuroatlas as wa

        self.atlas = wa.NeuroAtlas()

        self.all_cells = get_all_cells(self.atlas)

        cells, neuron_conns = self.read_data()

        for conn in neuron_conns:
            self.add_connection_info(conn)

    def read_data(self):
        conns = []

        if self.mono_or_pep == PEPTIDERGIC_SYN_CLASS:
            connectome = self.atlas.get_peptidergic_connectome()

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
                            ConnectionInfo(
                                str(pre),
                                str(post),
                                float(weight),
                                syntype=EXTRASYNAPTIC_SYN_TYPE,
                                synclass=PEPTIDERGIC_SYN_CLASS,
                            )
                        )
                        connection = True

                    if connection:
                        if pre not in connected_cells:
                            connected_cells.append(str(pre))
                        if post not in connected_cells:
                            connected_cells.append(str(post))

        if self.mono_or_pep == MONOAMINERGIC_SYN_GENERAL_CLASS:
            for synclass in MONOAMINERGIC_SYN_CLASSES:
                transmitters = [synclass.lower()]
                print_("Loading Bentley connectome for %s...." % (synclass))

                connectome = self.atlas._get_esconnectome_bentley(
                    fname=self.atlas.module_folder
                    + "esconnectome_monoamines_Bentley_2016.csv",
                    transmitters=transmitters,
                )

                # print_("Loaded %s" % (connectome))

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
                                ConnectionInfo(
                                    str(pre),
                                    str(post),
                                    float(weight),
                                    syntype=EXTRASYNAPTIC_SYN_TYPE,
                                    synclass=synclass,
                                )
                            )
                            connection = True

                        if connection:
                            if pre not in connected_cells:
                                connected_cells.append(str(pre))
                            if post not in connected_cells:
                                connected_cells.append(str(post))

        return connected_cells, conns

    def read_muscle_data(self):
        neurons = []
        muscles = []
        conns = []
        return neurons, muscles, conns


if __name__ == "__main__":
    syn_class_to_test = MONOAMINERGIC_SYN_GENERAL_CLASS

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

    print(my_instance.summary())
