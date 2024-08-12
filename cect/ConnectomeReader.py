# -*- coding: utf-8 -*-

############################################################

#    Utilities for reading C. elegans connectome data

############################################################

from cect import print_

from cect.Cells import PREFERRED_NEURON_NAMES
from cect.Cells import PREFERRED_MUSCLE_NAMES
from cect.Cells import KNOWN_OTHER_CELLS

DEFAULT_COLORMAP = ["white", "green", "black"]


def convert_to_preferred_muscle_name(muscle):
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
        if is_muscle(muscle):
            return muscle
        else:
            return muscle + "???"


def convert_to_preferred_phar_cell_name(cell):
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


def is_marginal_cell(cell):
    known_mc_prefix = get_marginal_cell_prefixes()
    return cell.startswith(tuple(known_mc_prefix))


def get_all_muscle_prefixes():
    return ["pm", "vm", "um", "mu_"] + get_body_wall_muscle_prefixes()


def get_body_wall_muscle_prefixes():
    return ["BWM-D", "BWM-V", "LegacyBodyWallMuscles", "vBWM", "dBWM"]


def is_muscle(cell):
    if cell in PREFERRED_MUSCLE_NAMES:
        return True
    known_muscle_prefixes = get_all_muscle_prefixes()
    return cell.startswith(tuple(known_muscle_prefixes))


def is_body_wall_muscle(cell):
    known_muscle_prefixes = get_body_wall_muscle_prefixes()
    return cell.startswith(tuple(known_muscle_prefixes))


def is_neuron(cell):
    return cell in PREFERRED_NEURON_NAMES


def remove_leading_index_zero(cell):
    """
    Returns neuron name with an index without leading zero. E.g. VB01 -> VB1.
    """
    if cell[:2] in ["DA", "AS", "DD", "DB", "VA", "VB", "VC", "VD"] and cell[
        -2:
    ].startswith("0"):
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


def check_cells(cells):
    in_preferred = []
    not_in_preferred = []
    missing_preferred = [n for n in PREFERRED_NEURON_NAMES]
    muscles = []

    for c in cells:
        if is_muscle(c):
            muscles.append(c)
        elif not c in PREFERRED_NEURON_NAMES:
            if not is_muscle(c):
                not_in_preferred.append(c)
        else:
            in_preferred.append(c)

        if c in missing_preferred:
            missing_preferred.remove(c)

    if False:
        print(
            "Of these %i cells:\n  %i in preferred: %s\n  %i not in preferred: %s\n  %i missing preferred: %s\n  %i muscles: %s"
            % (
                len(cells),
                len(in_preferred),
                in_preferred,
                len(not_in_preferred),
                not_in_preferred,
                len(missing_preferred),
                missing_preferred,
                len(muscles),
                muscles,
            )
        )

    return in_preferred, not_in_preferred, missing_preferred, muscles


def analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns):
    print_("Found %s non-muscle cells: %s\n" % (len(cells), sorted(cells)))

    preferred, not_in_preferred, missing_preferred, muscles_ = check_cells(cells)

    print_(
        "Found %s non-neuron(s) here: %s\n"
        % (len(not_in_preferred), sorted(not_in_preferred))
    )
    print_(
        "Known neurons not present (%i): %s\n"
        % (len(missing_preferred), sorted(missing_preferred))
    )

    print_("Found %s neuron->neuron connections..." % (len(neuron_conns)))
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

    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)
