"""
Data extracted from the **WormNeuroAtlas package** for neuronal connectivity
"""

import logging

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect import print_

from cect.Cells import GENERIC_CHEM_SYN
from cect.Cells import GENERIC_ELEC_SYN

from cect.ConnectomeDataset import ConnectomeDataset

from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

LOGGER = logging.getLogger(__name__)

READER_DESCRIPTION = """Data from the <b><a href="https://github.com/francescorandi/wormneuroatlas">WormNeuroAtlas package</a></b> for neuronal connectivity"""


def get_all_cells(watlas):
    all_cells = watlas.neuron_ids
    for i in range(len(all_cells)):
        if all_cells[i] == "AWCOFF":
            all_cells[i] = "AWCL"
        if all_cells[i] == "AWCON":
            all_cells[i] = "AWCR"

    return all_cells


class WormNeuroAtlasReader(ConnectomeDataset):
    """Data from the **[WormNeuroAtlas package](https://github.com/francescorandi/wormneuroatlas)** for neuronal connectivity"""

    def __init__(self, exclude_white=False, average=False):
        ConnectomeDataset.__init__(self)

        print_("Initialising WormNeuroAtlasReader")
        import wormneuroatlas as wa

        self.atlas = wa.NeuroAtlas(load_connectomes=False)
        self.atlas.load_aconnectome_from_file(
            exclude_white=exclude_white, average=average
        )
        syn_sign = wa.SynapseSign()

        self.dom_glu = syn_sign.get_neurons_producing("Glu", mode="dominant")
        self.dom_ach = syn_sign.get_neurons_producing("ACh", mode="dominant")
        self.dom_gaba = syn_sign.get_neurons_producing("GABA", mode="dominant")

        self.alt_glu = syn_sign.get_neurons_producing("Glu", mode="alternative")
        self.alt_ach = syn_sign.get_neurons_producing("ACh", mode="alternative")
        self.alt_gaba = syn_sign.get_neurons_producing("GABA", mode="alternative")

        self.all_cells = get_all_cells(self.atlas)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(conn)

    def determine_nt(self, neuron):
        if neuron in self.dom_glu:
            return "Glutamate"
        elif neuron in self.dom_ach:
            return "Acetylcholine"
        elif neuron in self.dom_gaba:
            return "GABA"
        else:
            nt = GENERIC_CHEM_SYN
            if neuron in self.alt_glu:
                nt += "_Glutamate"
            if neuron in self.alt_ach:
                nt += "_Acetylcholine"
            if neuron in self.dom_gaba:
                nt += "_GABA"

            return nt

    def read_data(self):
        conns = []
        gj = self.atlas.get_gap_junctions()
        cs = self.atlas.get_chemical_synapses()

        connected_cells = []

        for pre in self.all_cells:
            apre = self.atlas.ids_to_ai([pre])
            for post in self.all_cells:
                apost = self.atlas.ids_to_ai([post])

                connection = False

                gji = gj[apost, apre]
                num = gji[0]
                if num > 0:
                    # print("Gap junc (%s (%i) -> %s (%i): %s"%(pre, apre, post, apost, gji))
                    synclass = GENERIC_ELEC_SYN
                    syntype = "GapJunction"
                    conns.append(
                        ConnectionInfo(str(pre), str(post), num, syntype, synclass)
                    )
                    connection = True

                csi = cs[apost, apre]
                num = csi[0]
                if num > 0:
                    # print("Chem syn (%s (%i) -> %s (%i): %s"%(pre, apre, post, apost, gji))
                    synclass = self.determine_nt(pre)
                    syntype = "Chemical"
                    conns.append(
                        ConnectionInfo(str(pre), str(post), num, syntype, synclass)
                    )
                    connection = True

                if connection:
                    if pre not in connected_cells:
                        connected_cells.append(str(pre))
                    if post not in connected_cells:
                        connected_cells.append(str(post))

        """if include_nonconnected_cells:
            return self.all_cells, conns
        else:"""

        return connected_cells, conns

    def read_muscle_data(self):
        neurons = []
        muscles = []
        conns = []
        return neurons, muscles, conns


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache and 0:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(
            get_cache_filename(__file__.split("/")[-1].split(".")[0])
        )
    else:
        return WormNeuroAtlasReader(exclude_white=False, average=False)


"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""

if __name__ == "__main__":
    # my_instance = get_instance(True)
    my_instance = WormNeuroAtlasReader(exclude_white=True, average=False)

    cells, neuron_conns = my_instance._read_data()
    neurons2muscles, muscles, muscle_conns = my_instance._read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    cell = "RMHL"
    conns = my_instance.get_connections_from(cell, "Acetylcholine")

    print(f"There are {len(conns)} connections from {cell}:")
    for c in sorted(conns.keys()):
        print(f" {cell} -> {c}: {conns[c]}")
