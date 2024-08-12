import cect

from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeReader import check_cells
from cect.Cells import get_cell_internal_link
from cect import print_
import json

import sys
import numpy as np

import importlib

all_data = {}


reader_pages = {
    "TestData": "Test_data",
    "Varshney": "Varshney_data",
    "White_A": "White_A_data",
    "White_L4": "White_L4_data",
    "White_whole": "White_whole_data",
    "Witvliet1": "Witvliet1_data",
    "Witvliet2": "Witvliet2_data",
    "WormNeuroAtlas": "WormNeuroAtlas_data",
    "Cook2019Herm": "Cook2019Herm_data",
    "Cook2020": "Cook2020_data",
}

all_data[""] = [
    "Num neurons",
    "Missing neurons",
    "Non neurons",
    "Num muscles",
    "Num N->N conns",
    "Num N with ->M",
    "Num N->M conns",
    "N->N neurotrans.",
    "N->M neurotrans.",
]


def shorten_neurotransmitter(nt):
    return (
        nt.replace("Acetylcholine", "ACh")
        .replace("Serotonin", "5HT")
        .replace("Glutamate", "Glu")
        .replace("Tyramine", "Tyr")
        .replace("FMRFamide", "FMRFam")
        .replace("Generic_", "Gen_")
    )


def _format_json(json_str):
    return json.dumps(json.loads(json_str), sort_keys=True, indent=2)


def get_2d_graph_markdown(reader_name, view, connectome, synclass, indent="    "):
    view_name = view.name

    fig = connectome.to_plotly_graph_fig(synclass, view)

    asset_filename = "assets/%s_%s_%s_graph.json" % (
        reader_name,
        view_name,
        synclass.replace(" ", "_"),
    )

    with open("./docs/%s" % asset_filename, "w") as asset_file:
        asset_file.write(_format_json(fig.to_json()))

    if np.sum(connectome.connections[synclass]) == 0:
        return "\n%sNo connections of type **%s** in the **%s** for **%s**...\n" % (
            indent,
            synclass,
            view_name,
            reader_name,
        )

    return '\n%s```plotly\n%s---8<-- "./%s"\n%s```\n' % (
        indent,
        indent,
        asset_filename,
        indent,
    )


def get_matrix_markdown(reader_name, view_name, connectome, synclass, indent="    "):
    fig = connectome.to_plotly_matrix_fig(synclass)

    asset_filename = "assets/%s_%s_%s.json" % (
        reader_name,
        view_name,
        synclass.replace(" ", "_"),
    )

    with open("./docs/%s" % asset_filename, "w") as asset_file:
        asset_file.write(_format_json(fig.to_json()))

    if np.sum(connectome.connections[synclass]) == 0:
        return "\n%sNo connections of type **%s** in the **%s** for **%s**...\n" % (
            indent,
            synclass,
            view_name,
            reader_name,
        )

    return '\n%s```plotly\n%s---8<-- "./%s"\n%s```\n' % (
        indent,
        indent,
        asset_filename,
        indent,
    )


def generate_comparison_page(quick: bool):
    connectomes = {}

    readers = {
        "SSData": ["cect.SpreadsheetDataReader", None],
        "UpdSSData": ["cect.UpdatedSpreadsheetDataReader", None],
        "UpdSSData2": ["cect.UpdatedSpreadsheetDataReader2", None],
        "Varshney": ["cect.VarshneyDataReader", "Varshney_2011"],
        "White_whole": ["cect.White_whole", "White_1986"],
        "TestData": ["cect.TestDataReader", None],
        "Cook2020": ["cect.Cook2020DataReader", "Cook_2020"],
    }
    if not quick:
        readers["White_A"] = ["cect.White_A", "White_1986"]
        readers["White_L4"] = ["cect.White_L4", "White_1986"]
        readers["Witvliet1"] = ["cect.WitvlietDataReader1", "Witvliet_2021"]
        readers["Witvliet2"] = ["cect.WitvlietDataReader2", "Witvliet_2021"]
        readers["WormNeuroAtlas"] = ["cect.WormNeuroAtlasReader", "Randi_2023"]
        readers["Cook2019Herm"] = ["cect.Cook2019HermReader", "Cook_2019"]

    for reader_name, reader_info in readers.items():
        reader = reader_info[0]
        decription_page = reader_info[1] if len(reader_info) > 1 else None

        print_("\n****** Importing dataset %s using %s ******" % (reader_name, reader))

        reader_module = importlib.import_module(reader)

        """
        # exec("from %s import read_data, read_muscle_data, READER_DESCRIPTION" % reader)
        cells, neuron_conns = reader_module.read_data()

        preferred, not_in_preferred, missing_preferred = check_neurons(cells)

        connectome = None"""

        try:
            connectome = reader_module.get_instance()
            preferred, not_in_preferred, missing_preferred, muscles = check_cells(
                connectome.nodes
            )
            print_("Adding full connectome info: %s" % connectome)

        except Exception as e:
            print_("NOT adding full connectome info (%s)" % e)
            connectome = None

        if reader_name in reader_pages:
            connectomes[reader_name] = connectome

            matrix_filename = "docs/%s.md" % reader_pages[reader_name]
            graph_filename = "docs/%s_graph.md" % reader_pages[reader_name]

            for filename in [graph_filename, matrix_filename]:
                with open(filename, "w") as f:
                    matrix = filename == matrix_filename

                    f.write("## %s\n" % reader_name)
                    if decription_page is not None:
                        f.write(
                            "[Source publication of dataset](%s.md)\n\n"
                            % decription_page
                        )

                    f.write("%s\n\n" % reader_module.READER_DESCRIPTION)

                    f.write(
                        "[View as graph](%s_graph.md){ .md-button } [View as matrix](%s.md){ .md-button }\n\n"
                        % (reader_pages[reader_name], reader_pages[reader_name])
                    )

                    if connectome is not None:
                        from cect.ConnectomeView import ALL_VIEWS

                        indent = "    "

                        for view in ALL_VIEWS:
                            cv = connectome.get_connectome_view(view)

                            f.write('=== "%s"\n' % view.name)

                            for sc in view.synclass_sets:
                                f.write(indent + '=== "%s"\n' % sc)

                                if matrix:
                                    f.write(
                                        get_matrix_markdown(
                                            reader_name,
                                            view.name,
                                            cv,
                                            sc,
                                            indent=indent + indent,
                                        )
                                    )

                                else:
                                    f.write(
                                        get_2d_graph_markdown(
                                            reader_name,
                                            view,
                                            cv,
                                            sc,
                                            indent=indent + indent,
                                        )
                                    )

                    cell_types = {
                        "Neurons": preferred,
                        "Missing neurons": missing_preferred,
                        "Muscles": muscles,
                        "Other cells": not_in_preferred,
                    }

                    for t in cell_types:
                        f.write("\n### %s (%i)\n" % (t, len(cell_types[t])))
                        if len(cell_types[t]) > 0:
                            f.write("<details><summary>Full list of %s</summary>\n" % t)
                            ss = sorted(cell_types[t])
                            for n in ss:
                                f.write("%s" % (get_cell_internal_link(n, True)))
                                if n is not ss[-1]:
                                    f.write(" | ")

                            f.write("\n</details>\n")

                print_("Written page: %s" % filename)

        neurons, neuron_conns = connectome.get_neuron_to_neuron_conns()
        neurons2muscles, muscles, muscle_conns = connectome.get_neuron_to_muscle_conns()

        neuron_nts = {}

        for c in neuron_conns:
            nt = c.synclass
            if len(nt) == 0:
                nt = "**MISSING**"

            if not nt in neuron_nts:
                neuron_nts[nt] = 0

            neuron_nts[nt] += 1

        nts_info = ""
        for nt in sorted(neuron_nts.keys()):
            nts_info += "%s (%i)<br/>" % (shorten_neurotransmitter(nt), neuron_nts[nt])

        muscle_nts = {}
        for c in muscle_conns:
            nt = c.synclass
            if len(nt) == 0:
                nt = "**MISSING**"

            if not nt in muscle_nts:
                muscle_nts[nt] = 0

            muscle_nts[nt] += 1

        m_nts_info = ""
        for nt in sorted(muscle_nts):
            m_nts_info += "%s (%i)<br/>" % (
                shorten_neurotransmitter(nt),
                muscle_nts[nt],
            )

        ref = (
            "[%s](%s.md)" % (reader_name, reader_pages[reader_name])
            if reader_name in reader_pages
            else reader_name
        )

        all_data[ref] = [
            len(preferred),
            len(missing_preferred),
            len(not_in_preferred),
            len(muscles),
            len(neuron_conns),
            len(neurons2muscles),
            len(muscle_conns),
            nts_info,
            m_nts_info,
        ]

    print_("\nFinished loading all the data from the readers!")

    import pandas as pd
    import numpy as np

    df_all = pd.DataFrame(all_data).transpose()
    # df_all.set_index("Values")

    # h = HTML(df_all.to_html(escape=False, index=False))

    mk = df_all.to_markdown()

    filename = "docs/Comparison.md"
    with open(filename, "w") as f:
        f.write(mk)

    print_("Written page: %s" % filename)

    return connectomes


if __name__ == "__main__":
    quick = len(sys.argv) > 1 and eval(sys.argv[1])

    connectomes = generate_comparison_page(quick)

    print("Finished. All loaded connectomes:\n%s" % connectomes)
