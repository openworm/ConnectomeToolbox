#! /usr/bin/env python

from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

all_known_connectome_datasets = {}


readers = [
    "White_A",
    "White_L4",
    "White_whole",
    "WitvlietDataReader1",
    "WitvlietDataReader2",
    "WitvlietDataReader3",
    "WitvlietDataReader4",
    "WitvlietDataReader5",
    "WitvlietDataReader6",
    "WitvlietDataReader7",
    "WitvlietDataReader8",
    "VarshneyDataReader",
    "Cook2019HermReader",
    "Cook2019MaleReader",
    "Cook2020DataReader",
    "Yim2024DataReader",
]


def register_connectome_dataset(name, cds):
    all_known_connectome_datasets[name] = cds


for reader in readers:
    module = __import__("cect.%s" % reader, fromlist=["NAME", "get_instance"])
    NAME = getattr(module, "NAME")
    get_instance = getattr(module, "get_instance")

    register_connectome_dataset(NAME, get_instance)


def get_connectome_dataset(name, from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    if name not in all_known_connectome_datasets:
        raise Exception(
            "No such connectome dataset registered: %s\nKnown datasets: %s"
            % (name, list(all_known_connectome_datasets.keys()))
        )
    cds_instance = all_known_connectome_datasets[name]
    if callable(cds_instance):
        return cds_instance(from_cache=from_cache)
    else:
        return cds_instance
