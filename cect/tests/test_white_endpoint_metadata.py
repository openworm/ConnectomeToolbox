import unittest
from pathlib import Path

from cect.Cells import is_herm_neuron, is_known_muscle
from cect.readers.WhiteDataReader import WhiteDataReader


class TestWhiteEndpointMetadata(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        filename = (
            Path(__file__).parents[1] / "data" / "aconnectome_white_1986_whole.csv"
        )
        reader = WhiteDataReader(str(filename))
        neurons, muscles, other_cells, connections = reader.read_all_data()
        cls.neurons = set(neurons)
        cls.muscles = set(muscles)
        cls.other_cells = set(other_cells)
        cls.endpoints = {
            endpoint
            for connection in connections
            for endpoint in (connection.pre_cell, connection.post_cell)
        }

    def test_neurons_are_neuron_endpoints(self):
        expected = {cell for cell in self.endpoints if is_herm_neuron(cell)}
        self.assertSetEqual(self.neurons, expected)

    def test_muscles_are_muscle_endpoints(self):
        expected = {
            cell
            for cell in self.endpoints
            if not is_herm_neuron(cell) and is_known_muscle(cell)
        }
        self.assertSetEqual(self.muscles, expected)

    def test_other_cells_are_other_endpoints(self):
        expected = {
            cell
            for cell in self.endpoints
            if not is_herm_neuron(cell) and not is_known_muscle(cell)
        }
        self.assertSetEqual(self.other_cells, expected)

    def test_metadata_is_a_disjoint_complete_partition(self):
        self.assertTrue(self.neurons.isdisjoint(self.muscles))
        self.assertTrue(self.neurons.isdisjoint(self.other_cells))
        self.assertTrue(self.muscles.isdisjoint(self.other_cells))
        self.assertSetEqual(
            self.neurons | self.muscles | self.other_cells, self.endpoints
        )


if __name__ == "__main__":
    unittest.main()
