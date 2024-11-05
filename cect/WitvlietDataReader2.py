from cect.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import get_dataset_source_on_github


def get_instance():
    """Uses ``WitvlietDataReader`` to load data on Witvliet dataset 2 (L1 stage)

    Returns:
        WitvlietDataReader: The initialised connectome reader
    """
    return WitvlietDataReader("witvliet_2020_2.xlsx")


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


READER_DESCRIPTION = (
    """Data extracted from %s - Witvliet dataset 2 (L1 stage)"""
    % get_dataset_source_on_github(my_instance.filename.split("/")[-1])
)


def main2():
    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    main2()
