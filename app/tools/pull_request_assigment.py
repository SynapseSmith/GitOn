from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url
from typing import Optional, Literal, Union
from urllib.parse import quote

class PullRequestAssigment(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _rid(request_id: Union[int, str]) -> str:
        # safety for path segment
        return quote(str(request_id), safe="")

    @mcp_tool(name="get_pull_request_assignment", description="Get pull request assignments")
    def get_pull_request_assignments(self, assignment_id: Union[int, str]):
        rid = self._rid(assignment_id)
        return giton_get(f"/~api/pull-request-assignments/{rid}")

    @mcp_tool(name="create_pull_request_assignment", description="Create pull request assignment")
    def create_pull_request_assignment(self, user_id: int, request_id: int):
        missing = [k for k, v in {
            "user_id": user_id,
            "request_id": request_id
        }.items() if not v]

        if missing:
            return {"error": f"Missing required fields: {', '.join(missing)}"}

        json_body = {
            "user_id": user_id,
            "request_id": request_id
        }

        return giton_post(f"/~api/pull-request-assignments", json_body)


    # -------------- 일단 이건 나중 확인 받고 구현 예정 ---------------- #
    @mcp_tool(name="delete_pull_request_assignment", description="Delete pull request assignment")
    def delete_pull_request_assignment(self, assignment_id: Union[int, str]):
        rid = self._rid(assignment_id)
        return