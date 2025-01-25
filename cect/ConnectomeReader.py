# -*- coding: utf-8 -*-

############################################################

#    Utilities for reading C. elegans connectome data

############################################################

from cect import print_

from cect.Cells import PREFERRED_HERM_NEURON_NAMES
from cect.Cells import PREFERRED_MUSCLE_NAMES

from cect.Cells import is_known_muscle


DEFAULT_COLORMAP = [
    "white",
    "blue",
    "cyan",
    "green",
    "yellow",
    "orange",
]  # ["white", "green", "black"]
POS_NEG_COLORMAP = ["darkblue", "blue", "white", "red", "darkred"]


class ConnectionInfo:
    """Holds information on a single connection between a `pre_cell` and `post_cell` - the `number` of connections, the `syntype` and `synclass`"""

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
    missing_preferred = [n for n in PREFERRED_HERM_NEURON_NAMES]
    muscles = []

    for c in cells:
        if is_known_muscle(c):
            muscles.append(c)
        elif c not in PREFERRED_HERM_NEURON_NAMES:
            if not is_known_muscle(c):
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
        if nt not in nts:
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
        if m not in PREFERRED_MUSCLE_NAMES:
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
        if nt not in nts:
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

    print_details_on = ["ADAL"]
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
