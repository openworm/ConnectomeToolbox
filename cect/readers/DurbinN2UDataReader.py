# Reader for Durbin N2U data


from cect.readers.DurbinDataReader import DurbinDataReader
from cect.readers.DurbinDataReader import N2U_ADULT
from cect.readers.DurbinDataReader import filename

# ruff: noqa: F401
from cect.readers.DurbinDataReader import WEIGHTS

from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeReader import analyse_connections

import sys

from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

NAME = "WhiteN2U"

DATASET_DESCRIPTION = "Chemical and electrical connectivity of the N2U (adult hermaphrodite) worm from White et al. 1986 data, based on the neurodata.txt file from R. M. Durbin's thesis, 1987. See validation information for minor changes from that file."


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``DurbinDataReader`` to load data on N2U connectome

    Returns:
        (DurbinDataReader): The initialized N2U connectome reader
    """
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename("DurbinN2UDataReader"))
    else:
        return DurbinDataReader(worm_strain=N2U_ADULT, include_nmj=True)


READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity of N2U adult from Durbin thesis"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)


def main1():
    my_instance = get_instance()
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    if "-nogui" not in sys.argv:
        my_instance.connection_number_plot("Acetylcholine")

    print(my_instance.summary())

    cells = ["ADAL"]
    syntypes = ["Generic_CS", "Generic_GJ"]

    for cell in cells:
        for syntype in syntypes:
            conns = my_instance.get_connections_from(cell, syntype)
            print(f"There are {len(conns)} connections from {cell} of type {syntype}:")
            for c in sorted(conns.keys()):
                print(f" {cell} -> {c}: {conns[c]}")


if __name__ == "__main__":
    main1()
