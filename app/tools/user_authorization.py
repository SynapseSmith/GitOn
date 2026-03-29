from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class UserAuthorization(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _aid(auth_id: Union[int, str]) -> str:
        """Encode authorization ID for URL path."""
        return quote(str(auth_id), safe="")

    @mcp_tool(name="get_user_authorization", description="Get user authorization by ID")
    def get_user_authorization(
        self,
        authorization_id: Annotated[Union[int, str], "Authorization ID"]
    ):
        """Retrieve a specific user authorization."""
        aid = self._aid(authorization_id)
        return giton_get(f"/~api/user-authorizations/{aid}")

    @mcp_tool(name="create_user_authorization", description="Create a new user authorization")
    def create_user_authorization(self, json_body: Dict):
        """Create a user authorization."""
        return giton_post("/~api/user-authorizations", json_body)

    @mcp_tool(name="delete_user_authorization", description="Delete a user authorization by ID")
    def delete_user_authorization(
        self,
        authorization_id: Annotated[Union[int, str], "Authorization ID"]
    ):
        """Remove a user authorization."""
        aid = self._aid(authorization_id)
        return giton_post(f"/~api/user-authorizations/{aid}", authorization_id)
