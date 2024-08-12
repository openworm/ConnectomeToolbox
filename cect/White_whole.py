# Temporary class to allow this to be used in comparison notebook.
# Should be tidied up.

from cect.WhiteDataReader import White_whole

from cect.ConnectomeReader import analyse_connections


READER_DESCRIPTION = (
    """Data extracted from **%s** for neuronal connectivity"""
    % White_whole.filename.split("/")[-1]
)


def get_instance():
    return White_whole()


my_instance = get_instance()

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
