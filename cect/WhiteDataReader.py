# -*- coding: utf-8 -*-

############################################################

#    A simple script to read the values in herm_full_edgelist.csv.

#    This is on of a number of interchangeable "Readers" which can
#    be used to get connection data for c302

############################################################


from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeReader import convert_to_preferred_muscle_name
from cect.ConnectomeReader import is_neuron
from cect.ConnectomeReader import is_muscle
from cect.ConnectomeReader import remove_leading_index_zero

from cect.ConnectomeDataset import ConnectomeDataset

import os

from cect import print_


def get_syntype(syntype):
    if syntype == "electrical":
        return "GapJunction"
    elif syntype == "chemical":
        return "Send"
    else:
        raise NotImplementedError("Cannot parse syntype '%s'" % syntype)


def get_synclass(cell, syntype):
    # dirty hack
    if syntype == "GapJunction":
        return "Generic_GJ"
    else:
        if cell.startswith("DD") or cell.startswith("VD"):
            return "GABA"
        return "Acetylcholine"


def parse_line(line):
    elements = line.split()
    pre = str.strip(elements[0])
    post = str.strip(elements[1])
    num = int(elements[3])
    syntype = get_syntype(str.strip(elements[2]))
    synclass = get_synclass(pre, syntype)
    return pre, post, num, syntype, synclass


class WhiteDataReader(ConnectomeDataset):
    verbose = False

    def __init__(self, spreadsheet_filename):
        ConnectomeDataset.__init__(self)
        self.filename = spreadsheet_filename

        neurons, muscles, other_cells, conns = self.read_all_data()
        # neurons, conns = self.read_data()

        for conn in conns:
            self.add_connection_info(conn)

    def read_all_data(self):
        neurons = set([])
        muscles = set([])
        other_cells = set([])
        conns = []

        with open(self.filename, "r") as f:
            print_("Opened file: " + self.filename)
            f.readline()

            # known_nonconnected_cells = ["CANL", "CANR"]

            for line in f:
                pre, post, num, syntype, synclass = parse_line(line)

                pre = remove_leading_index_zero(pre)
                post = remove_leading_index_zero(post)

                if is_muscle(pre):
                    pre = convert_to_preferred_muscle_name(pre)

                if is_muscle(post):
                    post = convert_to_preferred_muscle_name(post)

                if synclass == "Generic_GJ":
                    conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))

                for p in [pre, post]:
                    if is_neuron(p):
                        neurons.add(pre)
                    elif is_muscle(p):
                        muscles.add(pre)
                    else:
                        other_cells.add(p)

        return list(neurons), list(muscles), list(other_cells), conns


if __name__ == "__main__":
    spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    filename = "%saconnectome_white_1986_whole.csv" % spreadsheet_location
    wdr = WhiteDataReader(filename)

    cells, neuron_conns = wdr.read_data()
    neurons2muscles, muscles, muscle_conns = wdr.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)
