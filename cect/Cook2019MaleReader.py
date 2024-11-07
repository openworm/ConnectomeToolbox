# Reader for Cook et al 2019 data

from cect.Cook2019DataReader import Cook2019DataReader
from cect.ConnectomeDataset import get_dataset_source_on_github

from cect.ConnectomeReader import analyse_connections


def get_instance():
    return Cook2019DataReader("Male")


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data

READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity of male"""
    % get_dataset_source_on_github(my_instance.filename.split("/")[-1])
)


def main1():
    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    main1()
