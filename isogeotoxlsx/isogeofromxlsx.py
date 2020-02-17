# -*- coding: UTF-8 -*-
#! python3

"""
    Make Metadatas from Excel worksheet like those returned by Isogeo2xlsx.

"""

# ##############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import logging
from collections.abc import KeysView
from pathlib import Path
from urllib.parse import urlparse

# 3rd party library
from isogeo_pysdk import IsogeoUtils, Isogeo, IsogeoChecker, Metadata, Keyword, Limitation, License, Specification
from openpyxl import Workbook
from openpyxl.styles import Alignment, NamedStyle
from openpyxl.utils import column_index_from_string, get_column_letter
from openpyxl.worksheet.worksheet import Worksheet

# custom submodules
from isogeotoxlsx.i18n import I18N_EN, I18N_FR
from isogeotoxlsx.matrix import (
    ColumnPattern,
    ATTRIBUTES_COLUMNS,
    RASTER_COLUMNS,
    RESOURCE_COLUMNS,
    SERVICE_COLUMNS,
    VECTOR_COLUMNS,
)
from isogeotoxlsx.utils import Formatter, Stats

# ##############################################################################
# ############ Globals ############
# #################################

logger = logging.getLogger("isogeotoxlsx")
utils = IsogeoUtils()

# ##############################################################################
# ########## Classes ###############
# ##################################


class IsogeoFromxlsx():
    """Used to store Isogeo API results into an Excel worksheet (.xlsx)

    :param str lang: selected language for output
    :param str url_base_edit: base url to format edit links (basically app.isogeo.com)
    :param str url_base_view: base url to format view links (basically open.isogeo.com)
    """

    def __init__(
        self,
        file_path: str = ""
    ):
        """Instanciating the output workbook.

        :param str lang: selected language for output
        :param str url_base_edit: base url to format edit links (basically app.isogeo.com)
        :param str url_base_view: base url to format view links (basically open.isogeo.com)
        """
        super(IsogeoFromxlsx, self).__init__()

        # LOCALE
        if lang.lower() == "fr":
            s_date.number_format = "dd/mm/yyyy"
            self.dates_fmt = "DD/MM/YYYY"
            self.locale_fmt = "fr_FR"
            self.tr = I18N_FR
        else:
            s_date.number_format = "yyyy/mm/dd"
            self.dates_fmt = "YYYY/MM/DD"
            self.locale_fmt = "uk_UK"
            self.tr = I18N_EN

    def build_index_dict(self, md_type: str = "vector"):

    def create_vector_md(self):

    def create_raster_md(self):

    def create_service_md(self):

    def fill_easy_fields(self):

    def manage_subressources(self):