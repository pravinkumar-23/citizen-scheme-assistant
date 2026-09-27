import json
from mcp.server.fastmcp import FastMCP
from mcp_server.eligibility import check_eligibility
from mcp_server.documents import get_required_documents
from mcp_server.application import create_application
from tools.tavily_search import search_government_information

# ============================================================
# Create MCP Server
# ============================================================

mcp = FastMCP("Citizen Scheme Assistant")


# ============================================================
# Eligibility Tool
# ============================================================

@mcp.tool()
def check_citizen_eligibility(profile: dict) -> dict:
    """
    Check the citizen profile against available schemes.

    Returns potential scheme matches based on the
    available eligibility criteria.
    """

    return check_eligibility(profile)


# ============================================================
# Documents Tool
# ============================================================

@mcp.tool()
def get_scheme_documents(scheme_name: str) -> str:
    """
    Return the documents required for a scheme.
    """

    documents = get_required_documents(
        scheme_name
    )

    return json.dumps(documents)


# ============================================================
# Application Tool
# ============================================================

@mcp.tool()
def create_scheme_application(
    profile: dict,
    scheme_name: str
) -> dict:
    """
    Create a draft application for a scheme.

    This only prepares the application.
    It does not submit the application.
    """

    return create_application(
        profile,
        scheme_name
    )


# ============================================================
# Government Information Search Tool
# ============================================================

@mcp.tool()
def search_government_scheme_information(query: str) -> list:
    """
    Search for government scheme information using Tavily.

    Returns relevant government information and source URLs.
    """

    return search_government_information(query)


# ============================================================
# Start MCP Server
# ============================================================

if __name__ == "__main__":

    mcp.run()