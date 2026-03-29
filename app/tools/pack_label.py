from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class PackLabel(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @mcp_tool(name="create_pack_label", description="Create a new package label")
    def create_pack_label(self, json_body: Dict):
        """Add a label to a package."""
        return giton_post("/~api/package-labels", json_body)

    @mcp_tool(name="delete_pack_label", description="Delete a package label by ID")
    def delete_pack_label(
        self,
        pack_label_id: Annotated[Union[int, str], "Package label ID"]
    ):
        """Remove a label from a package."""
        lid = quote(str(pack_label_id), safe="")
        return giton_post(f"/~api/package-labels/{lid}", pack_label_id)
