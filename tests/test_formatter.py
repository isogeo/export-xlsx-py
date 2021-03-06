# -*- coding: UTF-8 -*-
#! python3

"""
    Usage from the repo root folder:

    ```python
    # for whole test
    python -m unittest tests.test_formatter
    # for specific
    python -m unittest tests.test_formatter.TestFormatter.test_cgus
    ```
"""

# #############################################################################
# ########## Libraries #############
# ##################################
# Standard library
import json
import logging
import unittest
import urllib3
from os import environ
from pathlib import Path
from random import sample
from socket import gethostname
from sys import exit, _getframe
from time import gmtime, strftime

# 3rd party
from dotenv import load_dotenv
from isogeo_pysdk import Isogeo, Metadata, MetadataSearch

# target
from isogeotoxlsx import Formatter

# #############################################################################
# ######## Globals #################
# ##################################


if Path("dev.env").exists():
    load_dotenv("dev.env", override=True)

# host machine name - used as discriminator
hostname = gethostname()

# #############################################################################
# ########## Helpers ###############
# ##################################


def get_test_marker():
    """Returns the function name"""
    return "TEST_UNIT_PythonSDK - {}".format(_getframe(1).f_code.co_name)


# #############################################################################
# ########## Classes ###############
# ##################################


class TestFormatter(unittest.TestCase):
    """Test formatter of Isogeo API results."""

    # -- Standard methods --------------------------------------------------------
    @classmethod
    def setUpClass(cls):
        """Executed when module is loaded before any test."""
        # checks
        if not environ.get("ISOGEO_API_GROUP_CLIENT_ID") or not environ.get(
            "ISOGEO_API_GROUP_CLIENT_SECRET"
        ):
            logging.critical("No API credentials set as env variables.")
            exit()
        else:
            pass

        # ignore warnings related to the QA self-signed cert
        if environ.get("ISOGEO_PLATFORM").lower() == "qa":
            urllib3.disable_warnings()

        # API connection
        cls.isogeo = Isogeo(
            auth_mode="group",
            client_id=environ.get("ISOGEO_API_GROUP_CLIENT_ID"),
            client_secret=environ.get("ISOGEO_API_GROUP_CLIENT_SECRET"),
            auto_refresh_url="{}/oauth/token".format(environ.get("ISOGEO_ID_URL")),
            platform=environ.get("ISOGEO_PLATFORM", "qa"),
        )
        # getting a token
        cls.isogeo.connect()

        # load fixture search
        search_all_includes = Path("tests/fixtures/api_search_complete.json")
        with search_all_includes.open("r") as f:
            search = json.loads(f.read())
        cls.search = MetadataSearch(**search)

        # module to test
        cls.fmt = Formatter()

    def setUp(self):
        """Executed before each test."""
        # tests stuff
        self.discriminator = "{}_{}".format(
            hostname, strftime("%Y-%m-%d_%H%M%S", gmtime())
        )

    def tearDown(self):
        """Executed after each test."""
        pass

    @classmethod
    def tearDownClass(cls):
        """Executed after the last test."""
        # close sessions
        cls.isogeo.close()

    # -- TESTS ---------------------------------------------------------

    # formatter
    def test_cgus(self):
        """CGU formatter."""
        # get conditions reformatted
        for result in self.search.results:
            # load result
            md = Metadata.clean_attributes(result)

            # empty or not, it should work
            if len(md.conditions):
                cgus_out = self.fmt.conditions(md.conditions)
            else:
                cgus_out = self.fmt.conditions(md.conditions)

            # test
            self.assertIsInstance(cgus_out, list)
            self.assertEqual(len(result.get("conditions")), len(cgus_out))

    def test_limitations(self):
        """Limitations formatter."""
        # filtered search
        for md in self.search.results:
            if md.get("limitations"):
                md_lims = md
                break

        # get limitations reformatted
        lims_in = md_lims.get("limitations", [])
        lims_out = self.fmt.limitations(lims_in)
        lims_no = self.fmt.limitations([])
        # test
        self.assertIsInstance(lims_out, list)
        self.assertIsInstance(lims_no, list)

    def test_specifications(self):
        """Limitations formatter."""
        # filtered search
        for md in self.search.results:
            if md.get("specifications"):
                md_specs = md
                break

        # get limitations reformatted
        specs_in = md_specs.get("specifications", [])
        specs_out = self.fmt.specifications(specs_in)
        specs_no = self.fmt.specifications([])
        # test
        self.assertIsInstance(specs_out, list)
        self.assertIsInstance(specs_no, list)

    def test_update_frequencies(self):
        """Update frequency formatter."""
        # update frequencies
        self.assertEqual(self.fmt.frequency_as_explicit_str("P1D"), "1 jour(s)")


# ##############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    unittest.main()
