from typing import Union, Annotated, Dict
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Setting(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @mcp_tool(name="get_system_setting", description="Get system setting")
    def get_system_setting(self):
        """Retrieve global system setting."""
        return giton_get("/~api/settings/system")

    @mcp_tool(name="get_authenticator", description="Get authenticator setting")
    def get_authenticator(self):
        """Retrieve authenticator configuration."""
        return giton_get("/~api/settings/authenticator")

    @mcp_tool(name="get_backup_setting", description="Get backup setting")
    def get_backup_setting(self):
        """Retrieve backup configuration."""
        return giton_get("/~api/settings/backup")

    @mcp_tool(name="get_build_setting", description="Get build setting")
    def get_build_setting(self):
        """Retrieve build setting."""
        return giton_get("/~api/settings/build")

    @mcp_tool(name="get_groovy_scripts", description="Get groovy scripts setting")
    def get_groovy_scripts(self):
        """Retrieve groovy scripts setting."""
        return giton_get("/~api/settings/groovy-scripts")

    @mcp_tool(name="get_issue_setting", description="Get issue setting")
    def get_issue_setting(self):
        """Retrieve issue configuration."""
        return giton_get("/~api/settings/issue")

    @mcp_tool(name="get_job_executors", description="Get job executors setting")
    def get_job_executors(self):
        """Retrieve job executors list."""
        return giton_get("/~api/settings/job-executors")

    @mcp_tool(name="get_mail_service", description="Get mail service setting")
    def get_mail_service(self):
        """Retrieve mail service configuration."""
        return giton_get("/~api/settings/mail-service")

    @mcp_tool(name="get_service_desk_setting", description="Get service desk setting")
    def get_service_desk_setting(self):
        """Retrieve service desk configuration."""
        return giton_get("/~api/settings/service-desk")

    @mcp_tool(name="get_notification_template_setting", description="Get notification template setting")
    def get_notification_template_setting(self):
        """Retrieve notification template configuration."""
        return giton_get("/~api/settings/notification-template")

    @mcp_tool(name="get_project_setting", description="Get project setting")
    def get_project_setting(self):
        """Retrieve default project setting."""
        return giton_get("/~api/settings/project")

    @mcp_tool(name="get_pull_request_setting", description="Get pull request setting")
    def get_pull_request_setting(self):
        """Retrieve default pull request setting."""
        return giton_get("/~api/settings/pull-request")

    @mcp_tool(name="get_security_setting", description="Get security setting")
    def get_security_setting(self):
        """Retrieve security configuration."""
        return giton_get("/~api/settings/security")

    @mcp_tool(name="get_ssh_setting", description="Get SSH setting")
    def get_ssh_setting(self):
        """Retrieve SSH configuration."""
        return giton_get("/~api/settings/ssh")

    @mcp_tool(name="get_contributed_settings", description="Get contributed settings")
    def get_contributed_settings(self):
        """Retrieve contributed settings."""
        return giton_get("/~api/settings/contributed-settings")

    @mcp_tool(name="set_system_setting", description="Set system setting")
    def set_system_setting(self, json_body: Dict):
        """Update global system setting."""
        return giton_post("/~api/settings/system", json_body)

    @mcp_tool(name="set_authenticator", description="Set authenticator setting")
    def set_authenticator(self, json_body: Dict):
        """Update authenticator configuration."""
        return giton_post("/~api/settings/authenticator", json_body)

    @mcp_tool(name="set_backup_setting", description="Set backup setting")
    def set_backup_setting(self, json_body: Dict):
        """Update backup configuration."""
        return giton_post("/~api/settings/backup", json_body)

    @mcp_tool(name="set_build_setting", description="Set build setting")
    def set_build_setting(self, json_body: Dict):
        """Update build configuration."""
        return giton_post("/~api/settings/build", json_body)

    @mcp_tool(name="set_groovy_scripts", description="Set groovy scripts setting")
    def set_groovy_scripts(self, json_body: Dict):
        """Update groovy scripts configuration."""
        return giton_post("/~api/settings/groovy-scripts", json_body)

    @mcp_tool(name="set_issue_setting", description="Set issue setting")
    def set_issue_setting(self, json_body: Dict):
        """Update issue configuration."""
        return giton_post("/~api/settings/issue", json_body)

    @mcp_tool(name="set_job_executors", description="Set job executors setting")
    def set_job_executors(self, json_body: Dict):
        """Update job executors configuration."""
        return giton_post("/~api/settings/job-executors", json_body)

    @mcp_tool(name="set_mail_service", description="Set mail service setting")
    def set_mail_service(self, json_body: Dict):
        """Update mail service configuration."""
        return giton_post("/~api/settings/mail-service", json_body)

    @mcp_tool(name="set_service_desk_setting", description="Set service desk setting")
    def set_service_desk_setting(self, json_body: Dict):
        """Update service desk configuration."""
        return giton_post("/~api/settings/service-desk", json_body)

    @mcp_tool(name="set_notification_template_setting", description="Set notification template setting")
    def set_notification_template_setting(self, json_body: Dict):
        """Update notification template configuration."""
        return giton_post("/~api/settings/notification-template", json_body)

    @mcp_tool(name="set_project_setting", description="Set project setting")
    def set_project_setting(self, json_body: Dict):
        """Update default project setting."""
        return giton_post("/~api/settings/project", json_body)

    @mcp_tool(name="set_pull_request_setting", description="Set pull request setting")
    def set_pull_request_setting(self, json_body: Dict):
        """Update default pull request setting."""
        return giton_post("/~api/settings/pull-request", json_body)

    @mcp_tool(name="set_security_setting", description="Set security setting")
    def set_security_setting(self, json_body: Dict):
        """Update security configuration."""
        return giton_post("/~api/settings/security", json_body)

    @mcp_tool(name="set_ssh_setting", description="Set SSH setting")
    def set_ssh_setting(self, json_body: Dict):
        """Update SSH configuration."""
        return giton_post("/~api/settings/ssh", json_body)

    @mcp_tool(name="set_contributed_settings", description="Set contributed settings")
    def set_contributed_settings(self, json_body: Dict):
        """Update contributed settings."""
        return giton_post("/~api/settings/contributed-settings", json_body)
