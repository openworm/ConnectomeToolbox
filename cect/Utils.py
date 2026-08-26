#! /usr/bin/env python

from cect.ConnectomeDataset import LOAD_READERS_FROM_CACHE_BY_DEFAULT

from cect import print_

all_known_connectome_datasets = {}


readers = [
    "DurbinJSHDataReader",
    "DurbinN2UDataReader",
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
    "Bentley2016MAReader",
    "Bentley2016PepReader",
    "Cook2019HermReader",
    "Cook2019MaleReader",
    "Cook2020DataReader",
    "BrittinDataReader",
    "WormNeuroAtlasFuncReader",
    "RipollSanchezShortRangeReader",
    "RipollSanchezMidRangeReader",
    "RipollSanchezLongRangeReader",
    "Yim2024DataReader",
    "Yim2024NonNormDataReader",
    "Yim2024ContactomeDataReader",
    "Yim2024ContactomeNonNormDataReader",
    "Wang2024HermReader",
    "Wang2024MaleReader",
]


def register_connectome_dataset(name, cds):
    print_(" -- Registering connectome dataset: %s" % name)
    all_known_connectome_datasets[name] = cds


for reader in readers:
    module = __import__("cect.readers.%s" % reader, fromlist=["NAME", "get_instance"])
    NAME = getattr(module, "NAME")
    get_instance = getattr(module, "get_instance")

    register_connectome_dataset(NAME, get_instance)


def get_connectome_dataset(name, from_cache=LOAD_READERS_FROM_CACHE_BY_DEFAULT):
    name_no_reader = name.replace("Reader", "")
    if name not in all_known_connectome_datasets:
        if name_no_reader not in all_known_connectome_datasets:
            raise Exception(
                "No such connectome dataset registered: %s (or %s)\nKnown datasets: %s"
                % (name, name_no_reader, list(all_known_connectome_datasets.keys()))
            )
        name = name_no_reader
    cds_instance = all_known_connectome_datasets[name]
    if callable(cds_instance):
        return cds_instance(from_cache=from_cache)
    else:
        return cds_instance
