# -*- coding: utf-8 -*-

############################################################

#    A script to read the values of Ripoll-Sanchez et al 2023

############################################################


from cect.RipollSanchezDataReader import RipollSanchezDataReader, get_filename
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

MODEL = "long_range_model"


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``RipollSanchezDataReader`` to load data on the long range model of neuropedtidergic connectome

    Returns:
        RipollSanchezDataReader: The initialised connectome reader
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
        return RipollSanchezDataReader(MODEL)


"""
read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""


READER_DESCRIPTION = (
    """Data extracted from %s for long range model of neuropedtidergic connectome"""
    % get_dataset_source_on_github(get_filename(MODEL).split("/")[-1])
)


def main1():
    my_instance = get_instance()
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    main1()
