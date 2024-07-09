from cect import print_

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeDataset import ConnectomeDataset


import numpy as np


class NodeSet:
    def __init__(self, name, cells, color=None):
        self.name = name
        self.color = color
        self.cells = cells

    def __repr__(self):
        return "NodeSet %s (%s): %s" % (self.name, self.color, self.cells)


class View:
    def __init__(self, name, node_sets, synclasses):
        self.name = name
        self.node_sets = node_sets
        self.synclasses = synclasses

    def get_index_of_cell(self, cell):
        for i in range(len(self.node_sets)):
            if cell in self.node_sets[i].cells:
                return i
        return -1


class ConnectomeView(ConnectomeDataset):
    verbose = True

    def summary(self):
        print_("Nodes present: %s" % self.nodes)
        for c in self.connections:
            conn_array = self.connections[c]
            print_(
                "- Connections: %s %s, %i non-zero entries, %i total\n%s"
                % (
                    c,
                    conn_array.shape,
                    np.count_nonzero(conn_array),
                    np.sum(conn_array),
                    conn_array,
                )
            )


if __name__ == "__main__":
    ns_v = NodeSet("Vmn", ["VA6", "VB6", "VB3", "VD6", "VA3", "VD3", "VB2"])
    ns_d = NodeSet("Dmn", ["DB4", "DD4"])
    ns_p = NodeSet("PVCL", ["PVCL"])
    ns_a = NodeSet("AVBL", ["AVBL"])

    v1 = View("VandD", [ns_d, ns_v, ns_a, ns_p], ["Acetylcholine"])

    from cect.TestDataReader import tdr_instance

    tdr_instance.summary()

    cv = tdr_instance.get_connectome_view(v1)
    print("----------------")
    cv.summary()
