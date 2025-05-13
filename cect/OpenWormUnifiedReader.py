# -*- coding: utf-8 -*-

############################################################

#    A script to read the values from multiple connectomes. WORK IN PROGRESS!

############################################################


from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT
from cect.WormNeuroAtlasReader import WormNeuroAtlasReader
from cect.Cells import is_any_neuron
from cect.Cells import GENERIC_CHEM_SYN
from cect.ConnectomeDataset import load_connectome_dataset_file
from cect.ConnectomeDataset import get_cache_filename
from cect import print_


import os


READER_DESCRIPTION = """An OpenWorm unified reader combining multiple connectomes. <b>NOTE: WORK IN PROGRESS! SUBJECT TO CHANGE WITHOUT NOTICE!</b>"""


class OpenWormUnifiedReader(ConnectomeDataset):
    """
    Reader of data from multiple connectomes...
    """

    verbose = False

    def __init__(self):
        ConnectomeDataset.__init__(self)

        wna = WormNeuroAtlasReader(exclude_white=True, average=False)

        self.cook2029reader = load_connectome_dataset_file(
            get_cache_filename("Cook2019HermReader")
        )

        # neurons, muscles, other_cells, conns = self.read_all_data()

        conns = self.cook2029reader.get_current_connection_info_list()

        print_("Adding %i conns from Cook2019" % len(conns))
        for conn in conns:
            if is_any_neuron(conn.pre_cell) and conn.synclass == GENERIC_CHEM_SYN:
                nt = wna.determine_nt(conn.pre_cell)
                # print(" Changing nt to: %s" % nt)
                conn.synclass = nt
                # print(conn)
            self.add_connection_info(conn)

    def read_data(self):
        return self._read_data()

    def read_muscle_data(self):
        return self._read_muscle_data()


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    return OpenWormUnifiedReader()


def main():
    tdr_instance = OpenWormUnifiedReader()

    cells, neuron_conns = tdr_instance.read_data()

    neurons2muscles, muscles, muscle_conns = tdr_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    print(tdr_instance.summary())


if __name__ == "__main__":
    main()
