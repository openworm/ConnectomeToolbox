import csv

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.Cells import PREFERRED_HERM_NEURON_NAMES
from cect.Cells import PREFERRED_MUSCLE_NAMES
from cect.Cells import convert_to_preferred_muscle_name
from cect.Cells import is_potential_muscle
from cect.Cells import is_known_muscle
from cect.Cells import is_marginal_cell
from cect.Cells import convert_to_preferred_phar_cell_name
from cect.Cells import GENERIC_CHEM_SYN
from cect.Cells import GENERIC_ELEC_SYN

import os

from cect import print_

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
filename = "%scne24932-sup-0004-supinfo4.csv" % spreadsheet_location
filename2 = "%scne24932-sup-0005-supinfo5.csv" % spreadsheet_location


READER_DESCRIPTION = (
    """Data extracted from %s and %s for connectivity of pharyngeal neurons, muscles and other cells"""
    % (
        get_dataset_source_on_github(filename.split("/")[-1]),
        get_dataset_source_on_github(filename2.split("/")[-1]),
    )
)


class Cook2020DataReader(ConnectomeDataset):
    """
    Reader of data from Cook et al. 2020 - The connectome of the Caenorhabditis elegans pharynx
    """

    cells = []
    conns = []

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(conn, check_overwritten_connections=False)

    def read_data(self):
        """
        Returns:
            Tuple[list, list]: List of cells (str) and list of connections (``ConnectionInfo``) which have been read in
        """
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            print_("Opened file: " + filename)

            for row in reader:
                pre = str.strip(row["Source"])
                if is_potential_muscle(pre):
                    pre = convert_to_preferred_muscle_name(pre)
                post = str.strip(row["Target"])
                if is_potential_muscle(post):
                    post = convert_to_preferred_muscle_name(post)
                if is_marginal_cell(post):
                    post = convert_to_preferred_phar_cell_name(post)
                num = float(row["Weight"])
                syntype = str.strip(row["Type"])

                synclass = (
                    GENERIC_ELEC_SYN if "Electrical" in syntype else GENERIC_CHEM_SYN
                )

                if syntype == "Electrical":
                    self.conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                self.conns.append(ConnectionInfo(pre, post, num, syntype, synclass))

                if pre not in self.cells:
                    self.cells.append(pre)
                if post not in self.cells:
                    self.cells.append(post)

        with open(filename2, "r") as f:
            reader = csv.DictReader(f)
            print_("Opened file: " + filename)

            for row in reader:
                pre = str.strip(row["Source"])
                if is_potential_muscle(pre):
                    pre = convert_to_preferred_muscle_name(pre)
                if is_marginal_cell(pre):
                    pre = convert_to_preferred_phar_cell_name(pre)
                post = str.strip(row["Target"])

                if is_potential_muscle(post):
                    post = convert_to_preferred_muscle_name(post)
                if is_marginal_cell(post):
                    post = convert_to_preferred_phar_cell_name(post)

                num = float(row["Weight"])
                syntype = "Electrical"
                if syntype == "Electrical":
                    self.conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                synclass = (
                    GENERIC_ELEC_SYN if "Electrical" in syntype else GENERIC_CHEM_SYN
                )

                self.conns.append(ConnectionInfo(pre, post, num, syntype, synclass))

                if pre not in self.cells:
                    self.cells.append(pre)
                if post not in self.cells:
                    self.cells.append(post)

        return self.cells, self.conns

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
                pre = str.strip(row["Source"])
                if is_potential_muscle(pre):
                    pre = convert_to_preferred_muscle_name(pre)
                if is_marginal_cell(pre):
                    pre = convert_to_preferred_phar_cell_name(pre)
                post = str.strip(row["Target"])
                if is_potential_muscle(post):
                    post = convert_to_preferred_muscle_name(post)
                if is_marginal_cell(post):
                    post = convert_to_preferred_phar_cell_name(post)
                num = float(row["Weight"])
                syntype = str.strip(row["Type"])
                synclass = (
                    GENERIC_ELEC_SYN if "Electrical" in syntype else GENERIC_CHEM_SYN
                )

                if syntype == "Electrical":
                    conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))

                if is_known_muscle(post):
                    if post in PREFERRED_MUSCLE_NAMES and post not in muscles:
                        muscles.append(post)
                    if pre in PREFERRED_HERM_NEURON_NAMES and pre not in neurons:
                        neurons.append(pre)

        with open(filename2, "r") as f:
            reader = csv.DictReader(f)
            print_("Opened file: " + filename2)

            for row in reader:
                pre = str.strip(row["Source"])
                if is_potential_muscle(pre):
                    pre = convert_to_preferred_muscle_name(pre)
                if is_marginal_cell(pre):
                    pre = convert_to_preferred_phar_cell_name(pre)
                post = str.strip(row["Target"])
                if is_potential_muscle(post):
                    post = convert_to_preferred_muscle_name(post)
                if is_marginal_cell(post):
                    post = convert_to_preferred_phar_cell_name(post)
                num = float(row["Weight"])
                syntype = "Electrical"
                synclass = (
                    GENERIC_ELEC_SYN if "Electrical" in syntype else GENERIC_CHEM_SYN
                )

                if syntype == "Electrical":
                    conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))

                if is_known_muscle(post):
                    if post in PREFERRED_MUSCLE_NAMES and post not in muscles:
                        muscles.append(post)
                    if pre in PREFERRED_HERM_NEURON_NAMES and pre not in neurons:
                        neurons.append(pre)

        return neurons, muscles, conns


def get_instance():
    return Cook2020DataReader()


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


def main():
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))


if __name__ == "__main__":
    main()
