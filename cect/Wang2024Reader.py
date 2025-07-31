# -*- coding: utf-8 -*-

############################################################

#    A script to read the neurotransmitter atlas values from Wang et al. 2024.

############################################################


from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT
from cect.Cells import is_any_neuron
from cect.ConnectomeDataset import load_connectome_dataset_file
from cect.ConnectomeDataset import get_cache_filename
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect import print_

from cect.Cells import ACETYLCHOLINE
from cect.Cells import DOPAMINE
from cect.Cells import GABA
from cect.Cells import GLUTAMATE
from cect.Cells import OCTAPAMINE
from cect.Cells import SEROTONIN
from cect.Cells import TYRAMINE
from cect.Cells import BETAINE
from cect.Cells import ALL_KNOWN_CHEMICAL_NEUROTRANSMITTERS
from cect.Cells import GENERIC_CHEM_SYN

from openpyxl import load_workbook

import os

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
filename = "%selife-95402-supp2-v1.xlsx" % spreadsheet_location


BASIS_ANATOMICAL_CONN = "White_whole"
# BASIS_ANATOMICAL_CONN = "TestDataReader"
# BASIS_ANATOMICAL_CONN = "Cook2019HermReader"

READER_DESCRIPTION = (
    """A reader combining neurotransmitter atlas values from Wang et al. 2024 (source: %s) with basic anatomical connectivity information from %s"""
    % (get_dataset_source_on_github(filename.split("/")[-1]), BASIS_ANATOMICAL_CONN)
)


class Wang2024Reader(ConnectomeDataset):
    """
    Reader of data from multiple connectomes...
    """

    verbose = False

    def map_cell_name(self, cell_name: str) -> str:
        if cell_name == "DB1/3":
            return "DB1"
        elif cell_name == "DB3/1":
            return "DB3"
        else:
            return cell_name

    def map_neurotransmitter(
        self, neurotransmitter: str, cat_1_present: bool, snf_3_present: bool
    ) -> str:
        """
        Maps neurotransmitter names to a standard format.
        """
        if neurotransmitter is None:
            return None
        neurotransmitter = neurotransmitter.strip()
        if neurotransmitter == "ACh" or neurotransmitter == "ACh - NEW":
            return ACETYLCHOLINE
        elif neurotransmitter == "DA":
            return DOPAMINE
        elif neurotransmitter == "GABA":
            return GABA
        elif neurotransmitter == "Glu" or neurotransmitter == "Glu - NEW":
            return GLUTAMATE
        elif neurotransmitter == "octopamine":
            return OCTAPAMINE
        elif neurotransmitter == "tyramine (synthesis + uptake) - NEW":
            return TYRAMINE
        elif (
            neurotransmitter == "betaine (uptake) - NEW"
            or neurotransmitter == "*betaine (uptake) - NEW"
        ):
            if cat_1_present and snf_3_present:
                return BETAINE
            else:
                print_(
                    "  Note: Betaine neurotransmitter found without cat_1 or snf_3 present, returning None."
                )
                return None
        elif (
            neurotransmitter == "5-HT"
            or neurotransmitter == "5-HT (synthesis + uptake)"
        ):
            return SEROTONIN
        else:
            return "NT_not_yet_supported"  # neurotransmitter

    def __init__(self):
        ConnectomeDataset.__init__(self)

        wb = load_workbook(filename)
        print_("Opened the Excel file: " + filename)
        neurotransmitters = {}

        sheet = wb.get_sheet_by_name("Supp File 2")
        for i in range(5, 307):
            cell = self.map_cell_name(sheet.cell(row=i, column=3).value)

            cat_1_present = str(sheet.cell(row=i, column=9).fill.patternType) == "solid"
            snf_3_present = "NEW" in str(sheet.cell(row=i, column=16).value)

            nt_1 = self.map_neurotransmitter(
                sheet.cell(row=i, column=21).value, cat_1_present, snf_3_present
            )
            nt_2 = self.map_neurotransmitter(
                sheet.cell(row=i, column=22).value, cat_1_present, snf_3_present
            )
            nt_3 = self.map_neurotransmitter(
                sheet.cell(row=i, column=23).value, cat_1_present, snf_3_present
            )

            print_(
                f"Reading row {i}: {cell}, NTs: {nt_1}, {nt_2}, {nt_3}; cat_1_present: {cat_1_present}, snf_3_present: {snf_3_present}"
            )

            nts = [nt_1]
            if nt_2 is not None:
                nts.append(nt_2)
            if nt_3 is not None:
                nts.append(nt_3)
            print_("  - Cell: %s, nts: %s" % (cell, nts))
            neurotransmitters[cell] = nts

        self.anatomical_conn_reader = load_connectome_dataset_file(
            get_cache_filename(BASIS_ANATOMICAL_CONN)
        )

        # neurons, muscles, other_cells, conns = self.read_all_data()

        conns = self.anatomical_conn_reader.get_current_connection_info_list()

        print_("Adding %i conns from %s" % (len(conns), BASIS_ANATOMICAL_CONN))
        for conn in conns[:]:
            print_("Original conn: %s" % conn)

            if is_any_neuron(conn.pre_cell):
                if conn.synclass in ALL_KNOWN_CHEMICAL_NEUROTRANSMITTERS + [
                    GENERIC_CHEM_SYN
                ]:
                    conn.number = 1.0
                    for nt in neurotransmitters[conn.pre_cell]:
                        conn.synclass = nt
                        print_("    Adding new conn: %s" % conn)
                        self.add_connection_info(conn)
                else:
                    print_(
                        "     Not a known chemical neurotransmitter: %s" % conn.synclass
                    )
            else:
                print_("     Not a neuron: %s" % conn.pre_cell)

    def read_data(self):
        return self._read_data()

    def read_muscle_data(self):
        return self._read_muscle_data()


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    return Wang2024Reader()


def main():
    tdr_instance = Wang2024Reader()

    print(tdr_instance.summary(list_pre_cells=True))
    quit()

    cells, neuron_conns = tdr_instance.read_data()

    neurons2muscles, muscles, muscle_conns = tdr_instance.read_muscle_data()

    analyse_connections(
        cells,
        neuron_conns,
        neurons2muscles,
        muscles,
        muscle_conns,
        print_details_on=["ADFL"],
    )

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    """
    
    from cect.ConnectomeView import COOK_FIG3_VIEW as 
    from cect.ConnectomeView import LOCOMOTION_3_VIEW as view
    from cect.ConnectomeView import LOCOMOTION_1_VIEW as view
    """
    # from cect.ConnectomeView import SOCIAL_VIEW as view
    # from cect.ConnectomeView import LOCOMOTION_2_VIEW as view
    from cect.ConnectomeView import RAW_VIEW as view
    # from cect.ConnectomeView import NEURONS_VIEW as view

    cds2 = tdr_instance.get_connectome_view(view)

    print(cds2.summary(list_pre_cells=True))

    # fig = cds2.to_plotly_hive_plot_fig(list(view.synclass_sets.keys())[0], view)

    """
    fig = cds2.to_plotly_graph_fig(list(view.synclass_sets.keys())[0], view)
    """

    fig, _ = cds2.to_plotly_matrix_fig(
        list(view.synclass_sets.keys())[0],
        view,
    )
    import plotly.io as pio

    pio.renderers.default = "browser"
    import sys

    if "-nogui" not in sys.argv:
        fig.show()


if __name__ == "__main__":
    main()
