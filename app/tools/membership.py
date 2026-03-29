from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Membership(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _mid(membership_id: Union[int, str]) -> str:
        """Encode membership ID for URL path."""
        return quote(str(membership_id), safe="")

    @mcp_tool(name="get_membership", description="Get membership by ID")
    def get_membership(
        self,
        membership_id: Annotated[Union[int, str], "Membership ID"]
    ):
        """Retrieve a specific membership."""
        mid = self._mid(membership_id)
        return giton_get(f"/~api/memberships/{mid}")

    @mcp_tool(name="create_membership", description="Create a new membership")
    def create_membership(self, json_body: Dict):
        """Add a new membership."""
        return giton_post("/~api/memberships", json_body)

    @mcp_tool(name="delete_membership", description="Delete a membership by ID")
    def delete_membership(
        self,
        membership_id: Annotated[Union[int, str], "Membership ID"]
    ):
        """Remove a membership."""
        mid = self._mid(membership_id)
        return giton_post(f"/~api/memberships/{mid}", membership_id)
