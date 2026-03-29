from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class PullRequestReview(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _rid(review_id: Union[int, str]) -> str:
        """Encode review ID for URL path."""
        return quote(str(review_id), safe="")

    @mcp_tool(name="get_pull_request_review", description="Get a pull request review by ID")
    def get_pull_request_review(
        self,
        review_id: Annotated[Union[int, str], "Review ID"]
    ):
        """Retrieve review details."""
        rid = self._rid(review_id)
        return giton_get(f"/~api/pull-request-reviews/{rid}")

    @mcp_tool(name="create_pull_request_review", description="Create a new pull request review")
    def create_pull_request_review(self, json_body: Dict):
        """Add a review to a pull request."""
        return giton_post("/~api/pull-request-reviews", json_body)

    @mcp_tool(name="update_pull_request_review", description="Update a pull request review")
    def update_pull_request_review(
        self,
        review_id: Annotated[Union[int, str], "Review ID"],
        json_body: Dict
    ):
        """Modify an existing review."""
        rid = self._rid(review_id)
        return giton_post(f"/~api/pull-request-reviews/{rid}", json_body)
