import os
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

TARGET_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "D:\\agents-workshop")

toolset = McpToolset(
    connection_params=StdioConnectionParams(
        server_params = StdioServerParameters(
            command='npx',
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                # Replace with a valid absolute path on your system.
                # For example: "C:\\Users\\CSIT\\agent-workshop"
                # or use a dynamically constructed absolute path:
                TARGET_FOLDER_PATH,
            ],
        ),
    )
)

root_agent = LlmAgent(
    name='filesystem_assistant',
    model='gemini-2.5-flash',
    instruction='Help user interact with the local filesystem using available tools.',
    tools=[toolset], 
)