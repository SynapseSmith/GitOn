from typing import Union, Optional, Annotated, Dict
from urllib.parse import quote_plus, quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class User(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _uid(user_id: Union[int, str]) -> str:
        """Encode user ID for URL path."""
        return quote(str(user_id), safe="")

    @mcp_tool(name="get_user", description="Get user by ID")
    def get_user(self, user_id: Annotated[Union[int, str], "User ID"]):
        """Retrieve a specific user."""
        uid = self._uid(user_id)
        return giton_get(f"/~api/users/{uid}")

    @mcp_tool(name="get_me", description="Get current authenticated user")
    def get_me(self):
        """Retrieve the currently authenticated user's info."""
        return giton_get("/~api/users/me")

    @mcp_tool(name="query_users", description="Query users")
    def query_users(
        self,
        term: Annotated[Optional[str], "Search term"] = None,
        offset: Annotated[Optional[int], "Offset"] = None,
        count: Annotated[Optional[int], "Limit"] = None
    ):
        """Search and paginate users."""
        params = []
        if term is not None:
            params.append(f"term={quote_plus(term)}")
        if offset is not None:
            params.append(f"offset={offset}")
        if count is not None:
            params.append(f"count={count}")
        endpoint = "/~api/users"
        if params:
            endpoint += "?" + "&".join(params)
        return giton_get(endpoint)

    @mcp_tool(name="get_user_id", description="Get user ID by name")
    def get_user_id(self, name: Annotated[str, "Username"]):
        """Lookup user ID from username."""
        return giton_get(f"/~api/users/ids/{quote(name)}")

    @mcp_tool(name="create_user", description="Create a new user")
    def create_user(self, json_body: Dict):
        """Add a new user."""
        return giton_post("/~api/users", json_body)

    @mcp_tool(name="update_user", description="Update a user by ID")
    def update_user(self, user_id: Annotated[Union[int, str], "User ID"], json_body: Dict):
        """Modify existing user."""
        uid = self._uid(user_id)
        return giton_post(f"/~api/users/{uid}", json_body)

    @mcp_tool(name="disable_user", description="Disable a user by ID")
    def disable_user(self, user_id: Annotated[Union[int, str], "User ID"]):
        """Disable a user."""
        uid = self._uid(user_id)
        return giton_post(f"/~api/users/{uid}/disable", {})

    @mcp_tool(name="enable_user", description="Enable a user by ID")
    def enable_user(self, user_id: Annotated[Union[int, str], "User ID"]):
        """Enable a user."""
        uid = self._uid(user_id)
        return giton_post(f"/~api/users/{uid}/enable", {})

    @mcp_tool(name="convert_to_service_account", description="Convert user to service account")
    def convert_to_service_account(self, user_id: Annotated[Union[int, str], "User ID"]):
        """Convert a user to a service account."""
        uid = self._uid(user_id)
        return giton_post(f"/~api/users/{uid}/convert-to-service-account", {})

    @mcp_tool(name="set_password", description="Set user password")
    def set_password(self, user_id: Annotated[Union[int, str], "User ID"], password: Annotated[str, "New password"]):
        """Set or reset a user's password."""
        uid = self._uid(user_id)
        return giton_post(f"/~api/users/{uid}/password", password)

    @mcp_tool(name="reset_two_factor_authentication", description="Reset two-factor authentication for a user")
    def reset_two_factor_authentication(self, user_id: Annotated[Union[int, str], "User ID"]):
        """Reset a user's two-factor authentication."""
        uid = self._uid(user_id)
        return giton_post(f"/~api/users/{uid}/two-factor-authentication", {})

    @mcp_tool(name="set_queries_and_watches", description="Set queries and watches for a user")
    def set_queries_and_watches(self, user_id: Annotated[Union[int, str], "User ID"], json_body: Dict):
        """Update user's queries and watches."""
        uid = self._uid(user_id)
        return giton_post(f"/~api/users/{uid}/queries-and-watches", json_body)

    @mcp_tool(name="add_ssh_key_to_user", description="Add an SSH key for a user")
    def add_ssh_key_to_user(self, user_id: Annotated[Union[int, str], "User ID"], json_body: Dict):
        """Add an SSH key for a user."""
        uid = self._uid(user_id)
        return giton_post(f"/~api/users/{uid}/ssh-keys", json_body)

    @mcp_tool(name="delete_user", description="Delete a user by ID")
    def delete_user(self, user_id: Annotated[Union[int, str], "User ID"]):
        """Remove a user."""
        uid = self._uid(user_id)
        return giton_post(f"/~api/users/{uid}", {})
