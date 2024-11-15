# -*- coding: utf-8 -*-

############################################################

#    A script to read the values from Brittin et al 2021

############################################################


from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections

from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github

import os
from openpyxl import load_workbook

from cect import print_


spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"

filename = "%s41586_2021_3284_MOESM5_ESM.xlsx" % spreadsheet_location

READER_DESCRIPTION = (
    """Data extracted from %s for membrane contact information."""
    % get_dataset_source_on_github(filename.split("/")[-1])
)


class BrittinDataReader(ConnectomeDataset):
    """Reader for datasets from [Brittin et al. 2021](../../Brittin_2021.md)"""

    verbose = False

    def __init__(self, reference_graph):
        ConnectomeDataset.__init__(self)
        self.reference_graph = reference_graph

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(conn)

    def read_data(self):
        cells = []
        conns = []

        wb = load_workbook(filename)

        sheet = wb.get_sheet_by_name(self.reference_graph)

        print_("Opened sheet %s in Excel file: %s" % (sheet, filename))
        print(dir(sheet))

        for row in sheet.rows:
            print(row[0].value)
            if "cell_1" not in row[0].value:
                delta = int(row[3].value)
                if delta == 4:
                    pre = row[0].value
                    post = row[1].value
                    num = float(row[2].value)
                    syntype = "Contact"
                    synclass = "%s%s" % (self.reference_graph, row[3].value)
                    synclass = "Contact"
                    ci = ConnectionInfo(pre, post, num, syntype, synclass)
                    print("Adding  %s" % ci)
                    conns.append(ci)

                    if pre not in cells:
                        cells.append(pre)
                    if post not in cells:
                        cells.append(post)

        return cells, conns


def get_instance():
    return BrittinDataReader("M")


my_instance = get_instance()

if __name__ == "__main__":
    wdr = get_instance()

    cells, neuron_conns = wdr.read_data()
    neurons2muscles, muscles, muscle_conns = wdr.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)
