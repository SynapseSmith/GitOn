from typing import Union, Optional, Annotated
from urllib.parse import quote, quote_plus
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Package(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _pid(pack_id: Union[int, str]) -> str:
        """Encode the package ID for URL path."""
        return quote(str(pack_id), safe="")

    @mcp_tool(name="get_pack", description="Get package by ID")
    def get_pack(
        self,
        pack_id: Annotated[Union[int, str], "Package ID"]
    ):
        """Retrieve a package."""
        pid = self._pid(pack_id)
        return giton_get(f"/~api/packages/{pid}")

    @mcp_tool(name="get_package_labels", description="Get labels of a package")
    def get_package_labels(
        self,
        pack_id: Annotated[Union[int, str], "Package ID"]
    ):
        """List labels on a package."""
        pid = self._pid(pack_id)
        return giton_get(f"/~api/packages/{pid}/labels")

    @mcp_tool(name="get_package_blobs", description="Get blobs of a package")
    def get_package_blobs(
        self,
        pack_id: Annotated[Union[int, str], "Package ID"]
    ):
        """List blobs in a package."""
        pid = self._pid(pack_id)
        return giton_get(f"/~api/packages/{pid}/blobs")

    @mcp_tool(name="query_packs", description="Query packages")
    def query_packs(
        self,
        query: Annotated[Optional[str], "Search query"] = None,
        offset: Annotated[Optional[int], "Offset"] = None,
        count: Annotated[Optional[int], "Limit"] = None
    ):
        """Search and paginate packages."""
        params = []
        if query is not None:
            params.append(f"query={quote_plus(query)}")
        if offset is not None:
            params.append(f"offset={offset}")
        if count is not None:
            params.append(f"count={count}")
        endpoint = "/~api/packages"
        if params:
            endpoint += "?" + "&".join(params)
        return giton_get(endpoint)

    @mcp_tool(name="delete_pack", description="Delete a package by ID")
    def delete_pack(
        self,
        pack_id: Annotated[Union[int, str], "Package ID"]
    ):
        """Remove a package."""
        pid = self._pid(pack_id)
        return giton_post(f"/~api/packages/{pid}", pack_id)
