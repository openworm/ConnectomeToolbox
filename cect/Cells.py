# -*- coding: utf-8 -*-

############################################################

#    Information on cells in C. elegans
#    Much of this data taken from supplementary info of Ceook et al 2019

############################################################

import pandas as pd
import sys

from cect.WormAtlasInfo import WA_COLORS
from cect import print_

from typing import List


ALL_KNOWN_CHEMICAL_NEUROTRANSMITTERS = [
    "Acetylcholine",
    "Acetylcholine_Tyramine",
    "Dopamine",
    "FMRFamide",
    "GABA",
    "Glutamate",
    "Octapamine",
    "Serotonin",
    "Serotonin_Acetylcholine",
    "Serotonin_Glutamate",
]

GENERIC_CHEM_SYN = "Generic_CS"
GENERIC_ELEC_SYN = "Generic_GJ"

EXTRASYNAPTIC_SYN_TYPE = "Extrasynaptic"
MONOAMINERGIC_SYN_CLASS = "Monoaminergic"
PEPTIDERGIC_SYN_CLASS = "Peptidergic"

ALL_KNOWN_EXTRASYNAPTIC_CLASSES = [MONOAMINERGIC_SYN_CLASS, PEPTIDERGIC_SYN_CLASS]

cell_notes = {}

connectomes = None


def get_cell_notes(cell: str):
    """Get a short description of the cell, mainly cell type

    Args:
        cell (str): Name of the cell

    Returns:
        str: Description of the cell type
    """
    desc = cell_notes[cell] if cell in cell_notes else "???"
    desc = desc[0].upper() + desc[1:]
    return desc


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


MALE_HEAD_INTERNEURONS = ["MCML", "MCMR"]
for cell in MALE_HEAD_INTERNEURONS:
    cell_notes[cell] = "male head interneuron"

MALE_HEAD_SENSORY_NEURONS = ["CEMDL", "CEMDR", "CEMVL", "CEMVR"]
for cell in MALE_HEAD_SENSORY_NEURONS:
    cell_notes[cell] = "male head sensory neuron"

MALE_NON_HEAD_SENSORY_NEURONS = [
    "R1AL",
    "R1AR",
    "R1BL",
    "R1BR",
    "R2AL",
    "R2AR",
    "R2BL",
    "R2BR",
    "R3AL",
    "R3AR",
    "R3BL",
    "R3BR",
    "R4AL",
    "R4AR",
    "R4BL",
    "R4BR",
    "R5AL",
    "R5AR",
    "R5BL",
    "R5BR",
    "R6AL",
    "R6AR",
    "R6BL",
    "R6BR",
    "R7AL",
    "R7AR",
    "R7BL",
    "R7BR",
    "R8AL",
    "R8AR",
    "R8BL",
    "R8BR",
    "R9AL",
    "R9AR",
    "R9BL",
    "R9BR",
    "PHDL",
    "PHDR",
    "HOA",
    "HOB",
    "PCAL",
    "PCAR",
    "PCBL",
    "PCBR",
    "PCCL",
    "PCCR",
    "SPCL",
    "SPCR",
    "SPDL",
    "SPDR",
    "SPVL",
    "SPVR",
]

for cell in MALE_NON_HEAD_SENSORY_NEURONS:
    cell_notes[cell] = "male sensory neuron"

MALE_NON_HEAD_INTERNEURONS = [
    "PVV",
    "PVX",
    "PVY",
    "PVZ",
    "DVE",
    "DVF",
    "DX1",
    "DX2",
    "DX3",
    "EF1",
    "EF2",
    "EF3",
    "PDC",
    "PGA",
    "CA01",
    "CA02",
    "CA03",
    "CA04",
    "CA05",
    "CA06",
    "CA07",
    "CA08",
    "CA09",
    "CP01",
    "CP02",
    "CP03",
    "CP04",
    "CP05",
    "CP06",
    "CP07",
    "CP08",
    "CP09",
]


for cell in MALE_NON_HEAD_INTERNEURONS:
    cell_notes[cell] = "male interneuron"


MALE_SPECIFIC_NEURONS = (
    MALE_HEAD_INTERNEURONS
    + MALE_NON_HEAD_INTERNEURONS
    + MALE_HEAD_SENSORY_NEURONS
    + MALE_NON_HEAD_SENSORY_NEURONS
)

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

SENSORY_NEURONS_NONPHARYNGEAL_COOK = []
for cell in SENSORY_NEURONS_COOK:
    if cell not in PHARYNGEAL_NEURONS:
        SENSORY_NEURONS_NONPHARYNGEAL_COOK.append(cell)

MOTORNEURONS_NONPHARYNGEAL_COOK = (
    HEAD_MOTORNEURONS_COOK
    + SUBLATERAL_MOTORNEURONS_COOK
    + VENTRAL_CORD_MOTORNEURONS
    + HERM_SPECIFIC_MOTORNEURONS
)

MOTORNEURONS_COOK = MOTORNEURONS_NONPHARYNGEAL_COOK + PHARYNGEAL_MOTORNEURONS

PREFERRED_HERM_NEURON_NAMES_COOK = (
    INTERNEURONS_COOK
    + SENSORY_NEURONS_COOK
    + MOTORNEURONS_COOK
    + PHARYNGEAL_POLYMODAL_NEURONS
    + UNKNOWN_FUNCTION_NEURONS
)

ALL_NEURON_NAMES_COOK = PREFERRED_HERM_NEURON_NAMES_COOK + MALE_SPECIFIC_NEURONS

COOK_GROUPING_1 = {
    "Pharyngeal neurons": PHARYNGEAL_NEURONS,
    "Sensory neurons": SENSORY_NEURONS_NONPHARYNGEAL_COOK,
    "Interneurons": INTERNEURONS_NONPHARYNGEAL_COOK,
    "Motorneurons": MOTORNEURONS_NONPHARYNGEAL_COOK,
    "Unknown function neurons": UNKNOWN_FUNCTION_NEURONS,
}

PREFERRED_HERM_NEURON_NAMES = [
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

for n in PREFERRED_HERM_NEURON_NAMES:
    assert n in PREFERRED_HERM_NEURON_NAMES_COOK

for n in PREFERRED_HERM_NEURON_NAMES_COOK:
    assert n in PREFERRED_HERM_NEURON_NAMES

assert len(PREFERRED_HERM_NEURON_NAMES_COOK) == len(PREFERRED_HERM_NEURON_NAMES)
assert len(PREFERRED_HERM_NEURON_NAMES_COOK) == 302

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

UTERINE_MUSCLE_NAMES = [
    "um2AL",
    "um2AR",
    "um1AL",
    "um1AR",
    "um1PL",
    "um1PR",
    "um2PL",
    "um2PR",
]
for cell in UTERINE_MUSCLE_NAMES:
    cell_notes[cell] = "uterine muscle"

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
    "pm4_UNSPECIFIED",
    "pm6D",
    "pm6VR",
    "pm6VL",
    "pm8",
]


PHARYNGEAL_MUSCLE_NAMES = ODD_PHARYNGEAL_MUSCLE_NAMES + EVEN_PHARYNGEAL_MUSCLE_NAMES

for cell in PHARYNGEAL_MUSCLE_NAMES:
    cell_notes[cell] = "pharyngeal muscle"

UNSPECIFIED_BODY_WALL_MUSCLES = ["BWM"]

cell_notes["BWM"] = "unspecified body wall muscle"

MALE_DIAGONAL_MUSCLES = [
    "dglL1",
    "dglL2",
    "dglL3",
    "dglL4",
    "dglL5",
    "dglL6",
    "dglL7",
    "dglR1",
    "dglR2",
    "dglR3",
    "dglR4",
    "dglR5",
    "dglR6",
    "dglR7",
    "dglR8",
]
for cell in MALE_DIAGONAL_MUSCLES:
    cell_notes[cell] = "diagonal muscle (male specific)"


MALE_ANTERIOR_OBLIQUE_MUSCLES = ["aobL", "aobR"]
for cell in MALE_ANTERIOR_OBLIQUE_MUSCLES:
    cell_notes[cell] = "anterior oblique (male specific)"
MALE_POSTERIOR_OBLIQUE_MUSCLES = ["pobL", "pobR"]
for cell in MALE_POSTERIOR_OBLIQUE_MUSCLES:
    cell_notes[cell] = "posterior oblique (male specific)"

MALE_GUBERNACULAR_ERECTOR_MUSCLES = ["gecL", "gecR"]
for cell in MALE_GUBERNACULAR_ERECTOR_MUSCLES:
    cell_notes[cell] = "gubernacular erector (male specific)"
MALE_GUBERNACULAR_RETRACTOR_MUSCLES = ["grtL", "grtR"]
for cell in MALE_GUBERNACULAR_RETRACTOR_MUSCLES:
    cell_notes[cell] = "gubernacular retractor (male specific)"

MALE_CAUDAL_LONGITUDINAL_MUSCLES = ["cdlL", "cdlR"]
for cell in MALE_CAUDAL_LONGITUDINAL_MUSCLES:
    cell_notes[cell] = "caudal longitudinal muscle (male specific)"

MALE_ANTERIOR_INNER_LONGITUDINAL_MUSCLES = ["ailL", "ailR"]
for cell in MALE_ANTERIOR_INNER_LONGITUDINAL_MUSCLES:
    cell_notes[cell] = "anterior inner longitudinal muscle (male specific)"
MALE_POSTERIOR_INNER_LONGITUDINAL_MUSCLES = ["pilL", "pilR"]
for cell in MALE_POSTERIOR_INNER_LONGITUDINAL_MUSCLES:
    cell_notes[cell] = "posterior inner longitudinal muscle (male specific)"
MALE_POSTERIOR_OUTER_LONGITUDINAL_MUSCLES = ["polL", "polR"]
for cell in MALE_POSTERIOR_OUTER_LONGITUDINAL_MUSCLES:
    cell_notes[cell] = "posterior outer longitudinal muscle (male specific)"

MALE_DORSAL_SPICULE_PROTRACTOR = ["dspL", "dspR"]
for cell in MALE_DORSAL_SPICULE_PROTRACTOR:
    cell_notes[cell] = "dorsal spicule protractor (male specific)"
MALE_VENTRAL_SPICULE_PROTRACTOR = ["vspL", "vspR"]
for cell in MALE_VENTRAL_SPICULE_PROTRACTOR:
    cell_notes[cell] = "ventral spicule protractor (male specific)"

MALE_DORSAL_SPICULE_RETRACTOR = ["dsrL", "dsrR"]
for cell in MALE_DORSAL_SPICULE_RETRACTOR:
    cell_notes[cell] = "dorsal spicule retractor (male specific)"
MALE_VENTRAL_SPICULE_RETRACTOR = ["vsrL", "vsrR"]
for cell in MALE_VENTRAL_SPICULE_RETRACTOR:
    cell_notes[cell] = "ventral spicule retractor (male specific)"

MALE_SPECIFIC_MUSCLES = (
    MALE_DIAGONAL_MUSCLES
    + MALE_ANTERIOR_OBLIQUE_MUSCLES
    + MALE_POSTERIOR_OBLIQUE_MUSCLES
    + MALE_GUBERNACULAR_ERECTOR_MUSCLES
    + MALE_GUBERNACULAR_RETRACTOR_MUSCLES
    + MALE_CAUDAL_LONGITUDINAL_MUSCLES
    + MALE_ANTERIOR_INNER_LONGITUDINAL_MUSCLES
    + MALE_POSTERIOR_INNER_LONGITUDINAL_MUSCLES
    + MALE_POSTERIOR_OUTER_LONGITUDINAL_MUSCLES
    + MALE_DORSAL_SPICULE_PROTRACTOR
    + MALE_VENTRAL_SPICULE_PROTRACTOR
    + MALE_DORSAL_SPICULE_RETRACTOR
    + MALE_VENTRAL_SPICULE_RETRACTOR
)


GONAD_CELL_MALE = ["gonad"]
cell_notes["gonad"] = "gonad (male specific)"

PROCTODEUM_CELL_MALE = ["proctodeum"]
cell_notes["proctodeum"] = "proctodeum (male specific)"

# TODO: remove sh versions, R1shL, etc from here!!!
MALE_RAY_STRUCTURAL_CELLS = [
    "R1stL",
    "R1stR",
    "R2stL",
    "R2stR",
    "R3stL",
    "R3stR",
    "R4stL",
    "R4stR",
    "R5stL",
    "R5stR",
    "R6stL",
    "R6stR",
    "R7stL",
    "R7stR",
    "R8stL",
    "R8stR",
    "R9stL",
    "R9stR",
    "R1shL",
    "R1shR",
    "R2shL",
    "R2shR",
    "R3shL",
    "R3shR",
    "R4shL",
    "R4shR",
    "R5shL",
    "R5shR",
    "R6shL",
    "R6shR",
    "R7shL",
    "R7shR",
    "R8shL",
    "R8shR",
    "R9shL",
    "R9shR",
]

for cell in MALE_RAY_STRUCTURAL_CELLS:
    cell_notes[cell] = "male ray structural cell"

MALE_SPECIFIC_OTHER_CELLS = (
    MALE_RAY_STRUCTURAL_CELLS + GONAD_CELL_MALE + PROCTODEUM_CELL_MALE
)

INTESTINAL_MUSCLES = [
    "mu_intL",
    "mu_intR",
]

for cell in INTESTINAL_MUSCLES:
    cell_notes[cell] = "intestinal muscles"

PREFERRED_MUSCLE_NAMES = (
    BODY_WALL_MUSCLE_NAMES
    + PHARYNGEAL_MUSCLE_NAMES
    + VULVAL_MUSCLE_NAMES
    + UTERINE_MUSCLE_NAMES
    + ANAL_SPHINCTER_MUSCLES
    + MALE_SPECIFIC_MUSCLES
    + INTESTINAL_MUSCLES
    + UNSPECIFIED_BODY_WALL_MUSCLES
)

COOK_GROUPING_1["Body wall muscles"] = BODY_WALL_MUSCLE_NAMES

COOK_GROUPING_1["Other muscles"] = (
    PHARYNGEAL_MUSCLE_NAMES
    + VULVAL_MUSCLE_NAMES
    + UTERINE_MUSCLE_NAMES
    + ANAL_SPHINCTER_MUSCLES
    + UNSPECIFIED_BODY_WALL_MUSCLES
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
    cell_notes[cell] = "sheath cell other than amphid sheath and phasmid"

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


ALL_PHARYNGEAL_CELLS = (
    PHARYNGEAL_NEURONS
    + PHARYNGEAL_MUSCLE_NAMES
    + PHARYNGEAL_MARGINAL_CELLS
    + PHARYNGEAL_EPITHELIUM
    + PHARYNGEAL_GLIAL_CELL
    + PHARYNGEAL_BASEMENT_MEMBRANE
)

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


KNOWN_HERM_NON_NEURON_MUSCLE_CELLS_COOK_19 = (
    GLIAL_CELLS
    + PHARYNGEAL_MARGINAL_CELLS
    + PHARYNGEAL_EPITHELIUM
    + PHARYNGEAL_GLIAL_CELL
    + PHARYNGEAL_BASEMENT_MEMBRANE
    + EXCRETORY_CELL
    + EXCRETORY_GLAND
    + HEAD_MESODERMAL_CELL
    + HYPODERMIS
    + INTESTINE
)

COOK_GROUPING_1["Other cells"] = list(KNOWN_HERM_NON_NEURON_MUSCLE_CELLS_COOK_19)

"""
KNOWN_OTHER_CELLS = KNOWN_OTHER_CELLS_COOK_19


KNOWN_OTHER_CELLS += (
    MALE_SPECIFIC_NEURONS
    + MALE_RAY_STRUCTURAL_CELLS
    + PROCTODEUM_CELL_MALE
    + GONAD_CELL_MALE
)"""

ALL_NON_NEURON_MUSCLE_CELLS = (
    KNOWN_HERM_NON_NEURON_MUSCLE_CELLS_COOK_19
    + MALE_RAY_STRUCTURAL_CELLS
    + PROCTODEUM_CELL_MALE
    + GONAD_CELL_MALE
)

COOK_GROUPING_1["Male specific neurons"] = MALE_SPECIFIC_NEURONS

COOK_GROUPING_1["Male specific muscles "] = MALE_SPECIFIC_MUSCLES

COOK_GROUPING_1["Male other cells"] = (
    MALE_RAY_STRUCTURAL_CELLS + PROCTODEUM_CELL_MALE + GONAD_CELL_MALE
)

ALL_PREFERRED_NEURON_NAMES = PREFERRED_HERM_NEURON_NAMES + MALE_SPECIFIC_NEURONS


ALL_PREFERRED_CELL_NAMES = (
    ALL_PREFERRED_NEURON_NAMES + PREFERRED_MUSCLE_NAMES + ALL_NON_NEURON_MUSCLE_CELLS
)


def get_primary_classification():
    """Get the primary classification of the cells, based on https://www.wormatlas.org/colorcode.htm

    Returns:
        dict: Dict of cells vs classification/group from https://www.wormatlas.org/colorcode.htm
    """

    classification = {}

    for sex in WA_COLORS:
        for cell_class in WA_COLORS[sex]:
            for cell_type in WA_COLORS[sex][cell_class]:
                print_(" - %s/%s/%s" % (sex, cell_class, cell_type))

                if cell_type == "body wall muscle":
                    for cell in BODY_WALL_MUSCLE_NAMES + UNSPECIFIED_BODY_WALL_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "vulval muscle":
                    for cell in VULVAL_MUSCLE_NAMES:
                        classification[cell] = cell_type
                elif cell_type == "uterine muscle":
                    for cell in UTERINE_MUSCLE_NAMES:
                        classification[cell] = cell_type
                elif cell_type == "interneuron":
                    for cell in (
                        INTERNEURONS_COOK
                        + MALE_HEAD_INTERNEURONS
                        + MALE_NON_HEAD_INTERNEURONS
                    ):
                        classification[cell] = cell_type
                elif cell_type == "motor neuron":
                    for cell in MOTORNEURONS_COOK:
                        classification[cell] = cell_type
                elif cell_type == "sensory neuron":
                    for cell in (
                        SENSORY_NEURONS_COOK
                        + MALE_HEAD_SENSORY_NEURONS
                        + MALE_NON_HEAD_SENSORY_NEURONS
                    ):
                        classification[cell] = cell_type
                elif cell_type == "odd numbered pharyngeal muscle":
                    for cell in ODD_PHARYNGEAL_MUSCLE_NAMES:
                        classification[cell] = cell_type
                elif cell_type == "even numbered pharyngeal muscle":
                    for cell in EVEN_PHARYNGEAL_MUSCLE_NAMES:
                        classification[cell] = cell_type
                elif cell_type == "polymodal neuron":
                    for cell in PHARYNGEAL_POLYMODAL_NEURONS:
                        classification[cell] = cell_type
                elif cell_type == "marginal cells (mc) of the pharynx":
                    for cell in PHARYNGEAL_MARGINAL_CELLS:
                        classification[cell] = cell_type
                elif cell_type == "pharyngeal epithelium":
                    for cell in PHARYNGEAL_EPITHELIUM + PHARYNGEAL_GLIAL_CELL:
                        classification[cell] = cell_type  # TODO: check!
                elif cell_type == "basement membrane":
                    for cell in PHARYNGEAL_BASEMENT_MEMBRANE:
                        classification[cell] = cell_type  # TODO: check!
                elif cell_type == "neuron with unknown function":
                    for cell in UNKNOWN_FUNCTION_NEURONS:
                        classification[cell] = cell_type
                elif cell_type == "sheath cell other than amphid sheath and phasmid":
                    for cell in CEPSH_CELLS:
                        classification[cell] = cell_type
                elif cell_type == "excretory cell":
                    for cell in EXCRETORY_CELL:
                        classification[cell] = cell_type
                elif cell_type == "sphincter and anal depressor muscle":
                    for cell in ANAL_SPHINCTER_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "gland cell":
                    for cell in EXCRETORY_GLAND:
                        classification[cell] = cell_type
                elif cell_type == "head mesodermal cell":
                    for cell in HEAD_MESODERMAL_CELL:
                        classification[cell] = cell_type
                elif cell_type == "hypodermis":
                    for cell in HYPODERMIS:
                        classification[cell] = cell_type
                elif cell_type == "intestinal cells":
                    for cell in INTESTINE:
                        classification[cell] = cell_type
                elif cell_type == "intestinal muscle":
                    for cell in INTESTINAL_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "GLR cell":
                    for cell in GLR_CELLS:
                        classification[cell] = cell_type
                elif cell_type == "diagonal muscles":
                    for cell in MALE_DIAGONAL_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "posterior outer longitudinal muscles":
                    for cell in MALE_POSTERIOR_OUTER_LONGITUDINAL_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "anterior inner longitudinal muscles":
                    for cell in MALE_ANTERIOR_INNER_LONGITUDINAL_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "posterior inner longitudinal muscles":
                    for cell in MALE_POSTERIOR_INNER_LONGITUDINAL_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "caudal inner longitudinal muscles":
                    for cell in MALE_CAUDAL_LONGITUDINAL_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "spicule retractor muscles":
                    for cell in (
                        MALE_VENTRAL_SPICULE_RETRACTOR + MALE_DORSAL_SPICULE_RETRACTOR
                    ):
                        classification[cell] = cell_type
                elif cell_type == "spicule protractor muscles":
                    for cell in (
                        MALE_VENTRAL_SPICULE_PROTRACTOR + MALE_DORSAL_SPICULE_PROTRACTOR
                    ):
                        classification[cell] = cell_type
                elif cell_type == "gubernacular retractor muscles":
                    for cell in MALE_GUBERNACULAR_RETRACTOR_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "gubernacular erector muscles":
                    for cell in MALE_GUBERNACULAR_ERECTOR_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "anterior oblique muscles":
                    for cell in MALE_ANTERIOR_OBLIQUE_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "posterior oblique muscles":
                    for cell in MALE_POSTERIOR_OBLIQUE_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "vas deferens":
                    for cell in GONAD_CELL_MALE:
                        classification[cell] = cell_type
                elif cell_type == "proctodeum":
                    for cell in PROCTODEUM_CELL_MALE:
                        classification[cell] = cell_type
                elif cell_type == "diagonal muscles":
                    for cell in MALE_DIAGONAL_MUSCLES:
                        classification[cell] = cell_type
                elif cell_type == "ray structural cell":
                    for cell in MALE_RAY_STRUCTURAL_CELLS:
                        classification[cell] = cell_type
                elif cell_type in [
                    "General code for neuronal tissue if subtype is unspecified",
                    "vulval epithelium",
                    "germline",
                    "DTC and somatic gonad",
                    "embryo",
                    "uterus",
                    "spermatheca",
                    "spermatheca-uterine valve",
                    "excretory pore cell",
                    "duct cell",
                    "excretory duct",
                    "seam cell",
                    "socket cell, XXX cells",
                    "amphid sheath and phasmid sheath",
                    "pharyngeal-intestinal valve, intestinal rectal valve",
                    "arcade cell",
                    "rectal epithelium (U, F, K, K', Y, B)",
                    "rectal gland, pharyngeal glands",
                    "pseudocoelomic space",
                    "coeloemocyte",
                    "anterior outer longitudinal muscles",
                    "seminal vesicle",
                    "sheath cell (spicules, hook or post-cloacal sensilla)",
                    "socket cell (spicules, hook or post-cloacal sensilla)",
                ]:
                    print_(
                        "No synaptic connnections to cells of type %s..?" % cell_type
                    )
                else:
                    raise Exception("Cell type %s not handled" % cell_type)
    for cell in ALL_PREFERRED_CELL_NAMES:
        assert cell in classification

    return classification


def is_known_cell(cell: str):
    """Is this string the name of one of the known cells?

    Args:
        cell (str): Cell name

    Returns:
        bool: Whether this is a known cell name
    """
    return cell in ALL_PREFERRED_CELL_NAMES


def get_SIM_class(cell: str):
    """
    PROVISIONAL method to return whether a cell is Sensory/Interneuron/Motorneuron (or Other)

    Parameters:
        cell: which cell to assess

    Returns:
        str: whether a cell is Sensory/Interneuron/Motorneuron (or Other)
    """

    pharyngeal_polymodal_to_class_motor = [
        "MI",
        "NSML",
        "NSMR",
        "MCL",
        "MCR",
    ]
    pharyngeal_polymodal_to_class_sensory = [
        "NSML",
        "NSMR",
    ]

    if cell in SENSORY_NEURONS_COOK + pharyngeal_polymodal_to_class_sensory:
        return "Sensory"
    elif cell in MOTORNEURONS_COOK + pharyngeal_polymodal_to_class_motor:
        return "Motorneuron"
    elif cell in INTERNEURONS_COOK:
        return "Interneuron"
    else:
        if len(cell) == 3:
            if get_SIM_class("%sL" % cell) == get_SIM_class("%sR" % cell):
                return get_SIM_class("%sL" % cell)
        return "Other"


def is_one_of_bilateral_pair(cell: str):
    return is_bilateral_left(cell) or is_bilateral_right(cell)


def get_contralateral_neuron(cell: str):
    """Gets the contralateral neuron for a given neuron, based on Kim et al. 2024: https://doi.org/10.1101/2024.10.03.616419

    Args:
        cell (_type_): _description_

    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
    """
    if not is_any_neuron(cell):
        raise Exception("Not yet implemented/tested for non neuronal cells")
    if is_bilateral_left(cell):
        return cell[:-1] + "R"
    if is_bilateral_right(cell):
        return cell[:-1] + "L"
    else:
        return cell


def is_bilateral_left(cell: str):
    if (
        cell in ALL_PREFERRED_CELL_NAMES
        and cell.endswith("L")
        and cell[:-1] + "R" in ALL_PREFERRED_CELL_NAMES
    ):
        return True
    else:
        return False


def is_bilateral_right(cell: str):
    if (
        cell in ALL_PREFERRED_CELL_NAMES
        and cell.endswith("R")
        and cell[:-1] + "L" in ALL_PREFERRED_CELL_NAMES
    ):
        return True
    else:
        return False


def convert_to_preferred_muscle_name(muscle: str):
    if muscle.startswith("BWM-VL"):
        return "MVL%s" % muscle[6:]
    elif muscle.startswith("BWM-VR"):
        return "MVR%s" % muscle[6:]
    elif muscle.startswith("BWM-DL"):
        return "MDL%s" % muscle[6:]
    elif muscle.startswith("BWM-DR"):
        return "MDR%s" % muscle[6:]
    elif muscle.startswith("dBWM"):
        return (
            "MD%s" % muscle[4:]
            if len(muscle) == 7
            else "MD%s0%s" % (muscle[4], muscle[5])
        )
    elif muscle.startswith("vBWM"):
        return (
            "MV%s" % muscle[4:]
            if len(muscle) == 7
            else "MV%s0%s" % (muscle[4], muscle[5])
        )
    elif muscle == "LegacyBodyWallMuscles":
        return "BWM"
    elif muscle.startswith("pm1"):
        return "pm1"
    elif muscle == "pm2vl":
        return "pm2VL"
    elif muscle == "pm2vr":
        return "pm2VR"
    elif muscle == "pm2d":
        return "pm2D"
    elif muscle == "pm3vl":
        return "pm3VL"
    elif muscle == "pm3vr":
        return "pm3VR"
    elif muscle == "pm3d":
        return "pm3D"
    elif muscle == "pm4vl":
        return "pm4VL"
    elif muscle == "pm4vr":
        return "pm4VR"
    elif muscle == "pm4d":
        return "pm4D"
    elif muscle == "pm4":
        return "pm4_UNSPECIFIED"
    elif muscle == "pm5vl":
        return "pm5VL"
    elif muscle == "pm5vr":
        return "pm5VR"
    elif muscle == "pm5d":
        return "pm5D"
    elif muscle == "pm6vl":
        return "pm6VL"
    elif muscle == "pm6vr":
        return "pm6VR"
    elif muscle == "pm6d":
        return "pm6D"
    elif muscle == "pm7vl":
        return "pm7VL"
    elif muscle == "pm7vr":
        return "pm7VR"
    elif muscle == "pm7d":
        return "pm7D"
    else:
        if is_known_muscle(muscle):
            return muscle
        else:
            return muscle + "???"


def convert_to_preferred_phar_cell_name(cell: str):
    if cell == "mc1v":
        return "mc1V"
    elif cell == "mc1dr":
        return "mc1DR"
    elif cell == "mc1dl":
        return "mc1DL"
    elif cell == "mc2v":
        return "mc2V"
    elif cell == "mc2dr":
        return "mc2DR"
    elif cell == "mc2dl":
        return "mc2DL"
    elif cell == "mc3v":
        return "mc3V"
    elif cell == "mc3dr":
        return "mc3DR"
    elif cell == "mc3dl":
        return "mc3DL"
    elif cell.lower() == "g1p":  # Different between cook 19 & 20
        return "g1P"
    else:
        if is_marginal_cell(cell):
            return cell


def get_marginal_cell_prefixes():
    return ["mc"]


def is_marginal_cell(cell: str):
    known_mc_prefix = get_marginal_cell_prefixes()
    return cell.startswith(tuple(known_mc_prefix))


def get_all_muscle_prefixes():
    return ["pm", "vm", "um", "mu_"] + get_body_wall_muscle_prefixes()


def get_body_wall_muscle_prefixes():
    return ["BWM-D", "BWM-V", "LegacyBodyWallMuscles", "vBWM", "dBWM"]


def is_potential_muscle(cell: str):
    if cell in PREFERRED_MUSCLE_NAMES:
        return True
    known_muscle_prefixes = get_all_muscle_prefixes()
    return cell.startswith(tuple(known_muscle_prefixes))


def is_known_muscle(cell: str):
    if cell in PREFERRED_MUSCLE_NAMES:
        return True
    return False


def is_potential_body_wall_muscle(cell: str):
    known_muscle_prefixes = get_body_wall_muscle_prefixes()
    return cell.startswith(tuple(known_muscle_prefixes))


def is_known_body_wall_muscle(cell: str):
    return cell in BODY_WALL_MUSCLE_NAMES


def is_pharyngeal_cell(cell: str):
    return cell in ALL_PHARYNGEAL_CELLS


def is_herm_neuron(cell: str):
    return cell in PREFERRED_HERM_NEURON_NAMES


def is_male_specific_cell(cell: str):
    return (
        cell
        in MALE_SPECIFIC_NEURONS + MALE_SPECIFIC_MUSCLES + MALE_SPECIFIC_OTHER_CELLS
    )


def is_any_neuron(cell: str):
    return cell in PREFERRED_HERM_NEURON_NAMES + MALE_SPECIFIC_NEURONS


def remove_leading_index_zero(cell: str):
    """
    Returns neuron name with an index without leading zero. E.g. VB01 -> VB1.
    """
    if cell[:2] in ["DA", "AS", "DD", "DB", "VA", "VB", "VC", "VD"] and cell[
        -2:
    ].startswith("0"):
        return "%s%s" % (cell[:-2], cell[-1:])
    return cell


def are_bilateral_pair(cell_a: str, cell_b: str):
    if cell_a[:-1] == cell_b[:-1] and (
        (cell_a[-1] == "L" and cell_b[-1] == "R")
        or (cell_b[-1] == "L" and cell_a[-1] == "R")
    ):
        return True
    else:
        return False


def get_standard_color(cell: str):
    from cect.WormAtlasInfo import WA_COLORS

    if cell in BODY_WALL_MUSCLE_NAMES + UNSPECIFIED_BODY_WALL_MUSCLES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["body wall muscle"]
    elif cell in VULVAL_MUSCLE_NAMES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["vulval muscle"]
    elif cell in UTERINE_MUSCLE_NAMES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["uterine muscle"]
    elif cell in ODD_PHARYNGEAL_MUSCLE_NAMES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["odd numbered pharyngeal muscle"]
    elif cell in EVEN_PHARYNGEAL_MUSCLE_NAMES:
        return WA_COLORS["Hermaphrodite"]["Muscle"]["even numbered pharyngeal muscle"]
    elif (
        cell in INTERNEURONS_COOK + MALE_HEAD_INTERNEURONS + MALE_NON_HEAD_INTERNEURONS
    ):
        return WA_COLORS["Hermaphrodite"]["Nervous Tissue"]["interneuron"]
    elif (
        cell
        in SENSORY_NEURONS_COOK
        + MALE_HEAD_SENSORY_NEURONS
        + MALE_NON_HEAD_SENSORY_NEURONS
    ):
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

    elif cell in MALE_DIAGONAL_MUSCLES:
        return WA_COLORS["Male"]["Muscle"]["diagonal muscles"]
    elif cell in MALE_ANTERIOR_OBLIQUE_MUSCLES:
        return WA_COLORS["Male"]["Muscle"]["anterior oblique muscles"]
    elif cell in MALE_POSTERIOR_OBLIQUE_MUSCLES:
        return WA_COLORS["Male"]["Muscle"]["posterior oblique muscles"]
    elif cell in MALE_GUBERNACULAR_ERECTOR_MUSCLES:
        return WA_COLORS["Male"]["Muscle"]["gubernacular erector muscles"]
    elif cell in MALE_GUBERNACULAR_RETRACTOR_MUSCLES:
        return WA_COLORS["Male"]["Muscle"]["gubernacular retractor muscles"]
    elif cell in MALE_CAUDAL_LONGITUDINAL_MUSCLES:
        return WA_COLORS["Male"]["Muscle"]["caudal inner longitudinal muscles"]
    elif cell in MALE_ANTERIOR_INNER_LONGITUDINAL_MUSCLES:
        return WA_COLORS["Male"]["Muscle"]["anterior inner longitudinal muscles"]
    elif cell in MALE_POSTERIOR_INNER_LONGITUDINAL_MUSCLES:
        return WA_COLORS["Male"]["Muscle"]["posterior inner longitudinal muscles"]
    elif cell in MALE_POSTERIOR_OUTER_LONGITUDINAL_MUSCLES:
        return WA_COLORS["Male"]["Muscle"]["posterior outer longitudinal muscles"]
    elif (
        cell in MALE_DORSAL_SPICULE_PROTRACTOR
        or cell in MALE_VENTRAL_SPICULE_PROTRACTOR
    ):
        return WA_COLORS["Male"]["Muscle"]["spicule protractor muscles"]

    elif (
        cell in MALE_DORSAL_SPICULE_RETRACTOR or cell in MALE_VENTRAL_SPICULE_RETRACTOR
    ):
        return WA_COLORS["Male"]["Muscle"]["spicule retractor muscles"]

    elif cell in MALE_RAY_STRUCTURAL_CELLS:
        return WA_COLORS["Male"]["Epithelial Tissue"]["ray structural cell"]

    elif cell in PROCTODEUM_CELL_MALE:
        return WA_COLORS["Male"]["Reproductive System"]["proctodeum"]
    elif cell in GONAD_CELL_MALE:
        return WA_COLORS["Male"]["Reproductive System"]["vas deferens"]

    else:
        raise Exception("Unknown cell: %s!" % cell)


def get_short_description(cell: str):
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


def get_cell_internal_link(
    cell_name: str,
    html: bool = False,
    text: str = None,
    use_color: bool = False,
    individual_cell_page: bool = False,
):
    url = "../Cells/index.html#%s" % cell_name

    if individual_cell_page:
        url = "../%s" % cell_name

    if html:
        link_text = cell_name if text is None else text
        if use_color:
            color = get_standard_color(cell_name)
            link_text = f'<span style="color:{color};">{link_text}</span>'

        return '<a href="%s" title="%s">%s</a>' % (
            url,
            (cell_name + " (%s)" if text else "%s") % get_short_description(cell_name),
            link_text,
        )
    else:
        return '[%s "%s"](%s)' % (
            cell_name if text is None else text,
            get_short_description(cell_name),
            url,
        )


def get_cell_osbv1_link(cell: str, text: str = "OSB 3D", button: bool = False):
    osbv1_link = f"https://v1.opensourcebrain.org/projects/c302/repository/revisions/development/show/examples/cells?explorer=https%253A%252F%252Fraw.githubusercontent.com%252Fopenworm%252Fc302%252Fdevelopment%252Fexamples%252Fcells%252F{cell}.cell.nml"

    if button:
        return f"[{text}]({osbv1_link}){{ .md-button }}" if is_herm_neuron(cell) else ""
    return f'<a href="{osbv1_link}">{text}</a>' if is_herm_neuron(cell) else ""


def get_cell_wormatlas_link(
    cell_name: str, html: bool = False, text: str = None, button: bool = False
):
    url = None

    known_other = {
        "SABD": "SAB",
        "CEMDL": "CEM",
        "CEMDR": "CEM",
        "CEMVL": "CEM",
        "CEMVR": "CEM",
    }

    if (
        cell_name
        in PHARYNGEAL_MARGINAL_CELLS
        + PHARYNGEAL_EPITHELIUM
        + PHARYNGEAL_GLIAL_CELL
        + PHARYNGEAL_BASEMENT_MEMBRANE
        + PHARYNGEAL_MUSCLE_NAMES
    ):
        url = "https://www.wormatlas.org/hermaphrodite/pharynx/jump.html?newLink=mainframe.htm&newAnchor=Listofcellsinthepharynx11"

    elif cell_name in known_other:
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % known_other[cell_name]
        )

    elif cell_name in INTESTINE + INTESTINAL_MUSCLES:
        url = "https://www.wormatlas.org/hermaphrodite/intestine/Intframeset.html"

    elif cell_name in VULVAL_MUSCLE_NAMES:
        url = "https://www.wormatlas.org/hermaphrodite/egglaying%20apparatus/Eggframeset.html"

    elif cell_name in UTERINE_MUSCLE_NAMES:
        url = "https://www.wormatlas.org/hermaphrodite/egglaying%20apparatus/jump.html?newLink=mainframe.htm&newAnchor=Theuterus2"

    elif cell_name in ANAL_SPHINCTER_MUSCLES:
        url = "https://www.wormatlas.org/hermaphrodite/excretory/Excframeset.html"

    elif cell_name in BODY_WALL_MUSCLE_NAMES:
        url = "https://www.wormatlas.org/hermaphrodite/musclesomatic/MusSomaticframeset.html"

    elif cell_name in MALE_SPECIFIC_MUSCLES:
        url = "https://www.wormatlas.org/male/musclemale/Musmaleframeset.html"

    elif cell_name in HYPODERMIS:
        url = "https://www.wormatlas.org/hermaphrodite/hypodermis/Hypframeset.html"

    elif cell_name in CEPSH_CELLS:
        url = "https://www.wormatlas.org/hermaphrodite/neuronalsupport/Neurosupportframeset.html"

    elif cell_name in GLR_CELLS:
        url = "https://www.wormatlas.org/hermaphrodite/muscleGLR/MusGLRframeset.html"

    elif cell_name in HEAD_MESODERMAL_CELL:
        url = "https://www.wormatlas.org/hermaphrodite/muscleheadcell/mainframe.htm"

    elif cell_name in MALE_RAY_STRUCTURAL_CELLS:
        url = "https://www.wormatlas.org/male/rays/Rayframeset.html"

    elif is_any_neuron(cell_name) and len(cell_name) == 5:  # e.g. SAADL
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-2]
        )
    elif is_one_of_bilateral_pair(cell_name):
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-1]
        )
    elif cell_name[-2:].isnumeric():
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-2]
        )

    elif cell_name in PHARYNGEAL_NEURONS:  # if not caught already e.g. M1, I5...
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name
        )

    elif cell_name[-1].isdigit():
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-1]
        )
    elif (
        cell_name.endswith("EV") or cell_name.endswith("ED") or cell_name.endswith("BD")
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
        check_url = False
        if check_url:
            try:
                error = None

                import requests

                page = requests.get(url)
                if not page.status_code == 200:
                    error = "Status code: %s" % page.status_code
            except Exception as err:
                error = err

            print_(
                "URL for %s (%s): %s"
                % (cell_name, url, "SUCCESS" if error is None else "ERROR (%s)" % error)
            )
            if error is not None:
                exit(-1)

        if html:
            return '<a href="%s">%s</a>' % (url, cell_name if text is None else text)
        elif button:
            return "[%s](%s){ .md-button }" % (
                cell_name if text is None else text,
                url,
            )
        else:
            return "[%s](%s)" % (cell_name if text is None else text, url)
    else:
        return cell_name


def _get_dataset_link(reader_name: str, html: bool = False, text: str = None):
    url = "%s_data_graph.md" % reader_name

    if html:
        return '<a href="%s">%s</a>' % (url, reader_name if text is None else text)
    else:
        return "[%s](%s)" % (reader_name if text is None else text, url)


def _generate_cell_table(cell_type: str, cells: List[str]):
    import plotly.graph_objects as go

    from cect.Comparison import _format_json

    print_(" - Adding table for %s" % cell_type)

    syn_summaries = {
        "Chemical conns in": [GENERIC_CHEM_SYN] + ALL_KNOWN_CHEMICAL_NEUROTRANSMITTERS,
        "Chemical conns out": [GENERIC_CHEM_SYN] + ALL_KNOWN_CHEMICAL_NEUROTRANSMITTERS,
        "Electrical conns": [GENERIC_ELEC_SYN],
    }

    fig_md = ""

    verbose = False
    some_cells = False

    for syn_summary in syn_summaries:
        fig = go.Figure()
        fig.layout.showlegend = True

        fig_md += '\n=== "%s"\n\n' % syn_summary
        # fig_md += "    Connections to these cells of type: %s\n\n" % syn_type

        nonempty_fig_present = False
        for reader_name, connectome in connectomes.items():
            sorted_cells = sorted(cells)

            indent = "    "
            y = []
            for cell in sorted_cells:
                syn_types = syn_summaries[syn_summary]
                total_y = 0
                for syn_type in syn_types:
                    if "out" in syn_summary:
                        conns_here = connectome.get_connections_from(cell, syn_type)
                    else:
                        conns_here = connectome.get_connections_to(cell, syn_type)
                    if verbose:
                        print_(
                            "Conns: %i for %s of type %s (%s)"
                            % (len(conns_here), cell, syn_type, syn_summary)
                        )
                    total_y += len(conns_here)

                y.append(total_y)

            if sum(y) > 0:
                marker_symbol = "square"
                dash = "solid"

                fig.add_scatter(
                    name="%s %s" % (reader_name, syn_summary),
                    x=sorted_cells,
                    y=y,
                    marker_symbol=marker_symbol,
                    line=dict(dash=dash),
                )
                nonempty_fig_present = True
                some_cells = True

        if nonempty_fig_present:
            asset_filename = "assets/%s_%s_hist.json" % (
                cell_type.replace(" ", "_"),
                syn_summary.replace(" ", "_"),
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

        cell_link = get_cell_internal_link(
            cell, html=True, use_color=True, individual_cell_page=True
        )
        all_data[f'<a name="{cell}"></a>{cell_link}'] = [
            desc,
            datasets[:-2],
            get_cell_wormatlas_link(cell, text="WormAtlas")
            + ("<br/>%s" % get_cell_osbv1_link(cell)),
        ]

    df_all = pd.DataFrame(all_data).transpose()

    table_md = df_all.to_markdown()

    title = cell_type[0].upper() + cell_type[1:]
    title = ("%s" if some_cells else "<i>%s</i>") % title

    title_md = "#### ![#{0}](images/{0}.png) {1}\n".format(color, title)
    # title_md = '#### <span style="color:#{0};">\u2588</span> -- ![<span style="color:#{0};">\u2588</span>](https://via.placeholder.com/15/{0}/{0}.png) - {1}\n'.format(
    #    color, title
    # )

    return "%s\n%s\n%s\n\n" % (title_md, fig_md, table_md)


if __name__ == "__main__":
    quick = len(sys.argv) > 1 and eval(sys.argv[1])

    from cect.Comparison import generate_comparison_page

    connectomes = generate_comparison_page(quick)

    from cect.CellInfo import generate_cell_info_pages

    generate_cell_info_pages(connectomes)

    filename = "docs/Cells.md"

    with open(filename, "w") as f:
        f.write("---\ntitle: <i>C. elegans</i> cells\n---\n\n")

        for sex in WA_COLORS:
            f.write("\n## %s\n" % sex)

            for cell_class in WA_COLORS[sex]:
                f.write("\n### %s\n\n" % cell_class)

                for cell_type in WA_COLORS[sex][cell_class]:
                    if "General code" not in cell_type:
                        color = WA_COLORS[sex][cell_class][cell_type][1:]

                        if cell_type == "body wall muscle":
                            f.write(
                                _generate_cell_table(cell_type, BODY_WALL_MUSCLE_NAMES)
                            )
                        elif cell_type == "vulval muscle":
                            f.write(
                                _generate_cell_table(cell_type, VULVAL_MUSCLE_NAMES)
                            )
                        elif cell_type == "uterine muscle":
                            f.write(
                                _generate_cell_table(cell_type, UTERINE_MUSCLE_NAMES)
                            )
                        elif cell_type == "interneuron":
                            f.write(
                                _generate_cell_table(
                                    cell_type,
                                    INTERNEURONS_COOK
                                    + MALE_HEAD_INTERNEURONS
                                    + MALE_NON_HEAD_INTERNEURONS,
                                )
                            )
                        elif cell_type == "motor neuron":
                            f.write(_generate_cell_table(cell_type, MOTORNEURONS_COOK))
                        elif cell_type == "sensory neuron":
                            f.write(
                                _generate_cell_table(
                                    cell_type,
                                    SENSORY_NEURONS_COOK
                                    + MALE_HEAD_SENSORY_NEURONS
                                    + MALE_NON_HEAD_SENSORY_NEURONS,
                                )
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

                        elif cell_type == "diagonal muscles":
                            f.write(
                                _generate_cell_table(cell_type, MALE_DIAGONAL_MUSCLES)
                            )
                        elif cell_type == "posterior outer longitudinal muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type, MALE_POSTERIOR_OUTER_LONGITUDINAL_MUSCLES
                                )
                            )
                        elif cell_type == "anterior inner longitudinal muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type, MALE_ANTERIOR_INNER_LONGITUDINAL_MUSCLES
                                )
                            )
                        elif cell_type == "posterior inner longitudinal muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type, MALE_POSTERIOR_INNER_LONGITUDINAL_MUSCLES
                                )
                            )
                        elif cell_type == "caudal inner longitudinal muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type, MALE_CAUDAL_LONGITUDINAL_MUSCLES
                                )
                            )
                        elif cell_type == "spicule retractor muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type,
                                    MALE_VENTRAL_SPICULE_RETRACTOR
                                    + MALE_DORSAL_SPICULE_RETRACTOR,
                                )
                            )
                        elif cell_type == "spicule protractor muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type,
                                    MALE_VENTRAL_SPICULE_PROTRACTOR
                                    + MALE_DORSAL_SPICULE_PROTRACTOR,
                                )
                            )
                        elif cell_type == "gubernacular retractor muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type, MALE_GUBERNACULAR_RETRACTOR_MUSCLES
                                )
                            )
                        elif cell_type == "gubernacular erector muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type, MALE_GUBERNACULAR_ERECTOR_MUSCLES
                                )
                            )
                        elif cell_type == "anterior oblique muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type, MALE_ANTERIOR_OBLIQUE_MUSCLES
                                )
                            )
                        elif cell_type == "posterior oblique muscles":
                            f.write(
                                _generate_cell_table(
                                    cell_type, MALE_POSTERIOR_OBLIQUE_MUSCLES
                                )
                            )

                        elif cell_type == "vas deferens":
                            f.write(_generate_cell_table(cell_type, GONAD_CELL_MALE))
                        elif cell_type == "proctodeum":
                            f.write(
                                _generate_cell_table(cell_type, PROCTODEUM_CELL_MALE)
                            )

                        elif cell_type == "diagonal muscles":
                            f.write(
                                _generate_cell_table(cell_type, MALE_DIAGONAL_MUSCLES)
                            )
                        elif cell_type == "ray structural cell":
                            f.write(
                                _generate_cell_table(
                                    cell_type, MALE_RAY_STRUCTURAL_CELLS
                                )
                            )
                        elif cell_type in [
                            "vulval epithelium",
                            "germline",
                            "DTC and somatic gonad",
                            "embryo",
                            "uterus",
                            "spermatheca",
                            "spermatheca-uterine valve",
                            "excretory pore cell",
                            "duct cell",
                            "excretory duct",
                            "seam cell",
                            "socket cell, XXX cells",
                            "amphid sheath and phasmid sheath",
                            "pharyngeal-intestinal valve, intestinal rectal valve",
                            "arcade cell",
                            "rectal epithelium (U, F, K, K', Y, B)",
                            "rectal gland, pharyngeal glands",
                            "pseudocoelomic space",
                            "coeloemocyte",
                            "anterior outer longitudinal muscles",
                            "seminal vesicle",
                            "sheath cell (spicules, hook or post-cloacal sensilla)",
                            "socket cell (spicules, hook or post-cloacal sensilla)",
                        ]:
                            print_(
                                "No synaptic connnections to cells of type %s..?"
                                % cell_type
                            )
                        else:
                            raise Exception("Cell type %s not handled" % cell_type)
