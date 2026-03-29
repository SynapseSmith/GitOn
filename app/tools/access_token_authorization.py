from typing import Union, Annotated, List, Optional
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class AccessTokenAuthorization(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _aid(auth_id: Union[int, str]) -> str:
        """Encode the authorization ID for URL path."""
        return quote(str(auth_id), safe="")

    @mcp_tool(name="get_token_authorization", description="Get an access token authorization")
    def get_token_authorization(
        self,
        authorization_id: Annotated[Union[int, str], "Authorization ID"]
    ):
        """Retrieve a specific access token authorization."""
        aid = self._aid(authorization_id)
        return giton_get(f"/~api/access-token-authorizations/{aid}")

    @mcp_tool(name="create_token_authorization", description="Create a new access token authorization")
    def create_token_authorization(self, json_body: dict):
        """Create a new authorization for an access token."""
        return giton_post("/~api/access-token-authorizations", json_body)

    @mcp_tool(name="update_token_authorization", description="Update an existing access token authorization")
    def update_token_authorization(
        self,
        authorization_id: Annotated[Union[int, str], "Authorization ID"],
        json_body: dict
    ):
        """Update properties of an access token authorization."""
        aid = self._aid(authorization_id)
        return giton_post(f"/~api/access-token-authorizations/{aid}", json_body)

    @mcp_tool(name="delete_token_authorization", description="Delete an access token authorization")
    def delete_token_authorization(
        self,
        authorization_id: Annotated[Union[int, str], "Authorization ID"]
    ):
        """Remove an access token authorization."""
        aid = self._aid(authorization_id)
        return giton_post(f"/~api/access-token-authorizations/{aid}", authorization_id)
