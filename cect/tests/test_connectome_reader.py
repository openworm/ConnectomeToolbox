from cect import print_
import unittest


class TestConnectomeReader(unittest.TestCase):
    def test_conn_info(self):
        from cect.ConnectomeReader import ConnectionInfo, load_connection_info

        ci = ConnectionInfo("precell", "postcell", 66, "sy", "sc")

        str1 = str(ci)
        print_("Created: %s" % str1)

        d = ci.to_dict()

        print_("Dict version: %s" % d)

        ci2 = load_connection_info(d)

        str2 = str(ci2)
        print_("Reloaded: %s" % str2)

        assert str1 == str2


if __name__ == "__main__":
    unittest.main()
