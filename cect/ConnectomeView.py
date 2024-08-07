from cect import print_

from cect.ConnectomeReader import ConnectionInfo

from cect.Cells import PHARYNGEAL_NEURONS
from cect.Cells import PREFERRED_NEURON_NAMES
from cect.Cells import PREFERRED_MUSCLE_NAMES
from cect.Cells import KNOWN_OTHER_CELLS

from cect.Cells import SENSORY_NEURONS_COOK_CATEGORIES
from cect.Cells import INTERNEURONS_NONPHARYNGEAL_COOK_CATEGORIES

from cect.Cells import BODY_WALL_MUSCLE_NAMES
from cect.Cells import BODY_MUSCLES_COOK
from cect.Cells import HEAD_MUSCLES_COOK
from cect.Cells import HEAD_MOTORNEURONS_COOK
from cect.Cells import SUBLATERAL_MOTORNEURONS_COOK
from cect.Cells import VENTRAL_CORD_MOTORNEURONS
from cect.Cells import HSN_MOTORNEURONS
from cect.Cells import VC_HERM_MOTORNEURONS

from cect.Cells import get_standard_color

from cect.ConnectomeReader import DEFAULT_COLORMAP

import numpy as np


class NodeSet:
    def __init__(self, name, cells, color=None, shape=None):
        self.name = name
        self.color = color
        self.cells = cells
        self.color = color
        self.shape = shape

    def is_one_cell(self):
        return len(self.cells) == 1 and self.name == self.cells[0]

    def __repr__(self):
        return "NodeSet %s%s: %s" % (
            self.name,
            " (%s)"
            % (
                "%s%s" % (self.color, self.shape if self.shape is not None else "")
                if self.color is not None
                else ""
            ),
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
for cell in sorted(PHARYNGEAL_NEURONS):
    PHARYNX_VIEW.node_sets.append(NodeSet(cell, [cell]))

SOCIAL_VIEW = View("Social View", [], EXC_INH_GJ_SYN_CLASSES)
for cell in sorted(["RMGR", "ASHR", "ASKR", "AWBR", "IL2R", "RMHR", "URXR"]):
    SOCIAL_VIEW.node_sets.append(NodeSet(cell, [cell]))

SMALL_VIEW = View("Small View", [], CHEM_GJ_SYN_CLASSES)


for category in SENSORY_NEURONS_COOK_CATEGORIES:
    color = "#b31b1b"
    if category == "SN4":
        color = "#FFC0CB"
    SMALL_VIEW.node_sets.append(
        NodeSet(
            category,
            SENSORY_NEURONS_COOK_CATEGORIES[category],
            color=color,
            shape="triangle-up",
        )
    )

for category in INTERNEURONS_NONPHARYNGEAL_COOK_CATEGORIES:
    SMALL_VIEW.node_sets.append(
        NodeSet(
            category,
            INTERNEURONS_NONPHARYNGEAL_COOK_CATEGORIES[category],
            color="#16537E",
            shape="hexagon2",
        )
    )

SMALL_VIEW.node_sets.append(
    NodeSet("HMN", HEAD_MOTORNEURONS_COOK, color="#FFDF00", shape="circle")
)

SMALL_VIEW.node_sets.append(
    NodeSet("SMN", SUBLATERAL_MOTORNEURONS_COOK, color="#FF6000", shape="circle")
)

SMALL_VIEW.node_sets.append(
    NodeSet("MNVC", VENTRAL_CORD_MOTORNEURONS, color="#BFA700", shape="circle")
)

SMALL_VIEW.node_sets.append(
    NodeSet("VC", VC_HERM_MOTORNEURONS, color="#FF00FF", shape="circle")
)

SMALL_VIEW.node_sets.append(
    NodeSet("HSN", HSN_MOTORNEURONS, color="#FF00FF", shape="circle")
)

SMALL_VIEW.node_sets.append(
    NodeSet("MUBODY", BODY_MUSCLES_COOK, color="#964B00", shape="square")
)
SMALL_VIEW.node_sets.append(
    NodeSet("MUHEAD", HEAD_MUSCLES_COOK, color="#964B00", shape="square")
)


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
