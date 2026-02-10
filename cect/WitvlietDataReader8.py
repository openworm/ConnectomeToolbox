from cect.WitvlietDataReader import WitvlietDataReader
from cect.ConnectomeDataset import get_dataset_source_on_github
from cect.ConnectomeReader import analyse_connections


from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

NAME = "Witvliet8"
SRC_FILENAME = "witvliet_2020_8.xlsx"


def get_instance(from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    """Uses ``WitvlietDataReader`` to load data on Witvliet dataset 8 (adult stage)

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


"""
my_instance = get_instance()

read_data = my_instance.read_data
read_muscle_data = my_instance.read_muscle_data"""


READER_DESCRIPTION = (
    """Data extracted from %s - Witvliet dataset 8 (adult stage)"""
    % get_dataset_source_on_github(SRC_FILENAME)
)


if __name__ == "__main__":
    my_instance = get_instance(from_cache=False)
    cells, neuron_conns = my_instance.read_data()
    neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

    analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)

    print(my_instance.summary())
    print("--------------------------------")

    cells = ["VD8", "VD9", "SMDDR", "HSNR"]
    for cell in cells:
        print(f"\n -  {cell} - ")
        syntypes = ["Generic_CS"]
        for syntype in syntypes:
            conns = my_instance.get_connections_to(cell, syntype)

            print(f"There are {len(conns)} {syntype} connections to {cell}")
            max = 10
            for c in sorted(conns.keys())[:max]:
                print(f"   {c} -> {cell}: {conns[c]}")
            if len(conns) > max:
                print("   ...")

    # suspect connection: RIFR -> HSNR: 1.0
