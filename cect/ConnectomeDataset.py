from cect import print_

from cect.ConnectomeReader import ConnectionInfo

import numpy as np


class ConnectomeDataset:
    DEFAULT_DTYPE = np.float64

    verbose = False

    def __init__(self):
        self.nodes = []
        self.connections = {}

    def _expand_conn_arrays(self):
        for c in self.connections:
            conn_array = self.connections[c]

            dim = conn_array.shape[0]
            new_conn_array = np.zeros([dim + 1, dim + 1], dtype=self.DEFAULT_DTYPE)
            new_conn_array[: conn_array.shape[0], : conn_array.shape[1]] = conn_array

            self.connections[c] = new_conn_array

    def add_connection(self, conn):
        if self.verbose:
            print_("----   Adding: %s" % conn)

        if not conn.synclass in self.connections:
            if len(self.connections) == 0:
                self.connections[conn.synclass] = np.zeros(
                    [0, 0], dtype=self.DEFAULT_DTYPE
                )
            else:
                existing = list(self.connections.values())[0]
                self.connections[conn.synclass] = np.zeros(
                    existing.shape, dtype=self.DEFAULT_DTYPE
                )

        if not conn.pre_cell in self.nodes:
            self.nodes.append(conn.pre_cell)
            self._expand_conn_arrays()

        if not conn.post_cell in self.nodes:
            self.nodes.append(conn.post_cell)
            self._expand_conn_arrays()

        conn_array = self.connections[conn.synclass]

        pre_index = self.nodes.index(conn.pre_cell)
        post_index = self.nodes.index(conn.post_cell)

        conn_array[pre_index, post_index] = conn.number

        if self.verbose:
            print_(
                "Updated (%i,%i), nodes %s: \n%s"
                % (pre_index, post_index, self.nodes, conn_array)
            )

    def get_connectome_view(self, view):
        cv = ConnectomeDataset()

        for n in view.node_sets:
            cv.nodes.append(n.name)

        cv.connections[view.name] = np.zeros(
            [len(cv.nodes)] * 2, dtype=self.DEFAULT_DTYPE
        )
        for synclass in view.synclasses:
            conn_array = self.connections[synclass]
            for pre in self.nodes:
                pre_index = view.get_index_of_cell(pre)
                for post in self.nodes:
                    post_index = view.get_index_of_cell(post)

                    print(
                        "Testing if %s (%i), %s (%s) in %s"
                        % (pre, pre_index, post, post_index, view.node_sets)
                    )

                    if pre_index >= 0 and post_index >= 0:
                        cv.connections[view.name][pre_index, post_index] += conn_array[
                            self.nodes.index(pre), self.nodes.index(post)
                        ]

        return cv

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

    def to_plotly_matrix_fig(self, synclass):
        import plotly.express as px

        conn_array = self.connections[synclass]

        fig = px.imshow(
            conn_array,
            labels=dict(x="Postsynaptic", y="Presynaptic", color="Synapses"),
            x=self.nodes,
            y=self.nodes,
            color_continuous_scale="BuPu",
        )

        return fig


if __name__ == "__main__":
    cds = ConnectomeDataset()

    cds.add_connection(ConnectionInfo("VA6", "VD6", 6, "Send", "Acetylcholine"))
    cds.add_connection(ConnectionInfo("VB6", "DD4", 32, "Send", "Acetylcholine"))

    cds.add_connection(ConnectionInfo("VD6", "VA6", 3, "Send", "GABA"))

    cds.summary()
