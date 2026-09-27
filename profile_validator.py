def get_missing_fields(profile):

    required_fields = {
        "age": "age",
        "income": "annual income",
        "occupation": "occupation",
        "state": "state"
    }

    missing = []

    for field, display_name in required_fields.items():

        value = profile.get(field)

        if value is None or value == "":
            missing.append(display_name)

    return missing


def get_scheme_missing_fields(profile, schemes):

    missing_fields = set()

    for scheme in schemes:

        required_fields = scheme.get(
            "required_profile_fields",
            []
        )

        for field in required_fields:

            value = profile.get(field)

            if value is None or value == "":
                missing_fields.add(field)

    return list(missing_fields)