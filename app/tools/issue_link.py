from typing import Union, Annotated
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class IssueLink(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _lid(link_id: Union[int, str]) -> str:
        """Encode the issue link ID for URL path."""
        return quote(str(link_id), safe="")

    @mcp_tool(name="get_issue_link", description="Get issue link by ID")
    def get_issue_link(
        self,
        link_id: Annotated[Union[int, str], "Issue link ID"]
    ):
        """Retrieve a specific issue link."""
        lid = self._lid(link_id)
        return giton_get(f"/~api/issue-links/{lid}")

    @mcp_tool(name="create_issue_link", description="Create a new issue link")
    def create_issue_link(self, json_body: dict):
        """Add a link between issues."""
        return giton_post("/~api/issue-links", json_body)

    @mcp_tool(name="delete_issue_link", description="Delete an issue link by ID")
    def delete_issue_link(
        self,
        link_id: Annotated[Union[int, str], "Issue link ID"]
    ):
        """Remove an issue link."""
        lid = self._lid(link_id)
        return giton_post(f"/~api/issue-links/{lid}", link_id)
