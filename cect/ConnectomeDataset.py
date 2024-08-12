from cect import print_

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import DEFAULT_COLORMAP
from cect.Cells import get_short_description
from cect.Cells import get_standard_color
from cect.ConnectomeReader import is_neuron
from cect.ConnectomeReader import is_muscle

import numpy as np
import math


class ConnectomeDataset:
    DEFAULT_DTYPE = np.float64

    verbose = False

    def __init__(self):
        self.nodes = []
        self.connections = {}
        self.connection_infos = []

        self.view = None

    def _expand_conn_arrays(self):
        for c in self.connections:
            conn_array = self.connections[c]

            dim = conn_array.shape[0]
            new_conn_array = np.zeros([dim + 1, dim + 1], dtype=self.DEFAULT_DTYPE)
            new_conn_array[: conn_array.shape[0], : conn_array.shape[1]] = conn_array

            self.connections[c] = new_conn_array

    def add_connection_info(self, conn: ConnectionInfo):
        if self.verbose:
            print_("----   Adding: %s" % conn)

        self.connection_infos.append(conn)

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

    def read_data(self):
        return self.get_neuron_to_neuron_conns()

    def get_neuron_to_neuron_conns(self):
        neurons = set([])
        neuron_conns = []
        for conn_info in self.connection_infos:
            if is_neuron(conn_info.pre_cell) and is_neuron(conn_info.post_cell):
                neurons.add(conn_info.pre_cell)
                neurons.add(conn_info.post_cell)
                neuron_conns.append(conn_info)
        return list(neurons), neuron_conns

    def read_muscle_data(self):
        return self.get_neuron_to_muscle_conns()

    def get_neuron_to_muscle_conns(self):
        neurons = set([])
        muscles = set([])
        conns = []

        for conn_info in self.connection_infos:
            if is_neuron(conn_info.pre_cell) and is_muscle(conn_info.post_cell):
                neurons.add(conn_info.pre_cell)
                muscles.add(conn_info.post_cell)
                conns.append(conn_info)

        return list(neurons), list(muscles), conns

    def get_connections_from(self, node, synclass):
        if synclass not in self.connections:
            return {}
        conn_array = self.connections[synclass]
        if not node in self.nodes:
            return {}
        index = self.nodes.index(node)
        slice = conn_array[index]
        conns = {}
        for idn, n in enumerate(self.nodes):
            num = slice[idn]
            if num > 0:
                conns[n] = num
        return conns

    def get_connections_summary(self, node, synclass, direction, bold_cells=False):
        if direction == "from":
            conns = self.get_connections_from(node, synclass)
        elif direction == "to":
            conns = self.get_connections_to(node, synclass)

        ordered = dict(
            sorted(conns.items(), key=lambda key_val: key_val[1], reverse=True)
        )
        vals = [
            "%s: %s"
            % (
                k if not bold_cells else "<b>%s</b>" % k,
                int(v) if v == int(v) else v,
            )
            for k, v in ordered.items()
        ]
        info = ""
        count = 0
        for v in vals:
            if len(info.split("<br>")[-1]) > 80:
                info += "<br>"
            info += v + ", "

        return info[:-2]

    def get_connections_to(self, node, synclass):
        if synclass not in self.connections:
            return {}
        conn_array = self.connections[synclass]
        if not node in self.nodes:
            return {}
        index = self.nodes.index(node)
        slice = conn_array.T[index]
        conns = {}
        for idn, n in enumerate(self.nodes):
            num = slice[idn]
            if num > 0:
                conns[n] = num
        return conns

    def get_connectome_view(self, view):
        self.view = view

        cv = ConnectomeDataset()

        for n in view.node_sets:
            if view.only_show_existing_nodes:
                if n.name in self.nodes:
                    cv.nodes.append(n.name)
            else:
                cv.nodes.append(n.name)

        if self.verbose:
            print_(
                "-- Creating view (%s, only_show_existing_nodes=%s) with %i nodes: %s\n  My %i nodes: %s"
                % (
                    view.name,
                    view.only_show_existing_nodes,
                    len(cv.nodes),
                    sorted(cv.nodes),
                    len(self.nodes),
                    sorted(self.nodes),
                )
            )

        for synclass_set in view.synclass_sets:
            cv.connections[synclass_set] = np.zeros(
                [len(cv.nodes)] * 2, dtype=self.DEFAULT_DTYPE
            )

            for synclass in view.synclass_sets[synclass_set]:
                if synclass in self.connections:
                    conn_array = self.connections[synclass]
                    for pre in self.nodes:
                        pre_index = (
                            cv.nodes.index(pre)
                            if view.only_show_existing_nodes
                            else view.get_index_of_cell(pre)
                        )
                        for post in self.nodes:
                            post_index = (
                                cv.nodes.index(post)
                                if view.only_show_existing_nodes
                                else view.get_index_of_cell(post)
                            )

                            if self.verbose:
                                print(
                                    "-- Testing if %s (%i), %s (%s) in my %i node sets %s..."
                                    % (
                                        pre,
                                        pre_index,
                                        post,
                                        post_index,
                                        len(view.node_sets),
                                        view.node_sets[:5],
                                    )
                                )

                            if pre_index >= 0 and post_index >= 0:
                                cv.connections[synclass_set][
                                    pre_index, post_index
                                ] += conn_array[
                                    self.nodes.index(pre), self.nodes.index(post)
                                ]

        return cv

    def summary(self):
        info = "Nodes present: %s\n" % self.nodes
        for c in self.connections:
            conn_array = self.connections[c]
            info += (
                "- Connection type - %s: %s, %i non-zero entries, %i total\n%s\n"
                % (
                    c,
                    conn_array.shape,
                    np.count_nonzero(conn_array),
                    np.sum(conn_array),
                    conn_array,
                )
            )
        return info

    def to_plotly_matrix_fig(self, synclass, color_continuous_scale=DEFAULT_COLORMAP):
        import plotly.express as px

        def get_color_html(color, node):
            return f'<span style="color:{color};">{node}</span>'

        conn_array = self.connections[synclass]
        
        node_colors = [get_standard_color(node) for node in self.nodes]

        x_ticktext = [get_color_html(color, node) for node, color in zip(self.nodes, node_colors)]
        y_ticktext = [get_color_html(color, node) for node, color in zip(self.nodes, node_colors)]
      
        # Create the figure
        fig = px.imshow(
            conn_array,
            labels=dict(x="Postsynaptic", y="Presynaptic", color="Synapses"),
            x=x_ticktext,
            y=y_ticktext,
            color_continuous_scale=color_continuous_scale,
        )

        return fig



    def to_plotly_graph_fig(self, synclass, view):
        conn_array = self.connections[synclass]
        import plotly.graph_objects as go
        import networkx as nx

        G = nx.Graph(conn_array)
        pos = nx.spring_layout(G, seed=1)

        for i, node_value in enumerate(self.nodes):
            node_set = view.get_node_set(node_value)
            if node_set.position is not None:
                pos[i] = node_set.position

        node_x = [float("{:.6f}".format(pos[i][0])) for i in G.nodes()]
        node_y = [float("{:.6f}".format(pos[i][1])) for i in G.nodes()]

        edge_x = []
        edge_y = []
        weights = []

        import random

        for edge in G.edges():
            x0, y0 = (float("{:.6f}".format(a)) for a in pos[edge[0]])
            x1, y1 = (float("{:.6f}".format(a)) for a in pos[edge[1]])
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        # Add nodes to the figure
        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            mode="lines",
            text=self.nodes,
            line=dict(color="grey", width=1),
            hoverinfo="none",
        )

        node_adjacencies = []
        node_colours = []
        node_text = []
        node_sizes = []
        node_shapes = []

        DEFAULT_SIZE = 10

        for node, adjacencies in enumerate(G.adjacency()):
            node_adjacencies.append(len(adjacencies[1]))
            if not view.has_color():
                node_colours.append(len(adjacencies[1]))

        for i, node_value in enumerate(self.nodes):
            num_connections = node_adjacencies[i]

            node_set = view.get_node_set(node_value)

            if view.has_color():
                node_colours.append(node_set.color)

            node_sizes.append(DEFAULT_SIZE * math.sqrt(len(node_set.cells)))

            if node_set.shape is not None:
                node_shapes.append(node_set.shape)
            else:
                node_shapes.append("circle")

            if node_set.is_one_cell():
                desc = get_short_description(node_set.name)
            else:
                desc = "Cells: "
                cc = 0
                for c in node_set.cells:
                    if cc % 10 == 9:
                        desc += c + "<br>"
                    desc += c + ", "
                    cc += 1
                desc = desc[:-2]

            text = f"<b>{node_value}</b>"
            text += "<br>%s" % desc

            into = self.get_connections_summary(
                node_value, synclass, "to", bold_cells=True
            )
            if len(into) > 0:
                text += f"<br>Conns in: {into}"

            out_of = self.get_connections_summary(
                node_value, synclass, "from", bold_cells=True
            )
            if len(out_of) > 0:
                text += f"<br>Conns out: {out_of}"

            node_text.append(text)

        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers",
            text=self.nodes,
            marker=dict(
                showscale=not view.has_color(),
                colorscale="YlGnBu",
                reversescale=True,
                color=[],
                size=DEFAULT_SIZE,
                colorbar=dict(
                    thickness=15,
                    title="Node Connections",
                    xanchor="left",
                    titleside="right",
                ),
                line_width=1,
            ),
            hoverinfo="text",
        )

        node_trace.marker.size = node_sizes
        node_trace.marker.symbol = node_shapes
        node_trace.marker.color = node_colours
        node_trace.text = node_text

        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                showlegend=False,
                hovermode="closest",
                margin=dict(b=20, l=5, r=5, t=40),
                xaxis=dict(showgrid=False, zeroline=False),
                yaxis=dict(showgrid=False, zeroline=False),
            ),
        )

        return fig


if __name__ == "__main__":
    cds = ConnectomeDataset()

    cds.add_connection_info(ConnectionInfo("VA6", "VD6", 6, "Send", "Acetylcholine"))
    cds.add_connection_info(ConnectionInfo("VA6", "VD1", 1, "Send", "Acetylcholine"))
    cds.add_connection_info(ConnectionInfo("VA2", "VA6", 7, "Send", "Acetylcholine"))
    cds.add_connection_info(ConnectionInfo("VA6", "VD5", 5, "Send", "Acetylcholine"))
    cds.add_connection_info(ConnectionInfo("VB6", "DD4", 32, "Send", "Acetylcholine"))

    cds.add_connection_info(ConnectionInfo("VD6", "VA6", 3, "Send", "GABA"))

    print(cds.summary())

    print(cds.get_connections_from("VA6", "Acetylcholine"))
    print("From: %s" % cds.get_connections_summary("VA6", "Acetylcholine", "from"))
    print("To: %s" % cds.get_connections_summary("VA6", "Acetylcholine", "to"))
    print(cds.get_connections_to("DD4", "Acetylcholine"))
