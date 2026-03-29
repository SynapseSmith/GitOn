from typing import Union, Optional, List, Annotated
from urllib.parse import quote_plus, quote
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool
from app.utils.http_util import giton_get, giton_post, giton_url

class Agent(MCPMixin):
    def __init__(self):
        self.base_url = giton_url

    @staticmethod
    def _aid(agent_id: Union[int, str]) -> str:
        """Encode the agent ID for URL path."""
        return quote(str(agent_id), safe="")

    @mcp_tool(name="get_agent", description="Get Agent")
    def get_agent(
        self,
        agent_id: Annotated[Union[int, str], "Agent ID"]
    ):
        """Retrieve details of a specific agent."""
        aid = self._aid(agent_id)
        return giton_get(f"/~api/agents/{aid}")

    @mcp_tool(name="get_agent_attributes", description="Get Attributes of an Agent")
    def get_agent_attributes(
        self,
        agent_id: Annotated[Union[int, str], "Agent ID"]
    ):
        """List custom attributes for an agent."""
        aid = self._aid(agent_id)
        return giton_get(f"/~api/agents/{aid}/attributes")

    @mcp_tool(name="query_agents", description="Query Agents")
    def query_agents(
        self,
        query: Annotated[Optional[str], "Filter expression"] = None,
        offset: Annotated[Optional[int], "Offset"] = None,
        count: Annotated[Optional[int], "Max items"] = None
    ):
        """Search and paginate agents."""
        params: List[str] = []
        if query is not None:
            params.append(f"query={quote_plus(query)}")
        if offset is not None:
            params.append(f"offset={offset}")
        if count is not None:
            params.append(f"count={count}")
        endpoint = "/~api/agents"
        if params:
            endpoint += "?" + "&".join(params)
        return giton_get(endpoint)

    @mcp_tool(name="update_agent_attributes", description="Update Attributes of an Agent")
    def update_agent_attributes(
        self,
        agent_id: Annotated[Union[int, str], "Agent ID"],
        attributes: Annotated[dict, "Attributes key/value map"]
    ):
        """Modify attributes of an agent."""
        aid = self._aid(agent_id)
        return giton_post(f"/~api/agents/{aid}/attributes", attributes)
