from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Iteration(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _iid(iteration_id: Union[int, str]) -> str:
        """Encode iteration ID for URL path."""
        return quote(str(iteration_id), safe="")

    @mcp_tool(name="get_iteration", description="Get iteration by ID")
    def get_iteration(
        self,
        iteration_id: Annotated[Union[int, str], "Iteration ID"]
    ):
        """Retrieve a specific iteration."""
        iid = self._iid(iteration_id)
        return giton_get(f"/~api/iterations/{iid}")

    @mcp_tool(name="create_iteration", description="Create a new iteration")
    def create_iteration(self, json_body: Dict):
        """Create an iteration."""
        return giton_post("/~api/iterations", json_body)

    @mcp_tool(name="update_iteration", description="Update an iteration")
    def update_iteration(
        self,
        iteration_id: Annotated[Union[int, str], "Iteration ID"],
        json_body: Dict
    ):
        """Modify an existing iteration."""
        iid = self._iid(iteration_id)
        return giton_post(f"/~api/iterations/{iid}", json_body)

    @mcp_tool(name="delete_iteration", description="Delete an iteration by ID")
    def delete_iteration(
        self,
        iteration_id: Annotated[Union[int, str], "Iteration ID"]
    ):
        """Remove an iteration."""
        iid = self._iid(iteration_id)
        return giton_post(f"/~api/iterations/{iid}", iteration_id)
