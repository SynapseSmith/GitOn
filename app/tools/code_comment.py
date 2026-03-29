from typing import Union, Annotated
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class CodeComment(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _cid(comment_id: Union[int, str]) -> str:
        """Encode the code comment ID for URL path."""
        return quote(str(comment_id), safe="")

    @mcp_tool(name="get_code_comment", description="Get code comment by ID")
    def get_code_comment(
        self,
        comment_id: Annotated[Union[int, str], "Comment ID"]
    ):
        """Retrieve a specific code comment."""
        cid = self._cid(comment_id)
        return giton_get(f"/~api/code-comments/{cid}")

    @mcp_tool(name="delete_code_comment", description="Delete code comment by ID")
    def delete_code_comment(
        self,
        comment_id: Annotated[Union[int, str], "Comment ID"]
    ):
        """Remove a specific code comment."""
        cid = self._cid(comment_id)
        return giton_post(f"/~api/code-comments/{cid}", comment_id)
