from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class PullRequestWatch(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _wid(watch_id: Union[int, str]) -> str:
        """Encode pull request watch ID for URL path."""
        return quote(str(watch_id), safe="")

    @mcp_tool(name="get_pull_request_watch", description="Get a pull request watch by ID")
    def get_pull_request_watch(
        self,
        watch_id: Annotated[Union[int, str], "Watch ID"]
    ):
        """Retrieve a specific pull request watch."""
        wid = self._wid(watch_id)
        return giton_get(f"/~api/pull-request-watches/{wid}")

    @mcp_tool(name="create_pull_request_watch", description="Create a new pull request watch")
    def create_pull_request_watch(self, json_body: Dict):
        """Add a watch to a pull request."""
        return giton_post("/~api/pull-request-watches", json_body)

    @mcp_tool(name="update_pull_request_watch", description="Update a pull request watch")
    def update_pull_request_watch(
        self,
        watch_id: Annotated[Union[int, str], "Watch ID"],
        json_body: Dict
    ):
        """Modify an existing pull request watch."""
        wid = self._wid(watch_id)
        return giton_post(f"/~api/pull-request-watches/{wid}", json_body)

    @mcp_tool(name="delete_pull_request_watch", description="Delete a pull request watch by ID")
    def delete_pull_request_watch(
        self,
        watch_id: Annotated[Union[int, str], "Watch ID"]
    ):
        """Remove a pull request watch."""
        wid = self._wid(watch_id)
        return giton_post(f"/~api/pull-request-watches/{wid}", watch_id)
