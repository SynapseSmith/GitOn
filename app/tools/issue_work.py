from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class IssueWork(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _wid(work_id: Union[int, str]) -> str:
        """Encode the issue work ID for URL path."""
        return quote(str(work_id), safe="")

    @mcp_tool(name="get_issue_work", description="Get issue work by ID")
    def get_issue_work(
        self,
        work_id: Annotated[Union[int, str], "Work ID"]
    ):
        """Retrieve a specific issue work entry."""
        wid = self._wid(work_id)
        return giton_get(f"/~api/issue-works/{wid}")

    @mcp_tool(name="create_issue_work", description="Create a new issue work entry")
    def create_issue_work(self, json_body: Dict):
        """Add work log to an issue."""
        return giton_post("/~api/issue-works", json_body)

    @mcp_tool(name="update_issue_work", description="Update an issue work entry")
    def update_issue_work(
        self,
        work_id: Annotated[Union[int, str], "Work ID"],
        json_body: Dict
    ):
        """Modify an existing work log."""
        wid = self._wid(work_id)
        return giton_post(f"/~api/issue-works/{wid}", json_body)

    @mcp_tool(name="delete_issue_work", description="Delete an issue work entry by ID")
    def delete_issue_work(
        self,
        work_id: Annotated[Union[int, str], "Work ID"]
    ):
        """Remove a work log entry."""
        wid = self._wid(work_id)
        return giton_post(f"/~api/issue-works/{wid}", work_id)
