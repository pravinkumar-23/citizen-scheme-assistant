from mcp_server.schemes import SCHEMES

try:
    from rag.rag_service import get_scheme_information
except Exception:
    get_scheme_information = None


def is_missing(value):
    return value is None or value == ""


def check_condition(profile, rules, reasons):

    # --------------------------------------------------
    # Age
    # --------------------------------------------------

    age = profile.get("age")

    if "minimum_age" in rules:

        if is_missing(age):
            return False

        if age < rules["minimum_age"]:
            return False

        reasons.append(
            f"Age is {age}, which meets the minimum age of "
            f"{rules['minimum_age']}"
        )

    if "maximum_age" in rules:

        if is_missing(age):
            return False

        if age > rules["maximum_age"]:
            return False

        reasons.append(
            f"Age is {age}, which is within the maximum age of "
            f"{rules['maximum_age']}"
        )

    # --------------------------------------------------
    # Income
    # --------------------------------------------------

    income = profile.get("income")

    if "maximum_income" in rules:

        if is_missing(income):
            return False

        if income > rules["maximum_income"]:
            return False

        reasons.append(
            f"Annual income is ₹{income:,.0f}, within the "
            f"₹{rules['maximum_income']:,.0f} limit"
        )

    # --------------------------------------------------
    # Occupation
    # --------------------------------------------------

    if "occupation" in rules:

        occupation = profile.get("occupation")

        if is_missing(occupation):
            return False

        allowed = [
            x.lower()
            for x in rules["occupation"]
        ]

        if occupation.lower() not in allowed:
            return False

        reasons.append(
            f"Occupation is {occupation}"
        )

    # --------------------------------------------------
    # Gender
    # --------------------------------------------------

    if "gender" in rules:

        gender = profile.get("gender")

        if is_missing(gender):
            return False

        allowed = [
            x.lower()
            for x in rules["gender"]
        ]

        if gender.lower() not in allowed:
            return False

        reasons.append(
            f"Gender is {gender}"
        )

    # --------------------------------------------------
    # State
    # --------------------------------------------------

    if "states" in rules:

        state = profile.get("state")

        if is_missing(state):
            return False

        allowed = [
            x.lower()
            for x in rules["states"]
        ]

        if state.lower() not in allowed:
            return False

        reasons.append(
            f"State is {state}"
        )

    # --------------------------------------------------
    # Landholding
    # --------------------------------------------------

    if "minimum_landholding" in rules:

        landholding = profile.get("landholding")

        if is_missing(landholding):
            return False

        if landholding < rules["minimum_landholding"]:
            return False

        reasons.append(
            f"Landholding is {landholding} acres"
        )

    # --------------------------------------------------
    # Urban / Rural
    # --------------------------------------------------

    if "urban_rural" in rules:

        location = profile.get("urban_rural")

        if is_missing(location):
            return False

        allowed = [
            x.lower()
            for x in rules["urban_rural"]
        ]

        if location.lower() not in allowed:
            return False

        reasons.append(
            f"Location type is {location}"
        )

    # --------------------------------------------------
    # Street Vendor
    # --------------------------------------------------

    if rules.get("street_vendor") is True:

        if profile.get("street_vendor") is not True:
            return False

        reasons.append(
            "Applicant is a street vendor"
        )

    # --------------------------------------------------
    # Bank Account
    # --------------------------------------------------

    if rules.get("bank_account") is True:

        if profile.get("bank_account") is not True:
            return False

        reasons.append(
            "Applicant has a bank account"
        )

    # --------------------------------------------------
    # Income Taxpayer
    # --------------------------------------------------

    if rules.get("income_taxpayer") is False:

        if profile.get("income_taxpayer") is not False:
            return False

        reasons.append(
            "Applicant is not an income taxpayer"
        )

    # --------------------------------------------------
    # House Ownership
    # --------------------------------------------------

    if rules.get("house_ownership") is False:

        if profile.get("house_ownership") is not False:
            return False

        reasons.append(
            "Applicant does not own a house"
        )

    # --------------------------------------------------
    # Existing LPG
    # --------------------------------------------------

    if rules.get("existing_lpg") is False:

        if profile.get("existing_lpg") is not False:
            return False

        reasons.append(
            "Applicant does not already have an LPG connection"
        )

    return True


def check_eligibility(profile):

    matches = []

    for scheme in SCHEMES:

        rules = scheme.get(
            "eligibility",
            {}
        )

        required_fields = scheme.get(
            "required_profile_fields",
            []
        )

        # --------------------------------------------------
        # Check required fields
        # --------------------------------------------------

        missing = False

        for field in required_fields:

            value = profile.get(field)

            if is_missing(value):
                missing = True
                break

        if missing:
            continue

        # --------------------------------------------------
        # Check rules
        # --------------------------------------------------

        reasons = []

        eligible = check_condition(
            profile,
            rules,
            reasons
        )

        if not eligible:
            continue

        # --------------------------------------------------
        # RAG information
        # --------------------------------------------------

        rag_information = []

        if get_scheme_information is not None:

            try:

                rag_information = get_scheme_information(
                    scheme["name"],
                    "eligibility benefits requirements"
                )

            except Exception:

                rag_information = []

        # --------------------------------------------------
        # Add match
        # --------------------------------------------------

        matches.append(
            {
                "scheme": scheme["name"],

                "description": scheme.get(
                    "description",
                    ""
                ),

                "benefits": scheme.get(
                    "benefits",
                    []
                ),

                "status": "potentially_eligible",

                "reasons": reasons,

                "official_source": scheme.get(
                    "official_source"
                ),

                "rag_information": rag_information
            }
        )

    # ------------------------------------------------------
    # Final response
    # ------------------------------------------------------

    return {
        "success": True,

        "matches": matches,

        "message": (
            "These are potential matches based on "
            "the available scheme criteria and "
            "government scheme information. "
            "Final eligibility is determined by "
            "the concerned government authority."
        )
    }