from cect.Cells import ALL_PREFERRED_CELL_NAMES
from cect.Cells import GENERIC_CHEM_SYN
from cect.Cells import GENERIC_ELEC_SYN

from cect.Cells import get_cell_notes
from cect.Cells import get_cell_internal_link
from cect.Cells import get_cell_wormatlas_link
from cect.Cells import get_cell_osbv1_link
from cect.Cells import are_bilateral_pair
from cect.Cells import is_any_neuron
from cect.Cells import get_primary_classification
from cect.Cells import get_standard_color


from cect import print_
# from pprint import pprint

import pandas as pd
import csv

pd.options.plotting.backend = "plotly"


def get_dataset_link(dataset):
    """Helper method to generate an internal link to the page for a dataset

    Args:
        dataset (str): The dataset to link to

    Returns:
        str: A hyperlink to the dataset
    """
    # return dataset+'--'
    dataset_text = dataset.replace("Herm", " Herm").replace("Male", " Male")
    return f'<a href="../{dataset}_data">{dataset_text}</a>'


def get_weight_table_markdown(w):
    ww = {}
    tot_conns = 0

    for dataset in w:
        # print(dataset)
        # print(w[dataset].values())
        if (
            len(w[dataset]) > 0
            and sum(w[dataset].values()) > 0
            and "SSData" not in dataset
        ):
            ww[dataset] = w[dataset]
            tot_conns += sum(w[dataset].values())

    if tot_conns == 0:
        return "No connections found!"

    sort_by = (
        get_dataset_link("Cook2019Herm")
        if get_dataset_link("Cook2019Herm") in ww
        else get_dataset_link("White_whole")
        if get_dataset_link("White_whole") in ww
        else get_dataset_link("Randi2023")
        if get_dataset_link("Randi2023") in ww
        else get_dataset_link("RipollSanchezShortRange")
        if get_dataset_link("RipollSanchezShortRange") in ww
        else list(ww.keys())[0]
    )

    # print_("Sorting the following data by %s" % sort_by)
    # pprint(ww)

    indent = "    "

    df_all = pd.DataFrame(ww).fillna(0).sort_values(sort_by, ascending=False)

    if df_all is not None:
        fig = df_all.plot(
            labels=dict(index="Connection", value="Weight", variable="Dataset")
        )
        fig.update_traces(
            marker=dict(size=4), marker_symbol="circle", mode="lines+markers"
        )
        fig_md = f"\n{indent}```plotly\n{indent}{fig.to_json()}\n{indent}```\n"
    else:
        fig_md = ""

    return """
=== "Plot"
    %s
=== "Table"

    %s""" % (fig_md, df_all.to_markdown().replace("\n", "\n" + indent))


def load_individual_neuron_info():
    # Taken from https://wormatlas.org/neurons/Individual%20Neurons/Neuronframeset.html
    filename = "cect/data/IndividualNeurons.csv"
    cell_info = {}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        print(reader)

        for row in reader:
            print(", ".join(row))
            if not row[0].startswith("#"):
                cell_info[row[0]] = (row[1].strip(), row[2].strip(), row[3].strip())

    return cell_info


def _get_top_list(conns, num):
    conns_ord = {
        k: v for k, v in sorted(conns.items(), key=lambda item: item[1], reverse=True)
    }

    top = [
        "%s <b>%s</b>"
        % (
            get_cell_internal_link(
                k, html=True, use_color=True, individual_cell_page=True
            ),
            (
                int(conns_ord[k])
                if int(conns_ord[k]) == conns_ord[k]
                else "%.4g" % conns_ord[k]
            ),
        )
        for k in list(conns_ord.keys())[:num]
    ]

    return ", ".join(top)


def generate_cell_info_pages(connectomes):
    """Generates the individual cell pages

    Args:
        connectomes (list): The
    """
    cell_data = load_individual_neuron_info()
    cell_classification = get_primary_classification()

    all_cell_info = []

    for cell in ALL_PREFERRED_CELL_NAMES:
        print_("Generating individual cell page for: %s" % cell)

        cell_info = '---\ntitle: "Cell: %s"\n---\n\n' % cell

        # TODO: investigate  DX1, DX2, DX3, EF1, EF2, EF3
        if is_any_neuron(cell) and "DX" not in cell and "EF" not in cell:
            cell_ref = (
                cell
                if not (
                    (cell.startswith("CA") or cell.startswith("CP")) and cell[2] == "0"
                )
                else "%s%s" % (cell[:2], cell[-1])
            )  # CA04 -> CA4 etc.
            ackr = cell_data[cell_ref][0]
            from_ = 0
            for c in cell:
                # print('Replacing %s (from %s) in %s'%(c,from_,ackr))
                if c in ackr:
                    ii = ackr.index(c, from_)
                    ackr = "%s<b>%s</b>%s" % (ackr[:ii], ackr[ii], ackr[ii + 1 :])
                    from_ = ii + 1

            cell_info += '!!! question "**%s: %s**"\n\n' % (
                cell,
                cell_data[cell_ref][2],
            )
            cell_info += (
                '    <p class="subtext">%s&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' % (ackr)
            )
            cell_info += "Lineage: <b>%s</b></p>\n\n" % (cell_data[cell_ref][1])

            all_cell_info.append([cell, get_cell_notes(cell), cell_data[cell_ref][0], cell_data[cell_ref][1], cell_data[cell_ref][2]])

        else:
            cell_info += '!!! question "**%s: %s**"\n\n' % (cell, get_cell_notes(cell))
            all_cell_info.append([cell, get_cell_notes(cell), cell_data[cell_ref][0], '','',''])

        cell_info += (
            '    <p class="subtext"><a href="../Cook_2019">Cook 2019</a> classification: <b>%s</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
            % (get_cell_notes(cell))
        )
        cc = cell_classification[cell]
        color = get_standard_color(cell)[1:]


        cell_info += (
            'All cells of type: ![#%s](images/%s.png) <a href="../Cells/#%s"><b>%s</b></a></p>\n\n'
            % (
                color,
                color,
                cc.lower().replace(" ", "-").replace("(", "").replace(")", ""),
                cc[0].upper() + cc[1:],
            )
        )

        cell_info += "    %s " % (
            get_cell_wormatlas_link(cell, text="Info on WormAtlas", button=True)
        )

        cell_info += "%s\n\n" % get_cell_osbv1_link(
            cell, text="View in 3D on Open Source Brain", button=True
        )

        all_synclasses = [
            GENERIC_CHEM_SYN,
            GENERIC_ELEC_SYN,
        ]  # ensure these 2 are at the start...

        for cds_name in connectomes:
            cds = connectomes[cds_name]
            for synclass in cds.connections:
                if synclass not in all_synclasses:
                    all_synclasses.append(synclass)

        cell_link = get_cell_internal_link(
            cell, html=True, use_color=True, individual_cell_page=True
        )

        reference_cs = "Cook2019Herm"
        reference_gj = reference_cs
        reference_mono = "Bentley2016_MA"
        reference_pep = "RipollSanchezShortRange"
        reference_func = "Randi2023"
        max_conn_cells = 5
        conns_from_cs = "???"
        conns_to_cs = "???"
        conns_from_mono = "???"
        conns_to_mono = "???"
        conns_from_pep = "???"
        conns_to_pep = "???"
        conns_from_func = "???"
        conns_to_func = "???"
        conns_gj = "???"

        tables_md = ""

        for synclass in all_synclasses:
            synclass_info = synclass
            if synclass == GENERIC_CHEM_SYN:
                synclass_info = "Chemical synaptic"
            if synclass == GENERIC_ELEC_SYN:
                synclass_info = "Electrical synaptic"

            header = "### %s connections %s %s  { data-search-exclude }\n\n" % (
                synclass_info,
                "to" if not synclass == GENERIC_ELEC_SYN else "from/to",
                cell_link,
            )

            w = {}
            for cds_name in connectomes:
                r_name = get_dataset_link(cds_name)
                w[r_name] = {}
                cds = connectomes[cds_name]

                connection_symbol = "↔" if synclass == GENERIC_ELEC_SYN else "→"

                if synclass in cds.connections:
                    conns = cds.get_connections_to(cell, synclass)

                    if cds_name == reference_cs and synclass == GENERIC_CHEM_SYN:
                        conns_to_cs = _get_top_list(conns, max_conn_cells)
                    if cds_name == reference_gj and synclass == GENERIC_ELEC_SYN:
                        conns_gj = _get_top_list(conns, max_conn_cells)
                    if cds_name == reference_mono:
                        conns_to_mono = _get_top_list(conns, max_conn_cells)
                    if cds_name == reference_pep:
                        conns_to_pep = _get_top_list(conns, max_conn_cells)
                    if cds_name == reference_func:
                        conns_to_func = _get_top_list(conns, max_conn_cells)

                    for c in conns:
                        cc = get_cell_internal_link(
                            c, html=True, use_color=True, individual_cell_page=True
                        )
                        template = (
                            "<b><i>%s%s%s</i></b>"
                            if cell == c
                            else (
                                "<b>%s%s%s</b>"
                                if are_bilateral_pair(cell, c)
                                else "%s%s%s"
                            )
                        )
                        w[r_name][template % (cc, connection_symbol, cell_link)] = (
                            conns[c]
                        )

            w_md = get_weight_table_markdown(w)

            if "No connections" not in w_md:
                tables_md += "%s\n%s\n\n" % (header, w_md)

            if not synclass == GENERIC_ELEC_SYN:
                header = "### %s connections %s %s  { data-search-exclude }\n\n" % (
                    synclass_info,
                    "from",
                    cell_link,
                )

                w = {}
                for cds_name in connectomes:
                    r_name = get_dataset_link(cds_name)
                    w[r_name] = {}

                    cds = connectomes[cds_name]
                    if synclass in cds.connections:
                        conns = cds.get_connections_from(cell, synclass)

                        if cds_name == reference_cs and synclass == GENERIC_CHEM_SYN:
                            conns_from_cs = _get_top_list(conns, max_conn_cells)
                        if cds_name == reference_mono:
                            conns_from_mono = _get_top_list(conns, max_conn_cells)
                        if cds_name == reference_pep:
                            conns_from_pep = _get_top_list(conns, max_conn_cells)
                        if cds_name == reference_func:
                            conns_from_func = _get_top_list(conns, max_conn_cells)

                        for c in conns:
                            cc = get_cell_internal_link(
                                c, html=True, use_color=True, individual_cell_page=True
                            )
                            template = (
                                "<b><i>%s→%s</i></b>"
                                if cell == c
                                else (
                                    "<b>%s→%s</b>"
                                    if are_bilateral_pair(cell, c)
                                    else "%s→%s"
                                )
                            )
                            w[r_name][template % (cell_link, cc)] = conns[c]

                w_md = get_weight_table_markdown(w)

                if "No connections" not in w_md:
                    tables_md += "%s\n%s\n\n" % (header, w_md)

        cell_info += f"""

### Summary of connections

<p class="subtext">Top {max_conn_cells} connections of specified types to/from this cell (based on {get_dataset_link(reference_cs)}, {get_dataset_link(reference_mono)}, {get_dataset_link(reference_pep)} & {get_dataset_link(reference_func)})</p>

<table style="width:700px">
<tr>
    <td><b><a href="#chemical-synaptic-connections-to-{cell.lower()}">Chemical</a></b></td>
    <td style="width:40%">{conns_to_cs}</td>
    <td style="width:5%" align="middle">→</td>
    <td rowspan="4" style="vertical-align:middle;text-align:center;"><b>{cell_link}</b></td>
    <td style="width:5%" align="middle">→</td>
    <td style="width:40%">{conns_from_cs}</td>
</tr><tr>
    <td><b><a href="#monoaminergic-connections-to-{cell.lower()}">Monoaminergic</a></b></td><td>{conns_to_mono}</td><td align="middle">→</td><td align="middle">→</td><td>{conns_from_mono}</td>
</tr><tr>
    <td><b><a href="#peptidergic-connections-to-{cell.lower()}">Peptidergic</a></b></td>  <td>{conns_to_pep}</td><td align="middle">→</td><td align="middle">→</td><td>{conns_from_pep}</td>
</tr><tr>
    <td><b><a href="#functional-connections-to-{cell.lower()}">Functional</a></b></td>   <td>{conns_to_func}</td><td align="middle">→</td><td align="middle">→</td><td>{conns_from_func}</td>
</tr><tr>
    <td>&nbsp;</td> <td colspan="5" align="middle">↕</td> 
</tr><tr>
    <td><b><a href="#electrical-synaptic-connections-fromto-{cell.lower()}">Electrical</a></b></td> <td colspan="5" align="middle">{conns_gj}</td> 
</tr>
</table>

"""
        cell_info += tables_md

        cell_filename = "docs/%s.md" % cell
        with open(cell_filename, "w") as cell_file:
            print_(f"Writing info on cell {cell} to {cell_filename}")
            cell_file.write(cell_info)

    cell_info_filename = "cect/data/all_cell_info.csv"
    with open(cell_info_filename, "w") as csv_file:
        print_(f"Writing info on all cells to {cell_info_filename}")
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')
        for line in all_cell_info:
            csv_writer.writerow(line)


if __name__ == "__main__":
    from cect.White_whole import get_instance

    cds_white = get_instance()

    from cect.WitvlietDataReader8 import get_instance

    cds_w8 = get_instance()

    connectomes = {"White_whole": cds_white, "Witvliet8": cds_w8}

    """
    from cect.WormNeuroAtlasMAReader import get_instance
    connectomes['Bentley2016_MA'] = get_instance()

    from cect.WormNeuroAtlasFuncReader import get_instance
    connectomes['Randi2023'] = get_instance()

    from cect.RipollSanchezShortRangeReader import get_instance
    connectomes['RipollSanchezShortRange'] = get_instance() """

    # load_individual_neuron_info()
    generate_cell_info_pages(connectomes)
