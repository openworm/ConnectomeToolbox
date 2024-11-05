# -*- coding: utf-8 -*-

############################################################

#    A script to read the values of Ripoll-Sanchez et al 2023

############################################################


from cect.RipollSanchezDataReader import RipollSanchezDataReader
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeReader import analyse_connections


def get_instance():
    """Uses ``RipollSanchezDataReader`` to load data on the long range model of neuropedtidergic connectome

    Returns:
        RipollSanchezDataReader: The initialised connectome reader
    """
    return RipollSanchezDataReader("long_range_model")


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


READER_DESCRIPTION = (
    """Data extracted from %s for long range model of neuropedtidergic connectome"""
    % get_dataset_source_on_github(my_instance.filename.split("/")[-1])
)


def main1():
    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    main1()
