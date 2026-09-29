from cect.readers.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import get_dataset_source_on_github

from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

# ruff: noqa: F401
from cect.readers.WitvlietDataReader import WEIGHTS

NAME = "Witvliet2"
SRC_FILENAME = "witvliet_2020_2 L1.xlsx"

DATASET_DESCRIPTION = "Chemical and electrical connectivity from Witvliet et al. 2021, dataset 2 (L1 stage)"


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WitvlietDataReader`` to load data on Witvliet dataset 2 (L1 stage)

    Returns:
        (WitvlietDataReader): The initialized connectome reader
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


"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""


READER_DESCRIPTION = (
    """Data extracted from %s - Witvliet dataset 2 (L1 stage)"""
    % get_dataset_source_on_github(SRC_FILENAME)
)


def main2():
    my_instance = get_instance()
    cells, neuron_conns = my_instance._read_data()
    neurons2muscles, muscles, muscle_conns = my_instance._read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)
    oci = len(my_instance.original_connection_infos)
    cci = len(my_instance.get_current_connection_info_list())
    print(oci)
    print(cci)


if __name__ == "__main__":
    main2()
