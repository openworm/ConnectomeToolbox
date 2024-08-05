from cect import print_

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import PHARANGEAL_NEURONS
from cect.ConnectomeReader import PREFERRED_NEURON_NAMES
from cect.ConnectomeReader import PREFERRED_MUSCLE_NAMES
from cect.ConnectomeReader import KNOWN_OTHER_CELLS
from cect.ConnectomeReader import get_standard_color

from cect.ConnectomeReader import DEFAULT_COLORMAP

import numpy as np


class NodeSet:
    def __init__(self, name, cells, color=None):
        self.name = name
        self.color = color
        self.cells = cells
        self.color = color

    def is_one_cell(self):
        return len(self.cells) == 1 and self.name == self.cells[0]

    def __repr__(self):
        return "NodeSet %s%s: %s" % (
            self.name,
            " (%s)" % self.color if self.color is not None else "",
            self.cells,
        )


class View:
    def __init__(
        self,
        name,
        node_sets,
        synclass_sets={},
        colormap=DEFAULT_COLORMAP,
        only_show_existing_nodes=False,
    ):
        self.name = name
        self.node_sets = node_sets
        self.synclass_sets = synclass_sets
        self.colormap = colormap
        self.only_show_existing_nodes = only_show_existing_nodes

    def has_color(self):
        for ns in self.node_sets:
            if ns.color is not None:
                return True
        return False

    def get_node_set(self, node_set_name):
        for ns in self.node_sets:
            if ns.name == node_set_name:
                return ns
        return None

    def get_index_of_cell(self, cell):
        for i in range(len(self.node_sets)):
            if cell in self.node_sets[i].cells:
                return i
        return -1


EXC_INH_GJ_SYN_CLASSES = {
    "Chemical Exc": ["Acetylcholine", "Generic_CS"],
    "Chemical Inh": ["GABA"],
    "Electrical": ["Generic_GJ"],
}

CHEM_GJ_SYN_CLASSES = {
    "Chemical": EXC_INH_GJ_SYN_CLASSES["Chemical Exc"]
    + EXC_INH_GJ_SYN_CLASSES["Chemical Inh"],
    "Electrical": ["Generic_GJ"],
}

RAW_VIEW = View("Raw Data", [], CHEM_GJ_SYN_CLASSES, only_show_existing_nodes=True)
for cell in (
    sorted(PREFERRED_NEURON_NAMES)
    + sorted(PREFERRED_MUSCLE_NAMES)
    + sorted(KNOWN_OTHER_CELLS)
):
    RAW_VIEW.node_sets.append(NodeSet(cell, [cell], get_standard_color(cell)))


FULL_VIEW = View("Full View", [], EXC_INH_GJ_SYN_CLASSES)
for cell in sorted(PREFERRED_NEURON_NAMES):
    FULL_VIEW.node_sets.append(NodeSet(cell, [cell]))

PHARYNX_VIEW = View("Pharynx View", [], EXC_INH_GJ_SYN_CLASSES)
for cell in sorted(PHARANGEAL_NEURONS):
    PHARYNX_VIEW.node_sets.append(NodeSet(cell, [cell]))

SOCIAL_VIEW = View("Social View", [], EXC_INH_GJ_SYN_CLASSES)
for cell in sorted(["RMGR", "ASHR", "ASKR", "AWBR", "IL2R", "RMHR", "URXR"]):
    SOCIAL_VIEW.node_sets.append(NodeSet(cell, [cell]))

SMALL_VIEW = View("Small View", [], CHEM_GJ_SYN_CLASSES)

for cell in sorted(["ADAL", "ADAR", "ADFL", "ADFR"]):
    SMALL_VIEW.node_sets.append(
        NodeSet(cell, [cell], color="#FF0000" if "ADA" in cell else "#00FF00")
    )

motorneuron_prefixes = ["DB", "VB", "DD", "VD", "DA", "AS", "VA"]

for prefix in motorneuron_prefixes:
    SMALL_VIEW.node_sets.append(NodeSet(prefix, [], color="#be5103"))

for cell in sorted(PREFERRED_NEURON_NAMES):
    for prefix in motorneuron_prefixes:
        if cell.startswith(prefix):
            SMALL_VIEW.get_node_set(prefix).cells.append(cell)


ALL_VIEWS = [RAW_VIEW, FULL_VIEW, PHARYNX_VIEW, SOCIAL_VIEW, SMALL_VIEW]


if __name__ == "__main__":
    ns_v = NodeSet("Vmn", ["VA6", "VB6", "VB3", "VD6", "VA3", "VD3", "VB2"])
    ns_d = NodeSet("Dmn", ["DB4", "DD4"])
    ns_p = NodeSet("PVCL", ["PVCL"])
    ns_a = NodeSet("AVBL", ["AVBL"])

    v1 = View("VandD", [ns_d, ns_v, ns_a, ns_p], EXC_INH_GJ_SYN_CLASSES)

    from cect.TestDataReader import tdr_instance

    print(tdr_instance.summary())

    print("----------------")
    print(tdr_instance.get_connectome_view(v1).summary())

    print("----------------")
    print(tdr_instance.get_connectome_view(SOCIAL_VIEW).summary())
