############################################################

#   A script to read the values for monaoaminergic connectivity from Bentley et al. 2016

############################################################

from cect.Neurotransmitters import EXTRASYNAPTIC_SYN_TYPE
from cect.Neurotransmitters import DOPAMINE
from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT
from cect.ConnectomeDataset import get_dataset_source_on_github

from cect.ConnectomeReader import ConnectionInfo
from cect.ConnectomeDataset import ConnectomeDataset

import csv
import logging
import sys
import os

from cect import print_

LOGGER = logging.getLogger(__name__)

NAME = "Bentley2016_MA"

spreadsheet_location = os.path.dirname(os.path.abspath(__file__)) + "/../data/"
filename = "%sedgelist_MA.csv" % spreadsheet_location

READER_DESCRIPTION = (
    """Data extracted from %s for monoaminergic connectivity of Bentley et al. 2016"""
    % (get_dataset_source_on_github(filename.split("/")[-1]),)
)

DATASET_DESCRIPTION = """Data on monoaminergic connectivity from Bentley et al. 2016 (i.e. dopaminergic, tyraminergic, octopaminergic & serotonergic extracellular transmission)."""

WEIGHTS = "Adjacency matrices are binary and directed; a weight of 1 between neurons A and B signifies that cell A expresses a biosynthetic enzyme or transporter for the specific monoamine and neuron B expresses a cognate receptor for that monoamine."


class Bentley2016MAReader(ConnectomeDataset):
    """
    Reader of data from Bentley et al. 2016 - Monoaminergic connectivity in C. elegans

    Returns:
        (Bentley2016MAReader): The initialized Bentley et al. 2016 monoaminergic connectome reader
    """

    verbose = False

    def __init__(self):
        ConnectomeDataset.__init__(self)

        cells, neuron_conns = self.read_data()
        for conn in neuron_conns:
            self.add_connection_info(
                conn,
                check_overwritten_connections=False,
                append_existing_connections=False,
                fail_on_any_repeated_connection=False,
            )

        if self.verbose:
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
            reader = csv.reader(f)
            # print_("Opened file: " + filename)

            for row in reader:
                # print_("Reading row: " + str(row))
                pre = str.strip(row[0])
                post = str.strip(row[1])
                num = 1
                syntype = EXTRASYNAPTIC_SYN_TYPE

                synclass = str.strip(row[2]).capitalize()

                conns.append(ConnectionInfo(pre, post, num, syntype, synclass))

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
        return Bentley2016MAReader()


my_instance = get_instance()

if __name__ == "__main__":
    my_instance = get_instance(from_cache=False)
    cells, neuron_conns = my_instance._read_data()
    print("Loaded %s connections" % len(neuron_conns))

    # from cect.ConnectomeReader import analyse_connections
    # analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    to_test = ["ADEL", "RIML", "CEPVR"]

    synclass = DOPAMINE  # or 'Tyramine', 'Octopamine', 'Serotonin'

    for cell in to_test:
        # my_instance.atlas.all_about(cell)

        print(
            "MA conns from %s:\n%s"
            % (
                cell,
                "\n".join(
                    [
                        f"   {c}:  \t{float(w)}"
                        for c, w in my_instance.get_connections_from(
                            cell, synclass, ordered_by_weight=True
                        ).items()
                    ]
                ),
            )
        )

        print(
            "MA conns to %s:\n%s"
            % (
                cell,
                "\n".join(
                    [
                        f"   {c}:  \t{float(w)}"
                        for c, w in my_instance.get_connections_to(
                            cell, synclass, ordered_by_weight=True
                        ).items()
                    ]
                ),
            )
        )

    if "-nogui" not in sys.argv:
        print(my_instance.summary())

        # from cect.ConnectomeView import RAW_VIEW as view
        from cect.ConnectomeView import NEURONS_VIEW as view

        cds2 = my_instance.get_connectome_view(view)

        print(cds2.summary())

        """
        fig = cds2.to_plotly_graph_fig(DOPAMINE, view)
        """

        fig, _ = cds2.to_plotly_matrix_fig(
            EXTRASYNAPTIC_SYN_TYPE,
            view,
        )
        import plotly.io as pio

        pio.renderers.default = "browser"
        import sys

        fig.show()
