from typing import Union, Optional, Annotated
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Group(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _gid(group_id: Union[int, str]) -> str:
        """Encode the group ID for URL path."""
        return quote(str(group_id), safe="")

    @mcp_tool(name="get_group", description="Get group by ID")
    def get_group(
        self,
        group_id: Annotated[Union[int, str], "Group ID"]
    ):
        """Retrieve a specific group."""
        gid = self._gid(group_id)
        return giton_get(f"/~api/groups/{gid}")

    @mcp_tool(name="get_group_authorizations", description="Get authorizations of a group")
    def get_group_authorizations(
        self,
        group_id: Annotated[Union[int, str], "Group ID"]
    ):
        """List base authorizations granted to a group."""
        gid = self._gid(group_id)
        return giton_get(f"/~api/groups/{gid}/authorizations")

    @mcp_tool(name="get_group_memberships", description="Get memberships of a group")
    def get_group_memberships(
        self,
        group_id: Annotated[Union[int, str], "Group ID"]
    ):
        """List users belonging to a group."""
        gid = self._gid(group_id)
        return giton_get(f"/~api/groups/{gid}/memberships")

    @mcp_tool(name="query_groups", description="Query groups")
    def query_groups(
        self,
        name: Annotated[Optional[str], "Search by name"] = None,
        offset: Annotated[Optional[int], "Offset"] = None,
        count: Annotated[Optional[int], "Max items"] = None
    ):
        """Search and paginate groups."""
        params = []
        if name is not None:
            params.append(f"name={quote(name)}")
        if offset is not None:
            params.append(f"offset={offset}")
        if count is not None:
            params.append(f"count={count}")
        endpoint = "/~api/groups"
        if params:
            endpoint += "?" + "&".join(params)
        return giton_get(endpoint)

    @mcp_tool(name="get_group_id", description="Get group ID by name")
    def get_group_id(
        self,
        name: Annotated[str, "Group name"]
    ):
        """Lookup group ID from its name."""
        return giton_get(f"/~api/groups/ids/{quote(name)}")

    @mcp_tool(name="create_group", description="Create a new group")
    def create_group(self, json_body: dict):
        """Create a group."""
        return giton_post("/~api/groups", json_body)

    @mcp_tool(name="update_group", description="Update group by ID")
    def update_group(
        self,
        group_id: Annotated[Union[int, str], "Group ID"],
        json_body: dict
    ):
        """Modify an existing group."""
        gid = self._gid(group_id)
        return giton_post(f"/~api/groups/{gid}", json_body)

    @mcp_tool(name="delete_group", description="Delete a group by ID")
    def delete_group(
        self,
        group_id: Annotated[Union[int, str], "Group ID"]
    ):
        """Remove a group."""
        gid = self._gid(group_id)
        return giton_post(f"/~api/groups/{gid}", group_id)
