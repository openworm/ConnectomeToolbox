from cect.WitvlietDataReader import WitvlietDataReader


def get_instance():
    return WitvlietDataReader("witvliet_2020_6.xlsx")


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data

READER_DESCRIPTION = (
    """Data extracted from **%s** for neuronal connectivity"""
    % my_instance.filename.split("/")[-1]
)
