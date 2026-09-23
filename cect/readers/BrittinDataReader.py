# -*- coding: utf-8 -*-

############################################################

#    A script to read the values from Brittin et al 2021

############################################################


from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections

from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.Cells import is_one_of_bilateral_pair
from cect.Cells import get_contralateral_cell

from cect.Neurotransmitters import CONTACTOME_SYN_TYPE
from cect.Neurotransmitters import CONTACTOME_SYN_CLASS

from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

import os
from openpyxl import load_workbook

from cect import print_


spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/../data/"

filename = "%s41586_2021_3284_MOESM5_ESM.xlsx" % spreadsheet_location

NAME = "Brittin2021"

READER_DESCRIPTION = (
    """Data extracted from %s for membrane contact information."""
    % get_dataset_source_on_github(filename.split("/")[-1])
)

DATASET_DESCRIPTION = """Contactome information from Brittin et al. 2021. This dataset contains the contact area between pairs of cells in the _C. elegans_ nerve ring, as measured from volumetric reconstructions of the JSH and N2U animals, based on the previously published electron micrographs from White et al. 1986. The M<sup>4</sup> graph as described in the Brittin et al. 2021 paper is used here (i.e. limited to contacts that are conserved across the left and right sides of the JSH and N2U animals). 
"""

WEIGHTS = "Weights represent the contact area between pairs of cells"

pairs_added = []
repeated_pairs = []


def add_pair_of_contact_conns(conns, A, B, contact_area):
    syntype = CONTACTOME_SYN_TYPE
    synclass = CONTACTOME_SYN_CLASS

    if (A, B) not in pairs_added:
        ci = ConnectionInfo(A, B, contact_area, syntype, synclass)
        conns.append(ci)
        pairs_added.append((A, B))
    else:
        if (A, B) not in repeated_pairs:
            repeated_pairs.append((A, B))
    if (B, A) not in pairs_added:
        ci = ConnectionInfo(B, A, contact_area, syntype, synclass)
        conns.append(ci)
        pairs_added.append((B, A))
    else:
        if (B, A) not in repeated_pairs:
            repeated_pairs.append((B, A))


class BrittinDataReader(ConnectomeDataset):
    """Reader for datasets from [Brittin et al. 2021](../../Brittin_2021.md)"""

    verbose = False

    def __init__(self, reference_graph):
        ConnectomeDataset.__init__(self)
        self.reference_graph = reference_graph

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(
                conn,
                check_overwritten_connections=True,
                append_existing_connections=False,
                fail_on_any_repeated_connection=True,
            )

    def read_data(self):
        cells = []
        conns = []

        wb = load_workbook(filename)

        sheet = wb.get_sheet_by_name(self.reference_graph)

        bilaterals = []
        single_cells = []

        print_("Opened sheet %s in Excel file: %s" % (sheet, filename))
        # print(dir(sheet))

        DELTA_VALUE_4 = 4

        for row in sheet.rows:
            # print(row[0].value)
            if "cell_1" not in row[0].value:
                delta = int(row[3].value)
                if delta == DELTA_VALUE_4:
                    A = row[0].value
                    B = row[1].value
                    contact_area = float(row[2].value)

                    add_pair_of_contact_conns(conns, A, B, contact_area)

                    if A not in cells:
                        cells.append(A)
                    if B not in cells:
                        cells.append(B)

                    A_c = get_contralateral_cell(A)
                    B_c = get_contralateral_cell(B)

                    if not A_c == B:
                        add_pair_of_contact_conns(conns, A_c, B_c, contact_area)

                        if A_c not in cells:
                            cells.append(A_c)
                        if B_c not in cells:
                            cells.append(B_c)

        for cell in cells:
            if is_one_of_bilateral_pair(cell):
                bilaterals.append(cell)
            else:
                single_cells.append(cell)

        print_(
            "Finished processing %i cells, %i bilateral and %i single cells: %s"
            % (len(cells), len(bilaterals), len(single_cells), sorted(single_cells))
        )

        return cells, conns


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(
            get_cache_filename(__file__.split("/")[-1].split(".")[0])
        )
    else:
        return BrittinDataReader("M")


if __name__ == "__main__":
    wdr = get_instance()

    cells, neuron_conns = wdr._read_data()
    neurons2muscles, muscles, muscle_conns = wdr._read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print(len(wdr.original_connection_infos))
    print(len(wdr.get_current_connection_info_list()))

    print("Pairs added: %s" % len(pairs_added))
    print("Repeated pairs: %s" % len(repeated_pairs))
    print("Total pairs: %s" % (len(pairs_added) + len(repeated_pairs)))
