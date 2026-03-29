from typing import Optional, Union, Literal
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url
from urllib.parse import quote

class Issue(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _rid(request_id: Union[int, str]) -> str:
        return quote(str(request_id), safe="")

    @mcp_tool(name="get_issue", description="Get issue details by issue ID")
    def get_issue(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}")

    @mcp_tool(name="get_issue_fields", description="Get custom fields of an issue")
    def get_issue_fields(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/fields")

    @mcp_tool(name="get_issue_comments", description="Get issue comments of an issue")
    def get_issue_comments(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/comments")

    @mcp_tool(name="get_issue_works", description="Get issue works of an issue")
    def get_issue_works(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/works")

    @mcp_tool(name="get_issue_changes", description="Get issue changes of an issue")
    def get_issue_changes(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/changes")

    @mcp_tool(name="get_issue_iterations", description="Get issue iterations of an issue")
    def get_issue_iterations(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/iterations")

    @mcp_tool(name="get_issue_votes", description="Get issue votes of an issue")
    def get_issue_votes(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/votes")

    @mcp_tool(name="get_issue_watches", description="Get issue watches of an issue")
    def get_issue_watches(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/watches")

    @mcp_tool(name="get_issue_links", description="Get issue links of an issue")
    def get_issue_links(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/links")

    @mcp_tool(name="get_issue_pull_requests", description="Get pull requests of an issue")
    def get_issue_pull_requests(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/pulls")

    @mcp_tool(name="get_issue_commits", description="Get issue commits of an issue")
    def get_issue_commits(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_get(f"/~api/issues/{rid}/commits")

    @mcp_tool(name="query_issues", description="Query issues")
    def query_issues(self, params: dict = None):
        endpoint = "/~api/issues"
        if params:
            from urllib.parse import quote_plus
            query_str = "&".join(f"{quote_plus(str(k))}={quote_plus(str(v))}" for k,v in params.items())
            endpoint += f"?{query_str}"
        return giton_get(endpoint)

    @mcp_tool(name="create_issue", description="Create a new issue")
    def create_issue(self, json_body: dict):
        return giton_post("/~api/issues", json_body)

    @mcp_tool(name="set_title", description="Update issue title")
    def set_title(self, issue_id: Union[int, str], title: str):
        rid = self._rid(issue_id)
        return giton_post(f"/~api/issues/{rid}/title", title)

    @mcp_tool(name="set_description", description="Update issue description")
    def set_description(self, issue_id: Union[int, str], description: str):
        rid = self._rid(issue_id)
        return giton_post(f"/~api/issues/{rid}/description", description)

    @mcp_tool(name="set_confidential", description="Set issue confidential")
    def set_confidential(self, issue_id: Union[int, str], confidential: bool):
        rid = self._rid(issue_id)
        return giton_post(f"/~api/issues/{rid}/confidential", confidential)

    @mcp_tool(name="set_own_estimated_time", description="Set own estimated time of issue")
    def set_own_estimated_time(self, issue_id: Union[int, str], time: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_post(f"/~api/issues/{rid}/own-estimated-time", time)

    @mcp_tool(name="set_iterations", description="Set issue iterations")
    def set_iterations(self, issue_id: Union[int, str], iterations: list):
        rid = self._rid(issue_id)
        return giton_post(f"/~api/issues/{rid}/iterations", iterations)

    @mcp_tool(name="set_fields", description="Set issue fields")
    def set_fields(self, issue_id: Union[int, str], fields: dict):
        rid = self._rid(issue_id)
        return giton_post(f"/~api/issues/{rid}/fields", fields)

    @mcp_tool(name="transit_state", description="Transit issue state")
    def transit_state(self, issue_id: Union[int, str], state: str):
        rid = self._rid(issue_id)
        return giton_post(f"/~api/issues/{rid}/state-transitions", state)

    @mcp_tool(name="upload_attachment", description="Upload issue attachment")
    def upload_attachment(self, issue_id: Union[int, str], preferred_name: str, data: bytes):
        rid = self._rid(issue_id)
        endpoint = f"/~api/issues/{rid}/attachments/{quote(preferred_name, safe='')}"
        return giton_post(endpoint, data)

    @mcp_tool(name="delete_issue", description="Delete an issue")
    def delete_issue(self, issue_id: Union[int, str]):
        rid = self._rid(issue_id)
        return giton_post(f"/~api/issues/{rid}", issue_id)
