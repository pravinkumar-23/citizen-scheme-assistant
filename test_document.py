from mcp_server.server import search_government_scheme_information


print("Testing Tavily MCP tool...\n")

query = "PM-KISAN latest eligibility"

results = search_government_scheme_information(query)

print("Query:", query)
print("Number of results:", len(results))
print("\nResults:\n")

for i, result in enumerate(results, start=1):

    print(f"--- Result {i} ---")
    print("Title:", result.get("title"))
    print("URL:", result.get("url"))
    print("Content:", result.get("content"))
    print()