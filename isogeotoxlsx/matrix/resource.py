# -*- coding: UTF-8 -*-
#! python3

"""
    Matching table between Isogeo metadata model and Excel columns for Isogeo to Office.
"""

# ##############################################################################
# ############ Globals ############
# #################################
RESOURCE_COLUMNS = {
    "_created": ("T", "date"),
    "_creator": ("D", None),
    "_id": ("S", None),
    "_modified": ("U", "date"),
    "abstract": ("B", "wrap"),
    "conditions": ("K", "wrap"),
    "contacts": ("M", None),
    "created": ("F", "date"),
    "format": ("J", None),
    "keywords": ("E", "wrap"),
    "language": ("V", None),
    "limitations": ("L", "wrap"),
    "links": (None, None),
    "modified": ("H", "date"),
    "name": ("Z", None),
    "path": ("C", None),
    "published": ("I", "date"),
    "specifications": ("AB", "wrap"),
    "tags": (None, None),
    "title": ("A", None),
    # specific
    "hasLinkDownload": ("N", None),
    "hasLinkOther": ("P", None),
    "hasLinkView": ("O", None),
    "linkEdit": ("Q", None),
    "linkView": ("R", None),
    "inspireConformance": ("Y", None),
    "inspireThemes": ("X", "wrap"),
}

# #############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    """ Standalone execution and development tests """
    # specific imports
    from collections import namedtuple

    # set namedtuple structure
    Column = namedtuple("Column", ["letter", "title", "wrap"])
    # apply transformation
    columns_vector = {k: Column._make(v) for k, v in RESOURCE_COLUMNS.items()}
    # check
    print(isinstance(columns_vector, dict))
    print(isinstance(columns_vector.get("title"), Column))
