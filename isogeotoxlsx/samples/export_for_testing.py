# Standard lib
from os import environ
from pathlib import Path

# Third
from dotenv import load_dotenv

# Custom
from isogeo_pysdk import Isogeo, Metadata
from isogeotoxlsx import Isogeo2xlsx

load_dotenv("dev.env", override=True)

isogeo = Isogeo(
    auth_mode="group",
    client_id=environ.get("ISOGEO_API_GROUP_CLIENT_ID"),
    client_secret=environ.get("ISOGEO_API_GROUP_CLIENT_SECRET"),
    auto_refresh_url="{}/oauth/token".format(environ.get("ISOGEO_ID_URL")),
    platform=environ.get("ISOGEO_PLATFORM", "qa"),
)

# getting a token
isogeo.connect()

search = isogeo.search(include="all", share="1258fd9c21e347a6b6235b911826a798")

isogeo.close()

# print(search)

# instanciate the final workbook
out_workbook = Isogeo2xlsx(
    lang=isogeo.lang,
    url_base_edit=isogeo.app_url,
    url_base_view=isogeo.oc_url
)
# add needed worksheets
out_workbook.set_worksheets(auto=search.tags.keys())

# parse search results
for md in map(Metadata.clean_attributes, search.results):
    out_workbook.store_metadatas(md)

# save file
out_workbook.save("./try/_output/try_xlsxexport.xlsx")