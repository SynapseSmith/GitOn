from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class IssueComment(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _cid(comment_id: Union[int, str]) -> str:
        """Encode the issue comment ID for URL path."""
        return quote(str(comment_id), safe="")

    @mcp_tool(name="get_issue_comment", description="Get comment by ID")
    def get_issue_comment(
        self,
        comment_id: Annotated[Union[int, str], "Comment ID"]
    ):
        """Retrieve a specific issue comment."""
        cid = self._cid(comment_id)
        return giton_get(f"/~api/issue-comments/{cid}")

    @mcp_tool(name="create_issue_comment", description="Create a new issue comment")
    def create_issue_comment(self, json_body: Dict):
        """Add a new comment to an issue."""
        return giton_post("/~api/issue-comments", json_body)

    @mcp_tool(name="update_issue_comment", description="Update an existing issue comment")
    def update_issue_comment(
        self,
        comment_id: Annotated[Union[int, str], "Comment ID"],
        json_body: Dict
    ):
        """Modify an existing issue comment."""
        cid = self._cid(comment_id)
        return giton_post(f"/~api/issue-comments/{cid}", json_body)

    @mcp_tool(name="delete_issue_comment", description="Delete an issue comment by ID")
    def delete_issue_comment(
        self,
        comment_id: Annotated[Union[int, str], "Comment ID"]
    ):
        """Remove an issue comment."""
        cid = self._cid(comment_id)
        return giton_post(f"/~api/issue-comments/{cid}", comment_id)
