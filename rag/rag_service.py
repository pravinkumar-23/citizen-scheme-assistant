from rag.retriever import search_scheme_information


SCHEME_SOURCES = {

    "PM-KISAN":
        "pm_kisan.pdf",

    "PM-KUSUM":
        "pm_kusum.pdf",

    "PM SVANidhi":
        "pm_svanidhi.pdf",

    "PM Vishwakarma":
        "pm_vishwakarma.pdf",

    "PMGBY":
        "pmgby.pdf"
}


def get_scheme_information(
    scheme_name,
    question
):

    source = SCHEME_SOURCES.get(
        scheme_name
    )

    query = f"{scheme_name} {question}"

    results = search_scheme_information(
        query,
        top_k=3,
        source=source
    )

    return results