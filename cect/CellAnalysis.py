"""
This is still a work in progress...
"""

import sys

from cect import print_
from cect.Cells import COOK_GROUPING_1
from cect.Cells import get_standard_color
from matplotlib import pyplot as plt
from cect.Cells import are_bilateral_pair
from cect.Cells import is_bilateral_left
from cect.Cells import is_bilateral_right

all_sym_info = {}


def test_bilaterals():
    # from cect.White_whole import get_instance
    # from cect.Yim2024DataReader import get_instance

    # from cect.VarshneyDataReader import get_instance

    #
    from cect.White_whole import get_instance
    # from cect.WormNeuroAtlasFuncReader import get_instance

    # from cect.Cook2020DataReader import get_instance
    # from cect.TestDataReader import get_instance

    """
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
    from cect.WitvlietDataReader8 import get_instance
    from cect.SpreadsheetDataReader import get_instance
    from cect.BrittinDataReader import get_instance
    from cect.WormNeuroAtlasMAReader import get_instance
    from cect.RipollSanchezDataReader import get_instance
    from cect.Cook2019HermReader import get_instance
    from cect.ConnectomeView import SOCIAL_VIEW as view"""
    #
    # from cect.ConnectomeView import NEURONS_VIEW as view

    # from cect.ConnectomeView import NONPHARYNGEAL_NEURONS_HM_VIEW as view
    from cect.ConnectomeView import RAW_VIEW as view
    # from cect.ConnectomeView import PHARYNX_VIEW as view

    cds = get_instance()

    cds2 = cds.get_connectome_view(view)

    synclass = "Chemical Inh"

    synclass = (
        "Chemical Exc"
        if "Raw" not in view.name
        else ("Functional" if "Func" in view.name else "Chemical")
    )

    generate_graphs(cds2, synclass)


def generate_graphs(cds, synclass):
    if "-nogui" not in sys.argv:
        for group in COOK_GROUPING_1:
            print_(" = Adding plot for %s" % group)
            xs = []
            ys = []
            labels = []
            colors = []
            markers = []
            fill_styles = []
            pre_cells = sorted(COOK_GROUPING_1[group])

            for pre_cell_index in range(len(pre_cells)):
                pre_cell = pre_cells[pre_cell_index]
                conns = cds.get_connections_from(
                    pre_cell, synclass, ordered_by_weight=True
                )
                for post_cell in conns:
                    weight = conns[post_cell]
                    colors.append(get_standard_color(post_cell))
                    xs.append(pre_cell_index)
                    ys.append(weight)
                    labels.append(pre_cell)
                    if weight < 0:
                        fill_styles.append("none")
                    else:
                        fill_styles.append("full")

                    if are_bilateral_pair(pre_cell, post_cell):
                        markers.append("D")
                    elif is_bilateral_left(pre_cell):
                        markers.append(">")
                    elif is_bilateral_right(pre_cell):
                        markers.append("<")
                    else:
                        markers.append("o")

                    """print_(
                        f"  Adding {pre_cell}->{post_cell} with weight {weight} ({markers[-1]})"
                    )"""

            if len(xs) > 0:
                fig, ax = plt.subplots()
                plt.title("Conns of type: %s from cells in: %s" % (synclass, group))

                for i in zip(labels, ys, colors, markers, fill_styles):
                    plt.plot(
                        i[0], i[1], linewidth=0, color=i[2], marker=i[3], fillstyle=i[4]
                    )

                plt.setp(
                    ax.get_xticklabels(),
                    rotation=90,
                    ha="center",
                    rotation_mode="default",
                )

                # ax.set_xticks(ticks=range(len(pre_cells)), labels=pre_cells)

        plt.show()


if __name__ == "__main__":
    test_bilaterals()

    """
    from cect.Cells import _generate_cell_table
    from cect.Cells import PHARYNGEAL_NEURONS
    cells = PHARYNGEAL_NEURONS
    _generate_cell_table('Test', cells)"""
