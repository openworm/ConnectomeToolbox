# Temporary class to allow this to be used in comparison notebook.
# Should be tidied up.

from cect.WhiteDataReader import WhiteDataReader
from cect.ConnectomeReader import analyse_connections

import os


def get_instance():
    spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    filename = "%saconnectome_white_1986_whole.csv" % spreadsheet_location
    return WhiteDataReader(filename)


my_instance = get_instance()

READER_DESCRIPTION = (
    """Data extracted from **%s** for neuronal connectivity"""
    % my_instance.filename.split("/")[-1]
)

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


def main1():
    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()
    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    main1()

    import sys

    if not "-nogui" in sys.argv:
        fig = my_instance.to_plotly_matrix_fig("Acetylcholine")

        fig.show()
