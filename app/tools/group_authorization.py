from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class GroupAuthorization(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _aid(auth_id: Union[int, str]) -> str:
        """Encode group authorization ID for URL path."""
        return quote(str(auth_id), safe="")

    @mcp_tool(name="get_group_authorization", description="Get group authorization by ID")
    def get_group_authorization(
        self,
        authorization_id: Annotated[Union[int, str], "Group authorization ID"]
    ):
        """Retrieve a specific group authorization."""
        aid = self._aid(authorization_id)
        return giton_get(f"/~api/group-authorizations/{aid}")

    @mcp_tool(name="create_group_authorization", description="Create a new group authorization")
    def create_group_authorization(self, json_body: Dict):
        """Create a group authorization."""
        return giton_post("/~api/group-authorizations", json_body)

    @mcp_tool(name="delete_group_authorization", description="Delete a group authorization by ID")
    def delete_group_authorization(
        self,
        authorization_id: Annotated[Union[int, str], "Group authorization ID"]
    ):
        """Remove a group authorization."""
        aid = self._aid(authorization_id)
        return giton_post(f"/~api/group-authorizations/{aid}", authorization_id)
