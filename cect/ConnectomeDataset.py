from cect import print_

from cect.ConnectomeReader import ConnectionInfo

import numpy as np

class ConnectomeDataset():

    nodes = []
    connections = {}

    DEFAULT_DTYPE = np.float64

    verbose = False

    def _expand_conn_arrays(self):
        
        for c in self.connections:
            conn_array = self.connections[c]

            dim = conn_array.shape[0]
            new_conn_array = np.zeros([dim+1,dim+1], dtype=self.DEFAULT_DTYPE)
            new_conn_array[:conn_array.shape[0], :conn_array.shape[1]] = conn_array

            self.connections[c] = new_conn_array


    def add_connection(self, conn):

        if self.verbose: print_('----   Adding: %s'%conn)

        if not conn.synclass in self.connections:
            if len(self.connections)==0:
                self.connections[conn.synclass] = np.zeros([0,0], dtype=self.DEFAULT_DTYPE)
            else:
                existing = list(self.connections.values())[0]
                self.connections[conn.synclass] = np.zeros(existing.shape, dtype=self.DEFAULT_DTYPE)


        if not conn.pre_cell in self.nodes:
            self.nodes.append(conn.pre_cell)
            self._expand_conn_arrays()

        if not conn.post_cell in self.nodes:
            self.nodes.append(conn.post_cell)
            self._expand_conn_arrays()
        
        conn_array = self.connections[conn.synclass]

        pre_index = self.nodes.index(conn.pre_cell)
        post_index = self.nodes.index(conn.post_cell)

        conn_array[pre_index,post_index] = conn.number

        if self.verbose: print_('Updated (%i,%i), nodes %s: \n%s'%(pre_index,post_index,self.nodes,conn_array))

    def summary(self):

        print_("Nodes present: %s"%self.nodes)
        for c in self.connections:
            conn_array = self.connections[c]
            print_("- Connections: %s %s, %i non-zero entries\n%s"%(c, conn_array.shape, np.count_nonzero(conn_array), conn_array))




if __name__ == '__main__':
    cds = ConnectomeDataset()
    
    cds.add_connection(ConnectionInfo('VA6', 'VD6', 6, 'Send', 'Acetylcholine'))
    cds.add_connection(ConnectionInfo('VB6', 'DD4', 32, 'Send', 'Acetylcholine'))

    cds.add_connection(ConnectionInfo('VD6', 'VA6', 3, 'Send', 'GABA'))

    cds.summary()