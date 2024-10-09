from cect.ConnectomeReader import check_cells
from cect.Cells import get_cell_internal_link
from cect import print_
import json

import sys
import numpy as np

import importlib

all_data = {}


reader_pages = {
    "Test": "Test_data",
    "Varshney": "Varshney_data",
    "White_A": "White_A_data",
    "White_L4": "White_L4_data",
    "White_whole": "White_whole_data",
    "Witvliet1": "Witvliet1_data",
    "Witvliet2": "Witvliet2_data",
    "Witvliet3": "Witvliet3_data",
    "Witvliet4": "Witvliet4_data",
    "Witvliet5": "Witvliet5_data",
    "Witvliet6": "Witvliet6_data",
    "Witvliet7": "Witvliet7_data",
    "Witvliet8": "Witvliet8_data",
    "WormNeuroAtlas": "WormNeuroAtlas_data",
    "Cook2019Herm": "Cook2019Herm_data",
    "Cook2019Male": "Cook2019Male_data",
    "Cook2020": "Cook2020_data",
    "Randi2023": "Randi2023_data",
    "SSData": "SSData_data",
    "UpdSSData": "UpdSSData_data",
    "UpdSSData2": "UpdSSData2_data",
    "Bentley2016_MA": "Bentley2016_MA_data",
    "Bentley2016_PEP": "Bentley2016_PEP_data",
}

all_data[""] = [
    "Num<br/>neurons",
    "Missing<br/>neurons",
    "Non<br/>neurons",
    "Num<br/>muscles",
    "Num N->N<br/>conns",
    "Num N<br/>with ->M",
    "Num N->M<br/>conns",
    "N->N<br/>neurotrans.",
    "N->M<br/>neurotrans.",
]


def shorten_neurotransmitter(nt):
    return (
        nt.replace("Acetylcholine", "ACh")
        .replace("Serotonin", "5HT")
        .replace("Glutamate", "Glu.")
        .replace("Tyramine", "Tyr.")
        .replace("FMRFamide", "FMRFam.")
        .replace("Generic_", "Gen_")
        .replace("Octapamine", "Octapa.")
        .replace("Dopamine", "Dopa.")
    )


def _format_json(json_str):
    return json.dumps(json.loads(json_str), sort_keys=True, indent=2)


def get_2d_graph_markdown(reader_name, view, connectome, synclass, indent="    "):
    view_id = view.id

    if np.sum(connectome.connections[synclass]) == 0:
        return None

    fig = connectome.to_plotly_graph_fig(synclass, view)

    asset_filename = "assets/%s_%s_%s_graph.json" % (
        reader_name,
        view_id.replace(" ", "_"),
        synclass.replace(" ", "_"),
    )

    with open("./docs/%s" % asset_filename, "w") as asset_file:
        asset_file.write(_format_json(fig.to_json()))

    fig.write_image("./docs/%s" % asset_filename.replace(".json", ".png"))

    return '\n%s```plotly\n%s{ "file_path": "./%s" }\n%s```\n' % (
        indent,
        indent,
        asset_filename,
        indent,
    )


def get_matrix_markdown(reader_name, view, connectome, synclass, indent="    "):
    view_id = view.id

    if np.sum(connectome.connections[synclass]) == 0:
        return None

    fig = connectome.to_plotly_matrix_fig(synclass, view)

    asset_filename = "assets/%s_%s_%s.json" % (
        reader_name,
        view_id.replace(" ", "_"),
        synclass.replace(" ", "_"),
    )

    with open("./docs/%s" % asset_filename, "w") as asset_file:
        asset_file.write(_format_json(fig.to_json()))

    fig.write_image("./docs/%s" % asset_filename.replace(".json", ".png"))

    return '\n%s```plotly\n%s{ "file_path": "./%s" }\n%s```\n' % (
        indent,
        indent,
        asset_filename,
        indent,
    )


def get_hive_plot_markdown(reader_name, view, connectome, synclass, indent="    "):
    view_id = view.id

    if np.sum(connectome.connections[synclass]) == 0:
        return None

    fig = connectome.to_plotly_hive_plot_fig(synclass, view)

    if fig is None:
        return "No plottable connections of this type..."

    asset_filename = "assets/%s_%s_%s_hiveplot.json" % (
        reader_name,
        view_id.replace(" ", "_"),
        synclass.replace(" ", "_"),
    )

    with open("./docs/%s" % asset_filename, "w") as asset_file:
        asset_file.write(_format_json(fig.to_json()))

    fig.write_image("./docs/%s" % asset_filename.replace(".json", ".png"))

    return '\n%s```plotly\n%s{ "file_path": "./%s" }\n%s```\n' % (
        indent,
        indent,
        asset_filename,
        indent,
    )


def generate_comparison_page(quick: bool, color_table=True):
    connectomes = {}
    all_connectomes = {}

    readers = {}

    if not quick:
        readers["SSData"] = ["cect.SpreadsheetDataReader", None]
        readers["UpdSSData"] = ["cect.UpdatedSpreadsheetDataReader", None]
        readers["UpdSSData2"] = ["cect.UpdatedSpreadsheetDataReader2", None]

    readers["Varshney"] = ["cect.VarshneyDataReader", "Varshney_2011"]
    readers["White_whole"] = ["cect.White_whole", "White_1986"]
    readers["Test"] = ["cect.TestDataReader", None]
    readers["Cook2020"] = ["cect.Cook2020DataReader", "Cook_2020"]
    readers["Witvliet1"] = ["cect.WitvlietDataReader1", "Witvliet_2021"]

    if not quick:
        readers["Bentley2016_MA"] = ["cect.WormNeuroAtlasMAReader", "Bentley_2016"]
        readers["Bentley2016_PEP"] = ["cect.WormNeuroAtlasPepReader", "Bentley_2016"]
        readers["Witvliet2"] = ["cect.WitvlietDataReader2", "Witvliet_2021"]
        readers["Witvliet3"] = ["cect.WitvlietDataReader3", "Witvliet_2021"]
        readers["Witvliet4"] = ["cect.WitvlietDataReader4", "Witvliet_2021"]
        readers["Witvliet5"] = ["cect.WitvlietDataReader5", "Witvliet_2021"]
        readers["Witvliet6"] = ["cect.WitvlietDataReader6", "Witvliet_2021"]
        readers["Witvliet7"] = ["cect.WitvlietDataReader7", "Witvliet_2021"]
        readers["Witvliet8"] = ["cect.WitvlietDataReader8", "Witvliet_2021"]
        readers["White_A"] = ["cect.White_A", "White_1986"]
        readers["White_L4"] = ["cect.White_L4", "White_1986"]
        readers["Cook2019Herm"] = ["cect.Cook2019HermReader", "Cook_2019"]
        readers["Cook2019Male"] = ["cect.Cook2019MaleReader", "Cook_2019"]
        readers["WormNeuroAtlas"] = ["cect.WormNeuroAtlasReader", "Randi_2023"]
        readers["Randi2023"] = ["cect.WormNeuroAtlasFuncReader", "Randi_2023"]

    main_mk = "# Comparison between data readers\n"
    table = ""

    for reader_name, reader_info in readers.items():
        reader = reader_info[0]

        decription_page = reader_info[1] if len(reader_info) > 1 else None

        print_(
            "\n****** Importing dataset %s using %s ******\n" % (reader_name, reader)
        )

        reader_module = importlib.import_module(reader)

        try:
            connectome = reader_module.get_instance()
            all_connectomes[reader_name] = connectome
            preferred, not_in_preferred, missing_preferred, muscles = check_cells(
                connectome.nodes
            )
            print_("Adding full connectome info: %s" % connectome)

        except Exception as e:
            print_("NOT adding full connectome info (%s)" % e)
            connectome = None

        if reader_name in reader_pages:
            connectomes[reader_name] = connectome

            if connectome is not None:
                from cect.ConnectomeView import ALL_VIEWS

                indent = "    "

                for view in ALL_VIEWS:
                    print_("Generating view: %s (%s)" % (view.name, view.id))

                    view_prefix = "" if view.id == "Raw" else "%s_" % view.id

                    matrix_filename = "docs/%s%s.md" % (
                        view_prefix,
                        reader_pages[reader_name],
                    )
                    graph_filename = "docs/%s%s_graph.md" % (
                        view_prefix,
                        reader_pages[reader_name],
                    )
                    hiveplot_filename = "docs/%s%s_hiveplot.md" % (
                        view_prefix,
                        reader_pages[reader_name],
                    )

                    for filename in [
                        graph_filename,
                        matrix_filename,
                        hiveplot_filename,
                    ]:
                        with open(filename, "w") as f:
                            graph = "graph" in filename
                            hiveplot = "hiveplot" in filename
                            matrix = not graph and not hiveplot

                            f.write("---\ntitle: %s\n---\n\n" % reader_name)

                            f.write("## Dataset: %s\n" % reader_name)

                            f.write("%s\n\n" % reader_module.READER_DESCRIPTION)

                            if decription_page is not None:
                                f.write(
                                    "[Source publication of dataset](%s.md)\n\n"
                                    % decription_page
                                )

                            for viewb in ALL_VIEWS:
                                viewb_prefix = (
                                    "" if viewb.id == "Raw" else "%s_" % viewb.id
                                )

                                f.write(
                                    "[%s](%s%s%s.md){ .md-button %s } "
                                    % (
                                        viewb.name,
                                        viewb_prefix,
                                        reader_pages[reader_name],
                                        "_graph"
                                        if graph
                                        else ("_hiveplot" if hiveplot else ""),
                                        ".md-button--primary"
                                        if view.id == viewb.id
                                        else "",
                                    )
                                )
                            f.write("\n\n**%s**" % view.description)
                            f.write("\n\n")

                            f.write(
                                "[Graph :material-graphql:](%s%s_graph.md){ .md-button %s } "
                                % (
                                    view_prefix,
                                    reader_pages[reader_name],
                                    ".md-button--primary" if graph else "",
                                )
                            )
                            f.write(
                                "[Matrix :material-checkerboard:](%s%s.md){ .md-button %s } "
                                % (
                                    view_prefix,
                                    reader_pages[reader_name],
                                    ".md-button--primary" if matrix else "",
                                )
                            )
                            f.write(
                                "[Hive plot :material-star-three-points-outline:](%s%s_hiveplot.md){ .md-button %s }\n\n"
                                % (
                                    view_prefix,
                                    reader_pages[reader_name],
                                    ".md-button--primary" if hiveplot else "",
                                )
                            )

                            cv = connectome.get_connectome_view(view)

                            # f.write('=== "%s"\n' % view.name)

                            no_conns = True

                            for sc in view.synclass_sets:
                                if matrix:
                                    mkdown_fig = get_matrix_markdown(
                                        reader_name,
                                        view,
                                        cv,
                                        sc,
                                        indent=indent,
                                    )

                                elif graph:
                                    mkdown_fig = get_2d_graph_markdown(
                                        reader_name,
                                        view,
                                        cv,
                                        sc,
                                        indent=indent,
                                    )

                                elif hiveplot:
                                    mkdown_fig = get_hive_plot_markdown(
                                        reader_name,
                                        view,
                                        cv,
                                        sc,
                                        indent=indent,
                                    )

                                if mkdown_fig is not None:
                                    no_conns = False
                                    f.write('=== "%s"\n%s\n' % (sc, mkdown_fig))

                            if no_conns:
                                f.write("No connections present in this view\n")

                            cell_types = {
                                "Neurons": preferred,
                                "Missing neurons": missing_preferred,
                                "Muscles": muscles,
                                "Other cells": not_in_preferred,
                            }

                            for t in cell_types:
                                f.write("\n### %s (%i)\n" % (t, len(cell_types[t])))
                                if len(cell_types[t]) > 0:
                                    f.write(
                                        "<details><summary>Full list of %s</summary>\n"
                                        % t
                                    )
                                    ss = sorted(cell_types[t])
                                    for n in ss:
                                        f.write(
                                            "%s" % (get_cell_internal_link(n, True))
                                        )
                                        if n is not ss[-1]:
                                            f.write(" | ")

                                    f.write("\n</details>\n")

                        print_("Written page: %s" % filename)

        neurons, neuron_conns = connectome.get_neuron_to_neuron_conns()
        neurons2muscles, muscles, muscle_conns = connectome.get_neuron_to_muscle_conns()

        neuron_nts = {}

        print_(
            "\n\n  = Adding table entry for: %s with %i neurons"
            % (connectome, len(neurons))
        )

        for c in neuron_conns:
            nt = c.synclass
            if len(nt) == 0:
                nt = "**MISSING**"

            if nt not in neuron_nts:
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

            if nt not in muscle_nts:
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

    df_all = pd.DataFrame(all_data).transpose()
    pd.set_option("max_colwidth", 30)
    # df_all.set_index("Values")

    # h = HTML(df_all.to_html(escape=False, index=False))

    from cect.Cells import COOK_GROUPING_1

    if color_table:
        STYLE = '"width:80px"'
        table += f"<table>\n  <tr>\n    <th style={STYLE}>Group</th>\n"

        readers_to_include = []

        for reader_name, reader_info in readers.items():
            if "Test" not in reader_name and "SSData" not in reader_name:
                readers_to_include.append(reader_name)

        for reader_name in readers_to_include:
            table += f"    <th style={STYLE}>{reader_name}</th>\n"

        for group in COOK_GROUPING_1:
            table += f"  <tr>\n<td >{group}</th>\n"

            for reader_name in readers_to_include:
                connectome = all_connectomes[reader_name]
                cells_here = ""
                for cell in sorted(COOK_GROUPING_1[group]):
                    if cell in connectome.nodes:
                        cells_here += "%s&nbsp;" % get_cell_internal_link(
                            cell_name=cell, text="\u2b2e", html=True, use_color=True
                        )
                    else:
                        pass  # cells_here+='<s>%s</s>&nbsp;'%cell

                    if (cells_here.split("<br/>")[-1]).count("&nbsp;") > 5:
                        cells_here += "<br/>\n"

                table += f"    <td >{cells_here}</th>\n"

            table += "  </tr>\n"

        table += "  </tr>\n</table>\n"

        main_mk += table

    main_mk += df_all.to_markdown()

    filename = "docs/Comparison.md"
    with open(filename, "w") as f:
        f.write(main_mk)

    print_("Written page: %s" % filename)

    return connectomes


if __name__ == "__main__":
    quick = len(sys.argv) > 1 and eval(sys.argv[1])

    connectomes = generate_comparison_page(quick, color_table=True)

    print("Finished. All loaded connectomes:\n%s" % connectomes)
