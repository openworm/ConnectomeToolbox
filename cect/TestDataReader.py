from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeReader import DEFAULT_COLORMAP

import os
import sys
from cect import print_


READER_DESCRIPTION = """Dummy dataset used for testing webpage/graph generation. <b>Do not assume any of these connections are correct!</b>"""

NMJ_ENDPOINT = "NMJ"


def get_instance():
    return TestDataReader()


class TestDataReader(ConnectomeDataset):
    """Dummy dataset used for testing webpage/graph generation. Do not assume any of these connections are correct!"""

    cells = []
    conns = []

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(conn)

    def read_data(self):
        self.conns.append(ConnectionInfo("PVCL", "AVBL", 7, "Send", "Acetylcholine"))
        self.conns.append(ConnectionInfo("PVCL", "DB4", 6, "Send", "Acetylcholine"))
        self.conns.append(ConnectionInfo("PVCL", "VB6", 2, "Send", "Acetylcholine"))
        self.conns.append(ConnectionInfo("DB4", "DD4", 2, "Send", "Acetylcholine"))
        self.conns.append(ConnectionInfo("DB4", "VD6", 14, "Send", "Acetylcholine"))
        self.conns.append(ConnectionInfo("VA6", "VD6", 6, "Send", "Acetylcholine"))
        self.conns.append(ConnectionInfo("VB6", "DD4", 32, "Send", "Acetylcholine"))

        self.conns.append(ConnectionInfo("VD6", "VA6", 3, "Send", "GABA"))

        self.conns.append(ConnectionInfo("VD3", "VA3", 2, "Send", "GABA"))
        self.conns.append(ConnectionInfo("VD3", "VB2", 2, "Send", "GABA"))

        self.conns.append(ConnectionInfo("DB4", "AVBL", 4, "GapJunction", "Generic_GJ"))
        self.conns.append(ConnectionInfo("VB6", "AVBL", 3, "GapJunction", "Generic_GJ"))
        self.conns.append(ConnectionInfo("VB6", "VB6", 3, "GapJunction", "Generic_GJ"))

        self.conns.append(ConnectionInfo("DVA", "PVCL", 3, "Send", "Acetylcholine"))

        self.conns.append(ConnectionInfo("ASHR", "RMGR", 6, "Send", "Acetylcholine"))
        self.conns.append(ConnectionInfo("AWBR", "ASHR", 2, "Send", "Acetylcholine"))

        self.conns.append(ConnectionInfo("I5", "M4", 9, "Send", "Acetylcholine"))
        self.conns.append(ConnectionInfo("M4", "M1", 9, "Send", "Acetylcholine"))

        self.conns.append(
            ConnectionInfo("ASHR", "ASKR", 1, "GapJunction", "Generic_GJ")
        )

        for c in self.conns:
            if c.pre_cell not in self.cells:
                self.cells.append(c.pre_cell)
            if c.post_cell not in self.cells:
                self.cells.append(c.post_cell)

        return self.cells, self.conns

    def read_muscle_data(self):
        conns = []
        neurons = []
        muscles = []

        return neurons, muscles, conns


tdr_instance = get_instance()

read_data = tdr_instance.read_data
read_muscle_data = tdr_instance.read_muscle_data


def main():
    cells, neuron_conns = tdr_instance.read_data()
    neurons2muscles, muscles, muscle_conns = tdr_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    print(tdr_instance.summary())

    from cect.ConnectomeView import RAW_VIEW

    fig = tdr_instance.to_plotly_matrix_fig(
        "Acetylcholine", RAW_VIEW, color_continuous_scale=DEFAULT_COLORMAP
    )
    if "-nogui" not in sys.argv:
        fig.show()


if __name__ == "__main__":
    main()
