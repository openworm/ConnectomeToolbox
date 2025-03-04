from cect.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import get_dataset_source_on_github


from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WitvlietDataReader`` to load data on Witvliet dataset 2 (L1 stage)

    Returns:
        WitvlietDataReader: The initialised connectome reader
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
        return WitvlietDataReader("witvliet_2020_2.xlsx")


my_instance = get_instance()
"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""


READER_DESCRIPTION = (
    """Data extracted from %s - Witvliet dataset 2 (L1 stage)"""
    % get_dataset_source_on_github(my_instance.filename.split("/")[-1])
)


def main2():
    cells, neuron_conns = my_instance._read_data()
    neurons2muscles, muscles, muscle_conns = my_instance._read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)
    oci = len(my_instance.original_connection_infos)
    cci = len(my_instance.get_current_connection_info_list())
    print(oci)
    print(cci)


if __name__ == "__main__":
    main2()
