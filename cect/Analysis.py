import sys
import numpy as np

from cect.Cells import get_contralateral_cell
from cect.ConnectomeReader import SYMMETRY_COLORMAP


def array_info(conn_array):
    nonzero = np.count_nonzero(conn_array)
    print(
        "- Connection - shape: %s, %i non-zero entries, %i total\n%s\n"
        % (
            conn_array.shape,
            nonzero,
            np.sum(conn_array),
            conn_array,
        )
    )


def convert_to_symmetry_array(cds, synclasses):
    dim = list(cds.connections.values())[0].shape[0]

    new_conn_array = np.zeros([dim, dim], dtype=np.float64)
    array_info(new_conn_array)

    """for synclass in [
        "Chemical",
        "Chemical Exc",
        "Chemical Inh",
        "Electrical",
        "Contact",
        "Functional",
        "Extrasynaptic",
    ]:"""
    for synclass in synclasses:
        print("   Adding conns of type: %s" % synclass)
        if synclass in cds.connections:
            conns_cs = cds.connections[synclass]

            array_info(conns_cs)
            for i in range(len(conns_cs)):
                for j in range(len(conns_cs[i])):
                    if (
                        i != j
                    ):  #  Kim et al 2024: Self-connections are treated as nonexistent (∀𝐴𝑖𝑖 = 0).
                        new_conn_array[i, j] = (
                            new_conn_array[i, j] or conns_cs[i, j] > 0
                        )

    print("Amalgamated array:")
    array_info(new_conn_array)

    conn_count = 0
    symm_conn_count = 0

    scaled_conn_array = np.array(new_conn_array)

    for i in range(len(new_conn_array)):
        pre = cds.nodes[i]
        pre_ = get_contralateral_cell(pre)
        for j in range(len(new_conn_array[i])):
            post = cds.nodes[j]
            post_ = get_contralateral_cell(post)
            w = new_conn_array[i][j]
            if w != 0:
                print(f"Connection {conn_count}:\t{pre}->{post} ({w})")
                assert pre is not post
                w_ = new_conn_array[cds.nodes.index(pre_), cds.nodes.index(post_)]
                print(f"   - Mirror:\t{pre_}->{post_} ({w_})\n")
                symm_conn_count += w_
                if w_ == 0:
                    scaled_conn_array[i][j] = 0.5
                    scaled_conn_array[
                        cds.nodes.index(pre_), cds.nodes.index(post_)
                    ] = -1
                conn_count += 1

    info = f"Of {(len(new_conn_array) ** 2)} possible edges, {conn_count} are connected, {int(symm_conn_count)} are mirrored - {'%.2f' % (100 * symm_conn_count / conn_count)}% "
    print(info)

    return scaled_conn_array, info


def test_bilaterals():
    # from cect.White_whole import get_instance
    # from cect.Yim2024DataReader import get_instance

    # from cect.VarshneyDataReader import get_instance

    #
    from cect.White_whole import get_instance
    # from cect.TestDataReader import get_instance
    # from cect.Cook2020DataReader import get_instance

    """from cect.WormNeuroAtlasFuncReader import get_instance
    from cect.RipollSanchezDataReader import get_instance
    from cect.WitvlietDataReader1 import get_instance # 65
    from cect.WitvlietDataReader2 import get_instance # 70.85
    from cect.WitvlietDataReader3 import get_instance # 67.5
    from cect.WitvlietDataReader4 import get_instance # 78.27
    from cect.WitvlietDataReader5 import get_instance # 71.65
    from cect.WitvlietDataReader6 import get_instance # 71.31
    from cect.WitvlietDataReader7 import get_instance # 66.57
    from cect.WitvlietDataReader8 import get_instance # 69.70

    from cect.Cook2019MaleReader import get_instance
    from cect.Cook2019HermReader import get_instance
    from cect.WitvlietDataReader8 import get_instance
    from cect.SpreadsheetDataReader import get_instance
    from cect.BrittinDataReader import get_instance
    from cect.WormNeuroAtlasMAReader import get_instance
    from cect.RipollSanchezDataReader import get_instance
    from cect.ConnectomeView import SOCIAL_VIEW as view"""
    #
    # from cect.ConnectomeView import NEURONS_VIEW as view

    # from cect.ConnectomeView import NONPHARYNGEAL_NEURONS_HM_VIEW as view
    # from cect.ConnectomeView import RAW_VIEW as view
    from cect.ConnectomeView import PHARYNX_VIEW as view

    print(
        "NOTE: For the sake of this paper, we excluded the pharyngeal neurons from the connectome data for both genders due to their distinction from the somatic nervous system."
    )

    cds = get_instance()

    cds2 = cds.get_connectome_view(view)

    synclass = "Chemical Inh"
    synclass = "Chemical Exc" if "Raw" not in view.name else "Chemical"

    # synclass = "Acetylcholine"
    # synclass = "Chemical"
    # synclass = "Electrical"

    print(cds2.summary())

    print("Keys: %s, plotting: %s" % (view.synclass_sets.keys(), synclass))

    # scaled_conn_array, info = convert_to_symmetry_array(cds2)

    print("------")
    # print(array_info(scaled_conn_array))

    # amal = "CS+GJ"
    # cds2.connections[amal] = scaled_conn_array

    to_plot = "Electrical"
    to_plot = "Chemical Exc"

    # import plotly.io as pio
    # pio.renderers.default = "browser"
    if "-nogui" not in sys.argv:
        # cds2.connection_number_plot

        fig, info = cds2.to_plotly_matrix_fig(
            to_plot, view, SYMMETRY_COLORMAP, bold_bilaterals=True, symmetry=True
        )

        fig.show()


if __name__ == "__main__":
    test_bilaterals()
