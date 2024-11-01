from cect.Cells import ALL_PREFERRED_CELL_NAMES
from cect.Cells import GENERIC_CHEM_SYN
from cect.Cells import GENERIC_ELEC_SYN

from cect.Cells import get_cell_notes
from cect.Cells import get_cell_internal_link
from cect.Cells import get_cell_wormatlas_link
from cect.Cells import get_cell_osbv1_link

from cect import print_
# from pprint import pprint

import pandas as pd

pd.options.plotting.backend = "plotly"


def get_dataset_link(dataset):
    # return dataset+'--'
    return f'<a href="../{dataset}_data">{dataset}</a>'


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
        fig_md = f"\n{indent}<br/>\n{indent}```plotly\n{indent}{fig.to_json()}\n{indent}```\n"
    else:
        fig_md = ""

    return "%s\n\n%s" % (df_all.to_markdown(), fig_md)


def generate_cell_info_pages(connectomes):
    for cell in ALL_PREFERRED_CELL_NAMES:
        cell_info = '---\ntitle: "Cell: %s"\n---\n\n' % cell

        cell_info += "**%s**\n\n" % (get_cell_notes(cell))
        cell_info += "%s - " % (get_cell_wormatlas_link(cell, text="Info on WormAtlas"))

        cell_info += "%s\n\n" % get_cell_osbv1_link(
            cell, text="View in 3D on Open Source Brain"
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
                synclass_info = "Chemical synapse"
            if synclass == GENERIC_ELEC_SYN:
                synclass_info = "Electrical synapse"

            cell_link = get_cell_internal_link(
                cell, html=True, use_color=True, individual_cell_page=True
            )
            header = (
                "### Connections %s %s of type **%s**  { data-search-exclude }\n\n"
                % (
                    "from" if not synclass == GENERIC_ELEC_SYN else "from/to",
                    cell_link,
                    synclass_info,
                )
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
                        w[r_name]["%s%s%s" % (cell_link, connection_symbol, cc)] = (
                            conns[c]
                        )

            w_md = get_weight_table_markdown(w)

            if "No connections" not in w_md:
                cell_info += "%s\n%s\n\n" % (header, w_md)

            if not synclass == GENERIC_ELEC_SYN:
                cell_link = get_cell_internal_link(
                    cell, html=True, use_color=True, individual_cell_page=True
                )
                header = (
                    "### Connections %s %s of type **%s**  { data-search-exclude }\n\n"
                    % (
                        "to",
                        cell_link,
                        synclass_info,
                    )
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
                            w[r_name]["%s→%s" % (cc, cell_link)] = conns[c]

                w_md = get_weight_table_markdown(w)

                if "No connections" not in w_md:
                    cell_info += "%s\n%s\n\n" % (header, w_md)

        """
        for cds_name in connectomes:
            cds = connectomes[cds_name]

            for synclass in cds.connections:
                cell_info += "\n\n## %s (%s)\n" % (synclass, cds_name)

                cell_info += "### Connections %s %s of type %s\n\n" % (
                    "FROM" if not synclass == GENERIC_ELEC_SYN else "FROM/TO",
                    get_cell_internal_link(
                        cell, html=True, use_color=True, individual_cell_page=True
                    ),
                    synclass,
                )

                conns = cds.get_connections_from(cell, synclass, ordered_by_weight=True)
                for c in conns:
                    cell_info += "%s: **%s** - " % (
                        get_cell_internal_link(
                            c, html=True, use_color=True, individual_cell_page=True
                        ),
                        conns[c],
                    )

                if not synclass == GENERIC_ELEC_SYN:
                    cell_info += "\n### Connections TO %s of type %s\n\n" % (
                        get_cell_internal_link(
                            cell, html=True, use_color=True, individual_cell_page=True
                        ),
                        synclass,
                    )

                    conns = cds.get_connections_to(
                        cell, synclass, ordered_by_weight=True
                    )
                    for c in conns:
                        cell_info += "%s: **%s** - " % (
                            get_cell_internal_link(
                                c, html=True, use_color=True, individual_cell_page=True
                            ),
                            conns[c],
                        )"""

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

    generate_cell_info_pages(connectomes)
