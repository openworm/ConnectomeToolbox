from cect import print_

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import PHARYNX_CELLS
from cect.ConnectomeReader import PREFERRED_NEURON_NAMES


import numpy as np


class NodeSet:
    def __init__(self, name, cells, color=None):
        self.name = name
        self.color = color
        self.cells = cells

    def __repr__(self):
        return "NodeSet %s (%s): %s" % (self.name, self.color, self.cells)


class View:
    def __init__(self, name, node_sets, synclass_sets={}, colormap="BuPu"):
        self.name = name
        self.node_sets = node_sets
        self.synclass_sets = synclass_sets
        self.colormap = colormap

    def get_index_of_cell(self, cell):
        for i in range(len(self.node_sets)):
            if cell in self.node_sets[i].cells:
                return i
        return -1


STANDARD_SYN_CLASSES = {
    "Chemical Exc": ["Acetylcholine", "Generic_CS"],
    "Chemical Inh": ["GABA"],
    "Electrical": ["Generic_GJ"],
}

FULL_VIEW = View("Full View", [], STANDARD_SYN_CLASSES)
for cell in sorted(PREFERRED_NEURON_NAMES):
    FULL_VIEW.node_sets.append(NodeSet(cell, [cell]))

PHARYNX_VIEW = View("Pharynx View", [], STANDARD_SYN_CLASSES)
for cell in sorted(PHARYNX_CELLS):
    PHARYNX_VIEW.node_sets.append(NodeSet(cell, [cell]))

SOCIAL_VIEW = View("Social View", [], STANDARD_SYN_CLASSES)
for cell in sorted(["RMGR", "ASHR", "ASKR", "AWBR", "IL2R", "RMHR", "URXR"]):
    SOCIAL_VIEW.node_sets.append(NodeSet(cell, [cell]))

ALL_VIEWS = [FULL_VIEW, PHARYNX_VIEW, SOCIAL_VIEW]


if __name__ == "__main__":
    ns_v = NodeSet("Vmn", ["VA6", "VB6", "VB3", "VD6", "VA3", "VD3", "VB2"])
    ns_d = NodeSet("Dmn", ["DB4", "DD4"])
    ns_p = NodeSet("PVCL", ["PVCL"])
    ns_a = NodeSet("AVBL", ["AVBL"])

    v1 = View("VandD", [ns_d, ns_v, ns_a, ns_p], STANDARD_SYN_CLASSES)

    from cect.TestDataReader import tdr_instance

    print(tdr_instance.summary())

    print("----------------")
    print(tdr_instance.get_connectome_view(v1).summary())

    print("----------------")
    print(tdr_instance.get_connectome_view(SOCIAL_VIEW).summary())
