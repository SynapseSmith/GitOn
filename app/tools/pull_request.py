import os
from typing import Optional, Union, Literal
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post


class PullRequest(MCPMixin):
    def __init__(self, base_url: Optional[str] = None):
        self._base_url = base_url or os.getenv("giton_url")
        if not self._base_url:
            raise EnvironmentError("giton_url env is not set")

    @staticmethod
    def _rid(request_id: Union[int, str]) -> str:
        # safety for path segment
        return quote(str(request_id), safe="")

    @mcp_tool(name="get_pull_request_info", description="Get pull request basic info")
    def get_pull_request_info(self, request_id: Union[int, str]):
        rid = self._rid(request_id)
        return giton_get(f"/~api/pulls/{rid}")

    @mcp_tool(name="get_pull_request_labels", description="Get labels of a pull request")
    def get_pull_request_labels(self, request_id: Union[int, str]):
        rid = self._rid(request_id)
        return giton_get(f"/~api/pulls/{rid}/labels")

    @mcp_tool(name="get_merge_preview", description="Get merge preview of a pull request")
    def get_merge_preview(self, request_id: Union[int, str]):
        rid = self._rid(request_id)
        return giton_get(f"/~api/pulls/{rid}/merge-preview")

    @mcp_tool(name="get_pull_request_assignments", description="Get assignments of a pull request")
    def get_pull_request_assignments(self, request_id: Union[int, str]):
        rid = self._rid(request_id)
        return giton_get(f"/~api/pulls/{rid}/assignments")

    @mcp_tool(name="get_pull_request_comments", description="Get comments on a pull request")
    def get_pull_request_comments(self, request_id: Union[int, str]):
        rid = self._rid(request_id)
        return giton_get(f"/~api/pulls/{rid}/comments")

    @mcp_tool(name="get_pull_request_watches", description="Get watches of a pull request")
    def get_pull_request_watches(self, request_id: Union[int, str]):
        rid = self._rid(request_id)
        return giton_get(f"/~api/pulls/{rid}/watches")

    @mcp_tool(name="get_pull_request_query_basic_info", description="Get basic info of a pull request")
    def get_pull_request_query_basic_info(self, request_id: Union[int, str]):
        rid = self._rid(request_id)
        return giton_get(f"/~api/pulls/{rid}/query_basic_info")

    @mcp_tool(name="create_pull_request", description="Create a new pull request")
    def create_pull_request(self,
                            target_project_id: int,
                            source_project_id: int,
                            target_branch: str,
                            source_branch: str,
                            title: str,
                            description: str,
                            merge_strategy: Literal[
                                "CREATE_MERGE_COMMIT",
                                "CREATE_MERGE_COMMIT_IF_NECESSARY",
                                "SQUASH_SOURCE_BRANCH_COMMITS",
                                "REBASE_SOURCE_BRANCH_COMMITS"
                            ] = "CREATE_MERGE_COMMIT",
                            reviewer_ids: Optional[list[int]] = None,
                            assignee_ids: Optional[list[int]] = None,):

        # validation
        missing = [k for k, v in {
            "target_project_id": target_project_id,
            "source_project_id": source_project_id,
            "target_branch": target_branch,
            "source_branch": source_branch,
            "title": title
        }.items() if not v]

        if missing:
            return {"error": f"Missing required fields: {', '.join(missing)}"}

        json_body = {
            "target_project_id": target_project_id,
            "source_project_id": source_project_id,
            "target_branch": target_branch,
            "source_branch": source_branch,
            "title": title,
            "description": description,
            "merge_strategy": merge_strategy,
            "reviewer_ids": reviewer_ids or [],
            "assignee_ids": assignee_ids or [],
        }

        return giton_post(f"/~api/pulls", json_body)

    @mcp_tool(name="set_pull_request_title", description="Update title of a pull request")
    def set_pull_request_title(self,
                               request_id: Union[int, str],
                               title: str):
        rid = self._rid(request_id)
        json_body = title
        return giton_post(f"~api/pulls/{rid}/title", json_body)

    @mcp_tool(name="set_pull_request_description", description="Update pull request description")
    def set_pull_request_description(self, request_id: Union[int, str], description: str):
        rid = self._rid(request_id)
        json_body = description
        return giton_post(f"~api/pulls/{rid}/description", json_body)

    @mcp_tool(name="set_merge_strategy_pull_request", description="Update pull request merge strategy")
    def set_merge_strategy_pull_request(self,
                                        request_id: Union[int, str],
                                        merge_strategy: Literal[
                                            "CREATE_MERGE_COMMIT",
                                            "CREATE_MERGE_COMMIT_IF_NECESSARY",
                                            "SQUASH_SOURCE_BRANCH_COMMITS",
                                            "REBASE_SOURCE_BRANCH_COMMITS"
                                        ]):
        rid = self._rid(request_id)
        json_body = merge_strategy
        return giton_post(f"~api/pulls/{rid}/merge-strategy", json_body)

    @mcp_tool(name="reopen_pull_request", description="Reopen a closed pull request")
    def reopen_pull_request(self,
                            request_id: Union[int, str],
                            message: str):
        rid = self._rid(request_id)
        return giton_post(f"~api/pulls/{rid}/reopen", message)

    @mcp_tool(name="discard_pull_request", description="Discard (abandon) a pull request")
    def discard_pull_request(self,
                             request_id: Union[int, str],
                             message: str):
        rid = self._rid(request_id)
        return giton_post(f"~api/pulls/{rid}/discard", message)

    @mcp_tool(name="merge_pull_request", description="Merge a pull request")
    def merge_pull_request(self,
                           request_id: Union[int, str],
                           message: str):
        rid = self._rid(request_id)
        return giton_post(f"~api/pulls/{rid}/merge", message)

    @mcp_tool(name="delete_source_branch", description="Delete the source branch of a pull request")
    def delete_source_branch(self,
                             request_id: Union[int, str],
                             message: str):
        rid = self._rid(request_id)
        return giton_post(f"~api/pulls/{rid}/delete-source-branch", message)

    @mcp_tool(name="restore_source_branch", description="Restore the source branch of a pull request")
    def restore_source_branch(self,
                              request_id: Union[int, str],
                              message: str):
        rid = self._rid(request_id)
        return giton_post(f"~api/pulls/{rid}/restore-source-branch", message)

    @mcp_tool(name="delete_pull_request", description="Delete a pull request")
    def delete_pull_request(self, request_id: Union[int, str]):
        rid = self._rid(request_id)
        return giton_post(f"~api/pulls/{rid}", request_id)