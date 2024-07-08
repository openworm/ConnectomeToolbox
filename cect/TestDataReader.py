
from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset

import os
from cect import print_


READER_DESCRIPTION = """Dummy dataset used for testing webpage/graph generation - do not use!"""

NMJ_ENDPOINT = 'NMJ'


class TestDataReader(ConnectomeDataset):

    cells = []
    conns = []

    def __init__(self):

        cells, neuron_conns = self.read_data(include_nonconnected_cells=True)
        for conn in neuron_conns:
            self.add_connection(conn)

    def read_data(self, include_nonconnected_cells=False, neuron_connect=True):

        self.conns.append(ConnectionInfo('PVCL', 'AVBL', 7, 'Send', 'Acetylcholine'))
        self.conns.append(ConnectionInfo('PVCL', 'DB4', 6, 'Send', 'Acetylcholine'))
        self.conns.append(ConnectionInfo('PVCL', 'VB6', 2, 'Send', 'Acetylcholine'))
        self.conns.append(ConnectionInfo('DB4', 'DD4', 2, 'Send', 'Acetylcholine'))
        self.conns.append(ConnectionInfo('DB4', 'VD6', 14, 'Send', 'Acetylcholine'))
        self.conns.append(ConnectionInfo('VA6', 'VD6', 6, 'Send', 'Acetylcholine'))
        self.conns.append(ConnectionInfo('VB6', 'DD4', 32, 'Send', 'Acetylcholine'))

        self.conns.append(ConnectionInfo('VD6', 'VA6', 3, 'Send', 'GABA'))
        self.conns.append(ConnectionInfo('VD3', 'VA3', 2, 'Send', 'GABA'))
        self.conns.append(ConnectionInfo('VD3', 'VB2', 2, 'Send', 'GABA'))
        
        self.conns.append(ConnectionInfo('DB4', 'AVBL', 4, 'GapJunction', 'Generic_GJ'))
        self.conns.append(ConnectionInfo('VB6', 'AVBL', 3, 'GapJunction', 'Generic_GJ'))


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


tdr_instance = TestDataReader()

read_data = tdr_instance.read_data
read_muscle_data = tdr_instance.read_muscle_data


def main():

    cells, neuron_conns = tdr_instance.read_data(include_nonconnected_cells=True)
    neurons2muscles, muscles, muscle_conns = tdr_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(' -- Finished analysing connections using: %s'%os.path.basename(__file__))

    tdr_instance.summary()

    import sys

    if not '-nogui' in sys.argv:

        import plotly.express as px

        conn_array = tdr_instance.connections['Acetylcholine']

        fig = px.imshow(conn_array,
                        labels=dict(x ="Pre", y = "Post", color = "Synapses"),
                        x = tdr_instance.nodes,
                        y = tdr_instance.nodes)
        fig.show()

if __name__ == '__main__':

    main()
