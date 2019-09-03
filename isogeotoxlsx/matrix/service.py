# -*- coding: UTF-8 -*-
#! python3

"""
    Matching table between Isogeo metadata model and Excel columns for Isogeo to Office.
"""

# ##############################################################################
# ############ Globals ############
# #################################
SERVICE_COLUMNS = {
    "_created": ("X", "date"),
    "_creator": ("E", None),
    "_id": ("W", None),
    "_modified": ("Y", "date"),
    "abstract": ("C", "wrap"),
    "collectionContext": ("I", "wrap"),
    "collectionMethod": ("J", "wrap"),
    "conditions": ("O", "wrap"),
    "contacts": ("Q", None),
    "coordinateSystem": (None, None),
    "created": ("H", "date"),
    "distance": (None, None),
    "editionProfile": (None, None),
    "encoding": (None, None),
    "envelope": ("M", "wrap"),
    "events": ("I", None),
    "featureAttributes": (None, None),
    "features": ("Y", None),
    "format": ("L", None),
    "formatVersion": (None, None),
    "geometry": (None, None),
    "keywords": ("F", "wrap"),
    "language": ("AQZ", None),
    "layers": (None, None),
    "limitations": ("P", "wrap"),
    "links": (None, None),
    "modified": ("J", "date"),
    "name": ("B", None),
    "operations": (None, None),
    "path": ("D", None),
    "precision": (None, None),
    "published": ("K", "date"),
    "scale": ("X", None),
    "series": (None, None),
    "serviceLayers": (None, None),
    "specifications": ("N", "wrap"),
    "tags": (None, None),
    "title": ("A", None),
    "topologicalConsistency": ("AC", "wrap"),
    "type": (None, None),
    "updateFrequency": (None, None),
    "validFrom": (None, "date"),
    "validTo": (None, "date"),
    "validityComment": (None, None),
    # specific
    "hasLinkDownload": ("R", None),
    "hasLinkOther": ("T", None),
    "hasLinkView": ("S", None),
    "linkEdit": ("U", None),
    "linkView": ("V", None),
    "inspireConformance": ("G", None),
    "inspireThemes": (None, "wrap"),
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
    columns_vector = {k: Column._make(v) for k, v in SERVICE_COLUMNS.items()}
    # check
    print(isinstance(columns_vector, dict))
    print(isinstance(columns_vector.get("title"), Column))
