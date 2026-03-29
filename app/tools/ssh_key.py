from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class SshKey(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _kid(ssh_key_id: Union[int, str]) -> str:
        """Encode SSH key ID for URL path."""
        return quote(str(ssh_key_id), safe="")

    @mcp_tool(name="get_ssh_key", description="Get SSH key by ID")
    def get_ssh_key(
        self,
        ssh_key_id: Annotated[Union[int, str], "SSH key ID"]
    ):
        """Retrieve an SSH key."""
        kid = self._kid(ssh_key_id)
        return giton_get(f"/~api/ssh-keys/{kid}")

    @mcp_tool(name="create_ssh_key", description="Create a new SSH key")
    def create_ssh_key(self, json_body: Dict):
        """Add a new SSH key."""
        return giton_post("/~api/ssh-keys", json_body)

    @mcp_tool(name="delete_ssh_key", description="Delete an SSH key by ID")
    def delete_ssh_key(
        self,
        ssh_key_id: Annotated[Union[int, str], "SSH key ID"]
    ):
        """Remove an SSH key."""
        kid = self._kid(ssh_key_id)
        return giton_post(f"/~api/ssh-keys/{kid}", ssh_key_id)
