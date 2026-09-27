import re


def extract_profile(message: str) -> dict:

    profile = {
        "name": None,
        "age": None,
        "gender": None,
        "state": None,
        "district": None,
        "phone": None,
        "income": None,
        "occupation": None,

        # Scheme-specific fields
        "landholding": None,
        "crop": None,
        "artisan_trade": None,
        "street_vendor": None,
        "business_status": None,
        "social_category": None,
        "urban_rural": None,
        "house_ownership": None,
        "family_status": None,
        "housing_condition": None,
        "household_status": None,
        "existing_lpg": None,
        "pregnancy_status": None,
        "employment_status": None,
        "bank_account": None,
        "income_taxpayer": None,
        "academic_merit": None,
        "course_type": None,
        "school_type": None,
        "higher_education": None
    }

    message_lower = message.lower()

    # ==================================================
    # AGE
    # ==================================================

    age_patterns = [
        r'\b(\d{1,3})\s*[-]?\s*year[- ]old\b',
        r'\b(\d{1,3})\s+years?\s+old\b',
        r'\baged\s+(\d{1,3})\b',
        r'\bage\s*(?:is|:)?\s*(\d{1,3})\b'
    ]

    for pattern in age_patterns:

        match = re.search(
            pattern,
            message,
            re.IGNORECASE
        )

        if match:
            profile["age"] = int(match.group(1))
            break

    # ==================================================
    # OCCUPATION
    # ==================================================

    occupations = [
        "street vendor",
        "self-employed",
        "self employed",
        "businesswoman",
        "businessman",
        "farmer",
        "student",
        "teacher",
        "worker",
        "employee",
        "engineer",
        "artisan"
    ]

    for occupation in occupations:

        if occupation in message_lower:

            if occupation == "businesswoman":
                profile["occupation"] = "businesswoman"

            elif occupation == "businessman":
                profile["occupation"] = "businessman"

            elif occupation in [
                "street vendor"
            ]:
                profile["occupation"] = "street vendor"

            elif occupation in [
                "self-employed",
                "self employed"
            ]:
                profile["occupation"] = "self-employed"

            else:
                profile["occupation"] = occupation

            break

    # ==================================================
    # STATE
    # ==================================================

    states = [
        "Tamil Nadu",
        "Kerala",
        "Karnataka",
        "Andhra Pradesh",
        "Telangana",
        "Maharashtra",
        "Delhi",
        "Rajasthan",
        "Gujarat"
    ]

    for state in states:

        if state.lower() in message_lower:

            profile["state"] = state
            break

    # ==================================================
    # INCOME
    # ==================================================

    # Example:
    # 2 lakh
    # ₹2 lakh
    # 2.5 lakh

    lakh_match = re.search(
        r'₹?\s*(\d+(?:\.\d+)?)\s*lakh',
        message_lower
    )

    if lakh_match:

        profile["income"] = (
            float(lakh_match.group(1)) * 100000
        )

    else:

        # Example:
        # annual income is 150000
        # income: 150000
        # yearly income 200000

        income_match = re.search(
            r'(?:annual income|yearly income|income)'
            r'\s*(?:is|:)?\s*₹?\s*([\d,]+)',
            message_lower
        )

        if income_match:

            profile["income"] = float(
                income_match.group(1).replace(",", "")
            )

    # ==================================================
    # NAME
    # ==================================================

    # Deliberately do NOT use "I am" here.
    # Otherwise:
    # "I am a 45-year-old farmer"
    # would incorrectly extract "a" as the name.

    name_match = re.search(
        r"\b(?:my name is|i'm)\s+"
        r"([A-Za-z]+(?:\s+[A-Za-z]+){0,2})",
        message,
        re.IGNORECASE
    )

    if name_match:

        name = name_match.group(1).strip()

        invalid_names = [
            "a farmer",
            "a student",
            "a teacher",
            "a worker",
            "a businessman",
            "a businesswoman",
            "an engineer",
            "an employee",
            "an artisan",
            "from tamil nadu"
        ]

        if name.lower() not in invalid_names:

            profile["name"] = name

    # ==================================================
    # GENDER
    # ==================================================

    if (
        "female" in message_lower
        or "woman" in message_lower
    ):

        profile["gender"] = "Female"

    elif (
        "male" in message_lower
        or "man" in message_lower
    ):

        profile["gender"] = "Male"

    # ==================================================
    # DISTRICT
    # ==================================================

    districts = [
        "Coimbatore",
        "Chennai",
        "Madurai",
        "Salem",
        "Trichy",
        "Tiruppur",
        "Erode",
        "Thanjavur",
        "Vellore",
        "Dindigul",
        "Tirunelveli",
        "Thoothukudi"
    ]

    for district in districts:

        if district.lower() in message_lower:

            profile["district"] = district
            break

    # ==================================================
    # PHONE
    # ==================================================

    phone_match = re.search(
        r'\b[6-9]\d{9}\b',
        message
    )

    if phone_match:

        profile["phone"] = phone_match.group(0)

    # ==================================================
    # LANDHOLDING
    # ==================================================

    land_match = re.search(
        r'(\d+(?:\.\d+)?)\s*(?:acre|acres)',
        message_lower
    )

    if land_match:

        profile["landholding"] = float(
            land_match.group(1)
        )

    # ==================================================
    # CROP
    # ==================================================

    crops = [
        "rice",
        "paddy",
        "wheat",
        "maize",
        "cotton",
        "sugarcane",
        "groundnut",
        "banana",
        "coconut",
        "millet",
        "vegetables"
    ]

    for crop in crops:

        if crop in message_lower:

            profile["crop"] = crop
            break

    # ==================================================
    # ARTISAN TRADE
    # ==================================================

    artisan_trades = [
        "carpenter",
        "blacksmith",
        "goldsmith",
        "potter",
        "sculptor",
        "cobbler",
        "barber",
        "washerman",
        "tailor",
        "mason",
        "fisherman",
        "basket maker",
        "weaver"
    ]

    for trade in artisan_trades:

        if trade in message_lower:

            profile["artisan_trade"] = trade
            break

    # ==================================================
    # STREET VENDOR
    # ==================================================

    if (
        "street vendor" in message_lower
        or "street vending" in message_lower
        or "i sell on the street" in message_lower
    ):

        profile["street_vendor"] = True

    elif (
        "not a street vendor" in message_lower
        or "not street vendor" in message_lower
    ):

        profile["street_vendor"] = False

    # ==================================================
    # BUSINESS STATUS
    # ==================================================

    if (
        "own a business" in message_lower
        or "running a business" in message_lower
        or "have a business" in message_lower
        or "business owner" in message_lower
    ):

        profile["business_status"] = "existing"

    elif (
        "start a business" in message_lower
        or "starting a business" in message_lower
        or "new business" in message_lower
        or "start my business" in message_lower
    ):

        profile["business_status"] = "new"

    # ==================================================
    # SOCIAL CATEGORY
    # ==================================================

    social_categories = [
        "general",
        "sc",
        "st",
        "obc",
        "ews"
    ]

    for category in social_categories:

        if re.search(
            rf'\b{re.escape(category)}\b',
            message_lower
        ):

            profile["social_category"] = category.upper()
            break

    # ==================================================
    # URBAN / RURAL
    # ==================================================

    if "urban" in message_lower:

        profile["urban_rural"] = "urban"

    elif "rural" in message_lower:

        profile["urban_rural"] = "rural"

    elif "village" in message_lower:

        profile["urban_rural"] = "rural"

    elif "city" in message_lower:

        profile["urban_rural"] = "urban"

    # ==================================================
    # HOUSE OWNERSHIP
    # ==================================================

    if (
        "own a house" in message_lower
        or "own house" in message_lower
        or "own home" in message_lower
        or "own a home" in message_lower
    ):

        profile["house_ownership"] = True

    elif (
        "do not own a house" in message_lower
        or "don't own a house" in message_lower
        or "no house" in message_lower
        or "homeless" in message_lower
    ):

        profile["house_ownership"] = False

    # ==================================================
    # FAMILY STATUS
    # ==================================================

    if "married" in message_lower:

        profile["family_status"] = "married"

    elif (
        "unmarried" in message_lower
        or "single" in message_lower
    ):

        profile["family_status"] = "single"

    # ==================================================
    # HOUSING CONDITION
    # ==================================================

    if (
        "pucca house" in message_lower
        or "permanent house" in message_lower
    ):

        profile["housing_condition"] = "pucca"

    elif (
        "kutcha house" in message_lower
        or "temporary house" in message_lower
        or "thatched house" in message_lower
    ):

        profile["housing_condition"] = "kutcha"

    # ==================================================
    # HOUSEHOLD STATUS
    # ==================================================

    if "poor family" in message_lower:

        profile["household_status"] = "poor"

    elif "low income family" in message_lower:

        profile["household_status"] = "low_income"

    # ==================================================
    # EXISTING LPG
    # ==================================================

    if (
        "already have lpg" in message_lower
        or "have an lpg connection" in message_lower
        or "already have a gas connection" in message_lower
    ):

        profile["existing_lpg"] = True

    elif (
        "do not have lpg" in message_lower
        or "don't have lpg" in message_lower
        or "no lpg" in message_lower
        or "no gas connection" in message_lower
    ):

        profile["existing_lpg"] = False

    # ==================================================
    # PREGNANCY STATUS
    # ==================================================

    if (
        "pregnant" in message_lower
        or "pregnancy" in message_lower
    ):

        profile["pregnancy_status"] = True

    elif "not pregnant" in message_lower:

        profile["pregnancy_status"] = False

    # ==================================================
    # EMPLOYMENT STATUS
    # ==================================================

    if "unemployed" in message_lower:

        profile["employment_status"] = "unemployed"

    elif "employed" in message_lower:

        profile["employment_status"] = "employed"

    # ==================================================
    # BANK ACCOUNT
    # ==================================================

    if (
        "don't have a bank account" in message_lower
        or "do not have a bank account" in message_lower
        or "no bank account" in message_lower
    ):

        profile["bank_account"] = False

    elif (
        "have a bank account" in message_lower
        or "bank account" in message_lower
    ):

        profile["bank_account"] = True

    # ==================================================
    # INCOME TAXPAYER
    # ==================================================

    if (
        "not an income taxpayer" in message_lower
        or "do not pay income tax" in message_lower
        or "don't pay income tax" in message_lower
    ):

        profile["income_taxpayer"] = False

    elif (
        "income taxpayer" in message_lower
        or "pay income tax" in message_lower
        or "income tax payer" in message_lower
    ):

        profile["income_taxpayer"] = True

    # ==================================================
    # ACADEMIC MERIT
    # ==================================================

    merit_match = re.search(
        r'(\d+(?:\.\d+)?)\s*%\s*'
        r'(?:marks|score|percentage)',
        message_lower
    )

    if merit_match:

        profile["academic_merit"] = float(
            merit_match.group(1)
        )

    elif (
        "good marks" in message_lower
        or "high marks" in message_lower
        or "meritorious" in message_lower
    ):

        profile["academic_merit"] = True

    # ==================================================
    # COURSE TYPE
    # ==================================================

    course_types = [
        "engineering",
        "medicine",
        "arts",
        "science",
        "commerce",
        "diploma",
        "degree",
        "undergraduate",
        "postgraduate"
    ]

    for course in course_types:

        if course in message_lower:

            profile["course_type"] = course
            break

    # ==================================================
    # SCHOOL TYPE
    # ==================================================

    if (
        "government school" in message_lower
        or "govt school" in message_lower
    ):

        profile["school_type"] = "government"

    elif "private school" in message_lower:

        profile["school_type"] = "private"

    # ==================================================
    # HIGHER EDUCATION
    # ==================================================

    if (
        "college" in message_lower
        or "higher education" in message_lower
        or "university" in message_lower
    ):

        profile["higher_education"] = True

    elif "not studying" in message_lower:

        profile["higher_education"] = False

    return profile