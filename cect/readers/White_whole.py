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
from cect.readers.WhiteDataReader import WhiteDataReader

NAME = "White_whole"

DATASET_DESCRIPTION = "Reanalysis of the White et al. 1986 connectome data by Varshney et al. 2011. This version includes the pharynx."

WEIGHTS = "Used Varshney et al. 2011 interpretation of weights: the total number of synaptic contacts from neuron A to neuron B. Contacts are given equal weight regardless of the apparent size of the synaptic apposition."

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/../data/"
filename = "%saconnectome_white_1986_whole.csv" % spreadsheet_location


def get_cache() -> object:
    """Return a cached ConnectomeDataset for this reader, if present."""
    filename_cache = get_cache_filename(__file__.split("/")[-1].split(".")[0])
    return load_connectome_dataset_file(filename_cache) or None


def get_instance(from_cache: bool = LOAD_READERS_FROM_CACHE_BY_DEFAULT, **kwargs):
    """Uses ``WhiteDataReader`` to load data on the whole worm connectome, including pharynx and ventral cord

    Returns:
        (ConnectomeDataset or WhiteDataReader): The initialised connectome reader
    """
    cache = get_cache() if from_cache else None
    instance = cache or WhiteDataReader(kwargs.get("spreadsheet_location", filename))
    return instance


READER_DESCRIPTION = (
    """Data extracted from %s - all connectivity from White et al. 1986)"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)


def main1():
    my_instance = get_instance()
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    cell = "ADAL"
    conns = my_instance.get_connections_from(cell, "Generic_CS")
    print(f"There are {len(conns)} connections from {cell}:")
    for c in sorted(conns.keys()):
        print(f" {cell} -> {c}: {conns[c]}")

    from cect.ConnectomeView import NONPHARYNGEAL_NEURONS_HERM_VIEW as view
    # from cect.ConnectomeView import NEURONS_VIEW as view

    cds2 = my_instance.get_connectome_view(view)

    print(cds2.summary())
    ew = cds2.connections["Electrical"]

    from cect.readers.VarshneyDataReader import get_instance as get_varshney_instance

    var = get_varshney_instance()
    var_non = var.get_connectome_view(view)
    print(var_non.summary())
    ev = var_non.connections["Electrical"]
    diff = ew - ev
    print(diff)
    import numpy as np

    print(np.nonzero(diff))
    for pre, post in zip(*np.nonzero(diff)):
        print(f"Diff: {cds2.nodes[pre]} -> {cds2.nodes[post]}: {diff[pre, post]}")


if __name__ == "__main__":
    main1()
