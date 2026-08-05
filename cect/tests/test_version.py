from cect import __version__

import unittest


class TestVersion(unittest.TestCase):
    def test_version(self):

        # Load mkdocs.yml, and ensure version string is present on a line there
        with open("mkdocs.yml", "r") as f:
            mkdocs_yml = f.read()
        self.assertIn(
            __version__,
            mkdocs_yml,
            f"Version {__version__} not found in mkdocs.yml. Please update!",
        )
