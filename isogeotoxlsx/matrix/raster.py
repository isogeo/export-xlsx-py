# -*- coding: UTF-8 -*-
#! python3

"""
    Matching table between Isogeo metadata model and Excel columns for Isogeo to Office.
"""

# ##############################################################################
# ############ Globals ############
# #################################
RASTER_COLUMNS = {
    "_created": ("AI", "date"),
    "_creator": ("E", None),
    "_id": ("AH", None),
    "_modified": ("AJ", "date"),
    "abstract": ("C", "wrap"),
    "collectionContext": ("I", None),
    "collectionMethod": ("J", None),
    "conditions": ("Z", "wrap"),
    "contacts": ("AB", None),
    "coordinateSystem": ("T", None),
    "created": ("O", "date"),
    "distance": ("V", None),
    "editionProfile": (None, None),
    "encoding": (None, None),
    "envelope": ("U", "wrap"),
    "events": ("P", None),
    "featureAttributes": (None, None),
    "features": ("Y", None),
    "format": ("S", None),
    "formatVersion": (None, None),
    "geometry": (None, None),
    "keywords": ("F", "wrap"),
    "language": ("AK", None),
    "layers": (None, None),
    "limitations": ("AA", "wrap"),
    "links": (None, None),
    "modified": ("Q", "date"),
    "name": ("B", None),
    "operations": (None, None),
    "path": ("D", None),
    "precision": (None, None),
    "published": (None, "date"),
    "scale": ("X", None),
    "series": (None, None),
    "serviceLayers": (None, None),
    "specifications": ("X", None),
    "tags": (None, None),
    "title": ("A", None),
    "topologicalConsistency": ("AC", None),
    "type": (None, None),
    "updateFrequency": ("M", None),
    "validFrom": ("K", "date"),
    "validTo": ("L", "date"),
    "validityComment": ("N", None),
    # specific
    "hasLinkDownload": ("AC", None),
    "hasLinkOther": ("AE", None),
    "hasLinkView": ("AD", None),
    "linkEdit": ("AF", None),
    "linkView": ("AG", None),
    "inspireConformance": ("H", None),
    "inspireThemes": ("G", "wrap"),
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
    columns_vector = {k: Column._make(v) for k, v in RASTER_COLUMNS.items()}
    # check
    print(isinstance(columns_vector, dict))
    print(isinstance(columns_vector.get("title"), Column))
