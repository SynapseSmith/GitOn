from typing import Union, Optional, Annotated, Dict, List
from urllib.parse import quote, quote_plus
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Build(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _bid(build_id: Union[int, str]) -> str:
        """Encode the build ID for URL path."""
        return quote(str(build_id), safe="")

    @mcp_tool(name="get_build", description="Get build details")
    def get_build(
        self,
        build_id: Annotated[Union[int, str], "Build ID"]
    ):
        """Retrieve build information."""
        bid = self._bid(build_id)
        return giton_get(f"/~api/builds/{bid}")

    @mcp_tool(name="get_build_labels", description="Get labels of a build")
    def get_build_labels(
        self,
        build_id: Annotated[Union[int, str], "Build ID"]
    ):
        """List labels on a build."""
        bid = self._bid(build_id)
        return giton_get(f"/~api/builds/{bid}/labels")

    @mcp_tool(name="get_build_params", description="Get parameters of a build")
    def get_build_params(
        self,
        build_id: Annotated[Union[int, str], "Build ID"]
    ):
        """Retrieve build parameters."""
        bid = self._bid(build_id)
        return giton_get(f"/~api/builds/{bid}/params")

    @mcp_tool(name="get_build_dependencies", description="Get dependencies of a build")
    def get_build_dependencies(
        self,
        build_id: Annotated[Union[int, str], "Build ID"]
    ):
        """List builds this build depends on."""
        bid = self._bid(build_id)
        return giton_get(f"/~api/builds/{bid}/dependencies")

    @mcp_tool(name="get_build_dependents", description="Get dependents of a build")
    def get_build_dependents(
        self,
        build_id: Annotated[Union[int, str], "Build ID"]
    ):
        """List builds depending on this build."""
        bid = self._bid(build_id)
        return giton_get(f"/~api/builds/{bid}/dependents")

    @mcp_tool(name="get_build_fixed_issue_ids", description="Get fixed issue IDs of a build")
    def get_build_fixed_issue_ids(
        self,
        build_id: Annotated[Union[int, str], "Build ID"]
    ):
        """Retrieve IDs of issues fixed by this build."""
        bid = self._bid(build_id)
        return giton_get(f"/~api/builds/{bid}/fixed-issue-ids")

    @mcp_tool(name="query_builds", description="Query builds")
    def query_builds(self, params: Optional[Dict] = None):
        """Query builds with optional filters."""
        endpoint = "/~api/builds"
        if params:
            qs = "&".join(f"{quote_plus(str(k))}={quote_plus(str(v))}" for k, v in params.items())
            endpoint += f"?{qs}"
        return giton_get(endpoint)

    @mcp_tool(name="set_build_description", description="Set description of a build")
    def set_build_description(
        self,
        build_id: Annotated[Union[int, str], "Build ID"],
        description: Annotated[str, "Build description"]
    ):
        """Update the description of a build."""
        bid = self._bid(build_id)
        return giton_post(f"/~api/builds/{bid}/description", description)

    @mcp_tool(name="delete_build", description="Delete a build")
    def delete_build(
        self,
        build_id: Annotated[Union[int, str], "Build ID"]
    ):
        """Remove a build."""
        bid = self._bid(build_id)
        return giton_post(f"/~api/builds/{bid}", build_id)

    @mcp_tool(name="create_build_label", description="Create a build label")
    def create_build_label(self, json_body: Dict):
        """Add a label to a build."""
        return giton_post("/~api/build-labels", json_body)

    @mcp_tool(name="delete_build_label", description="Delete a build label")
    def delete_build_label(
        self,
        build_label_id: Annotated[Union[int, str], "Build label ID"]
    ):
        """Remove a label from a build."""
        lid = self._bid(build_label_id)
        return giton_post(f"/~api/build-labels/{lid}", build_label_id)

    @mcp_tool(name="download_build_log_stream", description="Download build log stream")
    def download_build_log_stream(
        self,
        build_id: Annotated[Union[int, str], "Build ID"]
    ):
        """Stream build logs."""
        bid = self._bid(build_id)
        return giton_get(f"/~api/streaming/build-logs/{bid}")
