# -*- coding: utf-8 -*-

############################################################

#    A simple script to read the values in CElegansNeuronTables.xls.

#    This is one of a number of interchangeable "Readers" which can
#    be used to get connection data

############################################################


from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset

from xlrd import open_workbook
import os

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"

from cect import print_

READER_DESCRIPTION = (
    """Data extracted from **CElegansNeuronTables.xls** for neuronal connectivity"""
)


class SpreadsheetDataReader(ConnectomeDataset):
    cells = []
    conns = []

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(conn)

    def read_data(self):
        # reading the NeuronConnectFormatted.xls file if neuron_connect = True
        neuron_connect = False
        if neuron_connect:
            filename = "%sNeuronConnectFormatted.xlsx" % spreadsheet_location
            rb = open_workbook(filename)
            print_("Opened the Excel file: " + filename)

            for row in range(1, rb.sheet_by_index(0).nrows):
                pre = str(rb.sheet_by_index(0).cell(row, 0).value)
                post = str(rb.sheet_by_index(0).cell(row, 1).value)
                syntype = rb.sheet_by_index(0).cell(row, 2).value
                num = int(rb.sheet_by_index(0).cell(row, 3).value)
                synclass = "Generic_GJ" if "EJ" in syntype else "Chemical_Synapse"

                self.conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                if pre not in self.cells:
                    self.cells.append(pre)
                if post not in self.cells:
                    self.cells.append(post)

            return self.cells, self.conns

        else:
            filename = "%sCElegansNeuronTables.xls" % spreadsheet_location
            rb = open_workbook(filename)

            print_("Opened Excel file: " + filename)

            # known_nonconnected_cells = ["CANL", "CANR", "VC6"]

            for row in range(1, rb.sheet_by_index(0).nrows):
                pre = str(rb.sheet_by_index(0).cell(row, 0).value)
                post = str(rb.sheet_by_index(0).cell(row, 1).value)
                syntype = rb.sheet_by_index(0).cell(row, 2).value
                num = int(rb.sheet_by_index(0).cell(row, 3).value)
                synclass = rb.sheet_by_index(0).cell(row, 4).value

                self.conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                if pre not in self.cells:
                    self.cells.append(pre)
                if post not in self.cells:
                    self.cells.append(post)

            """if include_nonconnected_cells:
                for c in known_nonconnected_cells:
                    self.cells.append(c)"""

            return self.cells, self.conns

    def read_muscle_data(self):
        conns = []
        neurons = []
        muscles = []

        filename = "%sCElegansNeuronTables.xls" % spreadsheet_location
        rb = open_workbook(filename)

        print_("Opened Excel file: " + filename)

        sheet = rb.sheet_by_index(1)

        for row in range(1, sheet.nrows):
            pre = str(sheet.cell(row, 0).value)
            post = str(sheet.cell(row, 1).value)
            syntype = "Send"
            num = int(sheet.cell(row, 2).value)
            synclass = sheet.cell(row, 3).value.replace(",", "plus").replace(" ", "_")

            conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
            if pre not in neurons:
                neurons.append(pre)
            if post not in muscles:
                muscles.append(post)

        return neurons, muscles, conns


def get_instance():
    return SpreadsheetDataReader()


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


def main():
    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))


if __name__ == "__main__":
    main()
