from cect.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeReader import analyse_connections


def get_instance():
    return WitvlietDataReader("witvliet_2020_1.xlsx")


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


READER_DESCRIPTION = (
    """Data extracted from **%s** for neuronal connectivity"""
    % my_instance.filename.split("/")[-1]
)


def main1():
    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    main1()
