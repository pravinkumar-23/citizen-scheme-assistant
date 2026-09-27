SCHEMES = [

    # ============================================================
    # 1. PM-KISAN
    # ============================================================

    {
        "name": "PM-KISAN",

        "description": (
            "Income support scheme for eligible landholding "
            "farmer families."
        ),

        "benefits": [
            "Financial assistance to eligible farmer families"
        ],

        "eligibility": {
            "occupation": ["farmer"],
            "minimum_age": 18
        },

        "required_profile_fields": [
            "age",
            "occupation",
            "landholding"
        ],

        "documents": [
            "Aadhaar Card",
            "Land Ownership Record",
            "Bank Account Details"
        ],

        "application_process": [
            "Visit the official PM-KISAN portal.",
            "Complete farmer registration.",
            "Submit the required information and documents."
        ],

        "official_source": "https://pmkisan.gov.in/",

        "notes": (
            "Eligibility is subject to government exclusions "
            "and verification of eligible landholding farmer families."
        )
    },


    # ============================================================
    # 2. KISAN CREDIT CARD
    # ============================================================

    {
        "name": "Kisan Credit Card",

        "description": (
            "Provides timely credit support to eligible farmers "
            "for cultivation and agricultural allied activities."
        ),

        "benefits": [
            "Credit support for cultivation",
            "Support for post-harvest expenses",
            "Credit for agricultural allied activities"
        ],

        "eligibility": {
            "occupation": ["farmer"],
            "minimum_age": 18,
            "maximum_age": 75
        },

        "required_profile_fields": [
            "age",
            "occupation",
            "landholding"
        ],

        "documents": [
            "Application Form",
            "Identity Proof",
            "Address Proof",
            "Landholding Proof",
            "Crop Details",
            "Passport Size Photograph"
        ],

        "application_process": [
            "Visit a participating bank.",
            "Select the Kisan Credit Card facility.",
            "Submit the application and required documents."
        ],

        "official_source": "https://www.myscheme.gov.in/schemes/kcc",

        "notes": (
            "Eligible categories include owner cultivators, "
            "tenant farmers, oral lessees, sharecroppers and "
            "eligible farmer groups."
        )
    },


    # ============================================================
    # 3. PRADHAN MANTRI FASAL BIMA YOJANA
    # ============================================================

    {
        "name": "Pradhan Mantri Fasal Bima Yojana",

        "description": (
            "Crop insurance scheme providing financial protection "
            "against specified crop losses and risks."
        ),

        "benefits": [
            "Crop insurance coverage",
            "Financial protection against eligible crop losses"
        ],

        "eligibility": {
            "occupation": ["farmer"]
        },

        "required_profile_fields": [
            "occupation",
            "landholding",
            "crop",
            "state"
        ],

        "documents": [
            "Identity Proof",
            "Land Records",
            "Bank Account Details",
            "Crop Details"
        ],

        "application_process": [
            "Check the notified crop and area.",
            "Apply through the authorized channel.",
            "Submit crop and land-related information."
        ],

        "official_source": "https://pmfby.gov.in/",

        "notes": (
            "Eligibility depends on notified crops, areas and "
            "applicable seasonal scheme conditions."
        )
    },


    # ============================================================
    # 4. PM-KUSUM
    # ============================================================

    {
        "name": "PM-KUSUM",

        "description": (
            "Scheme supporting decentralized solar energy "
            "and solar agricultural applications."
        ),

        "benefits": [
            "Support for solar agricultural systems",
            "Support for solar pumps",
            "Renewable energy support for eligible agricultural users"
        ],

        "eligibility": {
            "occupation": ["farmer"]
        },

        "required_profile_fields": [
            "occupation",
            "landholding",
            "state"
        ],

        "documents": [
            "Identity Proof",
            "Land Documents",
            "Bank Account Details",
            "Agricultural Land Details"
        ],

        "application_process": [
            "Check the applicable PM-KUSUM component.",
            "Apply through the designated state agency.",
            "Submit the required land and applicant information."
        ],

        "official_source": "https://pmkusum.mnre.gov.in/",

        "notes": (
            "Eligibility differs depending on the PM-KUSUM "
            "component and implementing state."
        )
    },


    # ============================================================
    # 5. PM VISHWAKARMA
    # ============================================================

    {
        "name": "PM Vishwakarma",

        "description": (
            "Support scheme for traditional artisans and "
            "craftspersons working with their hands and tools."
        ),

        "benefits": [
            "PM Vishwakarma certificate and ID",
            "Skill training",
            "Toolkit support",
            "Credit support"
        ],

        "eligibility": {
            "minimum_age": 18
        },

        "required_profile_fields": [
            "age",
            "occupation",
            "artisan_trade"
        ],

        "documents": [
            "Aadhaar Card",
            "Mobile Number",
            "Bank Account Details",
            "Other documents required during registration"
        ],

        "application_process": [
            "Visit an authorized Common Service Centre.",
            "Complete PM Vishwakarma registration.",
            "Complete verification and submit required information."
        ],

        "official_source": "https://pmvishwakarma.gov.in/",

        "notes": (
            "Applicant must be engaged in one of the notified "
            "traditional trades and satisfy scheme conditions."
        )
    },


    # ============================================================
    # 6. PM SVANIDHI
    # ============================================================

    {
        "name": "PM SVANidhi",

        "description": (
            "Credit support scheme for eligible street vendors."
        ),

        "benefits": [
            "Working capital loan support",
            "Support for street vending businesses"
        ],

        "eligibility": {
            "minimum_age": 18
        },

        "required_profile_fields": [
            "age",
            "occupation",
            "street_vendor",
            "state"
        ],

        "documents": [
            "Identity Proof",
            "Address Proof",
            "Street Vendor Certificate or Letter of Recommendation",
            "Bank Account Details"
        ],

        "application_process": [
            "Approach the designated lending institution.",
            "Complete the PM SVANidhi application.",
            "Submit vendor and identity details."
        ],

        "official_source": "https://pmsvanidhi.mohua.gov.in/",

        "notes": (
            "Eligibility depends on street-vendor status and "
            "applicable scheme requirements."
        )
    },


    # ============================================================
    # 7. PRADHAN MANTRI MUDRA YOJANA
    # ============================================================

    {
        "name": "Pradhan Mantri MUDRA Yojana",

        "description": (
            "Provides institutional credit support to eligible "
            "micro enterprises and small businesses."
        ),

        "benefits": [
            "Business credit support",
            "Loans for eligible micro enterprises"
        ],

        "eligibility": {
            "minimum_age": 18
        },

        "required_profile_fields": [
            "age",
            "occupation",
            "business_status"
        ],

        "documents": [
            "Identity Proof",
            "Address Proof",
            "Business Information",
            "Bank Account Details"
        ],

        "application_process": [
            "Approach a participating bank or financial institution.",
            "Choose the applicable MUDRA loan category.",
            "Submit business and financial information."
        ],

        "official_source": "https://www.mudra.org.in/",

        "notes": (
            "Applicable to eligible micro enterprises and "
            "specified non-corporate, non-farm activities."
        )
    },


    # ============================================================
    # 8. STAND-UP INDIA
    # ============================================================

    {
        "name": "Stand-Up India",

        "description": (
            "Bank loan support for eligible women and SC/ST "
            "entrepreneurs starting greenfield enterprises."
        ),

        "benefits": [
            "Bank loan support for eligible enterprises",
            "Support for greenfield business creation"
        ],

        "eligibility": {
            "minimum_age": 18
        },

        "required_profile_fields": [
            "age",
            "gender",
            "social_category",
            "business_status"
        ],

        "documents": [
            "Identity Proof",
            "Address Proof",
            "Caste Certificate where applicable",
            "Business Plan",
            "Financial Documents"
        ],

        "application_process": [
            "Visit the Stand-Up India portal or participating bank.",
            "Submit the business proposal.",
            "Complete bank appraisal and documentation."
        ],

        "official_source": "https://www.standupmitra.in/",

        "notes": (
            "The scheme covers eligible women and SC/ST entrepreneurs. "
            "The enterprise must generally be a greenfield enterprise."
        )
    },


    # ============================================================
    # 9. AYUSHMAN BHARAT PM-JAY
    # ============================================================

    {
        "name": "Ayushman Bharat - PM-JAY",

        "description": (
            "Government-funded health protection scheme for "
            "eligible poor and vulnerable families."
        ),

        "benefits": [
            "Health coverage for eligible families",
            "Cashless treatment at empanelled hospitals"
        ],

        "eligibility": {},

        "required_profile_fields": [
            "state",
            "urban_rural",
            "social_category",
            "occupation",
            "household_status"
        ],

        "documents": [
            "Government-approved identity document",
            "Beneficiary identification documents"
        ],

        "application_process": [
            "Check beneficiary eligibility.",
            "Visit an authorized Ayushman Bharat service point.",
            "Complete beneficiary verification."
        ],

        "official_source": "https://pmjay.gov.in/",

        "notes": (
            "Eligibility is based on government beneficiary databases "
            "and specified rural deprivation or urban occupational criteria."
        )
    },


    # ============================================================
    # 10. PMAY URBAN 2.0
    # ============================================================

    {
        "name": "Pradhan Mantri Awas Yojana - Urban 2.0",

        "description": (
            "Housing assistance scheme for eligible urban households "
            "meeting the prescribed conditions."
        ),

        "benefits": [
            "Housing assistance",
            "Home loan interest support under applicable component"
        ],

        "eligibility": {
            "maximum_income": 1800000
        },

        "required_profile_fields": [
            "income",
            "urban_rural",
            "house_ownership",
            "family_status"
        ],

        "documents": [
            "Identity Proof",
            "Address Proof",
            "Income Proof",
            "Property or Housing Documents"
        ],

        "application_process": [
            "Check eligibility under the applicable PMAY-U component.",
            "Apply through the designated portal or local authority.",
            "Submit household and housing information."
        ],

        "official_source": "https://www.myscheme.gov.in/schemes/pmay-u",

        "notes": (
            "Applicable income groups include EWS, LIG, MIG-I and MIG-II. "
            "The family must satisfy applicable house ownership conditions."
        )
    },


    # ============================================================
    # 11. PMAY GRAMIN
    # ============================================================

    {
        "name": "Pradhan Mantri Awas Yojana - Gramin",

        "description": (
            "Housing assistance scheme for eligible rural households "
            "that are houseless or living in inadequate housing."
        ),

        "benefits": [
            "Financial assistance for construction of a rural house"
        ],

        "eligibility": {},

        "required_profile_fields": [
            "urban_rural",
            "house_ownership",
            "housing_condition",
            "household_status"
        ],

        "documents": [
            "Identity Proof",
            "Residence Details",
            "Household Details",
            "Bank Account Details"
        ],

        "application_process": [
            "Eligibility is identified through the prescribed rural "
            "housing beneficiary process.",
            "Contact the Gram Panchayat or designated authority.",
            "Complete verification and documentation."
        ],

        "official_source": "https://pmayg.nic.in/",

        "notes": (
            "Eligibility is based on prescribed rural housing "
            "deprivation and exclusion criteria."
        )
    },


    # ============================================================
    # 12. PM UJJWALA YOJANA
    # ============================================================

    {
        "name": "Pradhan Mantri Ujjwala Yojana",

        "description": (
            "LPG connection support scheme for eligible women "
            "from poor households."
        ),

        "benefits": [
            "LPG connection support",
            "Support for clean cooking fuel access"
        ],

        "eligibility": {
            "gender": ["female"],
            "minimum_age": 18
        },

        "required_profile_fields": [
            "age",
            "gender",
            "household_status",
            "existing_lpg"
        ],

        "documents": [
            "Aadhaar Card",
            "Address Proof",
            "Bank Account Details",
            "Household Information"
        ],

        "application_process": [
            "Visit an LPG distributor or official PMUY portal.",
            "Complete the application.",
            "Submit household and identity documents."
        ],

        "official_source": "https://www.pmuy.gov.in/",

        "notes": (
            "Applicant must belong to an eligible poor household "
            "and the household should not already have an LPG connection."
        )
    },


    # ============================================================
    # 13. PMMVY
    # ============================================================

    {
        "name": "Pradhan Mantri Matru Vandana Yojana",

        "description": (
            "Maternity benefit scheme providing financial support "
            "to eligible pregnant and lactating women."
        ),

        "benefits": [
            "Maternity-related financial assistance"
        ],

        "eligibility": {
            "gender": ["female"],
            "minimum_age": 18
        },

        "required_profile_fields": [
            "age",
            "gender",
            "pregnancy_status",
            "social_category",
            "employment_status"
        ],

        "documents": [
            "Identity Proof",
            "Bank Account Details",
            "Pregnancy-related documents",
            "Mother and Child Protection Card where applicable"
        ],

        "application_process": [
            "Contact the designated Anganwadi Centre or health facility.",
            "Complete beneficiary registration.",
            "Submit required maternity and identity documents."
        ],

        "official_source": "https://pmmvy.wcd.gov.in/",

        "notes": (
            "Eligibility depends on the applicable PMMVY conditions "
            "and category of beneficiary."
        )
    },


    # ============================================================
    # 14. ATAL PENSION YOJANA
    # ============================================================

    {
        "name": "Atal Pension Yojana",

        "description": (
            "Pension scheme designed to encourage retirement savings."
        ),

        "benefits": [
            "Guaranteed pension according to the selected contribution plan",
            "Retirement income support"
        ],

        "eligibility": {
            "minimum_age": 18,
            "maximum_age": 40
        },

        "required_profile_fields": [
            "age",
            "bank_account",
            "income_taxpayer"
        ],

        "documents": [
            "Aadhaar Card",
            "Bank Account Details",
            "Mobile Number"
        ],

        "application_process": [
            "Approach a participating bank or post office.",
            "Complete APY registration.",
            "Select the pension contribution option."
        ],

        "official_source": "https://www.pfrda.org.in/",

        "notes": (
            "Subscriber must satisfy the current APY conditions, "
            "including applicable income-taxpayer restrictions."
        )
    },


    # ============================================================
    # 15. PMJJBY
    # ============================================================

    {
        "name": "Pradhan Mantri Jeevan Jyoti Bima Yojana",

        "description": (
            "Life insurance scheme available to eligible bank "
            "and post-office account holders."
        ),

        "benefits": [
            "Life insurance coverage"
        ],

        "eligibility": {
            "minimum_age": 18,
            "maximum_age": 50
        },

        "required_profile_fields": [
            "age",
            "bank_account"
        ],

        "documents": [
            "Bank or Post Office Account",
            "Identity Proof",
            "Consent for Auto-Debit"
        ],

        "application_process": [
            "Contact the participating bank or post office.",
            "Complete the PMJJBY enrollment form.",
            "Provide consent for premium auto-debit."
        ],

        "official_source": "https://financialservices.gov.in/",

        "notes": (
            "Eligibility is subject to current PMJJBY rules "
            "and account requirements."
        )
    },


    # ============================================================
    # 16. PMSBY
    # ============================================================

    {
        "name": "Pradhan Mantri Suraksha Bima Yojana",

        "description": (
            "Accident insurance scheme for eligible bank "
            "and post-office account holders."
        ),

        "benefits": [
            "Accidental death coverage",
            "Accidental disability coverage"
        ],

        "eligibility": {
            "minimum_age": 18,
            "maximum_age": 70
        },

        "required_profile_fields": [
            "age",
            "bank_account"
        ],

        "documents": [
            "Bank or Post Office Account",
            "Identity Proof",
            "Consent for Auto-Debit"
        ],

        "application_process": [
            "Contact the participating bank or post office.",
            "Complete PMSBY enrollment.",
            "Provide consent for premium auto-debit."
        ],

        "official_source": "https://financialservices.gov.in/",

        "notes": (
            "Eligibility is subject to current PMSBY rules "
            "and account requirements."
        )
    },


    # ============================================================
    # 17. CENTRAL SECTOR SCHOLARSHIP
    # ============================================================

    {
        "name": (
            "Central Sector Scheme of Scholarship for "
            "College and University Students"
        ),

        "description": (
            "Scholarship support for meritorious students "
            "pursuing higher education."
        ),

        "benefits": [
            "Financial scholarship support for higher education"
        ],

        "eligibility": {
            "occupation": ["student"]
        },

        "required_profile_fields": [
            "age",
            "occupation",
            "income",
            "academic_merit",
            "course_type"
        ],

        "documents": [
            "Aadhaar Card",
            "Income Certificate",
            "Class XII Mark Sheet",
            "College Admission Proof",
            "Bank Account Details"
        ],

        "application_process": [
            "Register on the National Scholarship Portal.",
            "Complete the scholarship application.",
            "Submit the required documents."
        ],

        "official_source": "https://scholarships.gov.in/",

        "notes": (
            "Eligibility depends on merit, family income, "
            "course and other scholarship conditions."
        )
    },


    # ============================================================
    # 18. NMMSS
    # ============================================================

    {
        "name": "National Means-cum-Merit Scholarship Scheme",

        "description": (
            "Scholarship scheme supporting meritorious students "
            "from economically weaker sections."
        ),

        "benefits": [
            "Financial scholarship support for school education"
        ],

        "eligibility": {
            "occupation": ["student"],
            "maximum_income": 350000
        },

        "required_profile_fields": [
            "occupation",
            "income",
            "academic_merit",
            "school_type"
        ],

        "documents": [
            "Income Certificate",
            "School Certificate",
            "Academic Mark Sheets",
            "Caste Certificate where applicable",
            "Bank Account Details"
        ],

        "application_process": [
            "Check the current scholarship notification.",
            "Apply through the designated scholarship portal.",
            "Submit academic and income documents."
        ],

        "official_source": "https://dsel.education.gov.in/",

        "notes": (
            "Students must satisfy the prescribed academic "
            "performance and income conditions."
        )
    },


    # ============================================================
    # 19. TAMIL NADU PUDHUMAI PENN
    # ============================================================

    {
        "name": "Tamil Nadu Pudhumai Penn Scheme",

        "description": (
            "Tamil Nadu higher-education support scheme "
            "for eligible girl students."
        ),

        "benefits": [
            "Monthly financial assistance for eligible students"
        ],

        "eligibility": {
            "gender": ["female"],
            "occupation": ["student"]
        },

        "required_profile_fields": [
            "gender",
            "occupation",
            "school_type",
            "higher_education",
            "state"
        ],

        "documents": [
            "Student ID",
            "School Education Details",
            "College Admission Details",
            "Bank Account Details"
        ],

        "application_process": [
            "Register through the institution and designated "
            "Tamil Nadu government process.",
            "Submit educational and bank details.",
            "Complete institutional verification."
        ],

        "official_source": "https://www.tn.gov.in/",

        "notes": (
            "Intended for eligible girl students who satisfy "
            "the applicable Tamil Nadu education and school-history "
            "conditions and pursue higher education."
        )
    },


    # ============================================================
    # 20. TAMIL NADU TAMIL PUDHALVAN
    # ============================================================

    {
        "name": "Tamil Nadu Tamil Pudhalvan Scheme",

        "description": (
            "Tamil Nadu higher-education support scheme "
            "for eligible boy students."
        ),

        "benefits": [
            "Monthly financial assistance for eligible students"
        ],

        "eligibility": {
            "gender": ["male"],
            "occupation": ["student"]
        },

        "required_profile_fields": [
            "gender",
            "occupation",
            "school_type",
            "higher_education",
            "state"
        ],

        "documents": [
            "Student ID",
            "School Education Details",
            "College Admission Details",
            "Bank Account Details"
        ],

        "application_process": [
            "Register through the institution and designated "
            "Tamil Nadu government process.",
            "Submit educational and bank details.",
            "Complete institutional verification."
        ],

        "official_source": "https://www.tn.gov.in/",

        "notes": (
            "Intended for eligible boy students who satisfy "
            "the applicable Tamil Nadu education and school-history "
            "conditions and pursue higher education."
        )
    }

]