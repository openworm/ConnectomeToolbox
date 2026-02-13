# Temporary class to allow this to be used in comparison notebook.
# Should be tidied up.


import os

from cect.ConnectomeDataset import (
    LOAD_READERS_FROM_CACHE_BY_DEFAULT,
    get_cache_filename,
    get_dataset_source_on_github,
    load_connectome_dataset_file,
)
from cect.ConnectomeReader import analyse_connections
from cect.WhiteDataReader import WhiteDataReader


NAME = "White_whole"

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
filename = "%saconnectome_white_1986_whole.csv" % spreadsheet_location


def get_cache() -> object:
    """Return a cached ConnectomeDataset for this reader, if present."""
    filename_cache = get_cache_filename(__file__.split("/")[-1].split(".")[0])
    return load_connectome_dataset_file(filename_cache) or None


def get_instance(from_cache: bool = LOAD_READERS_FROM_CACHE_BY_DEFAULT, **kwargs):
    """Uses ``WhiteDataReader`` to load data on the whole worm connectome, including pharynx and ventral cord

    Returns:
        ConnectomeDataset or WhiteDataReader: The initialised connectome reader
    """
    cache = get_cache() if from_cache else None
    instance = cache or WhiteDataReader(kwargs.get("spreadsheet_location", filename))
    return instance


READER_DESCRIPTION = (
    """Data extracted from %s - all connectivity from White et al. 1986)"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)

"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""


def main1():
    my_instance = get_instance()
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    cell = "RIFL"
    conns = my_instance.get_connections_from(cell, "Generic_CS")
    print(f"There are {len(conns)} connections from {cell}:")
    for c in sorted(conns.keys()):
        print(f" {cell} -> {c}: {conns[c]}")


if __name__ == "__main__":
    main1()
