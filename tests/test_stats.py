# -*- coding: UTF-8 -*-
#! python3

"""
    Usage from the repo root folder:

    ```python
    # for whole test
    python -m unittest tests.test_stats
    # for specific
    python -m unittest tests.test_stats.TestStats.test_translations_length
    ```
"""

# #############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import unittest

# 3rd party
from openpyxl import Workbook

# target
from isogeotoxlsx.utils import Stats


# #############################################################################
# ########## Classes ###############
# ##################################


class TestStats(unittest.TestCase):
    """Test stats and charts module."""

    def setUp(self):
        """Executed before each test."""
        pass

    def tearDown(self):
        """Executed after each test."""
        pass

    # -- TESTS ---------------------------------------------------
    def test_translations_length(self):
        """Ensure that different translations have the same length"""
        # this module
        app = Stats()
        # workbook
        wb = Workbook()

        # types of metadatas
        ws_types = wb.create_sheet(title="Types")
        app.md_types_repartition = {
            "raster": 50,
            "resource": 10,
            "service": 40,
            "vector": 100,
        }

        app.pie_types(ws_types)

        # formats of source datasets
        ws_formats = wb.create_sheet(title="Formats")
        app.data_formats = [
            "PostGIS",
            "WFS",
            "PostGIS",
            "WMS",
            "Esri Shapefiles",
            "Esri Shapefiles",
            "Esri Shapefiles",
            "Esri Shapefiles",
            "Esri Shapefiles",
        ]

        app.pie_formats(
            ws_formats,
            # cell_start_table="A"  # you can specify where to write table
        )

        # write xlsx
        wb.save("test_stats_charts.xlsx")


# #############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    unittest.main()
