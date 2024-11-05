# Temporary class to allow this to be used in comparison notebook.
# Should be tidied up.

from cect.WhiteDataReader import WhiteDataReader
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import get_dataset_source_on_github

import os


spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
filename = "%saconnectome_white_1986_L4.csv" % spreadsheet_location


def get_instance():
    """Uses ``WhiteDataReader`` to load data on the JSH series - a fourth stage (L4) larva

    Returns:
        WhiteDataReader: The initialised connectome reader
    """
    return WhiteDataReader(filename)


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data

READER_DESCRIPTION = (
    """Data extracted from %s - JSH series ("The JSH animal was a fourth stage (L4) larva" - White et al. 1986)"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)


def main1():
    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    main1()
