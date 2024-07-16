from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset

from openpyxl import load_workbook

import os
from cect import print_

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/data/"
spreadsheet_name = "NeuronConnect.xlsx"  # has old name...
spreadsheet_name = "NeuronConnectFormatted.xlsx"

READER_DESCRIPTION = (
    """Data extracted from **%s** for neuronal connectivity""" % spreadsheet_name
)

NMJ_ENDPOINT = "NMJ"


class VarshneyDataReader(ConnectomeDataset):
    cells = []
    conns = []

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data(include_nonconnected_cells=True)
        for conn in neuron_conns:
            self.add_connection(conn)

    def read_data(self, include_nonconnected_cells=False, neuron_connect=True):
        if neuron_connect:
            filename = "%s%s" % (spreadsheet_location, spreadsheet_name)
            wb = load_workbook(filename)
            sheet = wb.worksheets[0]
            print_("Opened the Excel file: " + filename)

            for row in sheet.iter_rows(
                min_row=2, values_only=True
            ):  # Assuming data starts from the second row
                pre = str(row[0])
                post = str(row[1])

                if not post == NMJ_ENDPOINT:
                    syntype = str(row[2])
                    num = int(row[3])
                    synclass = "Generic_GJ" if "EJ" in syntype else "Generic_CS"

                    self.conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                    if pre not in self.cells:
                        self.cells.append(pre)
                    if post not in self.cells:
                        self.cells.append(post)

            return self.cells, self.conns

    def read_muscle_data(self):
        conns = []
        neurons = []
        muscles = []

        filename = "%s%s" % (spreadsheet_location, spreadsheet_name)
        wb = load_workbook(filename)
        sheet = wb.worksheets[0]

        print_("Opened Excel file: " + filename)

        for row in sheet.iter_rows(
            min_row=2, values_only=True
        ):  # Assuming data starts from the second row
            pre = str(row[0])
            post = str(row[1])

            if post == NMJ_ENDPOINT:
                syntype = str(row[2])
                num = int(row[3])
                synclass = "Generic_GJ" if "EJ" in syntype else "Generic_CS"

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                if pre not in neurons:
                    neurons.append(pre)
                if not post in muscles:
                    muscles.append(post)

        return neurons, muscles, conns


def get_instance():
    return VarshneyDataReader()


my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data


def main():
    cells, neuron_conns = my_instance.read_data(include_nonconnected_cells=True)
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    print(my_instance.summary())

if __name__ == "__main__":
    main()
