# -*- coding: utf-8 -*-

############################################################

#    Information on neurotransmitters in C. elegans
#    Much of this data taken from Wang et al. 2024

############################################################

ACETYLCHOLINE = "Acetylcholine"
GLUTAMATE = "Glutamate"
GABA = "GABA"

OTHER_CHEMICAL_NT = "OtherChemicalNT"

BETAINE = "Betaine"


ALL_KNOWN_CHEMICAL_NEUROTRANSMITTERS = [
    ACETYLCHOLINE,
    "Acetylcholine_Tyramine",
    "FMRFamide",
    GABA,
    GLUTAMATE,
    BETAINE,
    "Serotonin_Acetylcholine",
    "Serotonin_Glutamate",
    OTHER_CHEMICAL_NT,
]

DOPAMINE = "Dopamine"
SEROTONIN = "Serotonin"
OCTOPAMINE = "Octopamine"
TYRAMINE = "Tyramine"

SEROTONIN_UPTAKE = "Serotonin_Uptake"
GABA_UPTAKE = "GABA_Uptake"
UNKNOWN_ORPHAN_NEUROTRANSMITTER = "Unknown_Orphan_Neurotransmitter"
UNKNOWN_MONOAMINERGIC_NEUROTRANSMITTER = "Unknown_Monoaminergic_Neurotransmitter"
FIVE_HTP = "5-HTP"
PEOH = "Possible_PEOH"
FIVE_HTP_FIVE_HT = "5-HTP_synthesis_5-HT_uptake"


WANG_2024_EXTRA_NT_INFO = [
    SEROTONIN_UPTAKE,
    GABA_UPTAKE,
    UNKNOWN_ORPHAN_NEUROTRANSMITTER,
    UNKNOWN_MONOAMINERGIC_NEUROTRANSMITTER,
    FIVE_HTP,
    PEOH,
    FIVE_HTP_FIVE_HT,
]

GENERIC_CHEM_SYN = "Generic_CS"
GENERIC_ELEC_SYN = "Generic_GJ"

CONTACTOME_SYN_TYPE = "Contact"
CONTACTOME_SYN_CLASS = "Contact"

EXTRASYNAPTIC_SYN_TYPE = "Extrasynaptic"
MONOAMINERGIC_SYN_GENERAL_CLASS = "Monoaminergic"

MONOAMINERGIC_SYN_CLASSES = [DOPAMINE, SEROTONIN, TYRAMINE, OCTOPAMINE]

PEPTIDERGIC_SYN_CLASS = "Peptidergic"

ALL_KNOWN_EXTRASYNAPTIC_CLASSES = [
    PEPTIDERGIC_SYN_CLASS,
]

ALL_KNOWN_EXTRASYNAPTIC_CLASSES += MONOAMINERGIC_SYN_CLASSES

FUNCTIONAL_SYN_TYPE = "Functional"
FUNCTIONAL_SYN_CLASS = "Functional"
