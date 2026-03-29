from typing import Union, Optional, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class LabelSpec(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _lsid(label_spec_id: Union[int, str]) -> str:
        """Encode the label spec ID for URL path."""
        return quote(str(label_spec_id), safe="")

    @mcp_tool(name="get_label_spec", description="Get a label spec by ID")
    def get_label_spec(
        self,
        label_spec_id: Annotated[Union[int, str], "Label spec ID"]
    ):
        """Retrieve a specific label specification."""
        lid = self._lsid(label_spec_id)
        return giton_get(f"/~api/label-specs/{lid}")

    @mcp_tool(name="query_label_specs", description="Query label specs")
    def query_label_specs(
        self,
        name: Annotated[Optional[str], "Filter by name"] = None,
        offset: Annotated[Optional[int], "Offset"] = None,
        count: Annotated[Optional[int], "Limit"] = None
    ):
        """List or search label specifications."""
        params = []
        if name is not None:
            params.append(f"name={quote(name)}")
        if offset is not None:
            params.append(f"offset={offset}")
        if count is not None:
            params.append(f"count={count}")
        endpoint = "/~api/label-specs"
        if params:
            endpoint += "?" + "&".join(params)
        return giton_get(endpoint)

    @mcp_tool(name="create_label_spec", description="Create a new label spec")
    def create_label_spec(self, json_body: Dict):
        """Add a new label specification."""
        return giton_post("/~api/label-specs", json_body)

    @mcp_tool(name="update_label_spec", description="Update a label spec by ID")
    def update_label_spec(
        self,
        label_spec_id: Annotated[Union[int, str], "Label spec ID"],
        json_body: Dict
    ):
        """Modify an existing label specification."""
        lid = self._lsid(label_spec_id)
        return giton_post(f"/~api/label-specs/{lid}", json_body)

    @mcp_tool(name="delete_label_spec", description="Delete a label spec by ID")
    def delete_label_spec(
        self,
        label_spec_id: Annotated[Union[int, str], "Label spec ID"]
    ):
        """Remove a label specification."""
        lid = self._lsid(label_spec_id)
        return giton_post(f"/~api/label-specs/{lid}", label_spec_id)
