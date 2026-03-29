from typing import Union, Annotated
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class BaseAuthorization(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _aid(auth_id: Union[int, str]) -> str:
        """Encode base authorization ID for URL path."""
        return quote(str(auth_id), safe="")

    @mcp_tool(name="get_base_authorization", description="Get base authorization by ID")
    def get_base_authorization(
        self,
        authorization_id: Annotated[Union[int, str], "Authorization ID"]
    ):
        """Retrieve a base authorization."""
        aid = self._aid(authorization_id)
        return giton_get(f"/~api/base-authorizations/{aid}")

    @mcp_tool(name="create_base_authorization", description="Create a new base authorization")
    def create_base_authorization(self, json_body: dict):
        """Create a base authorization."""
        return giton_post("/~api/base-authorizations", json_body)

    @mcp_tool(name="delete_base_authorization", description="Delete a base authorization")
    def delete_base_authorization(
        self,
        authorization_id: Annotated[Union[int, str], "Authorization ID"]
    ):
        """Remove a base authorization."""
        aid = self._aid(authorization_id)
        return giton_post(f"/~api/base-authorizations/{aid}", authorization_id)
