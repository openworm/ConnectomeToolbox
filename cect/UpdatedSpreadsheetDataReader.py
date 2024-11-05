# -*- coding: utf-8 -*-

############################################################

#    A simple script to read the values in herm_full_edgelist.csv.

#    This is on of a number of interchangeable "Readers" which can
#    be used to get connection data

############################################################

import csv

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github
import os

from cect import print_

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
filename = "%sherm_full_edgelist.csv" % spreadsheet_location


READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity. Note: legacy dataset (based on Cook et al. 2019) used in the past in OpenWorm. <b>Only included here for reference! Do not use!</b>"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)


def _get_all_muscle_prefixes():
    return ["pm", "vm", "um", "dBWM", "vBWM"]


def _get_body_wall_muscle_prefixes():
    return ["dBWM", "vBWM"]


def _is_muscle(cell):
    known_muscle_prefixes = _get_all_muscle_prefixes()
    return cell.startswith(tuple(known_muscle_prefixes))


def _is_body_wall_muscle(cell):
    known_muscle_prefixes = _get_body_wall_muscle_prefixes()
    return cell.startswith(tuple(known_muscle_prefixes))


def _is_neuron(cell):
    return cell[0].isupper()


def _remove_leading_index_zero(cell):
    """
    Returns neuron name with an index without leading zero. E.g. VB01 -> VB1.
    """
    if _is_neuron(cell) and cell[-2:].startswith("0"):
        return "%s%s" % (cell[:-2], cell[-1:])
    return cell


def _get_old_muscle_name(muscle):
    index = int(muscle[5:])
    if index < 10:
        index = "0%s" % index
    if muscle.startswith("vBWML"):
        return "MVL%s" % index
    elif muscle.startswith("vBWMR"):
        return "MVR%s" % index
    elif muscle.startswith("dBWML"):
        return "MDL%s" % index
    elif muscle.startswith("dBWMR"):
        return "MDR%s" % index


def _get_syntype(syntype):
    if syntype == "electrical":
        return "GapJunction"
    elif syntype == "chemical":
        return "Send"
    else:
        raise NotImplementedError("Cannot parse syntype '%s'" % syntype)


def _get_synclass(cell, syntype):
    # dirty hack
    if syntype == "GapJunction":
        return "Generic_GJ"
    else:
        if cell.startswith("DD") or cell.startswith("VD"):
            return "GABA"
        return "Acetylcholine"


def parse_row(row):
    pre = str.strip(row["Source"])
    post = str.strip(row["Target"])
    num = int(row["Weight"])
    syntype = _get_syntype(str.strip(row["Type"]))
    synclass = _get_synclass(pre, syntype)
    return pre, post, num, syntype, synclass


class UpdatedSpreadsheetDataReader(ConnectomeDataset):
    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(conn)

        neurons2muscles, muscles, muscle_conns = self.read_muscle_data()
        for conn in muscle_conns:
            self.add_connection_info(conn)

    def read_data(self, include_nonconnected_cells=False):
        """
        Returns:
            Tuple[list, list]: List of cells (str) and list of connections (``ConnectionInfo``) which have been read in
        """

        conns = []
        cells = []

        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            print_("Opened file: " + filename)

            # known_nonconnected_cells = ["CANL", "CANR"]

            for row in reader:
                pre, post, num, syntype, synclass = parse_row(row)

                if not _is_neuron(pre) or not _is_neuron(post):
                    continue  # pre or post is not a neuron

                pre = _remove_leading_index_zero(pre)
                post = _remove_leading_index_zero(post)

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                # print ConnectionInfo(pre, post, num, syntype, synclass)
                if pre not in cells:
                    cells.append(pre)
                if post not in cells:
                    cells.append(post)

            if include_nonconnected_cells:
                from cect.Cells import PREFERRED_HERM_NEURON_NAMES

                for c in PREFERRED_HERM_NEURON_NAMES:
                    if c not in cells:
                        cells.append(c)

        return cells, conns

    def read_muscle_data(self):
        """
        Returns:
            neurons (:obj:`list` of :obj:`str`): List of motor neurons. Each neuron has at least one connection with a post-synaptic muscle cell.
            muscles (:obj:`list` of :obj:`str`): List of muscle cells.
            conns (:obj:`list` of :obj:`ConnectionInfo`): List of neuron-muscle connections.
        """

        neurons = []
        muscles = []
        conns = []

        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            print_("Opened file: " + filename)

            for row in reader:
                pre, post, num, syntype, synclass = parse_row(row)

                if not (
                    _is_neuron(pre) or _is_body_wall_muscle(pre)
                ) or not _is_body_wall_muscle(post):
                    continue

                if _is_neuron(pre):
                    pre = _remove_leading_index_zero(pre)
                else:
                    pre = _get_old_muscle_name(pre)
                post = _get_old_muscle_name(post)

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                if _is_neuron(pre) and pre not in neurons:
                    neurons.append(pre)
                elif _is_body_wall_muscle(pre) and pre not in muscles:
                    muscles.append(pre)
                if post not in muscles:
                    muscles.append(post)

        return neurons, muscles, conns


def get_instance():
    return UpdatedSpreadsheetDataReader()


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


def main():
    cells, neuron_conns = read_data()

    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))


if __name__ == "__main__":
    main()
