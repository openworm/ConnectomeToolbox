from cect.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeReader import analyse_connections


def get_instance():
    return WitvlietDataReader("witvliet_2020_5.xlsx")


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data

READER_DESCRIPTION = (
    """Data extracted from **%s** for neuronal connectivity"""
    % my_instance.filename.split("/")[-1]
)
