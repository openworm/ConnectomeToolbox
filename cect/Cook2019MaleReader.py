# Reader for Cook et al 2019 data

from cect.Cook2019DataReader import Cook2019DataReader
from cect.ConnectomeDataset import get_dataset_source_on_github

from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[1]))
    else:
        return Cook2019DataReader("Male")


"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""

READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity of male"""
    % get_dataset_source_on_github(Cook2019DataReader.filename.split("/")[-1])
)


def main1():
    my_instance = get_instance()
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    main1()
