from typing import Union, Dict, Optional, List, Annotated
from urllib.parse import quote, quote_plus
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Repository(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _rid(request_id: Union[int, str]) -> str:
        """Encode project or request identifier for URL path."""
        return quote(str(request_id), safe="")

    @mcp_tool(name="get_branches", description="Get branches of a repository")
    def get_branches(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"]
    ):
        """List all branches in the given repository."""
        rid = self._rid(project_id)
        return giton_get(f"/~api/repositories/{rid}/branches")

    @mcp_tool(name="get_default_branch", description="Get default branch of a repository")
    def get_default_branch(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"]
    ):
        """Retrieve the default branch name for the repository."""
        rid = self._rid(project_id)
        return giton_get(f"/~api/repositories/{rid}/default-branch")

    @mcp_tool(name="set_default_branch", description="Set default branch of a repository")
    def set_default_branch(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        default_branch: Annotated[str, "Name of branch to set as default"]
    ):
        """Update the default branch for the repository."""
        rid = self._rid(project_id)
        return giton_post(f"/~api/repositories/{rid}/default-branch", default_branch)

    @mcp_tool(name="get_branch", description="Get a branch of a repository")
    def get_branch(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        branch: Annotated[str, "Branch name or pattern"]
    ):
        """Retrieve information about a specific branch."""
        rid = self._rid(project_id)
        branch_encoded = quote(branch, safe="")
        return giton_get(f"/~api/repositories/{rid}/branches/{branch_encoded}")

    @mcp_tool(name="create_branch", description="Create a new branch in a repository")
    def create_branch(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        new_branch: Annotated[str, "Name of the new branch"],
        base_revision: Annotated[str, "Revision or branch to base the new branch on"]
    ):
        """Create a new branch from specified base revision."""
        rid = self._rid(project_id)
        payload = {"newBranch": new_branch, "revision": base_revision}
        return giton_post(f"/~api/repositories/{rid}/branches", payload)

    @mcp_tool(name="delete_branch", description="Delete a branch from a repository")
    def delete_branch(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        branch: Annotated[str, "Branch name or pattern to delete"]
    ):
        """Remove a branch from the repository."""
        rid = self._rid(project_id)
        branch_encoded = quote(branch, safe="")
        return giton_post(f"/~api/repositories/{rid}/branches/{branch_encoded}")

    @mcp_tool(name="get_tags", description="Get tags of a repository")
    def get_tags(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"]
    ):
        """List all tags in the given repository."""
        rid = self._rid(project_id)
        return giton_get(f"/~api/repositories/{rid}/tags")

    @mcp_tool(name="get_tag", description="Get a tag of a repository")
    def get_tag(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        tag: Annotated[str, "Tag name or pattern"]
    ):
        """Retrieve information about a specific tag."""
        rid = self._rid(project_id)
        tag_encoded = quote(tag, safe="")
        return giton_get(f"/~api/repositories/{rid}/tags/{tag_encoded}")

    @mcp_tool(name="create_tag", description="Create a new tag in a repository")
    def create_tag(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        tag_name: Annotated[str, "Name of the new tag"],
        target_revision: Annotated[str, "Revision or commit ID to tag"]
    ):
        """Create a new tag for specified revision."""
        rid = self._rid(project_id)
        payload = {"tagName": tag_name, "revision": target_revision}
        return giton_post(f"/~api/repositories/{rid}/tags", payload)

    @mcp_tool(name="delete_tag", description="Delete a tag from a repository")
    def delete_tag(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        tag: Annotated[str, "Tag name or pattern to delete"]
    ):
        """Remove a tag from the repository."""
        rid = self._rid(project_id)
        tag_encoded = quote(tag, safe="")
        return giton_post(f"/~api/repositories/{rid}/tags/{tag_encoded}")

    @mcp_tool(name="query_commits", description="Query commits in a repository")
    def query_commits(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        count: Annotated[int, "Maximum number of commits to return"],
        query: Annotated[Optional[str], "Query filter string"] = None,
        fields: Annotated[Optional[List[str]], "List of fields to include in results"] = None
    ):
        """Retrieve a list of commits based on filters."""
        rid = self._rid(project_id)
        params_list = []
        if query:
            params_list.append(("query", quote_plus(query)))
        if count is not None:
            params_list.append(("count", str(count)))
        if fields:
            for f in fields:
                params_list.append(("field", quote_plus(f)))
        endpoint = f"/~api/repositories/{rid}/commits"
        if params_list:
            query_str = "&".join(f"{k}={v}" for k, v in params_list)
            endpoint += f"?{query_str}"
        return giton_get(endpoint)

    @mcp_tool(name="get_commit", description="Get a commit in a repository")
    def get_commit(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        commit_hash: Annotated[str, "SHA or hash of the commit"]
    ):
        """Retrieve a specific commit by its hash."""
        rid = self._rid(project_id)
        commit_encoded = quote(commit_hash, safe="")
        return giton_get(f"/~api/repositories/{rid}/commits/{commit_encoded}")

    @mcp_tool(name="get_directory", description="Get a directory in a repository")
    def get_directory(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        revision_and_directory: Annotated[str, "Revision and directory path"]
    ):
        """List contents of a directory at a specific revision."""
        rid = self._rid(project_id)
        rev_dir = quote(revision_and_directory, safe="")
        return giton_get(f"/~api/repositories/{rid}/directories/{rev_dir}")

    @mcp_tool(name="get_file", description="Get a file in a repository")
    def get_file(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        revision_and_file: Annotated[str, "Revision and file path"]
    ):
        """Retrieve file content at a specific revision."""
        rid = self._rid(project_id)
        rev_file = quote(revision_and_file, safe="")
        return giton_get(f"/~api/repositories/{rid}/files/{rev_file}")

    @mcp_tool(name="edit_file", description="Edit a file in a repository")
    def edit_file(
        self,
        project_id: Annotated[Union[int, str], "Repository project ID"],
        branch: Annotated[str, "Branch name"],
        file_path: Annotated[str, "File path relative to repository root"],
        content: Annotated[str, "Updated file content"],
        commit_message: Annotated[str, "Commit message for the edit"]
    ):
        """Apply edits to a file in the repository."""
        rid = self._rid(project_id)
        bf = quote(f"{branch}/{file_path}", safe="")
        payload = {"content": content, "message": commit_message}
        return giton_post(f"/~api/repositories/{rid}/files/{bf}", payload)
