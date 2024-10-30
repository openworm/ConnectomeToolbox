from cect.Cells import ALL_PREFERRED_CELL_NAMES
from cect.Cells import GENERIC_ELEC_SYN

from cect.Cells import get_cell_notes
from cect.Cells import get_cell_internal_link
from cect.Cells import get_cell_wormatlas_link
from cect.Cells import get_cell_osbv1_link

from cect import print_

import pandas as pd


def get_weight_table_markdown(w):
    sort_by = "White_whole"
    ww = {}
    tot_conns = 0
    for reader in w:
        # print(reader)
        # print(w[reader].values())
        if reader == sort_by or (len(w[reader]) > 0 and sum(w[reader].values()) > 0):
            ww[reader] = w[reader]
            tot_conns += sum(w[reader].values())
    print(ww)

    if tot_conns == 0:
        return "No connections found!"

    df_all = pd.DataFrame(ww).fillna(0).sort_values(sort_by, ascending=False)

    return df_all.to_markdown()


def generate_cell_info_pages(connectomes):
    for cell in ALL_PREFERRED_CELL_NAMES:
        cell_info = '---\ntitle: "Cell: %s"\n---\n\n' % cell

        cell_info += "**%s**\n\n" % (get_cell_notes(cell))
        cell_info += "%s - " % (get_cell_wormatlas_link(cell, text="Info on WormAtlas"))

        cell_info += "%s\n\n" % get_cell_osbv1_link(
            cell, text="View in 3D on Open Source Brain"
        )
        all_synclasses = []

        for cds_name in connectomes:
            cds = connectomes[cds_name]
            for synclass in cds.connections:
                if synclass not in all_synclasses:
                    all_synclasses.append(synclass)

        for synclass in all_synclasses:
            cell_info += "### Connections %s %s of type **%s**\n\n" % (
                "FROM" if not synclass == GENERIC_ELEC_SYN else "FROM/TO",
                get_cell_internal_link(
                    cell, html=True, use_color=True, individual_cell_page=True
                ),
                synclass,
            )

            w = {}
            for cds_name in connectomes:
                w[cds_name] = {}
                cds = connectomes[cds_name]
                if synclass in cds.connections:
                    conns = cds.get_connections_from(cell, synclass)
                    for c in conns:
                        cc = get_cell_internal_link(
                            c, html=True, use_color=True, individual_cell_page=True
                        )
                        w[cds_name][cc] = conns[c]

            cell_info += "%s\n\n" % get_weight_table_markdown(w)

            if not synclass == GENERIC_ELEC_SYN:
                cell_info += "### Connections %s %s of type **%s**\n\n" % (
                    "TO",
                    get_cell_internal_link(
                        cell, html=True, use_color=True, individual_cell_page=True
                    ),
                    synclass,
                )

                w = {}
                for cds_name in connectomes:
                    w[cds_name] = {}
                    cds = connectomes[cds_name]
                    if synclass in cds.connections:
                        conns = cds.get_connections_to(cell, synclass)
                        for c in conns:
                            cc = get_cell_internal_link(
                                c, html=True, use_color=True, individual_cell_page=True
                            )
                            w[cds_name][cc] = conns[c]

                cell_info += "%s\n\n" % get_weight_table_markdown(w)

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

        cell_filename = "docs/cells/%s.md" % cell
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
