import logging

from cect.ConnectomeReader import ConnectionInfo
from cect import print_

from cect.ConnectomeDataset import ConnectomeDataset

import math
import sys

from cect.readers.WormNeuroAtlasReader import get_all_cells
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

from cect.Neurotransmitters import FUNCTIONAL_SYN_CLASS
from cect.Neurotransmitters import FUNCTIONAL_SYN_TYPE

############################################################

#   A script to read the values in WormNeuroAtlas

############################################################

NAME = "Randi2023"

DEFAULT_MAX_Q = 0.05

LOGGER = logging.getLogger(__name__)

READER_DESCRIPTION = """Data on functional connectivity from the <b><a href="https://github.com/francescorandi/wormneuroatlas">WormNeuroAtlas package</a></b>"""

DATASET_DESCRIPTION = (
    "Data on functional connectivity of _C. elegans_ from WormNeuroAtlas Python package (values extracted with get_signal_propagation_map() & get_signal_propagation_q(), with max_q (q being the false discovery rate) = %s)"
    % DEFAULT_MAX_Q
)

WEIGHTS = "Weights represent the mean post-stimulus calcium response amplitude measured in a downstream neuron following two-photon optogenetic stimulation of an upstream neuron"


class WormNeuroAtlasFuncReader(ConnectomeDataset):
    """Data on functional connectivity from the **[WormNeuroAtlas package](https://github.com/francescorandi/wormneuroatlas)**"""

    def __init__(self, max_q):
        ConnectomeDataset.__init__(self)

        self.max_q = max_q

        print_(
            "Initialising WormNeuroAtlasFuncReader with max q value: %s" % self.max_q
        )
        import wormneuroatlas as wa

        self.verbose = False

        self.atlas = wa.NeuroAtlas()

        self.all_cells = get_all_cells(self.atlas)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(conn)

    def read_data(self):
        conns = []

        dff = self.atlas.get_signal_propagation_map(strain="wt")
        q = self.atlas.get_signal_propagation_q(strain="wt")

        connected_cells = []

        for pre in self.all_cells:
            apre = self.atlas.ids_to_ai([pre])
            for post in self.all_cells:
                apost = self.atlas.ids_to_ai([post])

                connection = False

                bound = 10

                dff_ij_orig = dff[apost, apre][0]

                dff_ij = (
                    0
                    if (apost == apre or math.isnan(dff_ij_orig))
                    else max(-1 * bound, min(bound, dff_ij_orig))
                )
                # dff_ij = dff_ij_orig

                q_ij = q[apost, apre]

                num = dff_ij

                if abs(num) > -10 and q_ij < self.max_q:
                    if num < 0:
                        if self.verbose:
                            print_(
                                "Functional conn junc (%s (%i) -> %s (%i):\t%s (orig = %s, q = %s)"
                                % (pre, apre, post, apost, dff_ij, dff_ij_orig, q_ij)
                            )
                    synclass = FUNCTIONAL_SYN_CLASS
                    syntype = FUNCTIONAL_SYN_TYPE
                    conns.append(
                        ConnectionInfo(
                            str(pre), str(post), float(num), syntype, synclass
                        )
                    )
                    connection = True

                if connection:
                    if pre not in connected_cells:
                        connected_cells.append(str(pre))
                    if post not in connected_cells:
                        connected_cells.append(str(post))

        return connected_cells, conns

    def read_muscle_data(self):
        neurons = []
        muscles = []
        conns = []
        return neurons, muscles, conns


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(
            get_cache_filename(__file__.split("/")[-1].split(".")[0])
        )
    else:
        try:
            return WormNeuroAtlasFuncReader(DEFAULT_MAX_Q)
        except Exception as e:
            print(
                "Problem loading WormNeuroAtlas data. Can be caused by WormBase url not working. Defaulting to loading from cache... Issue: %s"
                % str(e)
            )
            return get_instance(from_cache=True)


if __name__ == "__main__":
    my_instance = get_instance(from_cache=False)
    cells, neuron_conns = my_instance._read_data()
    print("Loaded %s connections" % len(neuron_conns))

    # from cect.ConnectomeReader import analyse_connections
    # analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    to_test = ["I1L", "MI", "MCR", "M2R", "AVBR", "AVEL"]

    import wormneuroatlas as wa

    atlas = wa.NeuroAtlas()
    dff = atlas.get_signal_propagation_map(strain="wt")
    q = atlas.get_signal_propagation_q(strain="wt")

    for cell in to_test:
        # my_instance.atlas.all_about(cell)

        print(
            "Func conns from %s: \n%s"
            % (
                cell,
                "\n".join(
                    [
                        f"   {c}:  \t{float(w)}"
                        for c, w in my_instance.get_connections_from(
                            cell, FUNCTIONAL_SYN_CLASS, ordered_by_weight=True
                        ).items()
                    ]
                ),
            )
        )
        print(
            "Func conns to %s: \n%s"
            % (
                cell,
                "\n".join(
                    [
                        f"   {c}:  \t{float(w)}"
                        for c, w in my_instance.get_connections_to(
                            cell, FUNCTIONAL_SYN_CLASS, ordered_by_weight=True
                        ).items()
                    ]
                ),
            )
        )

    for pre in to_test:
        for post in to_test:
            apre = atlas.ids_to_ai([pre])
            apost = atlas.ids_to_ai([post])

            dff_ij_orig = dff[apost, apre][0]

            print(
                "Func conn from WNA - %s (%i) -> %s (%i):\t%s\t%s(q = %s)"
                % (
                    pre,
                    apre,
                    post,
                    apost,
                    dff_ij_orig,
                    "" if q[apost, apre] < 0.05 else "     NOT INCLUDED...",
                    q[apost, apre],
                )
            )

    import numpy as np

    # ruff: noqa: E712
    dff_valid = np.isnan(dff) != True
    print("Number of valid dff values: %i" % np.count_nonzero(dff_valid))
    q_low = q < 0.05
    print("Number of valid q values (q < 0.05): %i" % np.count_nonzero(q_low))
    q_valid = np.isnan(q) != True
    print("Number of valid q values (not NaN): %i" % np.count_nonzero(q_valid))
    to_include_with_diags = np.multiply(dff_valid, q_low)

    print(
        "Number of connections to include: %i" % np.count_nonzero(to_include_with_diags)
    )
    to_include = to_include_with_diags.copy()
    for i in range(to_include.shape[0]):
        to_include[i, i] = False
    # print(to_include)
    print(
        "Number of connections to include (self conns excluded): %i"
        % np.count_nonzero(to_include)
    )

    if "-nogui" not in sys.argv:
        my_instance.connection_number_plot(FUNCTIONAL_SYN_CLASS)
