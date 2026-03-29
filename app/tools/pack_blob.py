from typing import Union, Optional, Annotated, Dict
from urllib.parse import quote, quote_plus
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class PackBlob(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @mcp_tool(name="find_blob_by_hash", description="Find package blob by hash")
    def find_blob_by_hash(
        self,
        projectId: Annotated[Optional[int], "Project ID"] = None,
        hash: Annotated[Optional[str], "Content hash"] = None
    ):
        """Locate a package blob by its hash, optionally scoped to a project."""
        params = []
        if projectId is not None:
            params.append(f"projectId={quote_plus(str(projectId))}")
        if hash is not None:
            params.append(f"hash={quote_plus(hash)}")
        endpoint = "/~api/package-blobs"
        if params:
            endpoint += "?" + "&".join(params)
        return giton_get(endpoint)

    @mcp_tool(name="download_pack_blob", description="Download package blob content")
    def download_pack_blob(
        self,
        pack_blob_id: Annotated[Union[int, str], "Package blob ID"]
    ):
        """Download content of a specific package blob."""
        pbid = quote(str(pack_blob_id), safe="")
        return giton_get(f"/~api/package-blobs/{pbid}/content")
