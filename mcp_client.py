
import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def call_mcp_tool(tool_name, arguments):

    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_server.server"]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                tool_name,
                arguments=arguments
            )

            # Extract the actual text from the MCP response
            if result.content:
                return result.content[0].text

            return "No response received from the MCP server."


def check_eligibility(profile):

    return asyncio.run(
        call_mcp_tool(
            "check_citizen_eligibility",
            {
                "profile": profile
            }
        )
    )


def get_documents(scheme_name):

    return asyncio.run(
        call_mcp_tool(
            "get_scheme_documents",
            {
                "scheme_name": scheme_name
            }
        )
    )


def create_application(profile, scheme_name):

    return asyncio.run(
        call_mcp_tool(
            "create_scheme_application",
            {
                "profile": profile,
                "scheme_name": scheme_name
            }
        )
    )

def search_government_information(query):

    return asyncio.run(
        call_mcp_tool(
            "search_government_scheme_information",
            {
                "query": query
            }
        )
    )