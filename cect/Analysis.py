import sys
import numpy as np

from cect.Cells import get_contralateral_cell
from cect.ConnectomeReader import SYMMETRY_COLORMAP
from cect import print_
import json
import matplotlib.pyplot as plt


all_sym_info = {}


def register_symmetry_info(reader, view, synclass, percentage):
    if reader not in all_sym_info:
        all_sym_info[reader] = {}
    if view not in all_sym_info[reader]:
        all_sym_info[reader][view] = {}
    all_sym_info[reader][view][synclass] = percentage


def save_symmetry_info():
    with open("cect/cache/symmetry_measures.json", "w") as fp:
        json.dump(all_sym_info, fp, indent=4)


def array_info(conn_array):
    nonzero = np.count_nonzero(conn_array)
    print_(
        "- Connection - shape: %s, %i non-zero entries, %i total\n%s\n"
        % (
            conn_array.shape,
            nonzero,
            np.sum(conn_array),
            conn_array,
        )
    )


def convert_to_symmetry_array(cds, synclasses, verbose=False):
    if verbose:
        print_("Converting to symmetry array for synclasses: %s" % (synclasses))
    dim = list(cds.connections.values())[0].shape[0]

    new_conn_array = np.zeros([dim, dim], dtype=np.float64)
    if verbose:
        array_info(new_conn_array)

    for synclass in synclasses:
        # print_("   Adding conns of type: %s" % synclass)
        if synclass in cds.connections:
            conns_cs = cds.connections[synclass]

            if verbose:
                array_info(conns_cs)
            for i in range(len(conns_cs)):
                for j in range(len(conns_cs[i])):
                    if (
                        i != j
                    ):  #  Kim et al 2024: Self-connections are treated as nonexistent (∀𝐴𝑖𝑖 = 0).
                        new_conn_array[i, j] = (
                            new_conn_array[i, j] or conns_cs[i, j] > 0
                        )

    if verbose:
        print_("Symm array:")
        array_info(new_conn_array)

    conn_count = 0
    symm_conn_count = 0

    scaled_conn_array = np.array(new_conn_array)

    verbose = False
    for i in range(len(new_conn_array)):
        pre = cds.nodes[i]
        pre_ = get_contralateral_cell(pre)
        for j in range(len(new_conn_array[i])):
            post = cds.nodes[j]
            post_ = get_contralateral_cell(post)
            w = new_conn_array[i][j]
            if w != 0:
                if verbose:
                    print_(f"Connection {conn_count}:\t{pre}->{post} ({w})")
                assert pre is not post
                if pre_ not in cds.nodes:
                    if verbose:
                        print_(
                            f"   - Mirror conn:\t{pre_}->{post_} not possible as {pre_} missing!\n"
                        )
                    w_ = -1
                elif post_ not in cds.nodes:
                    if verbose:
                        print_(
                            f"   - Mirror conn:\t{pre_}->{post_} not possible as {post_} missing!\n"
                        )
                    w_ = -1
                else:
                    w_ = new_conn_array[cds.nodes.index(pre_), cds.nodes.index(post_)]
                    if verbose:
                        print_(f"   - Mirror:\t{pre_}->{post_} ({w_})\n")

                symm_conn_count += w_
                if w_ <= 0:
                    scaled_conn_array[i][j] = 0.5
                    if w_ == 0:
                        scaled_conn_array[
                            cds.nodes.index(pre_), cds.nodes.index(post_)
                        ] = -1
                conn_count += 1

    percentage = 100 * symm_conn_count / conn_count
    info = f"Of {(len(new_conn_array) ** 2)} possible edges, {conn_count} are connected, {int(symm_conn_count)} are mirrored - {'%.2f' % percentage}% "
    if verbose:
        print_(info)

    return scaled_conn_array, percentage, info


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

    print(
        "NOTE: For the sake of this paper, we excluded the pharyngeal neurons from the connectome data for both genders due to their distinction from the somatic nervous system."
    )

    cds = get_instance()

    cds2 = cds.get_connectome_view(view)

    synclass = "Chemical Inh"

    synclass = (
        "Chemical"
        if "Raw" not in view.name
        else ("Functional" if "Func" in view.name else "Chemical")
    )

    # print(cds2.connect)

    # synclass = "Chemical"
    # synclass = "Electrical"

    # import plotly.io as pio
    # pio.renderers.default = "browser"

    if "-nogui" not in sys.argv:
        # cds2.connection_number_plot

        print(f"Plotting synclass {synclass} for {view.name}")
        fig, info = cds2.to_plotly_matrix_fig(
            synclass, view, SYMMETRY_COLORMAP, bold_bilaterals=True, symmetry=True
        )

        fig.show()


def plot_symmetry(
    json_file="cect/cache/symmetry_measures.json",
    synclass: str = "Chemical",
    datasets_line1=None,
    datasets_line2=None,
):
    """
    Plot symmetry for specified synclass across selected datasets.
    Produces 3 subplots for SensorySomaticH, MotorSomaticH, InterneuronsSomaticH.

    Parameters:
        json_file (str): Path to the cached JSON file.
        synclass (str): Synapse class to plot, e.g., "Chemical".
        datasets_to_plot (list, optional): List of datasets to include. Defaults to all.
    """
    # Load JSON data
    with open(json_file, "r") as f:
        data = json.load(f)

    views = [
        "SensorySomaticH",
        "MotorSomaticH",
        "InterneuronsSomaticH",
        "NonpharyngealH",
    ]

    if datasets_line1 is None:
        datasets_line1 = list(data.keys())
    if datasets_line2 is None:
        datasets_line2 = list(data.keys())

    x_labels = list(datasets_line2)
    x_full = np.arange(len(x_labels))

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle(f"Symmetry Across SomaticH Views ({synclass})", fontsize=16)

    def get_val(view, dataset):
        val = data.get(dataset, {}).get(view, {}).get(synclass)
        if val is None:
            return None
        try:
            return float(val)
        except (ValueError, TypeError):
            return None

    for i, view in enumerate(views):
        ax = axes[0]

        # --- Line 1 (baseline): use only its own x positions; this keeps the line continuous across Yim2024 ---
        x1 = []
        y1 = []
        for idx, lbl in enumerate(x_labels):
            if lbl in datasets_line1:
                v = get_val(view, lbl)
                if v is not None:
                    x1.append(idx)
                    y1.append(v)
        # --- Line 2 (with Yim2024): aligned to every x tick in datasets_line2 ---
        y2 = [get_val(view, lbl) if lbl in datasets_line2 else None for lbl in x_labels]
        # Convert None to np.nan for plotting
        y2 = [np.nan if v is None else v for v in y2]

        ax.plot(x1, y1, marker="o", linestyle="-", label="Normal")
        ax.plot(x_full, y2, marker="s", linestyle="--", label="Dauer")

        ax.set_xticks(x_full)
        ax.set_xticklabels(x_labels, rotation=45, ha="right")
        ax.set_title(view, fontsize=14)
        ax.set_xlabel("Dataset", fontsize=12)
        ax.set_ylabel("Symmetry (%)", fontsize=12)
        ax.set_ylim(0, 105)
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def main1():
    line1 = [
        "Witvliet1",
        "Witvliet2",
        "Witvliet3",
        "Witvliet4",
        "Witvliet5",
        "Witvliet6",
        "White_L4",
        "Witvliet7",
        "Witvliet8",
        "Cook2019Herm",
    ]
    print(line1)

    line2 = [
        "Witvliet1",
        "Witvliet2",
        "Witvliet3",
        "Witvliet4",
        "Witvliet5",
        "Witvliet6",
        "Yim2024",
        "White_L4",
        "Witvliet7",
        "Witvliet8",
        "Cook2019Herm",
    ]

    plot_symmetry(synclass="Chemical", datasets_line1=None, datasets_line2=line2)


def main2():
    from cect.Analysis import convert_to_symmetry_array
    from cect.Utils import get_connectome_dataset
    from cect.ConnectomeView import get_view

    # quit()

    datasets = [
        "Witvliet1",
        "Witvliet2",
        "Witvliet3",
        "Witvliet4",
        "Witvliet5",
        "Witvliet6",
        "Yim2024",
        "White_L4",
        "Witvliet7",
        "Witvliet8",
        "Cook2019Herm",
    ]
    views = [
        "SensorySomaticH",
        "MotorSomaticH",
        "InterneuronsSomaticH",
        "Neurons",
    ]

    synclass = "Chemical"

    symmetries = {}

    for dataset_name in datasets:
        print_(f"\n\n--- Loading dataset: {dataset_name} ---")
        cds = get_connectome_dataset(dataset_name, from_cache=True)

        for view in views:
            print_(f"  Applying view: {view} to dataset: {dataset_name} ---")

            v = get_view(view)
            if v.name not in symmetries:
                symmetries[v.name] = []

            cds_view = cds.get_connectome_view(v)

            conn_array, percentage, sym_info = convert_to_symmetry_array(
                cds_view, [synclass]
            )

            symmetries[v.name].append(percentage)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_ylabel("Symmetry (%)", fontsize=12)

    for view in symmetries:
        ax.plot(
            datasets,
            symmetries[view],
            marker="o",
            linestyle="-",
            label=view,
            linewidth=3 if view == "Neurons" else 1,
        )

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    ax.legend()

    """print_("\n\n=== Final Symmetry Info ===")
    for dataset_name in info:
        print_(f"\nDataset: {dataset_name}")
        for view in info[dataset_name]:
            print_(f"  View: {view} - {info[dataset_name][view]}")"""

    print_("\n\n=== Symmetry Percentages by View ===")
    for view in symmetries:
        print_(f"View: {view} - Symmetry Percentages: {symmetries[view]}")

    # plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    # main1()

    main2()
