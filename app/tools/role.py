from typing import Union, Optional, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Role(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _rid(role_id: Union[int, str]) -> str:
        """Encode role ID for URL path."""
        return quote(str(role_id), safe="")

    @mcp_tool(name="get_role", description="Get role by ID")
    def get_role(
        self,
        role_id: Annotated[Union[int, str], "Role ID"]
    ):
        """Retrieve a specific role."""
        rid = self._rid(role_id)
        return giton_get(f"/~api/roles/{rid}")

    @mcp_tool(name="query_roles", description="Query roles")
    def query_roles(
        self,
        name: Annotated[Optional[str], "Filter by name"] = None,
        offset: Annotated[Optional[int], "Offset"] = None,
        count: Annotated[Optional[int], "Limit"] = None
    ):
        """List or search roles."""
        params = []
        if name is not None:
            params.append(f"name={quote(name)}")
        if offset is not None:
            params.append(f"offset={offset}")
        if count is not None:
            params.append(f"count={count}")
        endpoint = "/~api/roles"
        if params:
            endpoint += "?" + "&".join(params)
        return giton_get(endpoint)

    @mcp_tool(name="get_role_id", description="Get role ID by name")
    def get_role_id(
        self,
        name: Annotated[str, "Role name"]
    ):
        """Lookup role ID by its name."""
        return giton_get(f"/~api/roles/ids/{quote(name)}")

    @mcp_tool(name="create_role", description="Create a new role")
    def create_role(self, json_body: Dict):
        """Create a role."""
        return giton_post("/~api/roles", json_body)

    @mcp_tool(name="update_role", description="Update a role by ID")
    def update_role(
        self,
        role_id: Annotated[Union[int, str], "Role ID"],
        json_body: Dict
    ):
        """Modify an existing role."""
        rid = self._rid(role_id)
        return giton_post(f"/~api/roles/{rid}", json_body)

    @mcp_tool(name="delete_role", description="Delete a role by ID")
    def delete_role(
        self,
        role_id: Annotated[Union[int, str], "Role ID"]
    ):
        """Remove a role."""
        rid = self._rid(role_id)
        return giton_post(f"/~api/roles/{rid}", role_id)
