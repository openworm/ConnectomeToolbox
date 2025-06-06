from cect.Cells import PHARYNGEAL_NEURONS

from cect.Cells import ALL_PREFERRED_CELL_NAMES

# from cect.Cells import PREFERRED_HERM_NEURON_NAMES
from cect.Cells import SENSORY_NEURONS_NONPHARYNGEAL_COOK
from cect.Cells import INTERNEURONS_NONPHARYNGEAL_COOK
from cect.Cells import UNKNOWN_FUNCTION_NEURONS
from cect.Cells import MALE_SPECIFIC_NEURONS
from cect.Cells import MALE_HEAD_INTERNEURONS
from cect.Cells import MALE_NON_HEAD_INTERNEURONS
from cect.Cells import MALE_HEAD_SENSORY_NEURONS
from cect.Cells import MALE_NON_HEAD_SENSORY_NEURONS
from cect.Cells import PREFERRED_MUSCLE_NAMES
from cect.Cells import ALL_NON_NEURON_MUSCLE_CELLS


from cect.Cells import SENSORY_NEURONS_COOK_CATEGORIES
from cect.Cells import INTERNEURONS_NONPHARYNGEAL_COOK_CATEGORIES

from cect.Cells import BODY_MUSCLES_COOK
from cect.Cells import UNSPECIFIED_BODY_WALL_MUSCLES
from cect.Cells import HEAD_MUSCLES_COOK

from cect.Cells import HEAD_MOTORNEURONS_COOK
from cect.Cells import SUBLATERAL_MOTORNEURONS_COOK
from cect.Cells import VENTRAL_CORD_MOTORNEURONS
from cect.Cells import HSN_MOTORNEURONS
from cect.Cells import VC_HERM_MOTORNEURONS
from cect.Cells import MOTORNEURONS_NONPHARYNGEAL_COOK
from cect.Cells import KNOWN_MODELLED_NEURONS


from cect.Cells import ALL_KNOWN_CHEMICAL_NEUROTRANSMITTERS
from cect.Cells import ALL_KNOWN_EXTRASYNAPTIC_CLASSES
from cect.Cells import GENERIC_CHEM_SYN
from cect.Cells import GENERIC_ELEC_SYN

from cect.Cells import get_standard_color

from cect.ConnectomeReader import DEFAULT_COLORMAP
from cect.RipollSanchezDataReader import load_hub_info

import copy


class NodeSet:
    """Set of nodes (can be single cells or lists of cells) to use in a ``View``. Can specify the `color`, `shape`, `position` or `size` to use in graphical depictions."""

    def __init__(self, name, cells, color=None, shape=None, position=None, size=None):
        self.name = name
        self.color = color
        self.cells = cells
        self.shape = shape
        self.position = position
        self.size = size

    def is_one_cell(self):
        return len(self.cells) == 1 and self.name == self.cells[0]

    def __repr__(self):
        info = "NodeSet: %s\t(" % self.name
        if self.color is not None:
            info += "%s " % self.color
        if self.shape is not None:
            info += "%s " % self.shape
        if self.position is not None:
            info += "%s " % (str(self.position))
        info += "\t%s" % self.cells

        return info


class View:
    """A view of a ``ConnectomeDataset`` specifying subsets of cells (or lists of cells) as ``NodeSet``s, e.g. can be used to just show the connections between the pharyngeal neurons in a whole connectome dataset, or to group the sensory neurons, interneuron, etc. together."""

    def __init__(
        self,
        id,
        name,
        description,
        node_sets,
        synclass_sets={},
        colormap=DEFAULT_COLORMAP,
        only_show_existing_nodes=False,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.node_sets = node_sets
        self.synclass_sets = synclass_sets
        self.colormap = colormap
        self.only_show_existing_nodes = only_show_existing_nodes

    def __repr__(self):
        info = "ConnectomeView: %s (%s)" % (
            self.name,
            self.id,
        )
        if self.description is not None:
            info += "\n  %s" % self.description
        for n in self.node_sets:
            info += "\n    %s" % n
        return info

    def has_color(self):
        for ns in self.node_sets:
            if ns.color is not None:
                return True
        return False

    def has_multicell_nodes(self):
        for ns in self.node_sets:
            if not ns.is_one_cell():
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


putative_exc_syn_class = ALL_KNOWN_CHEMICAL_NEUROTRANSMITTERS.copy()

putative_exc_syn_class.remove("GABA")

EXC_INH_GJ_SYN_CLASSES = {
    "Chemical Exc": [GENERIC_CHEM_SYN] + putative_exc_syn_class,
    "Chemical Inh": ["GABA"],
    "Electrical": [GENERIC_ELEC_SYN],
    "Extrasynaptic": ALL_KNOWN_EXTRASYNAPTIC_CLASSES,
}

EXC_INH_GJ_FUNC_CONT_SYN_CLASSES = copy.deepcopy(EXC_INH_GJ_SYN_CLASSES)
EXC_INH_GJ_FUNC_CONT_SYN_CLASSES["Functional"] = ["Functional"]
EXC_INH_GJ_FUNC_CONT_SYN_CLASSES["Contact"] = ["Contact"]

ALL_SYN_CLASSES = {
    "All synapses": [GENERIC_CHEM_SYN]
    + putative_exc_syn_class
    + ["GABA"]
    + [GENERIC_ELEC_SYN]
    + ALL_KNOWN_EXTRASYNAPTIC_CLASSES
    + ["Functional"]
    + ["Contact"]
}

CHEM_GJ_SYN_CLASSES = {
    "Chemical": EXC_INH_GJ_SYN_CLASSES["Chemical Exc"]
    + EXC_INH_GJ_SYN_CLASSES["Chemical Inh"],
    "Electrical": [GENERIC_ELEC_SYN],
    "Extrasynaptic": EXC_INH_GJ_SYN_CLASSES["Extrasynaptic"],
}

CHEM_GJ_FUNC_CONT_SYN_CLASSES = copy.deepcopy(CHEM_GJ_SYN_CLASSES)
CHEM_GJ_FUNC_CONT_SYN_CLASSES["Functional"] = ["Functional"]
CHEM_GJ_FUNC_CONT_SYN_CLASSES["Contact"] = ["Contact"]


RAW_VIEW = View(
    "Raw",
    "Raw Data",
    "All of the cells present in the original connectome dataset",
    [],
    CHEM_GJ_FUNC_CONT_SYN_CLASSES,
    only_show_existing_nodes=True,
)


NEURONS_VIEW = View(
    "Neurons",
    "Neurons",
    "All 302 **hermaphrodite** neurons (whether present or not in the connectome dataset)",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
)

SENSORY_NEURONS_SOMATIC_HERM_VIEW = View(
    "SensorySomaticH",
    "Sensory Neurons (somatic)",
    "All **hermaphrodite** sensory neurons except those in the pharynx",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
    only_show_existing_nodes=False,
)
INTERNEURONS_SOMATIC_HERM_VIEW = View(
    "InterneuronsSomaticH",
    "Interneurons (somatic)",
    "All **hermaphrodite** interneurons except those in the pharynx",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
    only_show_existing_nodes=False,
)
MOTORNEURONS_SOMATIC_HERM_VIEW = View(
    "MotorSomaticH",
    "Motor Neurons (somatic)",
    "All **hermaphrodite** motor neurons except those in the pharynx",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
    only_show_existing_nodes=False,
)

NONPHARYNGEAL_NEURONS_HERM_VIEW = View(
    "NonpharyngealH",
    "Nonpharyngeal Neurons (herm)",
    "All **hermaphrodite** neurons except those in the pharynx",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
    only_show_existing_nodes=False,
)

NONPHARYNGEAL_NEURONS_HM_VIEW = View(
    "NonpharyngealHM",
    "Nonpharyngeal Neurons",
    "All neurons (herm. & male) except those in the pharynx",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
    only_show_existing_nodes=False,
)

for cell in (
    sorted(PHARYNGEAL_NEURONS)
    + sorted(
        SENSORY_NEURONS_NONPHARYNGEAL_COOK
        + MALE_HEAD_SENSORY_NEURONS
        + MALE_NON_HEAD_SENSORY_NEURONS
    )
    + sorted(
        INTERNEURONS_NONPHARYNGEAL_COOK
        + MALE_HEAD_INTERNEURONS
        + MALE_NON_HEAD_INTERNEURONS
    )
    + sorted(
        HEAD_MOTORNEURONS_COOK
        + VENTRAL_CORD_MOTORNEURONS
        + SUBLATERAL_MOTORNEURONS_COOK
        + VC_HERM_MOTORNEURONS
        + HSN_MOTORNEURONS
    )
    + sorted(UNKNOWN_FUNCTION_NEURONS)
    + sorted(KNOWN_MODELLED_NEURONS)
):
    RAW_VIEW.node_sets.append(NodeSet(cell, [cell], get_standard_color(cell)))

    if cell not in MALE_SPECIFIC_NEURONS + KNOWN_MODELLED_NEURONS:
        NEURONS_VIEW.node_sets.append(NodeSet(cell, [cell], get_standard_color(cell)))

    if cell not in PHARYNGEAL_NEURONS:
        if cell not in MALE_SPECIFIC_NEURONS:
            NONPHARYNGEAL_NEURONS_HERM_VIEW.node_sets.append(
                NodeSet(cell, [cell], get_standard_color(cell))
            )
        NONPHARYNGEAL_NEURONS_HM_VIEW.node_sets.append(
            NodeSet(cell, [cell], get_standard_color(cell))
        )
        if cell in SENSORY_NEURONS_NONPHARYNGEAL_COOK:
            SENSORY_NEURONS_SOMATIC_HERM_VIEW.node_sets.append(
                NodeSet(cell, [cell], get_standard_color(cell))
            )
        if cell in MOTORNEURONS_NONPHARYNGEAL_COOK:
            MOTORNEURONS_SOMATIC_HERM_VIEW.node_sets.append(
                NodeSet(cell, [cell], get_standard_color(cell))
            )
        if cell in INTERNEURONS_NONPHARYNGEAL_COOK:
            INTERNEURONS_SOMATIC_HERM_VIEW.node_sets.append(
                NodeSet(cell, [cell], get_standard_color(cell))
            )


for cell in sorted(PREFERRED_MUSCLE_NAMES) + sorted(ALL_NON_NEURON_MUSCLE_CELLS):
    RAW_VIEW.node_sets.append(NodeSet(cell, [cell], get_standard_color(cell)))

assert len(NEURONS_VIEW.node_sets) == 302
assert len(RAW_VIEW.node_sets) == len(ALL_PREFERRED_CELL_NAMES + KNOWN_MODELLED_NEURONS)

PHARYNX_VIEW = View(
    "Pharynx",
    "Pharynx",
    "Only the 20 neurons of the pharynx (whether present or not in the connectome dataset)",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
)
for cell in sorted(PHARYNGEAL_NEURONS):
    PHARYNX_VIEW.node_sets.append(NodeSet(cell, [cell], get_standard_color(cell)))


ESCAPE_VIEW = View(
    "Escape",
    "Escape Response Circuit",
    "Escape Response Circuit from [Pirri & Alkema, 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3437330/)",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
)

len_scale = 1
step = len_scale * 0.3

esc_positions = {
    "ALM": (0, 0),
    "AVM": (step, 0),
    "PVM": (step * 3, 0),
    "PLM": (step * 4, 0),
    "PVC": (step, step * -1.3),
    "AVD": (step * 3, step * -1.3),
    "AVB": (0, step * -2.6),
    "AVA": (step * 4, step * -2.6),
    "RIM": (step * 2, step * -3.2),
    "RMD": (step * 1.5, step * -4.2),
    "SMD": (step * 2.5, step * -4.2),
    "VB/DB": (0, step * -3.9),
    "VA/DA": (step * 4, step * -3.9),
    "Body Musc": (step * 0.8, step * -5.2),
    "Head Musc": (step * 3.2, step * -5.2),
}


for cell_set in sorted(esc_positions.keys()):
    color = "purple"
    shape = "triangle-up"

    if cell_set in ["PVM", "PLM"]:
        color = "red"
    if cell_set in ["PVC", "AVB"]:
        color = "green"
        shape = "octagon"
    if cell_set in ["AVD", "AVA"]:
        color = "blue"
        shape = "octagon"
    if cell_set in ["RIM"]:
        color = "blue"
        shape = "circle"
    if cell_set in ["VB/DB"]:
        color = "lightgreen"
        shape = "circle"
    if cell_set in ["RMD", "SMD"]:
        color = "thistle"
        shape = "circle"
    if cell_set in ["VA/DA"]:
        color = "lightblue"
        shape = "circle"
    if "Musc" in cell_set:
        color = "dimgrey"
        shape = "diamond-wide"

    all_cells = []

    if cell_set == "VB/DB":
        for m in MOTORNEURONS_NONPHARYNGEAL_COOK:
            if "VB" in m or "DB" in m:
                all_cells.append(m)
    elif cell_set == "VA/DA":
        for m in MOTORNEURONS_NONPHARYNGEAL_COOK:
            if "VA" in m or "DA" in m:
                all_cells.append(m)
    elif cell_set == "Body Musc":
        for m in BODY_MUSCLES_COOK + UNSPECIFIED_BODY_WALL_MUSCLES:
            all_cells.append(m)
    elif cell_set == "Head Musc":
        for m in HEAD_MUSCLES_COOK:
            all_cells.append(m)

    elif cell_set in ["SMD"]:
        for s in ["DL", "DR", "VL", "VR"]:
            all_cells.append("%s%s" % (cell_set, s))

    elif cell_set in ["AVM", "PVM"]:
        all_cells.append(cell_set)
    else:
        all_cells = ["%sL" % cell_set, "%sR" % cell_set]

    ns = NodeSet(
        cell_set,
        all_cells,
        color=color,
        shape=shape,
        position=esc_positions[cell_set],
        size=len_scale * 80,
    )

    ESCAPE_VIEW.node_sets.append(ns)

MDLR = "MD"
MVLR = "MV"

loco1_2_positions = {
    "AVB": (step * -1, step * 0),
    "AVA": (step * 3, step * 0),
    "AS": (step * -1, step * 1.5),
    "DB": (0, step * 1),
    "DD": (step * 1, step * 0.8),
    "DA": (step * 2, step * 1),
    "VB": (0, step * -1),
    "VD": (step * 1, step * -0.8),
    "VA": (step * 2, step * -1),
    MDLR: (step * 1.5, step * 2),
    MVLR: (step * 1.5, step * -2),
}

mn_colors = {
    "DA": ".82 .7 .43",
    "DB": ".43 .69 .67",
    "DD": ".24 .32 .62",
    "VA": ".52 .33 .17",
    "VB": ".17 .4 .37",
    "VD": ".65 .78 .9",
    "AS": ".65 .2 .2",
    MDLR: ".2 .7 .2",
    MVLR: ".2 .7 .2",
}

LOCOMOTION_1_VIEW = View(
    "Loco1",
    "Locomotion 1",
    "Subset of cells involved in locomotion (work in progress!)",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
)

LOCOMOTION_2_VIEW = View(
    "Loco2",
    "Locomotion 2",
    "Subset of cells involved in locomotion (work in progress!)",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
)


def get_color_shape(cell_set):
    color = "purple"
    shape = "triangle-up"

    if cell_set in ["PVM", "PLM"]:
        color = "red"
    if cell_set in ["PVC", "AVB"]:
        color = "green"
        shape = "octagon"
    if cell_set in ["AVD", "AVA"]:
        color = "blue"
        shape = "octagon"
    if cell_set in ["RIM"]:
        color = "blue"
        shape = "circle"

    if cell_set in ["RMD", "SMD"]:
        color = "thistle"
        shape = "circle"
        shape = "circle"
    if "Musc" in cell_set:
        color = "dimgrey"
        shape = "diamond-wide"

    if cell_set in mn_colors or (len(cell_set) == 3 and cell_set[:2] in mn_colors):
        cell_set_ref = cell_set[:2]
        rgb = [int(float(c) * 256) for c in mn_colors[cell_set_ref].split()]
        color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
        # print(f"{cell_set} has color {mn_colors[cell_set_ref]}: {color}")
        shape = "circle"

    return color, shape


for cell_set in sorted(loco1_2_positions.keys()):
    color, shape = get_color_shape(cell_set)

    all_cells = []

    for cc in ["VA", "VB", "VD", "DA", "DB", "DD", "AS"]:
        # print("Adding " + cc)
        if cell_set == cc:
            for m in MOTORNEURONS_NONPHARYNGEAL_COOK + KNOWN_MODELLED_NEURONS:
                if m.startswith(cc):
                    all_cells.append(m)

    for cc in [MDLR, MVLR]:
        # print("Adding " + cc)
        if cell_set == cc:
            for m in BODY_MUSCLES_COOK:
                if m.startswith(cc):
                    all_cells.append(m)

    if cell_set in ["AVA", "AVB"]:
        all_cells = ["%sL" % cell_set, "%sR" % cell_set]

    ns = NodeSet(
        cell_set,
        all_cells,
        color=color,
        shape=shape,
        position=loco1_2_positions[cell_set],
        size=len_scale * 80,
    )

    if cell_set in [MDLR, MVLR]:
        LOCOMOTION_2_VIEW.node_sets.append(ns)

    elif cell_set in ["AS"]:
        LOCOMOTION_2_VIEW.node_sets.append(ns)

    elif cell_set in ["AVA", "AVB"]:
        LOCOMOTION_1_VIEW.node_sets.append(ns)

    else:
        LOCOMOTION_1_VIEW.node_sets.append(ns)
        LOCOMOTION_2_VIEW.node_sets.append(ns)


LOCOMOTION_3_VIEW = View(
    "Loco3",
    "Locomotion 3",
    "Subset of cells involved in locomotion (work in progress!)",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
)

hspacing = 7
vspacing = 10
max_mn = {"DB": 7, "DD": 6, "DA": 9, "VA": 12, "VD": 13, "VB": 11}
step = len_scale * 0.05
node_size = 40
total_width = 16

loco3_positions = {
    "AVB": (step * -1, step * 0),
    "AVA": (step * hspacing * total_width, step * 0),
    "DB": (0, step * vspacing * 3),
    "DD": (step * 1, step * vspacing * 2),
    "DA": (step * 2, step * vspacing * 1),
    "VB": (0, step * vspacing * -3),
    "VD": (step * 1, step * vspacing * -2),
    "VA": (step * 2, step * vspacing * -1),
}


mn_range = range(1, 4)
for cell_set in sorted(loco3_positions.keys()):
    color, shape = get_color_shape(cell_set)

    all_cells = []

    for cc in ["VA", "VB", "VD", "DA", "DB", "DD"]:
        # print("Adding " + cc)
        if cell_set == cc:
            for m in sorted(MOTORNEURONS_NONPHARYNGEAL_COOK):
                if m.startswith(cc):
                    # print("Adding %s" % m)

                    all_cells = [m]

                    pos = loco3_positions[cell_set]

                    pos = (
                        pos[0]
                        + (
                            int(m[2:])
                            * step
                            * hspacing
                            * ((total_width - 2) / max_mn[cell_set])
                        ),
                        pos[1],
                    )

                    ns = NodeSet(
                        m,
                        all_cells,
                        color=color,
                        shape=shape,
                        position=pos,
                        size=len_scale * node_size,
                    )

                    LOCOMOTION_3_VIEW.node_sets.append(ns)

    if cell_set in ["AVA", "AVB"]:
        all_cells = ["%sL" % cell_set, "%sR" % cell_set]

        ns = NodeSet(
            cell_set,
            all_cells,
            color=color,
            shape=shape,
            position=loco3_positions[cell_set],
            size=len_scale * node_size,
        )

        LOCOMOTION_3_VIEW.node_sets.append(ns)


PEP_HUBS_VIEW = View(
    "PeptidergicHubs",
    "Peptidergic Hubs",
    "Peptidergic hubs as outlined in in [Ripoll-Sánchez et al. 2023](../RipollSanchez_2023.md), Fig 7E",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
)

len_scale = 1.5

pep_positions = {
    "Periphery": [(0, 0), "Gainsboro"],
    "Motor core": [(-1 * len_scale, len_scale), "DarkSeaGreen"],
    "Sensory core": [(1 * len_scale, len_scale), "plum"],
    "Hubs": [(0, 2 * len_scale), "burlywood"],
}


clusters = load_hub_info()

for cluster, info in pep_positions.items():
    pos = info[0]
    color = info[1]

    shape = "circle"

    ns = NodeSet(
        cluster,
        clusters[cluster],
        color=color,
        shape=shape,
        position=pos,
        size=len_scale * 80,
    )

    PEP_HUBS_VIEW.node_sets.append(ns)


SOCIAL_VIEW = View(
    "Social",
    "Social Network",
    "Hub and spoke circuit for social behavior as in Macosko et al. 2009",
    [],
    EXC_INH_GJ_FUNC_CONT_SYN_CLASSES,
)

len_scale = 1.5

soc_positions = {
    "RMG": (0, 0),
    "RMH": (0, len_scale),
    "URX": (0.7 * len_scale, 0.7 * len_scale),
    "AWB": (len_scale, 0),
    "IL2": (0.7 * len_scale, -0.7 * len_scale),
    "ADL": (-0.7 * len_scale, -0.7 * len_scale),
    "ASH": (-1 * len_scale, 0),
    "ASK": (-0.7 * len_scale, 0.7 * len_scale),
}

for cell_pair in sorted(soc_positions.keys()):
    color = "grey"
    shape = "triangle-up"

    if cell_pair in ["RMG", "RMH"]:
        color = "lightgrey"
        shape = "octagon"

    ns = NodeSet(
        cell_pair,
        ["%sL" % cell_pair, "%sR" % cell_pair],
        color=color,
        shape=shape,
        position=soc_positions[cell_pair],
        size=len_scale * 80,
    )

    SOCIAL_VIEW.node_sets.append(ns)

COOK_FIG3_VIEW = View(
    "Full1",
    "Cook 2019 Fig 3",
    "A view of the data set with neurons grouped as in Figure 3 of Cook et al. 2019",
    [],
    CHEM_GJ_FUNC_CONT_SYN_CLASSES,
)

sn_pos = {
    "SN1": (2, 2.8),
    "SN2": (6.1, 2.9),
    "SN3": (6, 4.3),
    "SN4": (2.4, 3.6),
    "SN5": (3.4, 5.3),
    "SN6": (4, 5.4),
}

for category in SENSORY_NEURONS_COOK_CATEGORIES:
    color = "#b31b1b"
    if category == "SN1":
        color = "#FFC0CB"
    COOK_FIG3_VIEW.node_sets.append(
        NodeSet(
            category,
            SENSORY_NEURONS_COOK_CATEGORIES[category],
            color=color,
            shape="triangle-up",
            position=sn_pos[category],
        )
    )

in_pos = {"IN1": (4.2, 3.3), "IN2": (3.4, 4.2), "IN3": (5.1, 4.4), "IN4": (2.3, 4.8)}

for category in INTERNEURONS_NONPHARYNGEAL_COOK_CATEGORIES:
    if category != "RIML":
        COOK_FIG3_VIEW.node_sets.append(
            NodeSet(
                category,
                INTERNEURONS_NONPHARYNGEAL_COOK_CATEGORIES[category],
                color="#16537E",
                shape="hexagon2",
                position=in_pos[category],
            )
        )

COOK_FIG3_VIEW.node_sets.append(
    NodeSet(
        "HMN",
        HEAD_MOTORNEURONS_COOK,
        color="#FFDF00",
        shape="circle",
        position=(3.2, 2.2),
    )
)

COOK_FIG3_VIEW.node_sets.append(
    NodeSet(
        "SMN",
        SUBLATERAL_MOTORNEURONS_COOK,
        color="#e59636",
        shape="circle",
        position=(4.5, 2.2),
    )
)

COOK_FIG3_VIEW.node_sets.append(
    NodeSet(
        "MNVC",
        VENTRAL_CORD_MOTORNEURONS,
        color="#B2832b",
        shape="circle",
        position=(7.1, 1),
    )
)

COOK_FIG3_VIEW.node_sets.append(
    NodeSet(
        "VC", VC_HERM_MOTORNEURONS, color="#FF00FF", shape="circle", position=(7.8, 3.3)
    )
)

COOK_FIG3_VIEW.node_sets.append(
    NodeSet(
        "HSN", HSN_MOTORNEURONS, color="#FF00FF", shape="circle", position=(6.3, 5.9)
    )
)

COOK_FIG3_VIEW.node_sets.append(
    NodeSet(
        "MUBODY", BODY_MUSCLES_COOK, color="#5a2d0d", shape="square", position=(5, 0.73)
    )
)
COOK_FIG3_VIEW.node_sets.append(
    NodeSet(
        "MUHEAD", HEAD_MUSCLES_COOK, color="#5a2d0d", shape="square", position=(3.1, 1)
    )
)


ALL_VIEWS = [
    RAW_VIEW,
    NEURONS_VIEW,
    PHARYNX_VIEW,
    SOCIAL_VIEW,
    ESCAPE_VIEW,
    COOK_FIG3_VIEW,
    LOCOMOTION_1_VIEW,
    LOCOMOTION_2_VIEW,
    LOCOMOTION_3_VIEW,
    PEP_HUBS_VIEW,
    NONPHARYNGEAL_NEURONS_HERM_VIEW,
    SENSORY_NEURONS_SOMATIC_HERM_VIEW,
    MOTORNEURONS_SOMATIC_HERM_VIEW,
    INTERNEURONS_SOMATIC_HERM_VIEW,
]


if __name__ == "__main__":
    ns_v = NodeSet("Vmn", ["VA6", "VB6", "VB3", "VD6", "VA3", "VD3", "VB2"])
    ns_d = NodeSet("Dmn", ["DB4", "DD4"])
    ns_p = NodeSet("PVCL", ["PVCL"])
    ns_a = NodeSet("AVBL", ["AVBL"])

    v1 = View(
        "VandD", "V and D", "desc", [ns_d, ns_v, ns_a, ns_p], EXC_INH_GJ_SYN_CLASSES
    )

    v2 = View(
        "Donly",
        "Donly",
        "desc",
        [NodeSet("DB4", ["DB4"]), NodeSet("DD4", ["DD4"])],
        EXC_INH_GJ_SYN_CLASSES,
    )

    # from cect.TestDataReader import get_instance
    # from cect.Cook2019HermReader import get_instance
    from cect.White_whole import get_instance

    tdr_instance = get_instance()

    print(NodeSet(COOK_FIG3_VIEW, COOK_FIG3_VIEW))

    print(tdr_instance.summary())

    print("------- v1 ---------")
    print(tdr_instance.get_connectome_view(v1).summary())

    print("------- v2 ---------")
    print(tdr_instance.get_connectome_view(v2).summary())

    print("------- Raw ---------")
    print(tdr_instance.get_connectome_view(RAW_VIEW).summary())

    print("------- Neurons ---------")
    print(tdr_instance.get_connectome_view(NEURONS_VIEW).summary())

    print("-------- Social --------")
    view = SOCIAL_VIEW
    cv = tdr_instance.get_connectome_view(view)
    print(cv.summary())

    print("------- Nonpharyngeal ---------")
    print(tdr_instance.get_connectome_view(NONPHARYNGEAL_NEURONS_HM_VIEW).summary())

    print("------- Escape ---------")
    print(tdr_instance.get_connectome_view(ESCAPE_VIEW).summary())

    print("------- Locomotion 1 ---------")
    print(tdr_instance.get_connectome_view(LOCOMOTION_1_VIEW).summary())
    print(LOCOMOTION_1_VIEW)

    print("------- Locomotion 2 ---------")
    print(tdr_instance.get_connectome_view(LOCOMOTION_2_VIEW).summary())
    print(LOCOMOTION_2_VIEW)

    """
    from cect.Cells import ALL_PREFERRED_CELL_NAMES

    print("There are %i known cells..." % len(ALL_PREFERRED_CELL_NAMES))

    synclass = "Chemical Exc"
    G = cv.to_networkx_graph(synclass, view)
    import pprint
    import networkx as nx

    print(pprint.pprint(nx.node_link_data(G)))"""
