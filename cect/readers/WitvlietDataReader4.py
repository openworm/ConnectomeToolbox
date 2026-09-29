from cect.readers.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeDataset import get_dataset_source_on_github

from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

# ruff: noqa: F401
from cect.readers.WitvlietDataReader import WEIGHTS

NAME = "Witvliet4"
SRC_FILENAME = "witvliet_2020_4 L1.xlsx"

DATASET_DESCRIPTION = "Chemical and electrical connectivity from Witvliet et al. 2021, dataset 4 (L1 stage)"


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WitvlietDataReader`` to load data on Witvliet dataset 4 (L1 stage)

    Returns:
        (WitvlietDataReader): The initialized connectome reader
    """
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename("WitvlietDataReader4"))
    else:
        return WitvlietDataReader(SRC_FILENAME)


"""
my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""


READER_DESCRIPTION = (
    """Data extracted from %s - Witvliet dataset 4 (L1 stage)"""
    % get_dataset_source_on_github(SRC_FILENAME)
)
