import os

from dotenv import load_dotenv
from tavily import TavilyClient


# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()


# ============================================================
# Get Tavily API Key
# ============================================================

TAVILY_API_KEY = os.getenv(
    "TAVILY_API_KEY"
)


# ============================================================
# Validate API Key
# ============================================================

if not TAVILY_API_KEY:

    raise ValueError(
        "TAVILY_API_KEY was not found in the .env file."
    )


# ============================================================
# Create Tavily Client
# ============================================================

tavily_client = TavilyClient(
    api_key=TAVILY_API_KEY
)


# ============================================================
# Search Government Information
# ============================================================

def search_government_information(
    query: str,
    max_results: int = 5
):
    """
    Search the web for government scheme information.

    Tavily is used to find potentially updated information
    such as:

    - Newly announced schemes
    - Updated eligibility rules
    - Changed deadlines
    - Government announcements
    - Official scheme information

    Official government sources are preferred.

    Final eligibility is always determined by the
    concerned government authority.
    """

    # --------------------------------------------------------
    # Build Search Query
    # --------------------------------------------------------

    search_query = (
        f"{query} "
        "government scheme official "
        "site:gov.in OR site:nic.in"
    )


    # --------------------------------------------------------
    # Perform Tavily Search
    # --------------------------------------------------------

    response = tavily_client.search(
        query=search_query,
        search_depth="advanced",
        max_results=max_results
    )


    # --------------------------------------------------------
    # Separate Official and Other Sources
    # --------------------------------------------------------

    official_results = []

    other_results = []


    # --------------------------------------------------------
    # Process Search Results
    # --------------------------------------------------------

    for result in response.get(
        "results",
        []
    ):

        url = result.get(
            "url",
            ""
        )


        # ----------------------------------------------------
        # Create Result Object
        # ----------------------------------------------------

        result_data = {

            "title": result.get(
                "title"
            ),

            "url": url,

            "content": result.get(
                "content"
            ),

            "official": False
        }


        # ----------------------------------------------------
        # Check Official Government Domain
        # ----------------------------------------------------

        url_lower = url.lower()


        if (
            ".gov.in" in url_lower
            or
            ".nic.in" in url_lower
        ):

            result_data["official"] = True

            official_results.append(
                result_data
            )

        else:

            other_results.append(
                result_data
            )


    # --------------------------------------------------------
    # Prefer Official Sources
    # --------------------------------------------------------

    results = (
        official_results
        + other_results
    )


    # --------------------------------------------------------
    # Limit Number of Results
    # --------------------------------------------------------

    return results[:max_results]