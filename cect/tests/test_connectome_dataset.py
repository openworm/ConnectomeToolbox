from cect import print_
import unittest

import pprint


class TestConnectomeDataset(unittest.TestCase):

    def test_json(self):

        from cect.TestDataReader import get_instance
        from cect.Cook2019HermReader import get_instance


        print_('Loading from source...')
        cds1 = get_instance()
        summary1 = cds1.summary()

        print_('\nLoaded a dataset:\n%s'%summary1)

        d = cds1.to_dict()

        pprint.pprint(d)

        from cect.ConnectomeDataset import load_connectome_dataset
        print_('Reloading...')
        cds2 = load_connectome_dataset(d)
        summary2 = cds2.summary()

        print_('\nReloaded a dataset:\n%s'%summary2)

        assert(summary1==summary2)



if __name__ == "__main__":
    unittest.main()
