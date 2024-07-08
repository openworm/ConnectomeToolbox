
from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections

import os
from cect import print_


READER_DESCRIPTION = """Dummy dataset used for testing webpage/graph generation - do not use!"""

NMJ_ENDPOINT = 'NMJ'

def read_data(include_nonconnected_cells=False, neuron_connect=True):

    cells = []
    conns = []

    conns.append(ConnectionInfo('PVCL', 'AVBL', 7, 'Send', 'Acetylcholine'))
    conns.append(ConnectionInfo('PVCL', 'DB4', 6, 'Send', 'Acetylcholine'))
    conns.append(ConnectionInfo('PVCL', 'VB6', 2, 'Send', 'Acetylcholine'))
    conns.append(ConnectionInfo('DB4', 'DD4', 2, 'Send', 'Acetylcholine'))
    conns.append(ConnectionInfo('DB4', 'VD6', 14, 'Send', 'Acetylcholine'))
    conns.append(ConnectionInfo('VA6', 'VD6', 6, 'Send', 'Acetylcholine'))
    conns.append(ConnectionInfo('VB6', 'DD4', 32, 'Send', 'Acetylcholine'))

    conns.append(ConnectionInfo('VD6', 'VA6', 3, 'Send', 'GABA'))
    conns.append(ConnectionInfo('VD3', 'VA3', 2, 'Send', 'GABA'))
    conns.append(ConnectionInfo('VD3', 'VB2', 2, 'Send', 'GABA'))
    
    conns.append(ConnectionInfo('DB4', 'AVBL', 4, 'GapJunction', 'Generic_GJ'))
    conns.append(ConnectionInfo('VB6', 'AVBL', 3, 'GapJunction', 'Generic_GJ'))


    for c in conns:
        if c.pre_cell not in cells:
            cells.append(c.pre_cell)                
        if c.post_cell not in cells:
            cells.append(c.post_cell)

    return cells, conns


def read_muscle_data():

    conns = []
    neurons = []
    muscles = []

    return neurons, muscles, conns



def main():

    cells, neuron_conns = read_data(include_nonconnected_cells=True)
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(' -- Finished analysing connections using: %s'%os.path.basename(__file__))

if __name__ == '__main__':

    main()
