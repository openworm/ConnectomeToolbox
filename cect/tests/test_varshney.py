from cect.ConnectomeReader import analyse_connections

import unittest


class TestReader(unittest.TestCase):
    def test_reader(self):
        from cect.VarshneyDataReader import get_instance

        my_instance = get_instance()

        cells, neuron_conns = my_instance.read_data()
        neurons2muscles, muscles, muscle_conns = my_instance.read_muscle_data()

        analyse_connections(cells, neuron_conns, neurons2muscles, muscles, muscle_conns)


if __name__ == "__main__":
    unittest.main()
