# -*- coding: UTF-8 -*-
#! python3

"""
    Matching table between Isogeo metadata model and Excel columns for Isogeo to Office.
"""

# ##############################################################################
# ############ Globals ############
# #################################
VECTOR_COLUMNS = {
    "_created": ("AM", "date"),
    "_creator": ("E", None),
    "_id": ("AL", None),
    "_modified": ("AN", "date"),
    "abstract": ("C", "wrap"),
    "collectionContext": ("I", "wrap"),
    "collectionMethod": ("J", "wrap"),
    "conditions": ("AD", "wrap"),
    "contacts": ("AF", None),
    "coordinateSystem": ("T", None),
    "created": ("O", "date"),
    "distance": ("W", None),
    "editionProfile": (None, None),
    "encoding": (None, None),
    "envelope": ("U", "wrap"),
    "events": ("P", None),
    "featureAttributes": ("AA", "wrap"),
    "features": ("Y", None),
    "format": ("S", None),
    "formatVersion": (None, None),
    "geometry": ("V", None),
    "keywords": ("F", "wrap"),
    "language": ("AO", None),
    "layers": (None, None),
    "limitations": ("AE", "wrap"),
    "links": (None, None),
    "modified": ("Q", "date"),
    "name": ("B", None),
    "operations": (None, None),
    "path": ("D", None),
    "precision": (None, None),
    "published": ("R", None),
    "scale": ("X", None),
    "series": (None, None),
    "serviceLayers": (None, None),
    "specifications": ("AB", "wrap"),
    "tags": (None, None),
    "title": ("A", None),
    "topologicalConsistency": ("AC", "wrap"),
    "typ(e": (None, None),
    "updateFrequency": ("M", None),
    "validFrom": ("K", "date"),
    "validTo": ("L", "date"),
    "validityComment": ("N", None),
    # specific,
    "featureAttributesCount": ("Z", None),
    "hasLinkDownload": ("AG", None),
    "hasLinkOther": ("AI", None),
    "hasLinkView": ("AH", None),
    "linkEdit": ("AJ", None),
    "linkView": ("AK", None),
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
    Column = namedtuple("Column", ["letter", "wrap"])
    # apply transformation
    columns_vector = {k: Column._make(v) for k, v in VECTOR_COLUMNS.items()}
    # check
    print(isinstance(columns_vector, dict))
    print(isinstance(columns_vector.get("title"), Column))

    for k, v in columns_vector.items():
        print(k, type(v), v.letter)
