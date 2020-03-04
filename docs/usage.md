# Usage

IsogeoToXlsx processes a [Isogeo Search as defined in the Isogeo Python SDK](https://isogeo-api-pysdk.readthedocs.io/en/latest/_apidoc/isogeo_pysdk.models.metadata_search.html). You need to perform an authenticated search before using the export package.

## Basic workflow

1. Store your secret as environment variables (using an `.env` file for example)
2. Authenticate

    ```python
    # import
    from isogeo_pysdk import Isogeo
    # API client
    isogeo = Isogeo(
        auth_mode="group",
        client_id=ISOGEO_API_GROUP_CLIENT_ID,
        client_secret=ISOGEO_API_GROUP_CLIENT_SECRET,
        auto_refresh_url="{}/oauth/token".format(ISOGEO_ID_URL),
        platform=ISOGEO_PLATFORM,
    )

    # getting a token
    isogeo.connect()
    ```

3. Make a search:

    ```python
    search = isogeo.search(include="all", page_size=100)
    # close session
    isogeo.close()
    ```

4. Export:

    ```python
    # import
    from isogeotoxlsx import Isogeo2xlsx

    # instanciate the final workbook
    out_workbook = Isogeo2xlsx(
        lang=isogeo.lang,
        url_base_edit=isogeo.app_url,
        url_base_view=isogeo.oc_url,
        write_only=True
    )
    # add needed worksheets
    out_workbook.set_worksheets(
        auto=search.tags.keys(),  # create the relevant sheets according to the metadata types
    )

    # map search results and store method
    for md in map(Metadata.clean_attributes, search.results):
        out_workbook.store_metadatas(md)

    # save as file
    out_workbook.save("./isogeo_export_to_xlsx.xlsx")

    # close properly
    out_worbook.close()
    ```

---

## Advanced

### Add a dashboard sheet

1. Set the `dashboard` bool argument to True
2. After the export, launch the analisis.

```python
# import
from isogeotoxlsx import Isogeo2xlsx
# instanciate the final workbook
out_workbook = Isogeo2xlsx(
    lang=isogeo.lang,
    url_base_edit=isogeo.app_url,
    url_base_view=isogeo.oc_url,
    write_only=True
)
# add needed worksheets
out_workbook.set_worksheets(
    auto=search.tags.keys(),  # create the relevant sheets according to the metadata types
    dashboard=True  # set the dashboard to True
)

# map search results and store method
for md in map(Metadata.clean_attributes, search.results):
    out_workbook.store_metadatas(md)

# launch analisis
out_workbook.launch_analisis()

# save as file
out_workbook.save("./isogeo_export_to_xlsx.xlsx")

# close properly
out_worbook.close()
```

### Auto-tune the sheets

After the export, launch the spreadsheets auto-tunning:

```python
# apply filters
out_workbook.tunning_worksheets()
```

### Save the output as memory-like object

For certain use cases (read-only filesystems, email's attachment...), it's preferable to not save the file on the OS and use it as memory-like object.

```python
# import
from io import BytesIO
from isogeotoxlsx import Isogeo2xlsx

# instanciate the final workbook
out_workbook = Isogeo2xlsx(
    lang=isogeo.lang,
    url_base_edit=isogeo.app_url,
    url_base_view=isogeo.oc_url,
    write_only=True
)
# add needed worksheets
out_workbook.set_worksheets(
    auto=search.tags.keys(),  # create the relevant sheets according to the metadata types
)

# map search results and store method
for md in map(Metadata.clean_attributes, search.results):
    out_workbook.store_metadatas(md)

# or save in a memory object
mem_virtual_workbook = BytesIO()
out_workbook.save(mem_virtual_workbook)
out_worbook.close()

# DO YOUR STUFF

# close properly
mem_virtual_workbook.close()

```
