from typing import Union, Annotated, List, Optional
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class AccessToken(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _tid(token_id: Union[int, str]) -> str:
        """Encode the access token ID for URL path."""
        return quote(str(token_id), safe="")

    @mcp_tool(name="get_token", description="Get a token by ID")
    def get_token(
        self,
        access_token_id: Annotated[Union[int, str], "Access token ID"]
    ):
        """Retrieve an access token."""
        tid = self._tid(access_token_id)
        return giton_get(f"/~api/access-tokens/{tid}")

    @mcp_tool(name="get_token_authorizations", description="Get authorizations of a token")
    def get_token_authorizations(
        self,
        access_token_id: Annotated[Union[int, str], "Access token ID"]
    ):
        """List authorizations associated with an access token."""
        tid = self._tid(access_token_id)
        return giton_get(f"/~api/access-tokens/{tid}/authorizations")

    @mcp_tool(name="create_token", description="Create a new access token")
    def create_token(self, json_body: dict):
        """Create a new access token."""
        return giton_post("/~api/access-tokens", json_body)

    @mcp_tool(name="update_token", description="Update an existing access token")
    def update_token(
        self,
        access_token_id: Annotated[Union[int, str], "Access token ID"],
        json_body: dict
    ):
        """Update properties of an access token."""
        tid = self._tid(access_token_id)
        return giton_post(f"/~api/access-tokens/{tid}", json_body)

    @mcp_tool(name="delete_token", description="Delete an access token")
    def delete_token(
        self,
        access_token_id: Annotated[Union[int, str], "Access token ID"]
    ):
        """Remove an access token."""
        tid = self._tid(access_token_id)
        return giton_post(f"/~api/access-tokens/{tid}", access_token_id)
