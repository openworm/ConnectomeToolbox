from cect.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeReader import analyse_connections

from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

NAME = "Witvliet7"
SRC_FILENAME = "witvliet_2020_7.xlsx"


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WitvlietDataReader`` to load data on Witvliet dataset 7 (adult stage)

    Returns:
        WitvlietDataReader: The initialized connectome reader
    """
    if from_cache:
        from cect.ConnectomeDataset import (
            load_connectome_dataset_file,
            get_cache_filename,
        )

        return load_connectome_dataset_file(
            get_cache_filename(__file__.split("/")[-1].split(".")[0])
        )
    else:
        return WitvlietDataReader(SRC_FILENAME)


READER_DESCRIPTION = (
    """Data extracted from %s - Witvliet dataset 7 (adult stage)"""
    % get_dataset_source_on_github(SRC_FILENAME)
)


if __name__ == "__main__":
    my_instance = get_instance()

    read_data = my_instance.read_data
    read_muscle_data = my_instance.read_muscle_data
    cells, neuron_conns = read_data()
    neurons2muscles, muscles, muscle_conns = read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    cell = "RMDDR"
    cell = "RMDR"
    conns = my_instance.get_connections_from(cell, "Generic_CS")

    print(f"There are {len(conns)} connections from {cell}:")
    for c in sorted(conns.keys()):
        print(f" {cell} -> {c}: {conns[c]}")

    from cect.ConnectomeView import MOTORNEURONS_MUSCLES_VIEW as VIEW

    print("----------------")
    v = my_instance.get_connectome_view(VIEW)
    print(v.summary())

    conns = v.get_connections_from(cell, "Chemical")

    print(f"There are {len(conns)} connections from {cell} within view: {VIEW.name}:")
    for c in sorted(conns.keys()):
        print(f" (within view: {VIEW.name}) {cell} -> {c}: {conns[c]}")
