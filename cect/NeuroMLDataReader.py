# -*- coding: utf-8 -*-

############################################################

#    A script to read NeuroML files containing C. elegans based connectomes.

############################################################


from cect.ConnectomeReader import analyse_connections
from cect.Cells import is_known_muscle
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT
from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeDataset import ConnectomeDataset
from cect import print_
from cect.Cells import GENERIC_ELEC_SYN

from pyneuroml import pynml
import os


def get_file_location(nml_model):
    if "/" in nml_model:
        return nml_model
    location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    filename = "%s%s" % (
        location,
        nml_model,
    )
    return filename


file_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
filename = "%sWorm2D.net.nml" % file_location


READER_DESCRIPTION = """Data extracted from NeuroML file"""


class NeuroMLDataReader(ConnectomeDataset):
    """
    Reader of data from a NeuroML file
    """

    verbose = False

    def __init__(self, neuroml_filename):
        ConnectomeDataset.__init__(self)

        nml_doc = pynml.read_neuroml2_file(get_file_location(neuroml_filename))
        self.nml_net = nml_doc.networks[0]
        print_("Opened the NeuroML file: " + neuroml_filename)

        neurons, muscles, other_cells, conns = self.read_all_data()

        for conn in conns:
            self.add_connection_info(conn)

    def read_data(self):
        return self._read_data()

    def read_muscle_data(self):
        return self._read_muscle_data()

    cell_names = {}

    def _get_cell_name(self, pop, index, pop_size=None):
        ref = "%s_%i" % (pop, index)
        if ref in self.cell_names:
            # print_(" - Cell name is already known: %s = %s" % (ref, self.cell_names[ref]))
            return self.cell_names[ref]
        if pop_size is not None:
            if pop_size > 1:
                if "MD1" in pop or "MV1" in pop:
                    cell_name = "%sR%s" % (
                        pop[3:-1],
                        index + 1 if index > 8 else "0%s" % (index + 1),
                    )
                else:
                    cell_name = "%s%s" % (pop[3:] if "Pop" in pop else pop, index + 1)
            else:
                cell_name = pop
        else:
            raise Exception(
                f"Cannot determine cell name for cell {index} in population {pop} (size: {pop_size})\nCells: {self.cell_names}"
            )

        self.cell_names[ref] = cell_name
        print_(
            f" - Adding cell named {cell_name}, ref: {ref} - cell {index} in population {pop} (size of the pop: {pop_size}))"
        )
        return cell_name

    def read_all_data(self):
        """
        Returns:
            Tuple[list, list, list, list]: List of neurons, muscles), other cells and connections which have been read in
        """

        neurons = set([])
        muscles = set([])
        other_cells = set([])
        conns = []

        for pop in self.nml_net.populations:
            for inst in pop.instances:
                cell_name = self._get_cell_name(pop.id, inst.id, len(pop.instances))
                print_("Adding cell: %s" % cell_name)
                if is_known_muscle(cell_name):
                    muscles.add(cell_name)
                else:
                    neurons.add(cell_name)

        for cont_proj in self.nml_net.continuous_projections:
            print_("Adding proj: %s" % cont_proj.id)
            pre_pop = cont_proj.presynaptic_population
            post_pop = cont_proj.postsynaptic_population

            for conn in cont_proj.continuous_connection_instance_ws:
                # print_(" - Adding conn: %s" % conn)
                pre = self._get_cell_name(pre_pop, conn.get_pre_cell_id())
                post = self._get_cell_name(post_pop, conn.get_post_cell_id())
                w = conn.get_weight()
                synclass = "Acetylcholine"
                if w < 0:
                    w = -1 * w
                    synclass = "GABA"

                elif "inh_syn" in conn.post_component:
                    synclass = "GABA"  # e.g. postComponent="neuron_to_neuron_inh_syn",

                ci = ConnectionInfo(pre, post, w, "???", synclass)

                # print_("Conn: %s" % (ci))
                conns.append(ci)

        for elec_proj in self.nml_net.electrical_projections:
            print_("Adding proj: %s" % elec_proj.id)
            pre_pop = elec_proj.presynaptic_population
            post_pop = elec_proj.postsynaptic_population
            for conn in elec_proj.electrical_connection_instance_ws:
                # print_(" - Adding conn: %s" % conn)
                pre = self._get_cell_name(pre_pop, conn.get_pre_cell_id())
                post = self._get_cell_name(post_pop, conn.get_post_cell_id())
                w = conn.get_weight()
                synclass = GENERIC_ELEC_SYN
                ci = ConnectionInfo(pre, post, w, "???", synclass)

                # print_("Conn: %s" % (ci))
                conns.append(ci)

        return list(neurons), list(muscles), list(other_cells), conns


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``NeuroMLDataReader`` to load data on connectome

    Returns:
        NeuroMLDataReader: The initialised connectome reader
    """
    if from_cache and False:  #####
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(
            get_cache_filename(__file__.split("/")[-1].split(".")[0])
        )
    else:
        return NeuroMLDataReader("Worm2D.net.nml")


if __name__ == "__main__":
    #
    tdr_instance = NeuroMLDataReader("Worm2D.net.nml")
    # tdr_instance = NeuroMLDataReader("c302_C2_FW.net.nml")
    cells, neuron_conns = tdr_instance.read_data()

    neurons2muscles, muscles, muscle_conns = tdr_instance.read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    print(tdr_instance.summary())

    print("=======================================")
    """
    
    from cect.ConnectomeView import NEURONS_VIEW as view
    from cect.ConnectomeView import COOK_FIG3_VIEW as 
    from cect.ConnectomeView import RAW_VIEW as view
    from cect.ConnectomeView import LOCOMOTION_3_VIEW as view
    from cect.ConnectomeView import LOCOMOTION_1_VIEW as view
    """
    # from cect.ConnectomeView import SOCIAL_VIEW as view
    from cect.ConnectomeView import LOCOMOTION_2_VIEW as view

    print("--- Using view: %s" % view)
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
