# app/tools/project_tool.py
from datetime import datetime
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post

class Project(MCPMixin):

    @mcp_tool(name="get_project", description="Get project info")  # 여기서 이름 지정
    def get_project(self, project_id: int):

        endpoint = f"/~api/projects/{project_id}"
        return giton_get(endpoint)

    @mcp_tool(name="get_project_id", description="Get project id")
    def get_project_id(self, path: str):
        endpoint = f"/~api/projects/ids/{path}"

        return giton_get(endpoint)

    @mcp_tool(name="get_labels", description="Get list of labels")
    def get_labels(self, project_id: int):

        endpoint = f"/~api/projects/{project_id}/labels"

        return giton_get(endpoint)

    @mcp_tool(name="get_project_list", description="Get project list by Query")
    def get_project_list(self, offset: int, count: int, query: str = None):

        endpoint = f"/~api/projects?offset={offset}&count={count}"
        if query:
            endpoint += f"&query={query}"

        return giton_get(endpoint)

    @mcp_tool(name="get_project_iterations", description="Get project iterations list by Query")
    def get_project_iterations(self,project_id: int,
                               offset: int,
                               count: int,
                               name: str = None,
                               start_before: datetime = None,
                               start_after: datetime = None,
                               due_before: datetime = None,
                               due_after: datetime = None,
                               closed:bool = None):

        endpoint = f"/~api/projects/{project_id}/iterations?offset={offset}&count={count}"

        if name:
            endpoint += f"&name={quote(name)}"
        if start_before:
            endpoint += f"&startBefore={quote(start_before.isoformat())}"
        if start_after:
            endpoint += f"&startAfter={quote(start_after.isoformat())}"
        if due_before:
            endpoint += f"&dueBefore={quote(due_before.isoformat())}"
        if due_after:
            endpoint += f"&dueAfter={quote(due_after.isoformat())}"
        if closed is not None:
            endpoint += f"&closed={str(closed).lower()}"

        return giton_get(endpoint)

    @mcp_tool(name="create_project", description="Create a new project")
    def create_project(
            self,
            name: str,
            parent_id: int = None,
            key: str = None,
            forked_from_id: int = None,
            description: str = None,
            code_management: bool = True,
            pack_management: bool = True,
            issue_management: bool = True,
            time_tracking: bool = True,
            service_desk_email: str = None,
            git_window_memory: int = None,
            git_pack_size_limit: str = None,
            git_threads: int = None,
            git_window: int = None,
            analysis_files: str = None
    ):

        json_body = {
            "parentId": parent_id,
            "forkedFromId": forked_from_id,
            "name": name,
            "key": key,
            "description": description,
            "codeManagement": code_management,
            "packManagement": pack_management,
            "issueManagement": issue_management,
            "timeTracking": time_tracking,
            "serviceDeskEmailAddress": service_desk_email,
            "gitPackConfig": {
                "windowMemory": str(git_window_memory),
                "packSizeLimit": git_pack_size_limit,
                "threads": str(git_threads),
                "window": str(git_window)
            },
            "codeAnalysisSetting": {
                "analysisFiles": analysis_files
            }
        }
        json_body = {k: quote(v)  for k, v in json_body.items() if v is not None}

        return giton_post("/~api/projects", json_body)

    @mcp_tool(name="update_project", description="Update project")
    def update_project(
            self,
            project_id: int,
            name: str,
            parent_id: int = None,
            key: str = None,
            forked_from_id: int = None,
            description: str = None,
            code_management: bool = True,
            pack_management: bool = True,
            issue_management: bool = True,
            time_tracking: bool = True,
            service_desk_email: str = None,
            git_window_memory: int = None,
            git_pack_size_limit: str = None,
            git_threads: int = None,
            git_window: int = None,
            analysis_files: str = None
    ):

        json_body = {
            "parentId": parent_id,
            "forkedFromId": forked_from_id,
            "name": name,
            "key": key,
            "description": description,
            "codeManagement": code_management,
            "packManagement": pack_management,
            "issueManagement": issue_management,
            "timeTracking": time_tracking,
            "serviceDeskEmailAddress": service_desk_email,
            "gitPackConfig": {
                "windowMemory": str(git_window_memory),
                "packSizeLimit": git_pack_size_limit,
                "threads": str(git_threads),
                "window": str(git_window)
            },
            "codeAnalysisSetting": {
                "analysisFiles": analysis_files
            }
        }
        json_body = {k: quote(v)  for k, v in json_body.items() if v is not None}

        return giton_post(f"/~api/projects/{project_id}", json_body)
