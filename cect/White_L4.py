# Temporary class to allow this to be used in comparison notebook.
# Should be tidied up.

from cect.WhiteDataReader import WhiteDataReader
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

import os


spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
filename = "%saconnectome_white_1986_L4.csv" % spreadsheet_location


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WhiteDataReader`` to load data on the JSH series - a fourth stage (L4) larva

    Returns:
        WhiteDataReader: The initialised connectome reader
    """
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(
            get_cache_filename(__file__.split("/")[-1].split(".")[0])
        )
    else:
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

    cell = "RIFL"
    conns = my_instance.get_connections_from(cell, "Generic_CS")
    print(f"There are {len(conns)} connections from {cell}:")
    for c in sorted(conns.keys()):
        print(f" {cell} -> {c}: {conns[c]}")


if __name__ == "__main__":
    main1()
