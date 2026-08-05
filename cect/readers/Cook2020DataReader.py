import csv

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeReader import analyse_connections
from cect.ConnectomeDataset import ConnectomeDataset
from cect.ConnectomeDataset import get_dataset_source_on_github

# ruff: noqa: F401
from cect.Cells import PREFERRED_HERM_NEURON_NAMES

# ruff: noqa: F401
from cect.Cells import PREFERRED_MUSCLE_NAMES
from cect.Cells import convert_to_preferred_muscle_name
from cect.Cells import is_potential_muscle

# ruff: noqa: F401
from cect.Cells import is_known_muscle
from cect.Cells import is_marginal_epithelial_gland_cell
from cect.Cells import convert_to_preferred_phar_cell_name
from cect.Neurotransmitters import GENERIC_CHEM_SYN_CLASS, CHEMICAL_SYN_TYPE
from cect.Neurotransmitters import GENERIC_ELEC_SYN_CLASS, ELECTRICAL_SYN_TYPE
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

import os

from cect import print_

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/../data/"
filename = "%scne24932-sup-0004-supinfo4.csv" % spreadsheet_location
filename2 = "%scne24932-sup-0005-supinfo5.csv" % spreadsheet_location

NAME = "Cook2020"

DATASET_DESCRIPTION = "Chemical and electrical connectivity of the _C. elegans_ pharynx, from Cook et al 2020, including connections between pharyngeal neurons, muscles and other cells (epithelial, gland and marginal)."

WEIGHTS = "Weights represent the anatomical strength of a connection, calculated as the total number of serial EM sections across which the connection is observed, summed over all individual synapses between the two cells. For chemical connections, a section is counted if a presynaptic specialization is visible; for electrical connections, a section is counted if a gap junction is visible between the two cells."

READER_DESCRIPTION = (
    """Data extracted from %s and %s for connectivity of pharyngeal neurons, muscles and other cells"""
    % (
        get_dataset_source_on_github(filename.split("/")[-1]),
        get_dataset_source_on_github(filename2.split("/")[-1]),
    )
)


class Cook2020DataReader(ConnectomeDataset):
    """
    Reader of data from Cook et al. 2020 - The connectome of the Caenorhabditis elegans pharynx

    Returns:
        (Cook2020DataReader): The initialized Cook et al 2020 pharyngeal connectome reader
    """

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(
                conn,
                check_overwritten_connections=False,
                append_existing_connections=True,
                fail_on_any_repeated_connection=False,
            )

        print_("\n*********************** Validation Info ************************")
        print(self.validation_info)
        print_("****************************************************************")

    def read_data(self):
        """
        Returns:
            (tuple[list, list]): List of cells (str) and list of connections (``ConnectionInfo``) which have been read in
        """
        cells = []
        conns = []

        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            print_("Opened file: " + filename)

            for row in reader:
                pre = str.strip(row["Source"])
                if is_potential_muscle(pre):
                    pre = convert_to_preferred_muscle_name(pre)
                post = str.strip(row["Target"])
                if is_potential_muscle(post):
                    post = convert_to_preferred_muscle_name(post)
                if is_marginal_epithelial_gland_cell(post):
                    post = convert_to_preferred_phar_cell_name(post)
                num = float(row["Weight"])
                syntype = str.strip(row["Type"])

                if syntype == "Electrical":
                    syntype = ELECTRICAL_SYN_TYPE
                else:
                    syntype = CHEMICAL_SYN_TYPE

                synclass = (
                    GENERIC_ELEC_SYN_CLASS
                    if syntype == ELECTRICAL_SYN_TYPE
                    else GENERIC_CHEM_SYN_CLASS
                )

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                # Add post -> pre conn for gap junction connections
                if syntype == ELECTRICAL_SYN_TYPE:
                    conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                if pre not in cells:
                    cells.append(pre)
                if post not in cells:
                    cells.append(post)

        with open(filename2, "r") as f:
            reader = csv.DictReader(f)
            print_("Opened file: " + filename)

            for row in reader:
                pre = str.strip(row["Source"])
                if is_potential_muscle(pre):
                    pre = convert_to_preferred_muscle_name(pre)
                if is_marginal_epithelial_gland_cell(pre):
                    pre = convert_to_preferred_phar_cell_name(pre)
                post = str.strip(row["Target"])

                if is_potential_muscle(post):
                    post = convert_to_preferred_muscle_name(post)
                if is_marginal_epithelial_gland_cell(post):
                    post = convert_to_preferred_phar_cell_name(post)

                num = float(row["Weight"])

                syntype = ELECTRICAL_SYN_TYPE
                synclass = GENERIC_ELEC_SYN_CLASS

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))
                # Add post -> pre conn for gap junction connections
                conns.append(ConnectionInfo(post, pre, num, syntype, synclass))

                if pre not in cells:
                    cells.append(pre)
                if post not in cells:
                    cells.append(post)

        return cells, conns

    def read_muscle_data(self):
        return self._read_muscle_data()


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(get_cache_filename(__name__.split(".")[-1]))
    else:
        return Cook2020DataReader()


my_instance = get_instance()


def main():
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(
        cells, neuron_conns, neurons2muscles, muscles, muscle_conns, print_details_on=[]
    )

    print_(" -- Finished analysing connections using: %s" % os.path.basename(__file__))

    print_(my_instance.summary())

    cells = ["I5", "M4"]
    syntypes = ["Generic_CS", "Generic_GJ"]

    for cell in cells:
        for syntype in syntypes:
            conns = my_instance.get_connections_from(cell, syntype)
            print(f"There are {len(conns)} connections from {cell} of type {syntype}:")
            for c in sorted(conns.keys()):
                print(f" {cell} -> {c}: {conns[c]}")


if __name__ == "__main__":
    main()
