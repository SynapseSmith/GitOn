from typing import Union, Optional, Annotated, List
from urllib.parse import quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class AgentToken(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _tid(token_id: Union[int, str]) -> str:
        """Encode the agent token ID for URL path."""
        return quote(str(token_id), safe="")

    @mcp_tool(name="get_agent_for_token", description="Get agent for a token")
    def get_agent_for_token(
        self,
        token_id: Annotated[Union[int, str], "Agent token ID"]
    ):
        """Retrieve the agent associated with a token."""
        tid = self._tid(token_id)
        return giton_get(f"/~api/agent-tokens/{tid}/agent")

    @mcp_tool(name="get_agent_token", description="Get a token by ID")
    def get_agent_token(
        self,
        token_id: Annotated[Union[int, str], "Agent token ID"]
    ):
        """Retrieve an agent token."""
        tid = self._tid(token_id)
        return giton_get(f"/~api/agent-tokens/{tid}")

    @mcp_tool(name="query_agent_tokens", description="Query agent tokens")
    def query_agent_tokens(
        self,
        value: Annotated[Optional[str], "Filter by token value"] = None,
        offset: Annotated[Optional[int], "Offset"] = None,
        count: Annotated[Optional[int], "Maximum items"] = None
    ):
        """List or filter agent tokens."""
        params = []
        if value is not None:
            params.append(f"value={quote(str(value))}")
        if offset is not None:
            params.append(f"offset={offset}")
        if count is not None:
            params.append(f"count={count}")
        endpoint = "/~api/agent-tokens"
        if params:
            endpoint += "?" + "&".join(params)
        return giton_get(endpoint)

    @mcp_tool(name="create_agent_token", description="Create a new agent token")
    def create_agent_token(self, json_body: dict):
        """Create an agent token."""
        return giton_post("/~api/agent-tokens", json_body)

    @mcp_tool(name="delete_agent_token", description="Delete an agent token")
    def delete_agent_token(
        self,
        token_id: Annotated[Union[int, str], "Agent token ID"]
    ):
        """Delete an agent token."""
        tid = self._tid(token_id)
        return giton_post(f"/~api/agent-tokens/{tid}", token_id)
