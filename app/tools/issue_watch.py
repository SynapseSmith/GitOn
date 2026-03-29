from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class IssueWatch(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _wid(watch_id: Union[int, str]) -> str:
        """Encode the issue watch ID for URL path."""
        return quote(str(watch_id), safe="")

    @mcp_tool(name="get_issue_watch", description="Get issue watch by ID")
    def get_issue_watch(
        self,
        watch_id: Annotated[Union[int, str], "Watch ID"]
    ):
        """Retrieve a specific issue watch."""
        wid = self._wid(watch_id)
        return giton_get(f"/~api/issue-watches/{wid}")

    @mcp_tool(name="create_issue_watch", description="Create a new issue watch")
    def create_issue_watch(self, json_body: Dict):
        """Add a watch to an issue."""
        return giton_post("/~api/issue-watches", json_body)

    @mcp_tool(name="update_issue_watch", description="Update an issue watch")
    def update_issue_watch(
        self,
        watch_id: Annotated[Union[int, str], "Watch ID"],
        json_body: Dict
    ):
        """Modify an existing issue watch."""
        wid = self._wid(watch_id)
        return giton_post(f"/~api/issue-watches/{wid}", json_body)

    @mcp_tool(name="delete_issue_watch", description="Delete an issue watch by ID")
    def delete_issue_watch(
        self,
        watch_id: Annotated[Union[int, str], "Watch ID"]
    ):
        """Remove an issue watch."""
        wid = self._wid(watch_id)
        return giton_post(f"/~api/issue-watches/{wid}", watch_id)
