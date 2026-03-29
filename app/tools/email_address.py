from typing import Union, Annotated
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class EmailAddress(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _eid(email_id: Union[int, str]) -> str:
        """Encode the email address ID."""
        return quote(str(email_id), safe="")

    @mcp_tool(name="get_email_address", description="Get email address by ID")
    def get_email_address(
        self,
        email_address_id: Annotated[Union[int, str], "Email address ID"]
    ):
        """Retrieve an email address."""
        eid = self._eid(email_address_id)
        return giton_get(f"/~api/email-addresses/{eid}")

    @mcp_tool(name="is_email_verified", description="Check if email is verified")
    def is_email_verified(
        self,
        email_address_id: Annotated[Union[int, str], "Email address ID"]
    ):
        """Check verification status of email address."""
        eid = self._eid(email_address_id)
        return giton_get(f"/~api/email-addresses/{eid}/verified")

    @mcp_tool(name="create_email_address", description="Create a new email address")
    def create_email_address(self, json_body: dict):
        """Add a new email address."""
        return giton_post("/~api/email-addresses", json_body)

    @mcp_tool(name="set_email_public", description="Set email address as public")
    def set_email_public(self, json_body: dict):
        """Make an email address public."""
        return giton_post("/~api/email-addresses/public", json_body)

    @mcp_tool(name="set_email_private", description="Set email address as private")
    def set_email_private(self, json_body: dict):
        """Make an email address private."""
        return giton_post("/~api/email-addresses/private", json_body)

    @mcp_tool(name="set_email_primary", description="Set email address as primary")
    def set_email_primary(self, json_body: dict):
        """Set an email address as primary."""
        return giton_post("/~api/email-addresses/primary", json_body)

    @mcp_tool(name="use_email_for_git", description="Use email address for git operations")
    def use_email_for_git(self, json_body: dict):
        """Configure email for git operations."""
        return giton_post("/~api/email-addresses/git", json_body)

    @mcp_tool(name="resend_verification_email", description="Resend verification email")
    def resend_verification_email(self, json_body: dict):
        """Resend verification mail to an email address."""
        return giton_post("/~api/email-addresses/resend-verification-email", json_body)

    @mcp_tool(name="delete_email_address", description="Delete an email address")
    def delete_email_address(
        self,
        email_address_id: Annotated[Union[int, str], "Email address ID"]
    ):
        """Remove an email address."""
        eid = self._eid(email_address_id)
        return giton_post(f"/~api/email-addresses/{eid}", email_address_id)
