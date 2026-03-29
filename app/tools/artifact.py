from typing import Union, Annotated
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Artifact(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _bid(build_id: Union[int, str]) -> str:
        """Encode the build ID for URL path."""
        return quote(str(build_id), safe="")

    @staticmethod
    def _apath(path: str) -> str:
        """Encode the artifact path for URL path."""
        return quote(path, safe="/")

    @mcp_tool(name="get_artifact_info", description="Get artifact info")
    def get_artifact_info(
        self,
        build_id: Annotated[Union[int, str], "Build ID"],
        artifact_path: Annotated[str, "Artifact path"]
    ):
        """Retrieve artifact metadata info."""
        bid = self._bid(build_id)
        ap = self._apath(artifact_path)
        return giton_get(f"/~api/artifacts/{bid}/infos{ap}")

    @mcp_tool(name="download_artifact", description="Download artifact content")
    def download_artifact(
        self,
        build_id: Annotated[Union[int, str], "Build ID"],
        artifact_path: Annotated[str, "Artifact path"]
    ):
        """Download artifact content."""
        bid = self._bid(build_id)
        ap = self._apath(artifact_path)
        return giton_get(f"/~api/artifacts/{bid}/contents/{ap}")

    @mcp_tool(name="upload_artifact", description="Upload artifact")
    def upload_artifact(
        self,
        build_id: Annotated[Union[int, str], "Build ID"],
        artifact_path: Annotated[str, "Artifact path"]
    ):
        """Upload artifact to the server. Body is raw bytes."""
        bid = self._bid(build_id)
        ap = self._apath(artifact_path)
        # raw data should be passed as `json_body` or payload
        return giton_post(f"/~api/artifacts/{bid}/{ap}")

    @mcp_tool(name="delete_artifact", description="Delete artifact")
    def delete_artifact(
        self,
        build_id: Annotated[Union[int, str], "Build ID"],
        artifact_path: Annotated[str, "Artifact path"]
    ):
        """Delete an artifact."""
        bid = self._bid(build_id)
        ap = self._apath(artifact_path)
        return giton_post(f"/~api/artifacts/{bid}{ap}")
