import cect

from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeReader import check_neurons
from cect import print_

import sys
import numpy as np

all_data = {}

quick = len(sys.argv) > 1 and eval(sys.argv[1])

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
    "Cook2020":"Cook2020_data",
    "": "_data",
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

if quick:
    readers = {
        "SSData": "cect.SpreadsheetDataReader",
        "UpdSSData": "cect.UpdatedSpreadsheetDataReader",
        "UpdSSData2": "cect.UpdatedSpreadsheetDataReader2",
        "Varshney": "cect.VarshneyDataReader",
        "White_L4": "cect.White_L4",
        "White_whole": "cect.White_whole",
        "Cook2020":"cect.Cook2020DataReader",
        "TestData": "cect.TestDataReader",
    }
else:
    readers = {
        "SSData": "cect.SpreadsheetDataReader",
        "UpdSSData": "cect.UpdatedSpreadsheetDataReader",
        "UpdSSData2": "cect.UpdatedSpreadsheetDataReader2",
        "White_A": "cect.White_A",
        "White_L4": "cect.White_L4",
        "White_whole": "cect.White_whole",
        "Varshney": "cect.VarshneyDataReader",
        "Witvliet1": "cect.WitvlietDataReader1",
        "Witvliet2": "cect.WitvlietDataReader2",
        "WormNeuroAtlas": "cect.WormNeuroAtlasReader",
        "Cook2019Herm": "cect.Cook2019HermReader",
        "Cook2020":"cect.Cook2020DataReader",
        "TestData": "cect.TestDataReader",
    }


def shorten_neurotransmitter(nt):
    return (
        nt.replace("Acetylcholine", "ACh")
        .replace("Serotonin", "5HT")
        .replace("Glutamate", "Glu")
        .replace("Tyramine", "Tyr")
        .replace("FMRFamide", "FMRFam")
        .replace("Generic_", "Gen_")
    )


# TODO: move elsewhere and make more generic
def get_cell_link(cell_name, html=False):
    url = None

    known_indiv = ["SABD", "MI"]

    if cell_name in known_indiv:
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name
        )
    elif cell_name[-2:].isnumeric():
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-2]
        )
    elif cell_name[-1].isdigit():
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-1]
        )
    elif (
        cell_name.endswith("L")
        or cell_name.endswith("R")
        or cell_name.endswith("EV")
        or cell_name.endswith("ED")
        or cell_name.endswith("BD")
    ):
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name[:-1]
        )
    elif len(cell_name) == 3:
        url = (
            "https://www.wormatlas.org/neurons/Individual Neurons/%sframeset.html"
            % cell_name
        )

    if url is not None:
        if html:
            return '<a href="%s">%s</a>' % (url, cell_name)
        else:
            return "[%s](%s)" % (cell_name, url)
    else:
        return cell_name


def get_2d_graph_markdown(reader_name, view_name, connectome, synclass, indent="    "):

    fig = connectome.to_plotly_graph_fig(synclass)

    asset_filename = "assets/%s_%s_%s_graph.json" % (
        reader_name,
        view_name,
        synclass.replace(" ", "_"),
    )

    with open("./docs/%s" % asset_filename, "w") as asset_file:
        asset_file.write(fig.to_json())

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
        asset_file.write(fig.to_json())

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


for reader_name, reader in readers.items():
    print_("\n****** Importing dataset %s using %s ******" % (reader_name, reader))

    exec("from %s import read_data, read_muscle_data, READER_DESCRIPTION" % reader)
    cells, neuron_conns = read_data(include_nonconnected_cells=True)

    preferred, not_in_preferred, missing_preferred = check_neurons(cells)

    neuron_nts = {}

    connectome = None
    try:
        exec("from %s import get_instance" % reader)
        connectome = get_instance()
        print_("Adding full connectome info")
    except:
        print_("NOT adding full connectome info")
        connectome = None

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

    neurons2muscles, muscles, muscle_conns = read_muscle_data()

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
        m_nts_info += "%s (%i)<br/>" % (shorten_neurotransmitter(nt), muscle_nts[nt])

    ref = (
        "[%s](%s.md)" % (reader_name, reader_pages[reader_name])
        if reader_name in reader_pages
        else reader_name
    )

    if reader_name in reader_pages:

        matrix_filename = "docs/%s.md" % reader_pages[reader_name]
        graph_filename = "docs/%s_graph.md" % reader_pages[reader_name]

        for filename in [matrix_filename, graph_filename]:
                
            with open(filename, "w") as f:

                matrix = filename==matrix_filename

                f.write("## %s\n" % reader_name)
                f.write("%s\n\n" % READER_DESCRIPTION)

                f.write("[View as matrix](../%s/index.html){ .md-button } [View as graph](../%s_graph/index.html){ .md-button }\n\n" % (reader_pages[reader_name], reader_pages[reader_name]))

                if connectome is not None:
                    from ConnectomeView import ALL_VIEWS

                    indent = "    "

                    for view in ALL_VIEWS:
                        cv = connectome.get_connectome_view(view)

                        f.write('=== "%s"\n' % view.name)

                        for sc in view.synclass_sets:
                            f.write(indent + '=== "%s"\n' % sc)

                            if matrix:
                                f.write(
                                    get_matrix_markdown(
                                        reader_name, view.name, cv, sc, indent=indent + indent
                                    )
                                )
                                
                            else:

                                f.write(
                                    get_2d_graph_markdown(
                                        reader_name, view.name, cv, sc, indent=indent + indent
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
                            f.write("%s" % (get_cell_link(n, True)))
                            if n is not ss[-1]:
                                f.write(" | ")

                        f.write("\n</details>\n")

            print_("Written page: %s" % filename)

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
