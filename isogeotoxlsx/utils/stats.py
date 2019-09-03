# -*- coding: UTF-8 -*-
#!/usr/bin/env python


# ----------------------------------------------------------------------------
# Name:         OpenCatalog to Excel
# Purpose:      Get metadatas from an Isogeo OpenCatlog and store it into
#               an Excel workbook.
#
# Author:       Isogeo
#
# Python:       2.7.x
# Created:      14/08/2014
# Updated:      28/01/2016
# ----------------------------------------------------------------------------

# ###########################################################################
# ########## Libraries ##########
# ###############################

# Standard library
from collections import Counter, defaultdict
import logging

# submodule
from isogeotoxlsx.i18n import I18N_EN, I18N_FR

# 3rd party library
from openpyxl.chart import PieChart, Reference
from openpyxl.chart.series import DataPoint
from openpyxl.worksheet.worksheet import Worksheet


# ##############################################################################
# ############ Globals ############
# #################################

# LOG
logger = logging.getLogger("isogeotoxlsx")

# ############################################################################
# ######## Classes ###############
# ################################


class Stats(object):
    """Doc for Isogeo."""

    md_empty_fields = defaultdict(list)
    md_types_repartition = defaultdict(int)
    md_tags_occurences = defaultdict(int)

    def __init__(self, lang="fr"):
        """Instanciate stats class."""
        # self._ = _
        super(Stats, self).__init__()

        # LOCALE
        if lang.lower() == "fr":
            self.dates_fmt = "DD/MM/YYYY"
            self.locale_fmt = "fr_FR"
            self.tr = I18N_FR
        else:
            self.dates_fmt = "YYYY/MM/DD"
            self.locale_fmt = "uk_UK"
            self.tr = I18N_EN

    def attributes(self, ws_attributes: Worksheet, all_attributes: list):
        """Perform feature attributes analisis and write results into the
        dedicatedWworksheet."""
        idx_fa = 1
        # local arrays
        fa_names = []
        # fa_types = []
        # fa_alias = []
        # fa_descr = []

        # parsing
        for dico_fa in all_attributes:
            for fa in dico_fa:
                fa_names.append(fa.get("name"))
                # fa_alias.append(fa.get("alias", "NR"))
                # fa_types.append(fa.get("dataType"))
                # fa_descr.append(fa.get("description", "NR"))
                del fa

        # stats
        frq_names = Counter(fa_names)
        # frq_alias = Counter(fa_alias)
        # frq_types = Counter(fa_types)
        # frq_descr = Counter(fa_descr)

        # write
        ws = ws_attributes
        for fa in frq_names:
            idx_fa += 1
            ws["A{}".format(idx_fa)] = fa
            ws["B{}".format(idx_fa)] = frq_names.get(fa)

    # def fillfull(self):
    #     """Calculate fields fillfull level."""
    #     return "HOHOHOHO"

    # def week_work(self, search_results=list):
    #     """Return histogram data to represent cataloging activity per week."""
    #     for md in search_results:
    #         print(md.get("type", "No md, no type"))

    #     return "weekly baby!"

    def metadata_types(self, ws: Worksheet, types_counters: dict = None):
        """Return histogram data to represent cataloging activity per week."""
        if types_counters is None:
            types_counters = self.md_types_repartition

        # build the data for pie chart
        data = (
            (self.tr.get("type"), self.tr.get("occurrences")),
            (self.tr.get("vector"), self.md_types_repartition.get("vector", 0)),
            (self.tr.get("raster"), self.md_types_repartition.get("raster", 0)),
            (self.tr.get("service"), self.md_types_repartition.get("service", 0)),
            (self.tr.get("resource"), self.md_types_repartition.get("resource", 0)),
        )

        # write data into worksheet
        for row in data:
            ws.append(row)

        # Pie chart
        pie = PieChart()
        labels = Reference(ws, min_col=1, min_row=2, max_row=5)
        data = Reference(ws, min_col=2, min_row=1, max_row=5)
        pie.add_data(data, titles_from_data=True)
        pie.set_categories(labels)
        pie.title = self.tr.get("type") + "s"

        # Cut the first slice out of the pie
        slice = DataPoint(idx=0, explosion=20)
        pie.series[0].data_points = [slice]

        ws.add_chart(pie, "D1")

    # def keywords_bar(self, sheet, results, total=20):
    #     """Return histogram data to represent cataloging activity per week."""
    #     # tags parsing
    #     li_keywords = []
    #     li_inspire = []
    #     for md in results:
    #         li_keywords.extend(
    #             (
    #                 i.get("text")
    #                 for i in md.get("keywords", [])
    #                 if i.get("_tag").startswith("keyword:is")
    #             )
    #         )
    #         li_inspire.extend(
    #             (
    #                 i.get("text")
    #                 for i in md.get("keywords", [])
    #                 if i.get("_tag").startswith("keyword:in")
    #             )
    #         )
    #     keywords = Counter(li_keywords)
    #     inspire = Counter(li_inspire)

    #     data_k = [("Keyword", "Count")]
    #     for k, c in keywords.most_common(50):
    #         data_k.append((k, c))

    #     # write data into worksheet
    #     for row in data_k:
    #         sheet.append(row)

    #     bar = BarChart()
    #     bar.type = "bar"
    #     bar.style = 10
    #     bar.title = "Keywords by occurrences"
    #     bar.y_axis.title = "Occurences"
    #     bar.x_axis.title = "Keywords"

    #     data = Reference(sheet, min_col=2, min_row=1, max_row=50, max_col=3)
    #     cats = Reference(sheet, min_col=1, min_row=2, max_row=50)
    #     bar.add_data(data, titles_from_data=True)
    #     bar.set_categories(cats)
    #     bar.shape = 4

    #     return bar


# ############################################################################
# ###### Stand alone program ########
# ###################################
if __name__ == "__main__":
    """Standalone execution and tests."""
    from os import environ
    from isogeo_pysdk import Isogeo, __version__ as pysdk_version
    from openpyxl import Workbook

    # API access
    share_id = environ.get("ISOGEO_API_DEV_ID")
    share_token = environ.get("ISOGEO_API_DEV_SECRET")
    isogeo = Isogeo(client_id=share_id, client_secret=share_token)
    bearer = isogeo.connect()

    # search
    search = isogeo.search(bearer, whole_results=0, include=["keywords"])

    # workbook
    wb = Workbook()
    # ws = wb.active

    # this app
    app = Stats()
    # app.week_work(search.get("results"))
    # print(type(app.fillfull()))

    # metadata types
    ws_d = wb.create_sheet(title="Dashboard")
    # # pie = app.type_pie(ws_d,
    #                    search.get('total'))
    # # ws_d.add_chart(pie, "D1")

    bar = app.keywords_bar(ws_d, search.get("results"))
    ws_d.add_chart(bar, "A10")
    # write xlsx
    wb.save("test.xlsx")
