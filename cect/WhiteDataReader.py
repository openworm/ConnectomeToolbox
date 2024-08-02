# -*- coding: utf-8 -*-

############################################################

#    A simple script to read the values in herm_full_edgelist.csv.

#    This is on of a number of interchangeable "Readers" which can
#    be used to get connection data for c302

############################################################

import csv

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeReader import convert_to_preferred_muscle_name
from cect.ConnectomeReader import is_neuron
from cect.ConnectomeReader import is_body_wall_muscle

from cect.ConnectomeDataset import ConnectomeDataset


import os

from cect import print_


def remove_leading_index_zero(cell):
    """
    Returns neuron name with an index without leading zero. E.g. VB01 -> VB1.
    """
    if is_neuron(cell) and cell[-2:].startswith("0"):
        return "%s%s" % (cell[:-2], cell[-1:])
    return cell


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


class White_A(ConnectomeDataset):
    spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    filename = "%saconnectome_white_1986_A.csv" % spreadsheet_location

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data(include_nonconnected_cells=True)
        for conn in neuron_conns:
            self.add_connection(conn)

    def read_data(self, include_nonconnected_cells=False):
        conns = []
        cells = []

        with open(White_A.filename, "r") as f:
            print_("Opened file: " + White_A.filename)
            f.readline()

            known_nonconnected_cells = ["CANL", "CANR"]

            for line in f:
                pre, post, num, syntype, synclass = parse_line(line)

                if not is_neuron(pre) or not is_neuron(post):
                    continue  # pre or post is not a neuron

                pre = remove_leading_index_zero(pre)
                post = remove_leading_index_zero(post)

                if synclass == "Generic_GJ":
                    conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                # print ConnectionInfo(pre, post, num, syntype, synclass)
                if pre not in cells:
                    cells.append(pre)
                if post not in cells:
                    cells.append(post)

            if include_nonconnected_cells:
                for c in known_nonconnected_cells:
                    if c not in cells:
                        cells.append(c)

        return cells, conns

    def read_muscle_data(self):
        neurons = []
        muscles = []
        conns = []

        with open(White_A.filename, "r") as f:
            print_("Opened file: " + White_A.filename)
            f.readline()

            for line in f:
                pre, post, num, syntype, synclass = parse_line(line)

                if not is_body_wall_muscle(post):
                    continue

                if is_neuron(pre):
                    pre = remove_leading_index_zero(pre)
                post = convert_to_preferred_muscle_name(post)

                if synclass == "Generic_GJ":
                    conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))

                if is_neuron(pre) and pre not in neurons:
                    neurons.append(pre)
                if post not in muscles:
                    muscles.append(post)

            return neurons, muscles, conns


def main1():
    ww = White_A()
    cells, neuron_conns = ww.read_data(include_nonconnected_cells=True)
    neurons2muscles, muscles, muscle_conns = ww.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


class White_L4(ConnectomeDataset):
    spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    filename = "%saconnectome_white_1986_L4.csv" % spreadsheet_location

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data(include_nonconnected_cells=True)
        for conn in neuron_conns:
            self.add_connection(conn)

    def read_data(self, include_nonconnected_cells=False):
        conns = []
        cells = []

        with open(White_L4.filename, "r") as f:
            print_("Opened file: " + White_L4.filename)
            f.readline()

            known_nonconnected_cells = ["CANL", "CANR"]

            for line in f:
                pre, post, num, syntype, synclass = parse_line(line)

                if not is_neuron(pre) or not is_neuron(post):
                    continue  # pre or post is not a neuron

                pre = remove_leading_index_zero(pre)
                post = remove_leading_index_zero(post)
                if synclass == "Generic_GJ":
                    conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                # print ConnectionInfo(pre, post, num, syntype, synclass)
                if pre not in cells:
                    cells.append(pre)
                if post not in cells:
                    cells.append(post)

            if include_nonconnected_cells:
                for c in known_nonconnected_cells:
                    if c not in cells:
                        cells.append(c)

            return cells, conns

    def read_muscle_data(self):
        neurons = []
        muscles = []
        conns = []

        with open(White_L4.filename, "r") as f:
            print_("Opened file: " + White_L4.filename)
            f.readline()

            for line in f:
                pre, post, num, syntype, synclass = parse_line(line)

                if not is_body_wall_muscle(post):
                    continue

                if is_neuron(pre):
                    pre = remove_leading_index_zero(pre)
                post = convert_to_preferred_muscle_name(post)
                if synclass == "Generic_GJ":
                    conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))

                if is_neuron(pre) and pre not in neurons:
                    neurons.append(pre)
                if post not in muscles:
                    muscles.append(post)

            return neurons, muscles, conns


def main2():
    ww = White_L4()
    cells, neuron_conns = ww.read_data(include_nonconnected_cells=True)
    neurons2muscles, muscles, muscle_conns = ww.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


class White_whole(ConnectomeDataset):
    spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    filename = "%saconnectome_white_1986_whole.csv" % spreadsheet_location

    BODYWALLMUSCLE_ENDPOINT = "LegacyBodyWallMuscles"

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data(include_nonconnected_cells=True)
        for conn in neuron_conns:
            self.add_connection(conn)

    def read_data(self, include_nonconnected_cells=False):
        conns = []
        cells = []

        with open(White_whole.filename, "r") as f:
            print_("Opened file: " + White_whole.filename)
            f.readline()

            known_nonconnected_cells = ["CANL", "CANR"]

            for line in f:
                pre, post, num, syntype, synclass = parse_line(line)

                if not is_neuron(pre) or not is_neuron(post):
                    continue  # pre or post is not a neuron
                pre = remove_leading_index_zero(pre)
                post = remove_leading_index_zero(post)
                if synclass == "Generic_GJ":
                    conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                # print ConnectionInfo(pre, post, num, syntype, synclass)
                if pre not in cells:
                    cells.append(pre)
                if post not in cells:
                    cells.append(post)

            if include_nonconnected_cells:
                for c in known_nonconnected_cells:
                    if c not in cells:
                        cells.append(c)

        return cells, conns

    def read_muscle_data(self):
        neurons = []
        muscles = []
        conns = []

        with open(White_whole.filename, "r") as f:
            print_("Opened file: " + White_whole.filename)
            f.readline()

            for line in f:
                pre, post, num, syntype, synclass = parse_line(line)

                if not is_body_wall_muscle(post):
                    continue

                if is_neuron(pre):
                    pre = remove_leading_index_zero(pre)
                    post = convert_to_preferred_muscle_name(post)
                    if synclass == "Generic_GJ":
                        conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                    conns.append(ConnectionInfo(pre, post, num, syntype, synclass))

                if is_neuron(pre) and pre not in neurons:
                    neurons.append(pre)
                if post not in muscles:
                    muscles.append(post)

            return neurons, muscles, conns


def main3():
    ww = White_whole()
    cells, neuron_conns = ww.read_data(include_nonconnected_cells=True)
    neurons2muscles, muscles, muscle_conns = ww.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

if __name__ == "__main__":
    main1()
    main2()
    main3()
