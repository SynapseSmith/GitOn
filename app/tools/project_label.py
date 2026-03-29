from typing import Union, Annotated, Dict
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class ProjectLabel(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @mcp_tool(name="add_project_label", description="Add a label to a project")
    def add_project_label(self, json_body: Dict):
        """Create a new project-label association."""
        return giton_post("/~api/project-labels", json_body)

    @mcp_tool(name="remove_project_label", description="Remove a label from a project")
    def remove_project_label(
        self,
        project_label_id: Annotated[Union[int, str], "Project label ID"]
    ):
        """Delete a project-label association."""
        plid = quote(str(project_label_id), safe="")
        return giton_post(f"/~api/project-labels/{plid}", project_label_id)
