def create_application(profile: dict, scheme_name: str) -> dict:
    """
    Create a draft application for a government scheme.

    This only prepares the application data.
    It does not submit the application to the government.
    """

    application = {
        "scheme_name": scheme_name,
        "applicant": {
            "name": profile.get("name"),
            "age": profile.get("age"),
            "gender": profile.get("gender"),
            "state": profile.get("state"),
            "district": profile.get("district"),
            "phone": profile.get("phone")
        },
        "income": profile.get("income"),
        "occupation": profile.get("occupation"),
        "status": "Draft"
    }

    return application