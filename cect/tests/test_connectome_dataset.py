from cect import print_
import unittest

import pprint


class TestConnectomeDataset(unittest.TestCase):
    def test_json(self):
        # from cect.Cook2019HermReader import get_instance
        import importlib

        for r in [
            "BrittinDataReader",
            "Cook2019HermReader",
            "Cook2019MaleReader",
            "Cook2020DataReader",
            "RipollSanchezLongRangeReader",
            "RipollSanchezMidRangeReader",
            "RipollSanchezShortRangeReader",
            "SpreadsheetDataReader",
            "UpdatedSpreadsheetDataReader",
            "UpdatedSpreadsheetDataReader2",
            "VarshneyDataReader",
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
            "WormNeuroAtlasFuncReader",
            "WormNeuroAtlasMAReader",
            "WormNeuroAtlasPepReader",
            "WormNeuroAtlasReader",
            "Yim2024DataReader",
            "TestDataReader",
        ]:  # "VarshneyDataReader",
            m = importlib.import_module("cect." + r)

            print_("Loading %s from source..." % r)
            cds1 = m.get_instance(from_cache=False)
            summary1 = cds1.summary()

            print_("\nLoaded a dataset:\n%s" % summary1)

            d = cds1.to_dict()

            if "Test" in r:
                print_("\nAs a dictionary:\n")
                pprint.pprint(d)

            from cect.ConnectomeDataset import (
                load_connectome_dataset,
                load_connectome_dataset_file,
            )

            print_("Reloading %s from dict..." % r)
            cds2 = load_connectome_dataset(d)
            summary2 = cds2.summary()

            print_("\nReloaded a dataset:\n%s" % summary2)

            assert summary1 == summary2

            filename = cds1.save_to_cache(r)
            print_("Saved to: %s" % filename)

            print_("Reloading %s from file..." % r)
            cds3 = load_connectome_dataset_file(filename)
            summary3 = cds3.summary()

            print_("\nReloaded a dataset from file:\n%s" % summary3)

            assert summary1 == summary3

            print_("Contents of %s identical to that in original reader" % filename)

            cds4 = m.get_instance(from_cache=True)
            summary4 = cds4.summary()

            print_("\nLoaded a dataset:\n%s" % summary4)
            assert summary1 == summary4
            print_("Contents of cached %s identical to that in original reader" % r)


if __name__ == "__main__":
    unittest.main()
