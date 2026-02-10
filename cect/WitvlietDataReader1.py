from cect.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import get_dataset_source_on_github


from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

NAME = "Witvliet1"
SRC_FILENAME = "witvliet_2020_1.xlsx"


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WitvlietDataReader`` to load data on Witvliet dataset 1 (L1 stage)

    Returns:
        WitvlietDataReader: The initialized connectome reader
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
        return WitvlietDataReader(SRC_FILENAME)


READER_DESCRIPTION = (
    """Data extracted from %s - Witvliet dataset 1 (L1 stage)"""
    % get_dataset_source_on_github(SRC_FILENAME)
)


def main1():
    my_instance = get_instance()

    read_data = my_instance.read_data
    read_muscle_data = my_instance.read_muscle_data
    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    main1()
