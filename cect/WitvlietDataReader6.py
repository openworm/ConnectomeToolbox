from cect.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeDataset import get_dataset_source_on_github


def get_instance():
    """Uses ``WitvlietDataReader`` to load data on Witvliet dataset 6 (L3 stage)

    Returns:
        WitvlietDataReader: The initialised connectome reader
    """
    return WitvlietDataReader("witvliet_2020_6.xlsx")


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


READER_DESCRIPTION = (
    """Data extracted from %s - Witvliet dataset 6 (L3 stage)"""
    % get_dataset_source_on_github(my_instance.filename.split("/")[-1])
)
