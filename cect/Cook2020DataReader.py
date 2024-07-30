import csv

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeReader import PREFERRED_NEURON_NAMES
from cect.ConnectomeReader import PREFERRED_MUSCLE_NAMES
from cect.ConnectomeReader import convert_to_preferred_muscle_name

import os

from cect import print_

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
filename = "%scne24932-sup-0004-supinfo4.csv" % spreadsheet_location

READER_DESCRIPTION = (
    """Data extracted from **%s** for neuronal connectivity""" % filename
)


class Cook2020DataReader(ConnectomeDataset):
    cells = []
    conns = []

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data(include_nonconnected_cells=True)
        for conn in neuron_conns:
            self.add_connection(conn)

    def read_data(self, include_nonconnected_cells=False, neuron_connect=True):
        """
        Args:
            include_nonconnected_cells (bool): Also append neurons without known connections to other neurons to the 'cells' list. True if they should get appended, False otherwise.
        Returns:
            cells (:obj:`list` of :obj:`str`): List of neurons
            conns (:obj:`list` of :obj:`ConnectionInfo`): List of connections from neuron to neuron
        """
        if neuron_connect:
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                print_("Opened file: " + filename)

                for row in reader:
                    pre = str.strip(row["Source"])
                    post = str.strip(row["Target"])
                    num = float(row["Weight"])
                    syntype = (str.strip(row["Type"]))
                    synclass = "Generic_GJ" if "Electrical" in syntype else "Generic_CS"

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
                post = str.strip(row["Target"])
                num = float(row["Weight"])
                syntype = (str.strip(row["Type"]))
                synclass = "Generic_GJ" if "Electrical" in syntype else "Generic_CS"

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                
                if post in PREFERRED_MUSCLE_NAMES and post not in muscles:
                        convert_to_preferred_muscle_name("%s"%muscles)
                        muscles.append(post)
                if pre in PREFERRED_NEURON_NAMES and pre not in neurons:
                        neurons.append(pre)

        return neurons, muscles, conns

def get_instance():
    return Cook2020DataReader()

my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


def main():
    cells, neuron_conns = my_instance.read_data(include_nonconnected_cells=True)
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))


if __name__ == "__main__":
    main()