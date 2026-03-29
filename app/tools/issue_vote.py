from typing import Union, Annotated
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class IssueVote(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _vid(vote_id: Union[int, str]) -> str:
        """Encode the issue vote ID for URL path."""
        return quote(str(vote_id), safe="")

    @mcp_tool(name="get_issue_vote", description="Get vote by ID")
    def get_issue_vote(
        self,
        vote_id: Annotated[Union[int, str], "Vote ID"]
    ):
        """Retrieve a specific vote."""
        vid = self._vid(vote_id)
        return giton_get(f"/~api/issue-votes/{vid}")

    @mcp_tool(name="create_issue_vote", description="Create a new issue vote")
    def create_issue_vote(self, json_body: dict):
        """Add a vote to an issue."""
        return giton_post("/~api/issue-votes", json_body)

    @mcp_tool(name="delete_issue_vote", description="Delete an issue vote by ID")
    def delete_issue_vote(
        self,
        vote_id: Annotated[Union[int, str], "Vote ID"]
    ):
        """Remove a vote."""
        vid = self._vid(vote_id)
        return giton_post(f"/~api/issue-votes/{vid}", vote_id)
