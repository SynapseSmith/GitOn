from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class JobRun(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _bid(build_id: Union[int, str]) -> str:
        """Encode the build ID for URL path."""
        return quote(str(build_id), safe="")

    @mcp_tool(name="run_build", description="Run a build job")
    def run_build(self, json_body: Dict):
        """Trigger a build run."""
        return giton_post("/~api/job-runs", json_body)

    @mcp_tool(name="rebuild_build", description="Rebuild a job")
    def rebuild_build(self, json_body: Dict):
        """Re-trigger a build run."""
        return giton_post("/~api/job-runs/rebuild", json_body)

    @mcp_tool(name="cancel_build", description="Cancel a build run")
    def cancel_build(
        self,
        build_id: Annotated[Union[int, str], "Build ID"]
    ):
        """Cancel a running build."""
        bid = self._bid(build_id)
        return giton_post(f"/~api/job-runs/{bid}", build_id)
