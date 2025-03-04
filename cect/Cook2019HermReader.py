# Reader for Cook et al 2019 data


from cect.Cook2019DataReader import Cook2019DataReader
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeReader import analyse_connections

import sys


from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``Cook2019DataReader`` to load data on hermaphrodite connectome

    Returns:
        Cook2019DataReader: The initialised hermaphrodite connectome reader
    """
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename("Cook2019HermReader"))
    else:
        return Cook2019DataReader("Hermaphodite")


"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""

READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity of hermaphrodite"""
    % get_dataset_source_on_github(Cook2019DataReader.filename.split("/")[-1])
)


def main1():
    my_instance = get_instance()
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    if "-nogui" not in sys.argv:
        my_instance.connection_number_plot("Acetylcholine")


if __name__ == "__main__":
    main1()
