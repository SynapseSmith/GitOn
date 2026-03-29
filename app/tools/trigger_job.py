from typing import Optional, Annotated, Dict
from urllib.parse import quote_plus
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class TriggerJob(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @mcp_tool(name="trigger_job_get", description="Trigger job via GET")
    def trigger_job_get(
        self,
        project: Annotated[Optional[str], "Project name"] = None,
        branch: Annotated[Optional[str], "Branch name"] = None,
        tag: Annotated[Optional[str], "Tag name"] = None,
        job: Annotated[Optional[str], "Job name"] = None,
        access_token: Annotated[Optional[str], "Access token"] = None
    ):
        """Trigger a job via GET with optional query parameters."""
        params = []
        if project is not None: params.append(f"project={quote_plus(project)}")
        if branch is not None: params.append(f"branch={quote_plus(branch)}")
        if tag is not None: params.append(f"tag={quote_plus(tag)}")
        if job is not None: params.append(f"job={quote_plus(job)}")
        if access_token is not None: params.append(f"access-token={quote_plus(access_token)}")
        endpoint = "/~api/trigger-job"
        if params: endpoint += "?" + "&".join(params)
        return giton_get(endpoint)

    @mcp_tool(name="trigger_job_post", description="Trigger job via POST")
    def trigger_job_post(
        self,
        project: Annotated[Optional[str], "Project name"] = None,
        branch: Annotated[Optional[str], "Branch name"] = None,
        tag: Annotated[Optional[str], "Tag name"] = None,
        job: Annotated[Optional[str], "Job name"] = None,
        access_token: Annotated[Optional[str], "Access token"] = None
    ):
        """Trigger a job via POST with optional form parameters."""
        params = {}
        if project is not None: params["project"] = project
        if branch is not None: params["branch"] = branch
        if tag is not None: params["tag"] = tag
        if job is not None: params["job"] = job
        if access_token is not None: params["access-token"] = access_token
        return giton_post("/~api/trigger-job", params)
