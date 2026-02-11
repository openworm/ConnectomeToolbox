# -*- coding: utf-8 -*-

############################################################

#    A script to read the values from multiple connectomes. WORK IN PROGRESS!

############################################################


from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT
from cect import print_

from cect.Wang2024Reader import Wang2024Reader

import os


READER_DESCRIPTION = """An OpenWorm unified reader combining multiple connectomes. <b>NOTE: WORK IN PROGRESS! SUBJECT TO CHANGE WITHOUT NOTICE!</b>"""


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[1]))
    else:
        global READER_DESCRIPTION
        inst = Wang2024Reader(
            sex="Hermaphrodite",
            normalize_conn_numbers=False,
            include_monoamine_conns=False,
            include_electrical_connections=True,
        )
        READER_DESCRIPTION = inst.reader_description
        return inst


'''
class OpenWormUnifiedReader(ConnectomeDataset):
    """
    Reader of data from multiple connectomes...
    """

    verbose = False

    def __init__(self):
        ConnectomeDataset.__init__(self)

        wna = WormNeuroAtlasReader(exclude_white=True, average=False)

        self.cook2019reader = load_connectome_dataset_file(
            get_cache_filename("Cook2019HermReader")
        )

        # neurons, muscles, other_cells, conns = self.read_all_data()

        conns = self.cook2019reader.get_current_connection_info_list()

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
'''


def main():
    tdr_instance = get_instance(from_cache=False)

    cells, neuron_conns = tdr_instance.read_data()

    neurons2muscles, muscles, muscle_conns = tdr_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    print(tdr_instance.summary())
    quit()

    """
    
    from cect.ConnectomeView import NEURONS_VIEW as view
    from cect.ConnectomeView import COOK_FIG3_VIEW as 
    from cect.ConnectomeView import LOCOMOTION_3_VIEW as view
    from cect.ConnectomeView import LOCOMOTION_1_VIEW as view
    """
    # from cect.ConnectomeView import SOCIAL_VIEW as view
    from cect.ConnectomeView import LOCOMOTION_2_VIEW as view
    # from cect.ConnectomeView import RAW_VIEW as view

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


if __name__ == "__main__":
    main()
