# -*- coding: utf-8 -*-

############################################################

#    Utilities for reading/writing/parsing NeuroML 2 files

############################################################

from cect import print_

DEFAULT_COLORMAP = ["white", "green", "black"]

PREFERRED_NEURON_NAMES = [
    "ADAL",
    "ADAR",
    "ADEL",
    "ADER",
    "ADFL",
    "ADFR",
    "ADLL",
    "ADLR",
    "AFDL",
    "AFDR",
    "AIAL",
    "AIAR",
    "AIBL",
    "AIBR",
    "AIML",
    "AIMR",
    "AINL",
    "AINR",
    "AIYL",
    "AIYR",
    "AIZL",
    "AIZR",
    "ALA",
    "ALML",
    "ALMR",
    "ALNL",
    "ALNR",
    "AQR",
    "AS1",
    "AS10",
    "AS11",
    "AS2",
    "AS3",
    "AS4",
    "AS5",
    "AS6",
    "AS7",
    "AS8",
    "AS9",
    "ASEL",
    "ASER",
    "ASGL",
    "ASGR",
    "ASHL",
    "ASHR",
    "ASIL",
    "ASIR",
    "ASJL",
    "ASJR",
    "ASKL",
    "ASKR",
    "AUAL",
    "AUAR",
    "AVAL",
    "AVAR",
    "AVBL",
    "AVBR",
    "AVDL",
    "AVDR",
    "AVEL",
    "AVER",
    "AVFL",
    "AVFR",
    "AVG",
    "AVHL",
    "AVHR",
    "AVJL",
    "AVJR",
    "AVKL",
    "AVKR",
    "AVL",
    "AVM",
    "AWAL",
    "AWAR",
    "AWBL",
    "AWBR",
    "AWCL",
    "AWCR",
    "BAGL",
    "BAGR",
    "BDUL",
    "BDUR",
    "CANL",
    "CANR",
    "CEPDL",
    "CEPDR",
    "CEPVL",
    "CEPVR",
    "DA1",
    "DA2",
    "DA3",
    "DA4",
    "DA5",
    "DA6",
    "DA7",
    "DA8",
    "DA9",
    "DB1",
    "DB2",
    "DB3",
    "DB4",
    "DB5",
    "DB6",
    "DB7",
    "DD1",
    "DD2",
    "DD3",
    "DD4",
    "DD5",
    "DD6",
    "DVA",
    "DVB",
    "DVC",
    "FLPL",
    "FLPR",
    "HSNL",
    "HSNR",
    "I1L",
    "I1R",
    "I2L",
    "I2R",
    "I3",
    "I4",
    "I5",
    "I6",
    "IL1DL",
    "IL1DR",
    "IL1L",
    "IL1R",
    "IL1VL",
    "IL1VR",
    "IL2DL",
    "IL2DR",
    "IL2L",
    "IL2R",
    "IL2VL",
    "IL2VR",
    "LUAL",
    "LUAR",
    "M1",
    "M2L",
    "M2R",
    "M3L",
    "M3R",
    "M4",
    "M5",
    "MCL",
    "MCR",
    "MI",
    "NSML",
    "NSMR",
    "OLLL",
    "OLLR",
    "OLQDL",
    "OLQDR",
    "OLQVL",
    "OLQVR",
    "PDA",
    "PDB",
    "PDEL",
    "PDER",
    "PHAL",
    "PHAR",
    "PHBL",
    "PHBR",
    "PHCL",
    "PHCR",
    "PLML",
    "PLMR",
    "PLNL",
    "PLNR",
    "PQR",
    "PVCL",
    "PVCR",
    "PVDL",
    "PVDR",
    "PVM",
    "PVNL",
    "PVNR",
    "PVPL",
    "PVPR",
    "PVQL",
    "PVQR",
    "PVR",
    "PVT",
    "PVWL",
    "PVWR",
    "RIAL",
    "RIAR",
    "RIBL",
    "RIBR",
    "RICL",
    "RICR",
    "RID",
    "RIFL",
    "RIFR",
    "RIGL",
    "RIGR",
    "RIH",
    "RIML",
    "RIMR",
    "RIPL",
    "RIPR",
    "RIR",
    "RIS",
    "RIVL",
    "RIVR",
    "RMDDL",
    "RMDDR",
    "RMDL",
    "RMDR",
    "RMDVL",
    "RMDVR",
    "RMED",
    "RMEL",
    "RMER",
    "RMEV",
    "RMFL",
    "RMFR",
    "RMGL",
    "RMGR",
    "RMHL",
    "RMHR",
    "SAADL",
    "SAADR",
    "SAAVL",
    "SAAVR",
    "SABD",
    "SABVL",
    "SABVR",
    "SDQL",
    "SDQR",
    "SIADL",
    "SIADR",
    "SIAVL",
    "SIAVR",
    "SIBDL",
    "SIBDR",
    "SIBVL",
    "SIBVR",
    "SMBDL",
    "SMBDR",
    "SMBVL",
    "SMBVR",
    "SMDDL",
    "SMDDR",
    "SMDVL",
    "SMDVR",
    "URADL",
    "URADR",
    "URAVL",
    "URAVR",
    "URBL",
    "URBR",
    "URXL",
    "URXR",
    "URYDL",
    "URYDR",
    "URYVL",
    "URYVR",
    "VA1",
    "VA10",
    "VA11",
    "VA12",
    "VA2",
    "VA3",
    "VA4",
    "VA5",
    "VA6",
    "VA7",
    "VA8",
    "VA9",
    "VB1",
    "VB10",
    "VB11",
    "VB2",
    "VB3",
    "VB4",
    "VB5",
    "VB6",
    "VB7",
    "VB8",
    "VB9",
    "VC1",
    "VC2",
    "VC3",
    "VC4",
    "VC5",
    "VC6",
    "VD1",
    "VD10",
    "VD11",
    "VD12",
    "VD13",
    "VD2",
    "VD3",
    "VD4",
    "VD5",
    "VD6",
    "VD7",
    "VD8",
    "VD9",
]

BODY_WALL_MUSCLE_NAMES = [
    "MANAL",
    "MDL01",
    "MDL02",
    "MDL03",
    "MDL04",
    "MDL05",
    "MDL06",
    "MDL07",
    "MDL08",
    "MDL09",
    "MDL10",
    "MDL11",
    "MDL12",
    "MDL13",
    "MDL14",
    "MDL15",
    "MDL16",
    "MDL17",
    "MDL18",
    "MDL19",
    "MDL20",
    "MDL21",
    "MDL22",
    "MDL23",
    "MDL24",
    "MDR01",
    "MDR02",
    "MDR03",
    "MDR04",
    "MDR05",
    "MDR06",
    "MDR07",
    "MDR08",
    "MDR09",
    "MDR10",
    "MDR11",
    "MDR12",
    "MDR13",
    "MDR14",
    "MDR15",
    "MDR16",
    "MDR17",
    "MDR18",
    "MDR19",
    "MDR20",
    "MDR21",
    "MDR22",
    "MDR23",
    "MDR24",
    "MVL01",
    "MVL02",
    "MVL03",
    "MVL04",
    "MVL05",
    "MVL06",
    "MVL07",
    "MVL08",
    "MVL09",
    "MVL10",
    "MVL11",
    "MVL12",
    "MVL13",
    "MVL14",
    "MVL15",
    "MVL16",
    "MVL17",
    "MVL18",
    "MVL19",
    "MVL20",
    "MVL21",
    "MVL22",
    "MVL23",
    "MVR01",
    "MVR02",
    "MVR03",
    "MVR04",
    "MVR05",
    "MVR06",
    "MVR07",
    "MVR08",
    "MVR09",
    "MVR10",
    "MVR11",
    "MVR12",
    "MVR13",
    "MVR14",
    "MVR15",
    "MVR16",
    "MVR17",
    "MVR18",
    "MVR19",
    "MVR20",
    "MVR21",
    "MVR22",
    "MVR23",
    "MVR24",
]


VULVAL_MUSCLE_NAMES = [
    "MVULVA",
    "vm1AL",
    "vm1PL",
    "vm1PR",
    "vm1AR",
    "vm2AL",
    "vm2AR",
    "vm2PL",
    "vm2PR",
]

PHARANGEAL_MUSCLE_NAMES = [
    "pm1",
    "pm2D",
    "pm2VL",
    "pm2VR",
    "pm3D",
    "pm3VL",
    "pm3VR",
    "pm4D",
    "pm4VR",
    "pm4VL",
    "pm5D",
    "pm5VR",
    "pm5VL",
    "pm6D",
    "pm6VR",
    "pm6VL",
    "pm7D",
    "pm7VL",
    "pm7VR",
    "pm8",
]


PREFERRED_MUSCLE_NAMES = (
    BODY_WALL_MUSCLE_NAMES + PHARANGEAL_MUSCLE_NAMES + VULVAL_MUSCLE_NAMES
)

PHARYNX_CELLS = [
    "M1",
    "M2L",
    "M2R",
    "M3L",
    "M3R",
    "M4",
    "M5",
    "I1L",
    "I1R",
    "I2L",
    "I2R",
    "I3",
    "I4",
    "I5",
    "I6",
    "MI",
    "NSML",
    "NSMR",
    "MCL",
    "MCR",
]

KNOWN_OTHER_CELLS_COOK_19 = [
    "CEPshDL",
    "CEPshDR",
    "CEPshVL",
    "CEPshVR",
    "GLRDL",
    "GLRDR",
    "GLRL",
    "GLRR",
    "GLRVL",
    "GLRVR",
    "bm",
    "e2D",
    "e2VL",
    "e2VR",
    "e3D",
    "e3VL",
    "e3VR",
    "exc_cell",
    "exc_gl",
    "g1AL",
    "g1AR",
    "g1p",
    "g2L",
    "g2R",
    "hmc",
    "hyp",
    "int",
    "mc1DL",
    "mc1DR",
    "mc1V",
    "mc2DL",
    "mc2DR",
    "mc2V",
    "mc3DL",
    "mc3DR",
    "mc3V",
    "mu_anal",
    "mu_intL",
    "mu_intR",
    "mu_sph",
]
KNOWN_OTHER_CELLS_COOK_20 = [
    "bm",
    "e2DL",
    "e2DR",
    "e2V",
    "e3D",
    "e3VL",
    "e3VR",
    "g1AL",
    "g1AR",
    "g1P",
    "g2L",
    "g2R",
    "mc2DL",
    "mc2DR",
    "mc2V",
    "mc2dl",
    "mc2dr",
    "mc3V",
]

KNOWN_OTHER_CELLS = KNOWN_OTHER_CELLS_COOK_19

for cell in KNOWN_OTHER_CELLS_COOK_20:
    if not cell in KNOWN_OTHER_CELLS:
        KNOWN_OTHER_CELLS.append(cell)


def convert_to_preferred_muscle_name(muscle):
    if muscle.startswith("BWM-VL"):
        return "MVL%s" % muscle[6:]
    elif muscle.startswith("BWM-VR"):
        return "MVR%s" % muscle[6:]
    elif muscle.startswith("BWM-DL"):
        return "MDL%s" % muscle[6:]
    elif muscle.startswith("BWM-DR"):
        return "MDR%s" % muscle[6:]
    elif muscle == "LegacyBodyWallMuscles":
        return "BWM"
    elif muscle == "pm3vl":
        return "pm3VL"
    elif muscle == "pm3vr":
        return "pm3VR"
    else:
        if is_muscle(muscle):
            return muscle
        else:
            return muscle + "???"


def get_standard_color(cell):
    if is_muscle(cell):
        return "#00dd00"
    elif cell in PHARYNX_CELLS:
        return "#0000dd"
    elif cell in PREFERRED_NEURON_NAMES:
        return "#dd0000"
    else:
        return "#dddd00"


def get_all_muscle_prefixes():
    return ["pm", "vm", "um"] + get_body_wall_muscle_prefixes()


def get_body_wall_muscle_prefixes():
    return ["BWM-D", "BWM-V", "LegacyBodyWallMuscles", "vBWM", "dBWM"]


def is_muscle(cell):
    known_muscle_prefixes = get_all_muscle_prefixes()
    return cell.startswith(tuple(known_muscle_prefixes))


def is_body_wall_muscle(cell):
    known_muscle_prefixes = get_body_wall_muscle_prefixes()
    return cell.startswith(tuple(known_muscle_prefixes))


def is_neuron(cell):
    return not is_muscle(cell)


def remove_leading_index_zero(cell):
    """
    Returns neuron name with an index without leading zero. E.g. VB01 -> VB1.
    """
    if is_neuron(cell) and cell[-2:].startswith("0"):
        return "%s%s" % (cell[:-2], cell[-1:])
    return cell


class ConnectionInfo:
    def __init__(self, pre_cell, post_cell, number, syntype, synclass):
        self.pre_cell = pre_cell
        self.post_cell = post_cell
        self.number = number
        self.syntype = syntype
        self.synclass = synclass

    def __str__(self):
        return "Connection from %s to %s (%i times, type: %s, neurotransmitter: %s)" % (
            self.pre_cell,
            self.post_cell,
            self.number,
            self.syntype,
            self.synclass,
        )

    def short(self):
        return "Connection from %s to %s (%s)" % (
            self.pre_cell,
            self.post_cell,
            self.syntype,
        )

    def __eq__(self, other):
        return (
            other.pre_cell == self.pre_cell
            and other.post_cell == self.post_cell
            and other.number == self.number
            and other.syntype == self.syntype
            and other.synclass == self.synclass
        )

    def __lt__(self, other):
        if other.pre_cell + other.post_cell > self.pre_cell + self.post_cell:
            return True
        else:
            return False

    def __repr__(self):
        return self.__str__()


def check_neurons(cells):
    preferred = []
    not_in_preferred = []
    missing_preferred = [n for n in PREFERRED_NEURON_NAMES]
    for c in cells:
        if not c in PREFERRED_NEURON_NAMES:
            if not is_muscle(c):
                not_in_preferred.append(c)
        else:
            preferred.append(c)
        if c in missing_preferred:
            missing_preferred.remove(c)

    return preferred, not_in_preferred, missing_preferred


def analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns):
    print_("Found %s cells: %s\n" % (len(cells), sorted(cells)))
    # assert(len(cells) == 302)
    # print_("Expected number of cells correct if include_nonconnected_cells=True")

    preferred, not_in_preferred, missing_preferred = check_neurons(cells)

    print_(
        "Found %s non-neuron(s) here: %s\n"
        % (len(not_in_preferred), sorted(not_in_preferred))
    )
    print_("Known neurons not present: %s\n" % (sorted(missing_preferred)))

    print_("Found %s connections..." % (len(neuron_conns)))
    for c in neuron_conns[:5]:
        print_("   %s" % c)

    print_("   ...\n")
    nts = {}
    nts_tot = {}
    for c in neuron_conns:
        nt = c.synclass
        if not nt in nts:
            nts[nt] = 0
            nts_tot[nt] = 0
        nts[nt] += 1
        nts_tot[nt] += c.number

    for nt in sorted(nts.keys()):
        print_(
            "   %s present in %s connections, %s synapses total (avg %.3f syns per conn)"
            % (nt, nts[nt], nts_tot[nt], nts_tot[nt] / nts[nt])
        )

    print_("")
    print_("   ---  Muscles  ---")
    print_("")

    print_("Found %s muscles: %s\n" % (len(muscles), sorted(muscles)))
    not_in_preferred = []
    for m in muscles:
        if not m in PREFERRED_MUSCLE_NAMES:
            not_in_preferred.append(m)

    print_(
        "Found %s unidentified muscles: %s\n"
        % (len(not_in_preferred), sorted(not_in_preferred))
    )

    print_(
        "Found %i neurons connected to muscles: %s\n"
        % (len(neurons2muscles), sorted(neurons2muscles))
    )
    print_(
        "Found %i muscles connected to neurons: %s\n" % (len(muscles), sorted(muscles))
    )

    print_(
        "Found %i connections between neurons and muscles%s\n"
        % (
            len(muscle_conns),
            (", e.g. %s" % muscle_conns[0]) if len(muscle_conns) > 0 else "",
        )
    )

    nts = {}
    nts_tot = {}
    for c in muscle_conns:
        nt = c.synclass
        if not nt in nts:
            nts[nt] = 0
            nts_tot[nt] = 0
        nts[nt] += 1
        nts_tot[nt] += c.number

    for nt in nts:
        print_(
            "  %s present in %s connections, %s synapses total (avg %.3f syns per conn)"
            % (nt, nts[nt], nts_tot[nt], nts_tot[nt] / nts[nt])
        )

    core_set = ["AVBL", "PVCL", "VA6", "VB6", "VD6", "DB4", "DD4"]
    # core_set = ['VA6', 'VD6']
    print_("\n\nConnections between cells in the subset %s:\n" % (core_set))

    for c in neuron_conns:
        if c.pre_cell in core_set and c.post_cell in core_set:
            print_(str(c))

    print_details_on = ["AVBR", "NSMR"]
    for cd in print_details_on:
        print_("\n\nAll outgoing connections of %s:\n" % (cd))
        for c in neuron_conns:
            if c.pre_cell == cd:
                print_(str(c))
        print_("\n\nAll incoming connections of %s:\n" % (cd))
        for c in neuron_conns:
            if c.post_cell == cd:
                print_(str(c))

    print_("")


if __name__ == "__main__":
    from SpreadsheetDataReader import read_data, read_muscle_data

    cells, neuron_conns = read_data(include_nonconnected_cells=True)
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)
