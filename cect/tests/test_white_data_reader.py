import unittest
from pathlib import Path

from cect.ConnectomeDataset import (
    ConnectomeDataset,
    get_cache_filename,
)
from cect.WhiteDataReader import WhiteDataReader, get_cache, get_instance


class TestReader(unittest.TestCase):
    def setUp(self):
       self.cache_files_to_cleanup = [] 

    def tearDown(self):
        for file in self.cache_files_to_cleanup:
            Path(file).unlink(missing_ok=True)

    def test_get_instance(self):
        current_filepath = Path(__file__)
        spreadsheet_directory: Path = current_filepath.parents[1] / "data"
        spreadsheet_filepath: Path = spreadsheet_directory / "aconnectome_white_1986_whole.csv"

        assert spreadsheet_filepath.is_file(), f"Test data file should exist at {spreadsheet_filepath}"
        filename = str(spreadsheet_filepath)
        instance: WhiteDataReader = get_instance(from_cache=False, spreadsheet_location=filename)
        data: tuple = instance.read_data()
        
        assert isinstance(instance, WhiteDataReader), "Instance should be of type WhiteDataReader"
        assert any([any(_) for _ in data]), "Instance should contain data"

    def test_get_cache(self):
        current_filepath = Path(__file__)
        spreadsheet_directory: Path = current_filepath.parents[1] / "data"
        spreadsheet_filepath: Path = spreadsheet_directory / "aconnectome_white_1986_whole.csv"
        filename = str(spreadsheet_filepath)
        self.cache_files_to_cleanup.append(get_cache_filename('WhiteDataReader'))
        instance: WhiteDataReader = get_instance(from_cache=False, spreadsheet_location=filename)
        instance.save_to_cache('WhiteDataReader')
        
        cache: ConnectomeDataset | None = get_cache()

        assert cache is not None, "Cache should not be None"
        assert any([any(_) for _ in cache._read_data()]), "Cache should contain data"
        assert isinstance(cache, ConnectomeDataset), "Cache should be of type WhiteDataReader"
        assert instance._read_data() == cache._read_data(), "Data from instance and cache should be identical"

if __name__ == "__main__":
    unittest.main()