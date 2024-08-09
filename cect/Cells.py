# -*- coding: utf-8 -*-

############################################################

#    Information on cells in C. elegans
#    Much of this data taken from supplementary info of Ceook et al 2019

############################################################

import pandas as pd
import sys

from cect.WormAtlasInfo import WA_COLORS

cell_notes = {}

connectomes = None


SENSORY_NEURONS_1_COOK = [
    "IL2DL",
    "IL2DR",
    "IL2L",
    "IL2R",
    "IL2VL",
    "IL2VR",
    "CEPDL",
    "CEPDR",
    "CEPVL",
    "CEPVR",
    "OLQDL",
    "OLQDR",
    "OLQVL",
    "OLQVR",
    "URYDL",
    "URYDR",
    "URYVL",
    "URYVR",
    "OLLL",
    "OLLR",
    "IL1DL",
    "IL1DR",
    "IL1L",
    "IL1R",
    "IL1VL",
    "IL1VR",
]

for cell in SENSORY_NEURONS_1_COOK:
    cell_notes[cell] = "cephalic"

SENSORY_NEURONS_2_COOK = [
    "PHAL",
    "PHAR",
    "PHBL",
    "PHBR",
    "PHCL",
    "PHCR",
]

for cell in SENSORY_NEURONS_2_COOK:
    cell_notes[cell] = "phasmid"

SENSORY_NEURONS_3_COOK = [
    "ADEL",
    "ADER",
    "PDEL",
    "PDER",
    "ALML",
    "ALMR",
    "AVM",
    "PVM",
    "PLML",
    "PLMR",
    "FLPL",
    "FLPR",
    "DVA",
    "PVDL",
    "PVDR",
]

for cell in SENSORY_NEURONS_3_COOK:
    cell_notes[cell] = "mechanosensory"


SENSORY_NEURONS_4_COOK = [
    "BAGL",
    "BAGR",
    "URXL",
    "URXR",
    "ALNL",
    "ALNR",
    "PLNL",
    "PLNR",
    "SDQL",
    "SDQR",
    "AQR",
    "PQR",
]

for cell in SENSORY_NEURONS_4_COOK:
    if cell in ["BAGL", "BAGR", "URXL", "URXR"]:
        cell_notes[cell] = "O2, CO2, social signals, touch"
    else:
        cell_notes[cell] = "touch"


SENSORY_NEURONS_5_COOK = [
    "ASHL",
    "ASHR",
    "ADLL",
    "ADLR",
]

for cell in SENSORY_NEURONS_5_COOK:
    cell_notes[cell] = "amphid, nociceptive"

SENSORY_NEURONS_6_COOK = [
    "ASJL",
    "ASJR",
    "ASKL",
    "ASKR",
    "ASGL",
    "ASGR",
    "ASIL",
    "ASIR",
    "AFDL",
    "AFDR",
    "AWAL",
    "AWAR",
    "AWBL",
    "AWBR",
    "AWCL",
    "AWCR",
    "ASEL",
    "ASER",
    "ADFL",
    "ADFR",
]

for cell in SENSORY_NEURONS_6_COOK:
    cell_notes[cell] = "amphid"

SENSORY_NEURONS_COOK = (
    SENSORY_NEURONS_1_COOK
    + SENSORY_NEURONS_2_COOK
    + SENSORY_NEURONS_3_COOK
    + SENSORY_NEURONS_4_COOK
    + SENSORY_NEURONS_5_COOK
    + SENSORY_NEURONS_6_COOK
)

SENSORY_NEURONS_COOK_CATEGORIES = {
    "SN1": SENSORY_NEURONS_1_COOK,
    "SN2": SENSORY_NEURONS_2_COOK,
    "SN3": SENSORY_NEURONS_3_COOK,
    "SN4": SENSORY_NEURONS_4_COOK,
    "SN5": SENSORY_NEURONS_5_COOK,
    "SN6": SENSORY_NEURONS_6_COOK,
}

INTERNEURONS_4_COOK = [
    "AIML",
    "AIMR",
    "AINL",
    "AINR",
    "RIH",
    "URBL",
    "URBR",
    "RIR",
]

for cell in INTERNEURONS_4_COOK:
    cell_notes[cell] = "category 4 interneuron"

INTERNEURONS_3_COOK = [
    "PVQL",
    "PVQR",
    "ALA",
    "BDUL",
    "BDUR",
    "AIYL",
    "AIYR",
    "AIAL",
    "AIAR",
    "AUAL",
    "AUAR",
    "AIZL",
    "AIZR",
    "RIS",
    "ADAL",
    "ADAR",
    "RIFL",
    "RIFR",
    "PVR",
    "AVFL",
    "AVFR",
    "AVHL",
    "AVHR",
    "PVPL",
    "PVPR",
    "PVNL",
    "PVNR",
    "AVG",
    "LUAL",
    "LUAR",
    "DVB",
]

for cell in INTERNEURONS_3_COOK:
    cell_notes[cell] = "layer 3 interneuron"

INTERNEURONS_2_COOK = [
    "RIBL",
    "RIBR",
    "AIBL",
    "AIBR",
    "RIGL",
    "RIGR",
    "RMGL",
    "RMGR",
    "RICL",
    "RICR",
    "SAADR",
    "SAAVL",
    "SAADL",
    "SAAVR",
    "RMFL",
    "RMFR",
    "AVKL",
    "AVKR",
    "DVC",
    "AVJR",
    "AVJL",
    "PVT",
    "AVDL",
    "AVDR",
    "AVL",
    "PVWL",
    "PVWR",
]


for cell in INTERNEURONS_2_COOK:
    cell_notes[cell] = "layer 2 interneuron"

INTERNEURONS_1_COOK = [
    "RIAL",
    "RIAR",
    "RIML",
    "RIMR",
    "AVEL",
    "AVER",
    "RID",
    "AVBL",
    "AVBR",
    "AVAL",
    "AVAR",
    "PVCL",
    "PVCR",
]

for cell in INTERNEURONS_1_COOK:
    cell_notes[cell] = "layer 1 interneuron"

for cell in ["RIML", "RIMR"]:
    cell_notes[cell] += "; motorneuron in White et al., 1986"

INTERNEURONS_LINK_TO_PHARYNX_COOK = ["RIPL", "RIPR"]

for cell in INTERNEURONS_LINK_TO_PHARYNX_COOK:
    cell_notes[cell] = "linker to pharynx"

INTERNEURONS_NONPHARYNGEAL_COOK = (
    INTERNEURONS_1_COOK
    + INTERNEURONS_2_COOK
    + INTERNEURONS_3_COOK
    + INTERNEURONS_4_COOK
    + INTERNEURONS_LINK_TO_PHARYNX_COOK
)

INTERNEURONS_NONPHARYNGEAL_COOK_CATEGORIES = {
    "IN1": INTERNEURONS_1_COOK,
    "IN2": INTERNEURONS_2_COOK,
    "IN3": INTERNEURONS_3_COOK,
    "IN4": INTERNEURONS_4_COOK,
    "RIML": INTERNEURONS_LINK_TO_PHARYNX_COOK,
}


HEAD_MOTORNEURONS_COOK = [
    "URADL",
    "URADR",
    "URAVL",
    "URAVR",
    "RMEL",
    "RMER",
    "RMED",
    "RMEV",
    "RMDDL",
    "RMDDR",
    "RMDL",
    "RMDR",
    "RMDVL",
    "RMDVR",
    "RIVL",
    "RIVR",
    "RMHL",
    "RMHR",
]

for cell in HEAD_MOTORNEURONS_COOK:
    cell_notes[cell] = "head motor neuron"

SUBLATERAL_MOTORNEURONS_COOK = [
    "SABD",
    "SABVL",
    "SABVR",
    "SMDDL",
    "SMDDR",
    "SMDVL",
    "SMDVR",
    "SMBDL",
    "SMBDR",
    "SMBVL",
    "SMBVR",
    "SIBDL",
    "SIBDR",
    "SIBVL",
    "SIBVR",
    "SIADL",
    "SIADR",
    "SIAVL",
    "SIAVR",
]


for cell in SUBLATERAL_MOTORNEURONS_COOK:
    cell_notes[cell] = "sublateral motor neuron"

for cell in [
    "SABD",
    "SABVL",
    "SABVR",
    "SIBDL",
    "SIBDR",
    "SIBVL",
    "SIBVR",
    "SIADL",
    "SIADR",
    "SIAVL",
    "SIAVR",
]:
    cell_notes[cell] += "; interneuron in White et al., 1986"

VENTRAL_CORD_MOTORNEURONS = [
    "DA1",
    "DA2",
    "DA3",
    "DA4",
    "DA5",
    "DA6",
    "DA7",
    "DA8",
    "DA9",
    "PDA",
    "DB1",
    "DB2",
    "DB3",
    "DB4",
    "DB5",
    "DB6",
    "DB7",
    "AS1",
    "AS2",
    "AS3",
    "AS4",
    "AS5",
    "AS6",
    "AS7",
    "AS8",
    "AS9",
    "AS10",
    "AS11",
    "PDB",
    "DD1",
    "DD2",
    "DD3",
    "DD4",
    "DD5",
    "DD6",
    "VA1",
    "VA2",
    "VA3",
    "VA4",
    "VA5",
    "VA6",
    "VA7",
    "VA8",
    "VA9",
    "VA10",
    "VA11",
    "VA12",
    "VB1",
    "VB2",
    "VB3",
    "VB4",
    "VB5",
    "VB6",
    "VB7",
    "VB8",
    "VB9",
    "VB10",
    "VB11",
    "VD1",
    "VD2",
    "VD3",
    "VD4",
    "VD5",
    "VD6",
    "VD7",
    "VD8",
    "VD9",
    "VD10",
    "VD11",
    "VD12",
    "VD13",
]

for cell in VENTRAL_CORD_MOTORNEURONS:
    cell_notes[cell] = "ventral cord motor neuron"


HSN_MOTORNEURONS = [
    "HSNL",
    "HSNR",
]


VC_HERM_MOTORNEURONS = [
    "VC1",
    "VC2",
    "VC3",
    "VC4",
    "VC5",
    "VC6",
]

HERM_SPECIFIC_MOTORNEURONS = HSN_MOTORNEURONS + VC_HERM_MOTORNEURONS

for cell in HERM_SPECIFIC_MOTORNEURONS:
    cell_notes[cell] = "hermaphrodite specific motor neuron"

UNKNOWN_FUNCTION_NEURONS = ["CANL", "CANR"]

for cell in UNKNOWN_FUNCTION_NEURONS:
    cell_notes[cell] = "canal neuron"


PHARYNGEAL_MOTORNEURONS = [
    "M1",
    "M2L",
    "M2R",
    "M3L",
    "M3R",
    "M4",
    "M5",
]

for cell in PHARYNGEAL_MOTORNEURONS:
    cell_notes[cell] = "pharyngeal motor neuron"

PHARYNGEAL_INTERNEURONS = [
    "I1L",
    "I1R",
    "I2L",
    "I2R",
    "I3",
    "I4",
    "I5",
    "I6",
]

for cell in PHARYNGEAL_INTERNEURONS:
    cell_notes[cell] = "pharyngeal interneuron"

PHARYNGEAL_POLYMODAL_NEURONS = [
    "MI",
    "NSML",
    "NSMR",
    "MCL",
    "MCR",
]

for cell in PHARYNGEAL_POLYMODAL_NEURONS:
    cell_notes[cell] = "pharyngeal polymodal neuron"

INTERNEURONS_COOK = INTERNEURONS_NONPHARYNGEAL_COOK + PHARYNGEAL_INTERNEURONS

PHARYNGEAL_NEURONS = (
    PHARYNGEAL_INTERNEURONS + PHARYNGEAL_MOTORNEURONS + PHARYNGEAL_POLYMODAL_NEURONS
)

MOTORNEURONS_COOK = (
    HEAD_MOTORNEURONS_COOK
    + SUBLATERAL_MOTORNEURONS_COOK
    + VENTRAL_CORD_MOTORNEURONS
    + PHARYNGEAL_MOTORNEURONS
    + HERM_SPECIFIC_MOTORNEURONS
)

PREFERRED_NEURON_NAMES_COOK = (
    INTERNEURONS_COOK
    + SENSORY_NEURONS_COOK
    + MOTORNEURONS_COOK
    + PHARYNGEAL_POLYMODAL_NEURONS
    + UNKNOWN_FUNCTION_NEURONS
)


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

for n in PREFERRED_NEURON_NAMES:
    assert n in PREFERRED_NEURON_NAMES_COOK
for n in PREFERRED_NEURON_NAMES_COOK:
    assert n in PREFERRED_NEURON_NAMES

assert len(PREFERRED_NEURON_NAMES_COOK) == len(PREFERRED_NEURON_NAMES)

BODY_WALL_MUSCLE_NAMES = [
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

HEAD_MUSCLES_COOK = []
BODY_MUSCLES_COOK = []

for bwm in BODY_WALL_MUSCLE_NAMES:
    num = int(bwm[3:5])
    if num < 8:
        HEAD_MUSCLES_COOK.append(bwm)
        cell_notes[bwm] = "head muscle"
    else:
        BODY_MUSCLES_COOK.append(bwm)
        cell_notes[bwm] = "main body muscle"


ANAL_SPHINCTER_MUSCLES = ["MANAL", "mu_sph", "mu_anal"]  # TODO: remove duplicate!

for cell in ANAL_SPHINCTER_MUSCLES:
    cell_notes[cell] = "anal/sphincter muscle"

VULVAL_MUSCLE_NAMES = [
    "MVULVA",
    "um2AL",
    "um2AR",
    "um1AL",
    "um1AR",
    "um1PL",
    "um1PR",
    "um2PL",
    "um2PR",
    "vm1AL",
    "vm1PL",
    "vm1PR",
    "vm1AR",
    "vm2AL",
    "vm2AR",
    "vm2PL",
    "vm2PR",
]
for cell in VULVAL_MUSCLE_NAMES:
    cell_notes[cell] = "vulval muscle"

ODD_PHARYNGEAL_MUSCLE_NAMES = [
    "pm1",
    "pm3D",
    "pm3VL",
    "pm3VR",
    "pm5D",
    "pm5VR",
    "pm5VL",
    "pm7D",
    "pm7VL",
    "pm7VR",
]

EVEN_PHARYNGEAL_MUSCLE_NAMES = [
    "pm2D",
    "pm2VL",
    "pm2VR",
    "pm4D",
    "pm4VR",
    "pm4VL",
    "pm6D",
    "pm6VR",
    "pm6VL",
    "pm8",
]


PHARYNGEAL_MUSCLE_NAMES = ODD_PHARYNGEAL_MUSCLE_NAMES + EVEN_PHARYNGEAL_MUSCLE_NAMES

for cell in PHARYNGEAL_MUSCLE_NAMES:
    cell_notes[cell] = "pharyngeal muscle"

PREFERRED_MUSCLE_NAMES = (
    BODY_WALL_MUSCLE_NAMES
    + PHARYNGEAL_MUSCLE_NAMES
    + VULVAL_MUSCLE_NAMES
    + ANAL_SPHINCTER_MUSCLES
)

GLR_CELLS = [
    "GLRDL",
    "GLRDR",
    "GLRL",
    "GLRR",
    "GLRVL",
    "GLRVR",
]

for cell in GLR_CELLS:
    cell_notes[cell] = "GLR cell"

CEPSH_CELLS = [
    "CEPshDL",
    "CEPshDR",
    "CEPshVL",
    "CEPshVR",
]

for cell in CEPSH_CELLS:
    cell_notes[cell] = "glial"

GLIAL_CELLS = GLR_CELLS + CEPSH_CELLS


PHARYNGEAL_MARGINAL_CELLS = [
    "mc1DL",
    "mc1DR",
    "mc1V",
    "mc2DL",
    "mc2DR",
    "mc2V",
    "mc3DL",
    "mc3DR",
    "mc3V",
]

for cell in PHARYNGEAL_MARGINAL_CELLS:
    cell_notes[cell] = "marginal cell of the pharynx"

PHARYNGEAL_EPITHELIUM = [
    "e2DL",
    "e2DR",
    "e2D",
    "e2V",
    "e2VL",
    "e2VR",
    "e3D",
    "e3VL",
    "e3VR",
]

for cell in PHARYNGEAL_EPITHELIUM:
    cell_notes[cell] = "pharyngeal epithelium"

PHARYNGEAL_GLIAL_CELL = [
    "g1AL",
    "g1AR",
    "g1p",  # TODO remove!
    "g1P",
    "g2L",
    "g2R",
]

for cell in PHARYNGEAL_GLIAL_CELL:
    cell_notes[cell] = "pharyngeal glial cell"

PHARYNGEAL_BASEMENT_MEMBRANE = ["bm"]
cell_notes["bm"] = "pharyngeal basement membrane"

EXCRETORY_CELL = [
    "exc_cell",
]
cell_notes["exc_cell"] = "excretory cell"

EXCRETORY_GLAND = [
    "exc_gl",
]
cell_notes["exc_gl"] = "excretory gland"

HEAD_MESODERMAL_CELL = [
    "hmc",
]
cell_notes["hmc"] = "head mesodermal cell"

HYPODERMIS = [
    "hyp",
]
cell_notes["hyp"] = "hypodermis"

INTESTINE = [
    "int",
]
cell_notes["int"] = "intestine"

INTESTINAL_MUSCLES = [
    "mu_intL",
    "mu_intR",
]


for cell in INTESTINAL_MUSCLES:
    cell_notes[cell] = "intestinal muscles"


KNOWN_OTHER_CELLS_COOK_19 = (
    []
    + GLIAL_CELLS
    + PHARYNGEAL_MARGINAL_CELLS
    + PHARYNGEAL_EPITHELIUM
    + PHARYNGEAL_GLIAL_CELL
    + PHARYNGEAL_BASEMENT_MEMBRANE
    + EXCRETORY_CELL
    + EXCRETORY_GLAND
    + HEAD_MESODERMAL_CELL
    + HYPODERMIS
    + INTESTINE
    + INTESTINAL_MUSCLES
)


KNOWN_OTHER_CELLS = KNOWN_OTHER_CELLS_COOK_19


def get_standard_color(cell):
    from cect.WormAtlasInfo import WA_COLORS

    if cell in BODY_WALL_MUSCLE_NAMES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["body wall muscle"]
    elif cell in VULVAL_MUSCLE_NAMES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["vulval muscle"]
    elif cell in ODD_PHARYNGEAL_MUSCLE_NAMES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["odd numbered pharyngeal muscle"]
    elif cell in EVEN_PHARYNGEAL_MUSCLE_NAMES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["even numbered pharyngeal muscle"]
    elif cell in INTERNEURONS_COOK:
        return WA_COLORS["Hermaphrodite"]["Nervous Tissue"]["interneuron"]
    elif cell in SENSORY_NEURONS_COOK:
        return WA_COLORS["Hermaphrodite"]["Nervous Tissue"]["sensory neuron"]
    elif cell in MOTORNEURONS_COOK:
        return WA_COLORS["Hermaphrodite"]["Nervous Tissue"]["motor neuron"]
    elif cell in PHARYNGEAL_POLYMODAL_NEURONS:
        return WA_COLORS["Hermaphrodite"]["Nervous Tissue"]["polymodal neuron"]
    elif cell in PHARYNGEAL_MARGINAL_CELLS:
        return WA_COLORS["Hermaphrodite"]["Alimentary System"][
            "marginal cells (mc) of the pharynx"
        ]
    elif cell in PHARYNGEAL_EPITHELIUM:
        return WA_COLORS["Hermaphrodite"]["Epithelial Tissue"]["pharyngeal epithelium"]
    elif cell in PHARYNGEAL_GLIAL_CELL:
        return WA_COLORS["Hermaphrodite"]["Epithelial Tissue"][
            "pharyngeal epithelium"
        ]  # TODO: check!!
    elif cell in PHARYNGEAL_BASEMENT_MEMBRANE:
        return WA_COLORS["Hermaphrodite"]["Other Tissues"]["basement membrane"]
    elif cell in GLR_CELLS:
        return WA_COLORS["Hermaphrodite"]["Other Tissues"]["GLR cell"]
    elif cell in CEPSH_CELLS:
        return WA_COLORS["Hermaphrodite"]["Epithelial Tissue"][
            "sheath cell other than amphid sheath and phasmid"
        ]
    elif cell in UNKNOWN_FUNCTION_NEURONS:
        return WA_COLORS["Hermaphrodite"]["Nervous Tissue"][
            "neuron with unknown function"
        ]
    elif cell in ANAL_SPHINCTER_MUSCLES:
        return WA_COLORS["Hermaphrodite"]["Muscle"][
            "sphincter and anal depressor muscle"
        ]
    elif cell in EXCRETORY_CELL:
        return WA_COLORS["Hermaphrodite"]["Excretory System"]["excretory cell"]
    elif cell in EXCRETORY_GLAND:
        return WA_COLORS["Hermaphrodite"]["Excretory System"]["gland cell"]
    elif cell in HEAD_MESODERMAL_CELL:
        return WA_COLORS["Hermaphrodite"]["Other Tissues"]["head mesodermal cell"]
    elif cell in HYPODERMIS:
        return WA_COLORS["Hermaphrodite"]["Epithelial Tissue"]["hypodermis"]
    elif cell in INTESTINE:
        return WA_COLORS["Hermaphrodite"]["Alimentary System"]["intestinal cells"]
    elif cell in INTESTINAL_MUSCLES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["intestinal muscle"]

    else:
        raise Exception("Unknown cell: %s!" % cell)


def get_short_description(cell):
    if cell in cell_notes:
        desc = cell_notes[cell]
        if cell in SENSORY_NEURONS_COOK:
            desc = "Sensory neuron (%s)" % desc
        return desc[0].upper() + desc[1:]

    else:
        return "???"


"""
    if cell in BODY_WALL_MUSCLE_NAMES:
        return "Body wall muscle"
    elif cell in VULVAL_MUSCLE_NAMES:
        return "Vulval muscle"
    elif cell in ODD_PHARYNGEAL_MUSCLE_NAMES or cell in EVEN_PHARYNGEAL_MUSCLE_NAMES:
        return "Pharyngeal muscle"
    elif cell in PHARYNGEAL_INTERNEURONS:
        return "Pharyngeal interneuron"
    elif cell in PHARYNGEAL_MOTORNEURONS:
        return "Pharyngeal motor neuron"
    elif cell in PHARYNGEAL_POLYMODAL_NEURONS:
        return "Pharyngeal polymodal neuron"
    elif cell in HERM_SPECIFIC_MOTORNEURONS:
        return "Hermaphrodite specific motor neuron"
    elif cell in INTERNEURONS_NONPHARYNGEAL_COOK:
        return "Interneuron"
    elif cell in SENSORY_NEURONS_COOK:
        return "Sensory neuron"
    elif cell in MOTORNEURONS_COOK:
        return "Motor neuron"
    elif cell in GLR_CELLS:
        return "GLR cell"
    else:
        return "???"
"""


def get_cell_internal_link(cell_name, html=False, text=None):
    url = "../Cells/index.html#%s" % cell_name

    if html:
        return '<a href="%s">%s</a>' % (url, cell_name if text is None else text)
    else:
        return "[%s](%s)" % (cell_name if text is None else text, url)


def get_cell_link(cell_name, html=False, text=None):
    url = None

    known_indiv = ["SABD", "MI"]

    if (
        cell_name
        in PHARYNGEAL_MARGINAL_CELLS
        + PHARYNGEAL_EPITHELIUM
        + PHARYNGEAL_GLIAL_CELL
        + PHARYNGEAL_BASEMENT_MEMBRANE
        + PHARYNGEAL_MUSCLE_NAMES
    ):
        url = "https://www.wormatlas.org/hermaphrodite/pharynx/jump.html?newLink=mainframe.htm&newAnchor=Listofcellsinthepharynx11"
    elif cell_name in known_indiv:
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name
        )
    elif cell_name[-2:].isnumeric():
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-2]
        )
    elif cell_name[-1].isdigit():
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-1]
        )
    elif (
        cell_name.endswith("L")
        or cell_name.endswith("R")
        or cell_name.endswith("EV")
        or cell_name.endswith("ED")
        or cell_name.endswith("BD")
    ):
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-1]
        )
    elif len(cell_name) == 3:
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name
        )

    if url is not None:
        if html:
            return '<a href="%s">%s</a>' % (url, cell_name if text is None else text)
        else:
            return "[%s](%s)" % (cell_name if text is None else text, url)
    else:
        return cell_name


def _get_dataset_link(reader_name, html=False, text=None):
    url = "%s_data_graph.md" % reader_name

    if html:
        return '<a href="%s">%s</a>' % (url, reader_name if text is None else text)
    else:
        return "[%s](%s)" % (reader_name if text is None else text, url)


def _generate_cell_table(cell_type, cells):
    import plotly.express as px
    import plotly.graph_objects as go
    import numpy as np

    from cect.Comparison import _format_json
    from cect.Comparison import shorten_neurotransmitter

    all_syn_types = set([])
    for connectome in connectomes.values():
        for st in connectome.connections:
            all_syn_types.add(st)
    fig_md = ""

    for syn_type in all_syn_types:
        fig = go.Figure()
        fig.layout.showlegend = True

        fig_md += '\n=== "%s"\n\n' % syn_type
        fig_md += "    Connections to these cells of type: %s\n\n" % syn_type

        for reader_name, connectome in connectomes.items():
            sorted_cells = sorted(cells)

            indent = "    "
            nonempty_fig_present = False
            y = []
            for cell in sorted_cells:
                conns_from = connectome.get_connections_to(cell, syn_type)
                y.append(len(conns_from))

            if sum(y) > 0:
                marker_symbol = "square"
                dash = "solid"
                if "GJ" in syn_type:
                    marker_symbol = "circle"
                    dash = "dot"

                data = fig.add_scatter(
                    name="%s %s" % (reader_name, shorten_neurotransmitter(syn_type)),
                    x=sorted_cells,
                    y=y,
                    marker_symbol=marker_symbol,
                    line=dict(dash=dash),
                )
                nonempty_fig_present = True

        if nonempty_fig_present:
            asset_filename = "assets/%s_%s_hist.json" % (
                cell_type.replace(" ", "_"),
                syn_type,
            )

            with open("./docs/%s" % asset_filename, "w") as asset_file:
                asset_file.write(_format_json(fig.to_json()))

            fig_md += '\n%s```plotly\n%s---8<-- "./%s"\n%s```\n\n' % (
                indent,
                indent,
                asset_filename,
                indent,
            )
        else:
            fig_md += "    No connections of this type found.\n\n"

    all_data = {}

    all_data[""] = ["Notes", "Datasets", "Link"]

    for cell in sorted(cells):
        desc = cell_notes[cell] if cell in cell_notes else "???"
        desc = desc[0].upper() + desc[1:]

        datasets = " "
        for reader_name, conn in connectomes.items():
            if cell in conn.nodes:
                datasets += "%s, " % _get_dataset_link(reader_name)

        all_data[f'<a name="{cell}"></a>{cell}'] = [
            desc,
            datasets[:-2],
            get_cell_link(cell, text="WormAtlas"),
        ]

    df_all = pd.DataFrame(all_data).transpose()

    table_md = df_all.to_markdown()

    return "%s\n%s\n\n" % (fig_md, table_md)


if __name__ == "__main__":
    quick = len(sys.argv) > 1 and eval(sys.argv[1])

    from cect.Comparison import generate_comparison_page

    connectomes = generate_comparison_page(quick)

    filename = "docs/Cells.md"

    with open(filename, "w") as f:
        for sex in WA_COLORS:
            f.write("\n## %s\n" % sex)

            for cell_class in WA_COLORS[sex]:
                f.write("\n### %s\n\n" % cell_class)

                for cell_type in WA_COLORS[sex][cell_class]:
                    if not "General code" in cell_type:
                        color = WA_COLORS[sex][cell_class][cell_type][1:]
                        f.write(
                            "#### ![#{0}](https://via.placeholder.com/15/{0}/{0}.png) {1}\n".format(
                                color, cell_type[0].upper() + cell_type[1:]
                            )
                        )
                        if cell_type == "body wall muscle":
                            f.write(
                                _generate_cell_table(cell_type, BODY_WALL_MUSCLE_NAMES)
                            )
                        elif cell_type == "interneuron":
                            f.write(_generate_cell_table(cell_type, INTERNEURONS_COOK))
                        elif cell_type == "motor neuron":
                            f.write(_generate_cell_table(cell_type, MOTORNEURONS_COOK))
                        elif cell_type == "sensory neuron":
                            f.write(
                                _generate_cell_table(cell_type, SENSORY_NEURONS_COOK)
                            )
                        elif cell_type == "odd numbered pharyngeal muscle":
                            f.write(
                                _generate_cell_table(
                                    cell_type, ODD_PHARYNGEAL_MUSCLE_NAMES
                                )
                            )
                        elif cell_type == "even numbered pharyngeal muscle":
                            f.write(
                                _generate_cell_table(
                                    cell_type, EVEN_PHARYNGEAL_MUSCLE_NAMES
                                )
                            )
                        elif cell_type == "polymodal neuron":
                            f.write(
                                _generate_cell_table(
                                    cell_type, PHARYNGEAL_POLYMODAL_NEURONS
                                )
                            )
                        elif cell_type == "marginal cells (mc) of the pharynx":
                            f.write(
                                _generate_cell_table(
                                    cell_type, PHARYNGEAL_MARGINAL_CELLS
                                )
                            )
                        elif cell_type == "pharyngeal epithelium":
                            f.write(
                                _generate_cell_table(
                                    cell_type,
                                    PHARYNGEAL_EPITHELIUM + PHARYNGEAL_GLIAL_CELL,
                                )
                            )  # TODO: check!
                        elif cell_type == "basement membrane":
                            f.write(
                                _generate_cell_table(
                                    cell_type, PHARYNGEAL_BASEMENT_MEMBRANE
                                )
                            )  # TODO: check!
                        elif cell_type == "neuron with unknown function":
                            f.write(
                                _generate_cell_table(
                                    cell_type, UNKNOWN_FUNCTION_NEURONS
                                )
                            )
                        elif (
                            cell_type
                            == "sheath cell other than amphid sheath and phasmid"
                        ):
                            f.write(_generate_cell_table(cell_type, CEPSH_CELLS))
                        elif cell_type == "excretory cell":
                            f.write(_generate_cell_table(cell_type, EXCRETORY_CELL))
                        elif cell_type == "sphincter and anal depressor muscle":
                            f.write(
                                _generate_cell_table(cell_type, ANAL_SPHINCTER_MUSCLES)
                            )
                        elif cell_type == "gland cell":
                            f.write(_generate_cell_table(cell_type, EXCRETORY_GLAND))
                        elif cell_type == "head mesodermal cell":
                            f.write(
                                _generate_cell_table(cell_type, HEAD_MESODERMAL_CELL)
                            )
                        elif cell_type == "hypodermis":
                            f.write(_generate_cell_table(cell_type, HYPODERMIS))
                        elif cell_type == "intestinal cells":
                            f.write(_generate_cell_table(cell_type, INTESTINE))
                        elif cell_type == "intestinal muscle":
                            f.write(_generate_cell_table(cell_type, INTESTINAL_MUSCLES))
                        elif cell_type == "GLR cell":
                            f.write(_generate_cell_table(cell_type, GLR_CELLS))
