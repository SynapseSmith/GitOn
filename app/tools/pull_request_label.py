from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class PullRequestLabel(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @mcp_tool(name="create_pull_request_label", description="Create a new pull request label")
    def create_pull_request_label(self, json_body: Dict):
        """Add a label to a pull request."""
        return giton_post("/~api/pull-request-labels", json_body)

    @mcp_tool(name="delete_pull_request_label", description="Delete a pull request label by ID")
    def delete_pull_request_label(
        self,
        pull_request_label_id: Annotated[Union[int, str], "Pull request label ID"]
    ):
        """Remove a label from a pull request."""
        lid = quote(str(pull_request_label_id), safe="")
        return giton_post(f"/~api/pull-request-labels/{lid}", pull_request_label_id)
