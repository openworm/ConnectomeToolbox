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


from cect import print_
# from pprint import pprint

import pandas as pd
import csv

pd.options.plotting.backend = "plotly"


def get_dataset_link(dataset):
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

    df_all = pd.DataFrame(ww).fillna(0).sort_values(sort_by, ascending=False)

    if df_all is not None:
        fig = df_all.plot(
            labels=dict(index="Connection", value="Weight", variable="Dataset")
        )
        fig.update_traces(
            marker=dict(size=4), marker_symbol="circle", mode="lines+markers"
        )
        indent = ""
        fig_md = f"\n{indent}```plotly\n{indent}{fig.to_json()}\n{indent}```\n"
    else:
        fig_md = ""

    return "%s\n\n%s" % (df_all.to_markdown(), fig_md)


def load_individual_neuron_info():
    # From https://wormatlas.org/neurons/Individual%20Neurons/Neuronframeset.html
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


def generate_cell_info_pages(connectomes):
    cell_data = load_individual_neuron_info()
    cell_classification = get_primary_classification()

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

            cell_info += "**%s**\n\n" % (cell_data[cell_ref][2])
            cell_info += '<p class="subtext">%s&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' % (
                ackr
            )
            cell_info += "Lineage: <b>%s</b></p>\n\n" % (cell_data[cell_ref][1])
        else:
            cell_info += "**%s**\n\n" % (get_cell_notes(cell))

        cell_info += (
            '<p class="subtext"><a href="../Cook_2019">Cook 2019</a> classification: <b>%s</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
            % (get_cell_notes(cell))
        )
        cc = cell_classification[cell]
        cell_info += (
            'All cells of type: <a href="../Cells/#%s"><b>%s</b></a></p>\n\n'
            % (
                cc.replace(" ", "-").replace("(", "").replace(")", ""),
                cc[0].upper() + cc[1:],
            )
        )

        cell_info += "%s " % (
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

        for synclass in all_synclasses:
            synclass_info = synclass
            if synclass == GENERIC_CHEM_SYN:
                synclass_info = "Chemical synaptic"
            if synclass == GENERIC_ELEC_SYN:
                synclass_info = "Electrical synaptic"

            cell_link = get_cell_internal_link(
                cell, html=True, use_color=True, individual_cell_page=True
            )
            header = "### %s connections %s %s  { data-search-exclude }\n\n" % (
                synclass_info,
                "from" if not synclass == GENERIC_ELEC_SYN else "from/to",
                cell_link,
            )

            w = {}
            for cds_name in connectomes:
                r_name = get_dataset_link(cds_name)
                w[r_name] = {}
                cds = connectomes[cds_name]

                connection_symbol = "↔" if synclass == GENERIC_ELEC_SYN else "→"
                if synclass in cds.connections:
                    conns = cds.get_connections_from(cell, synclass)
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
                        w[r_name][template % (cell_link, connection_symbol, cc)] = (
                            conns[c]
                        )

            w_md = get_weight_table_markdown(w)

            if "No connections" not in w_md:
                cell_info += "%s\n%s\n\n" % (header, w_md)

            if not synclass == GENERIC_ELEC_SYN:
                cell_link = get_cell_internal_link(
                    cell, html=True, use_color=True, individual_cell_page=True
                )
                header = "### %s connections %s %s  { data-search-exclude }\n\n" % (
                    synclass_info,
                    "to",
                    cell_link,
                )

                w = {}
                for cds_name in connectomes:
                    r_name = get_dataset_link(cds_name)
                    w[r_name] = {}

                    cds = connectomes[cds_name]
                    if synclass in cds.connections:
                        conns = cds.get_connections_to(cell, synclass)
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
                            w[r_name][template % (cc, cell_link)] = conns[c]

                w_md = get_weight_table_markdown(w)

                if "No connections" not in w_md:
                    cell_info += "%s\n%s\n\n" % (header, w_md)

        cell_filename = "docs/%s.md" % cell
        with open(cell_filename, "w") as cell_file:
            print_(f"Writing info on cell {cell} to {cell_filename}")
            cell_file.write(cell_info)


if __name__ == "__main__":
    from cect.White_whole import get_instance

    cds_white = get_instance()

    from cect.WitvlietDataReader8 import get_instance

    cds_w8 = get_instance()

    connectomes = {"White_whole": cds_white, "Witvliet8": cds_w8}

    # load_individual_neuron_info()
    generate_cell_info_pages(connectomes)
