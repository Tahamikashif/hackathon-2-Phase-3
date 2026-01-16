import asyncio
from .task_operations import (
    add_task_tool,
    list_tasks_tool,
    complete_task_tool,
    delete_task_tool,
    update_task_tool
)


# Mock MCPServer class since the actual package isn't available
class MCPServer:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.tools = []

    def register_tool(self, tool):
        self.tools.append(tool)
        print(f"Registered tool: {tool.name}")

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def serve(self):
        print(f"MCP Server {self.name} v{self.version} is serving with {len(self.tools)} tools")


# Initialize the MCPServer
server = MCPServer(
    name="Todo Chatbot MCP Server",
    version="1.0.0"
)


# Register all tools with the server
server.register_tool(add_task_tool)
server.register_tool(list_tasks_tool)
server.register_tool(complete_task_tool)
server.register_tool(delete_task_tool)
server.register_tool(update_task_tool)


async def main():
    """Main function to start the MCP server"""
    async with server.context() as ctx:
        await ctx.serve()


if __name__ == "__main__":
    asyncio.run(main())