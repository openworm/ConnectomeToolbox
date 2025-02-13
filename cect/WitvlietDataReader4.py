from cect.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeDataset import get_dataset_source_on_github


from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WitvlietDataReader`` to load data on Witvliet dataset 4 (L1 stage)

    Returns:
        WitvlietDataReader: The initialised connectome reader
    """
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename("WitvlietDataReader4"))
    else:
        return WitvlietDataReader("witvliet_2020_4.xlsx")


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


READER_DESCRIPTION = (
    """Data extracted from %s - Witvliet dataset 4 (L1 stage)"""
    % get_dataset_source_on_github(my_instance.filename.split("/")[-1])
)
