# Usage

IsogeoToXlsx processes a [Isogeo Search as defined in the Isogeo Python SDK](https://isogeo-api-pysdk.readthedocs.io/en/latest/_apidoc/isogeo_pysdk.models.metadata_search.html).

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
        dashboard=True  # add a dashboard sheet
    )

    # map search results and store method
    for md in map(Metadata.clean_attributes, search.results):
        out_workbook.store_metadatas(md)

    # save as file
    out_workbook.save("./isogeo_export_to_xlsx.xlsx")

    # or save in a memory object
    mem_virtual_workbook = BytesIO()
    out_workbook.save(mem_virtual_workbook)
    ```

