from mcp_server.schemes import SCHEMES


def get_required_documents(scheme_name: str) -> list:
    """
    Return the documents required for a scheme
    from the central scheme dataset.
    """

    for scheme in SCHEMES:

        if scheme["name"].lower().strip() == scheme_name.lower().strip():

            return scheme["documents"]

    return []