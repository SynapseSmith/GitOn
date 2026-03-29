import pkgutil
import importlib
import inspect

from fastmcp import FastMCP
from fastmcp.contrib.mcp_mixin import MCPMixin
import app.tools  # package containing all tool modules

mcp = FastMCP("Giton MCP Server")

# Dynamically register all MCPMixin subclasses in app.tools
for finder, module_name, ispkg in pkgutil.iter_modules(app.tools.__path__):
    module = importlib.import_module(f"app.tools.{module_name}")
    for _, member in inspect.getmembers(module, inspect.isclass):
        if issubclass(member, MCPMixin) and member is not MCPMixin:
            member().register_tools(mcp)

if __name__ == "__main__":
    mcp.run()
