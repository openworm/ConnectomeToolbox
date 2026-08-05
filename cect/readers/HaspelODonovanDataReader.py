from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

from cect.Neurotransmitters import CHEMICAL_SYN_TYPE

# from cect.Neurotransmitters import ACETYLCHOLINE, GABA
from cect.Neurotransmitters import (
    GENERIC_EXCITATORY_CHEM_SYN_CLASS,
    GENERIC_INHIBITORY_CHEM_SYN_CLASS,
)
from cect.Neurotransmitters import GENERIC_ELEC_SYN_CLASS, ELECTRICAL_SYN_TYPE

from cect import print_
import os


data_location = os.path.dirname(os.path.abspath(__file__)) + "/../data/"

mat_filename = "CeConnMtrcs_170626.mat"
filename = "%s%s" % (data_location, mat_filename)

NAME = "HaspelODonovan"

READER_DESCRIPTION = (
    """Data extracted from %s for neuronal connectivity"""
    % get_dataset_source_on_github(filename.split("/")[-1])
)

DATASET_DESCRIPTION = "A complete connectivity model for all 75 _C. elegans_ ventral cord motorneurons from Haspel and O'Donovan 2011, produced by identifying a repeating pattern in the empirically known anterior connections and extrapolating it into the posterior half of the animal where direct EM data were absent. TODO: correct muscle numbering!!"


WEIGHTS = "Weights are based on White et al. 1986 and Varshney et al. 2011 connectivity datasets"

FULL_CONN = "full"
ONE_SEG_CONN = "seg"


def _standardise_cell_name(cell):
    """
    Returns cell name with an index without leading zero. E.g. VB01 -> VB1.
    """
    if cell[:2] in ["VA", "VB", "VC", "VD", "DA", "DB", "DD", "AS"] and cell[
        -2:
    ].startswith("0"):
        return ["%s%s" % (cell[:-2], cell[-1:])]

    if cell.startswith("MDlr"):
        return ["MDL%s" % (cell[4:]), "MDR%s" % (cell[4:])]
    if cell.startswith("MVlr"):
        return ["MVL%s" % (cell[4:]), "MVR%s" % (cell[4:])]

    return [cell]


class HaspelODonovanDataReader(ConnectomeDataset):
    """Reader for HaspelODonovan connectivity dataset"""

    def __init__(self, full_or_one_seg):
        ConnectomeDataset.__init__(self)

        self.full_or_one_seg = full_or_one_seg

        cells, conns = self.read_all_data()

        for conn in conns:
            self.add_connection_info(
                conn,
                append_existing_connections=False,
                check_overwritten_connections=True,
                fail_on_any_repeated_connection=True,
            )

    def read_all_data(self):

        cells = set([])
        conns = []

        import scipy.io

        print_("Loading data from: %s" % filename)
        mat = scipy.io.loadmat(filename)

        names = [
            str(n[0]) for n in mat["Names_conn_%s" % self.full_or_one_seg].flatten()
        ]
        A = mat["A_conn_%s" % self.full_or_one_seg]
        J = mat["J_conn_%s" % self.full_or_one_seg]

        for i, pre in enumerate(names):
            orig_pre = pre
            pre = _standardise_cell_name(pre)[0]
            cells.add(pre)
            for j, post in enumerate(names):
                orig_posts = post
                posts = _standardise_cell_name(post)
                for post in posts:
                    cells.add(post)
                    w = A[j, i]
                    if w != 0:
                        print_(
                            " - %s -> %s;\t(was: %s -> %s);\tA=%d"
                            % (pre, post, orig_pre, orig_posts, w)
                        )
                        conns.append(
                            ConnectionInfo(
                                pre,
                                post,
                                w if w > 0 else -w,
                                CHEMICAL_SYN_TYPE,
                                GENERIC_EXCITATORY_CHEM_SYN_CLASS
                                if w > 0
                                else GENERIC_INHIBITORY_CHEM_SYN_CLASS,
                            )
                        )

                    if J[j, i] != 0:
                        print_("%s -> %s: J=%d" % (pre, post, J[j, i]))
                        conns.append(
                            ConnectionInfo(
                                pre,
                                post,
                                J[j, i],
                                ELECTRICAL_SYN_TYPE,
                                GENERIC_ELEC_SYN_CLASS,
                            )
                        )

        print_("Loaded %d cells and %d connections" % (len(cells), len(conns)))

        return cells, conns

    def read_data(self):
        return self._read_data()

    def read_muscle_data(self):
        return self._read_muscle_data()


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[-1]))
    else:
        return HaspelODonovanDataReader(full_or_one_seg=FULL_CONN)


def main():
    my_instance = get_instance()

    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(
        cells, neuron_conns, neurons2muscles, muscles, muscle_conns, print_details_on=[]
    )

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    cell = "ADAR"
    syntype = "Generic_CS"
    conns = my_instance.get_connections_from(cell, syntype)
    print(f"There are {len(conns)} connections from {cell} of type {syntype}:")
    for c in sorted(conns.keys()):
        print(f" {cell} -> {c}: {conns[c]}")

    import numpy as np

    for syntype in my_instance.connections.keys():
        conn_array = my_instance.connections[syntype]
        print(
            f"\n === Connection array for synapse type {syntype} has shape: {conn_array.shape}"
        )
        nonzero = np.count_nonzero(conn_array)
        count_diagonal_entries = np.count_nonzero(np.diag(conn_array))
        is_symmetric = np.array_equal(conn_array, conn_array.T)
        sym_info = ""
        if is_symmetric:
            diagonal_sum = np.sum(np.diag(conn_array))
            unique_sum = (np.sum(conn_array) - diagonal_sum) / 2 + diagonal_sum

            sym_info = f"\nMatrix is symmetric with <b>{count_diagonal_entries + int((nonzero - count_diagonal_entries) / 2)}</b> unique pairs (total unique pair weight: <b>{unique_sum}</b>)<br/>"
        else:
            sym_info = "\nNOT symmetric"
        diag_info = (
            "<b>%s</b> nodes with self-connections<br/>" % count_diagonal_entries
            if count_diagonal_entries > 0
            else ""
        )
        print(
            f"<b>{nonzero}</b> non-zero entries<br/>{diag_info}{sym_info}Avg. weight: <b>{np.mean(conn_array[conn_array != 0])}</b><br/>Sum of weights: <b>{np.sum(conn_array)}</b>\n"
        )

        import sys

        if "-nogui" not in sys.argv:
            print(my_instance.summary())

            # from cect.ConnectomeView import RAW_VIEW as view
            from cect.ConnectomeView import LOCOMOTION_4_VIEW as view
            # from cect.ConnectomeView import NEURONS_VIEW as view

            cds2 = my_instance.get_connectome_view(view)

            print(cds2.summary())

            fig = cds2.to_plotly_graph_fig(GENERIC_EXCITATORY_CHEM_SYN_CLASS, view)
            fig = cds2.to_plotly_graph_fig("Chemical", view)
            """

            fig, _ = cds2.to_plotly_matrix_fig(
                "Chemical",
                view,
            )"""
            import plotly.io as pio

            pio.renderers.default = "browser"
            import sys

            fig.show()


if __name__ == "__main__":
    main()
