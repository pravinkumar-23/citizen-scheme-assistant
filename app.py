# import json
# import streamlit as st
# from profile_validator import get_missing_fields
# from profile_extractor import extract_profile

# from mcp_client import (
#     check_eligibility,
#     get_documents,
#     create_application,
#     search_government_information
# )


# # ============================================================
# # Reset Application
# # ============================================================

# def reset_application():

#     st.session_state.profile = None
#     st.session_state.eligibility_data = None
#     st.session_state.documents = None
#     st.session_state.waiting_for = None
#     st.session_state.messages = []
#     st.session_state.last_question = None
#     st.session_state.application_data = None
#     st.session_state.selected_scheme = None
#     st.session_state.previous_selected_scheme = None


# # ============================================================
# # Helper Function
# # ============================================================

# def add_message(role, content):

#     st.session_state.messages.append(
#         {
#             "role": role,
#             "content": content
#         }
#     )


# # ============================================================
# # Get Relevant Extra Fields
# # ============================================================

# def get_relevant_extra_fields(profile):

#     occupation = profile.get("occupation")

#     fields = []

#     # --------------------------------------------------------
#     # Farmer
#     # --------------------------------------------------------

#     if occupation == "farmer":

#         fields = [
#             ("landholding", "landholding in acres"),
#             ("crop", "main crop you grow")
#         ]

#     # --------------------------------------------------------
#     # Student
#     # --------------------------------------------------------

#     elif occupation == "student":

#         fields = [
#             ("academic_merit", "academic marks or percentage"),
#             ("course_type", "course type"),
#             ("school_type", "school type")
#         ]

#     # --------------------------------------------------------
#     # Artisan
#     # --------------------------------------------------------

#     elif occupation == "artisan":

#         fields = [
#             ("artisan_trade", "artisan trade")
#         ]

#     # --------------------------------------------------------
#     # Street Vendor
#     # --------------------------------------------------------

#     elif occupation == "street vendor":

#         fields = [
#             ("street_vendor", "whether you are a street vendor")
#         ]

#     # --------------------------------------------------------
#     # Business / Entrepreneur
#     # --------------------------------------------------------

#     elif occupation in [
#         "businessman",
#         "businesswoman",
#         "self-employed"
#     ]:

#         fields = [
#             ("business_status", "business status")
#         ]

#     return fields


# # ============================================================
# # Page Configuration
# # ============================================================

# st.set_page_config(
#     page_title="Citizen Scheme Eligibility Assistant",
#     page_icon="🏛️",
#     layout="wide"
# )


# # ============================================================
# # Language Selection
# # ============================================================

# LANGUAGES = {
#     "English": "en",
#     "தமிழ்": "ta",
#     "हिन्दी": "hi",
#     "తెలుగు": "te",
#     "ಕನ್ನಡ": "kn",
#     "മലയാളം": "ml"
# }

# selected_language = st.selectbox(
#     "🌐 Select Language",
#     list(LANGUAGES.keys()),
#     index=0
# )

# language_code = LANGUAGES[selected_language]



# # ============================================================
# # Session State
# # ============================================================

# if "profile" not in st.session_state:
#     st.session_state.profile = None

# if "eligibility_data" not in st.session_state:
#     st.session_state.eligibility_data = None

# if "documents" not in st.session_state:
#     st.session_state.documents = None

# if "waiting_for" not in st.session_state:
#     st.session_state.waiting_for = None

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "last_question" not in st.session_state:
#     st.session_state.last_question = None

# if "application_data" not in st.session_state:
#     st.session_state.application_data = None

# if "selected_scheme" not in st.session_state:
#     st.session_state.selected_scheme = None

# if "previous_selected_scheme" not in st.session_state:
#     st.session_state.previous_selected_scheme = None


# # ============================================================
# # Application Title
# # ============================================================

# st.title(
#     "🏛️ Citizen Scheme Eligibility Assistant"
# )

# st.write(
#     "Find government schemes you may be eligible for, "
#     "understand the requirements, and prepare your application."
# )


# # ============================================================
# # Start New Application
# # ============================================================

# if st.button("🔄 Start New Application"):

#     reset_application()

#     st.rerun()


# st.divider()


# # ============================================================
# # Chat Input
# # ============================================================

# st.subheader(
#     "💬 Tell us what you need"
# )

# user_message = st.chat_input(
#     "Example: I am a 45-year-old farmer from Tamil Nadu "
#     "with an income of ₹1.5 lakh."
# )


# # ============================================================
# # Process New User Message
# # ============================================================

# if user_message:

#     # --------------------------------------------------------
#     # Save User Message
#     # --------------------------------------------------------

#     add_message(
#         "user",
#         user_message
#     )


#     # --------------------------------------------------------
#     # Extract / Update Profile
#     # --------------------------------------------------------

#     if st.session_state.profile is None:

#         profile = extract_profile(
#             user_message
#         )

#         st.session_state.profile = profile

#     else:

#         profile = st.session_state.profile

#         new_profile = extract_profile(
#             user_message
#         )

#         # Update only fields where new information was found
#         for field in profile:

#             if new_profile.get(field) is not None:

#                 profile[field] = new_profile[field]

#         st.session_state.profile = profile


#     # --------------------------------------------------------
#     # STEP 1: Check Basic Profile Information
#     # --------------------------------------------------------

#     profile = st.session_state.profile

#     missing_fields = get_missing_fields(
#         profile
#     )


#     if missing_fields:

#         field = missing_fields[0]

#         st.session_state.waiting_for = field

#         question = (
#             f"Could you please provide your {field}?"
#         )

#         # Prevent duplicate questions
#         if st.session_state.last_question != field:

#             add_message(
#                 "assistant",
#                 question
#             )

#             st.session_state.last_question = field


#     else:

#         # ----------------------------------------------------
#         # STEP 2: Check Relevant Extra Information
#         # ----------------------------------------------------

#         extra_fields = get_relevant_extra_fields(
#             profile
#         )

#         missing_extra_fields = []

#         for field, display_name in extra_fields:

#             value = profile.get(field)

#             if value is None or value == "":

#                 missing_extra_fields.append(
#                     (field, display_name)
#                 )


#         # ----------------------------------------------------
#         # Ask Relevant Extra Question
#         # ----------------------------------------------------

#         if missing_extra_fields:

#             field, display_name = (
#                 missing_extra_fields[0]
#             )

#             st.session_state.waiting_for = field


#             # ------------------------------------------------
#             # Friendly Questions
#             # ------------------------------------------------

#             questions = {

#                 "landholding":
#                     "How many acres of agricultural land do you own or cultivate?",

#                 "crop":
#                     "What is the main crop you grow?",

#                 "academic_merit":
#                     "What was your latest academic percentage or marks?",

#                 "course_type":
#                     "What course are you currently studying?",

#                 "school_type":
#                     "Did you study in a government school or private school?",

#                 "artisan_trade":
#                     "What traditional artisan trade do you practice?",

#                 "street_vendor":
#                     "Are you currently working as a street vendor?",

#                 "business_status":
#                     "Do you already have a business, or are you planning to start one?"
#             }


#             question = questions.get(
#                 field,
#                 f"Could you please provide your {display_name}?"
#             )


#             # Prevent duplicate questions
#             if (
#                 st.session_state.last_question
#                 != field
#             ):

#                 add_message(
#                     "assistant",
#                     question
#                 )

#                 st.session_state.last_question = field


#         else:

#             # ------------------------------------------------
#             # ALL REQUIRED INFORMATION AVAILABLE
#             # ------------------------------------------------

#             st.session_state.waiting_for = None
#             st.session_state.last_question = None


#             # ------------------------------------------------
#             # Conversational Confirmation
#             # ------------------------------------------------

#             profile = st.session_state.profile

#             confirmation = (
#                 "✅ Thanks! I have collected the "
#                 "following information:\n\n"

#                 f"**Age:** "
#                 f"{profile.get('age')}\n\n"

#                 f"**Occupation:** "
#                 f"{profile.get('occupation').title()}\n\n"

#                 f"**State:** "
#                 f"{profile.get('state')}\n\n"

#                 f"**Annual Income:** "
#                 f"₹{profile.get('income'):,.0f}\n\n"

#                 "🔍 I will now check which schemes "
#                 "may match your profile."
#             )


#             add_message(
#                 "assistant",
#                 confirmation
#             )


#             # ------------------------------------------------
#             # Reset Previous Selection
#             # ------------------------------------------------

#             st.session_state.selected_scheme = None

#             st.session_state.previous_selected_scheme = None

#             st.session_state.documents = None

#             st.session_state.application_data = None


#             # ------------------------------------------------
#             # Check Eligibility Through MCP
#             # ------------------------------------------------

#             try:

#                 with st.spinner(
#                     "🔍 Checking available schemes..."
#                 ):

#                     result = check_eligibility(
#                         st.session_state.profile
#                     )

#             except Exception as e:

#                 st.error(
#                     "⚠️ Unable to check scheme eligibility. "
#                     "Please try again."
#                 )

#                 result = None


#             # ------------------------------------------------
#             # Convert MCP Response to Dictionary
#             # ------------------------------------------------

#             if result is not None:

#                 try:

#                     eligibility_data = json.loads(
#                         result
#                     )

#                 except Exception:

#                     st.error(
#                         "⚠️ Received an unexpected response "
#                         "from the scheme service."
#                     )

#                     eligibility_data = None

#             else:

#                 eligibility_data = None


#             st.session_state.eligibility_data = (
#                 eligibility_data
#             )


# # ============================================================
# # Display Chat History
# # ============================================================

# for message in st.session_state.messages:

#     with st.chat_message(
#         message["role"]
#     ):

#         st.write(
#             message["content"]
#         )


# # ============================================================
# # Display Extracted Profile
# # ============================================================

# if st.session_state.profile:

#     with st.expander(
#         "👤 Extracted Profile"
#     ):

#         st.json(
#             st.session_state.profile
#         )


# # ============================================================
# # Display Eligibility
# # ============================================================

# if st.session_state.eligibility_data:

#     st.subheader(
#         "✅ Potential Scheme Matches"
#     )

#     eligibility = (
#         st.session_state.eligibility_data
#     )

#     matches = eligibility.get(
#         "matches",
#         []
#     )


#     # --------------------------------------------------------
#     # Display Matching Schemes
#     # --------------------------------------------------------

#     if matches:

#         st.write(
#             "Based on the information provided, "
#             "the following schemes may match your profile:"
#         )


#         # ----------------------------------------------------
#         # Create Scheme List
#         # ----------------------------------------------------

#         scheme_names = [
#             match["scheme"]
#             for match in matches
#         ]


#         # ----------------------------------------------------
#         # Scheme Selection
#         # ----------------------------------------------------

#         selected_scheme = st.selectbox(
#             "🏛️ Select a scheme",
#             scheme_names
#         )


#         # ----------------------------------------------------
#         # Detect Scheme Change
#         # ----------------------------------------------------

#         if (
#             st.session_state.previous_selected_scheme
#             is not None
#             and
#             st.session_state.previous_selected_scheme
#             != selected_scheme
#         ):

#             st.session_state.documents = None

#             st.session_state.application_data = None


#         st.session_state.selected_scheme = (
#             selected_scheme
#         )

#         st.session_state.previous_selected_scheme = (
#             selected_scheme
#         )


#         # ----------------------------------------------------
#         # Find Selected Scheme
#         # ----------------------------------------------------

#         selected_match = None

#         for match in matches:

#             if match["scheme"] == selected_scheme:

#                 selected_match = match

#                 break


#         # ----------------------------------------------------
#         # Display Selected Scheme
#         # ----------------------------------------------------

#         if selected_match:

#             st.markdown(
#                 f"### 🏛️ {selected_match['scheme']}"
#             )


#             # Scheme Description
#             if selected_match.get(
#                 "description"
#             ):

#                 st.write(
#                     selected_match["description"]
#                 )


#             # Scheme Status
#             st.write(
#                 "**Status:** 🟢 Potentially Eligible"
#             )


#             # Matching Criteria
#             st.markdown(
#                 "#### Matching Criteria"
#             )


#             for reason in selected_match.get(
#                 "reasons",
#                 []
#             ):

#                 st.write(
#                     f"✅ {reason}"
#                 )


#     else:

#         st.warning(
#             "No potential scheme matches were found "
#             "based on the information provided."
#         )


#     # --------------------------------------------------------
#     # Government Disclaimer
#     # --------------------------------------------------------

#     if eligibility.get("message"):

#         st.info(
#             eligibility["message"]
#         )


# # ============================================================
# # Display Required Documents
# # ============================================================

# if (
#     st.session_state.selected_scheme
#     and st.session_state.eligibility_data
# ):

#     scheme_name = (
#         st.session_state.selected_scheme
#     )


#     st.subheader(
#         "📄 Required Documents"
#     )


#     st.write(
#         f"Documents commonly required for "
#         f"**{scheme_name}**:"
#     )


#     st.info(
#         "The document list is based on the available "
#         "scheme information. The concerned government "
#         "authority may request additional documents."
#     )


#     # --------------------------------------------------------
#     # Get Documents Button
#     # --------------------------------------------------------

#     if st.button(
#         "📄 Get Required Documents"
#     ):

#         try:

#             with st.spinner(
#                 "📄 Fetching required documents..."
#             ):

#                 documents = get_documents(
#                     scheme_name
#                 )

#         except Exception:

#             st.error(
#                 "⚠️ Unable to retrieve the required "
#                 "documents. Please try again."
#             )

#             documents = None


#         # ----------------------------------------------------
#         # Convert MCP JSON Response
#         # ----------------------------------------------------

#         if (
#             documents is not None
#             and isinstance(documents, str)
#         ):

#             try:

#                 documents = json.loads(
#                     documents
#                 )

#             except Exception:

#                 documents = documents.splitlines()


#         st.session_state.documents = (
#             documents
#         )


#     # --------------------------------------------------------
#     # Display Documents
#     # --------------------------------------------------------

#     if st.session_state.documents:

#         st.markdown(
#             "### 📋 Document Checklist"
#         )

#         for document in (
#             st.session_state.documents
#         ):

#             st.checkbox(
#                 document,
#                 value=False
#             )


# # ============================================================
# # Create Application Draft
# # ============================================================

# if st.session_state.selected_scheme:

#     scheme_name = (
#         st.session_state.selected_scheme
#     )


#     st.subheader(
#         "📝 Application"
#     )


#     st.write(
#         f"Prepare a draft application for "
#         f"**{scheme_name}** using the information "
#         f"collected during the conversation."
#     )


#     # --------------------------------------------------------
#     # Create Draft Button
#     # --------------------------------------------------------

#     if st.button(
#         "📝 Create Application Draft"
#     ):

#         try:

#             with st.spinner(
#                 "📝 Preparing application..."
#             ):

#                 application = create_application(
#                     st.session_state.profile,
#                     scheme_name
#                 )

#         except Exception:

#             st.error(
#                 "⚠️ Unable to create the application "
#                 "draft. Please try again."
#             )

#             application = None


#         # ----------------------------------------------------
#         # Convert MCP JSON Response to Dictionary
#         # ----------------------------------------------------

#         if application is not None:

#             try:

#                 application_data = json.loads(
#                     application
#                 )

#                 st.session_state.application_data = (
#                     application_data
#                 )

#             except Exception:

#                 st.session_state.application_data = {
#                     "raw": application
#                 }


#     # --------------------------------------------------------
#     # Display Application Draft
#     # --------------------------------------------------------

#     if st.session_state.application_data:

#         application = (
#             st.session_state.application_data
#         )


#         st.success(
#             "Application draft created successfully!"
#         )


#         # ====================================================
#         # Scheme Information
#         # ====================================================

#         st.markdown(
#             "### 🏛️ Scheme Information"
#         )


#         st.write(
#             f"**Scheme:** "
#             f"{application.get('scheme_name', scheme_name)}"
#         )


#         st.write(
#             "**Status:** Draft"
#         )


#         st.divider()


#         # ====================================================
#         # Applicant Information
#         # ====================================================

#         st.markdown(
#             "### 👤 Applicant Information"
#         )


#         applicant = application.get(
#             "applicant",
#             {}
#         )


#         col1, col2 = st.columns(2)


#         # ----------------------------------------------------
#         # Left Column
#         # ----------------------------------------------------

#         with col1:

#             st.write(
#                 f"**Name:** "
#                 f"{applicant.get('name') or 'Not provided'}"
#             )


#             st.write(
#                 f"**Age:** "
#                 f"{applicant.get('age') or 'Not provided'}"
#             )


#             st.write(
#                 f"**Gender:** "
#                 f"{applicant.get('gender') or 'Not provided'}"
#             )


#             st.write(
#                 f"**Phone:** "
#                 f"{applicant.get('phone') or 'Not provided'}"
#             )


#         # ----------------------------------------------------
#         # Right Column
#         # ----------------------------------------------------

#         with col2:

#             st.write(
#                 f"**State:** "
#                 f"{applicant.get('state') or 'Not provided'}"
#             )


#             st.write(
#                 f"**District:** "
#                 f"{applicant.get('district') or 'Not provided'}"
#             )


#             income = application.get(
#                 "income"
#             )


#             if income is not None:

#                 st.write(
#                     f"**Annual Income:** "
#                     f"₹{income:,.0f}"
#                 )

#             else:

#                 st.write(
#                     "**Annual Income:** "
#                     "Not provided"
#                 )


#             st.write(
#                 f"**Occupation:** "
#                 f"{application.get('occupation') or 'Not provided'}"
#             )


#         st.divider()


#         # ====================================================
#         # Draft Notice
#         # ====================================================

#         st.info(
#             "This is a draft application prepared from "
#             "the information provided in the conversation. "
#             "It has not been submitted to any government authority."
#         )


#         # ====================================================
#         # Download Application Draft
#         # ====================================================

#         income = application.get(
#             "income"
#         )


#         if income is not None:

#             income_text = f"₹{income:,.0f}"

#         else:

#             income_text = "Not provided"


#         application_text = f"""
# CITIZEN SCHEME APPLICATION DRAFT
# ================================

# Scheme Information
# ------------------
# Scheme: {application.get('scheme_name', scheme_name)}
# Status: Draft


# Applicant Information
# ---------------------
# Name: {applicant.get('name') or 'Not provided'}
# Age: {applicant.get('age') or 'Not provided'}
# Gender: {applicant.get('gender') or 'Not provided'}
# State: {applicant.get('state') or 'Not provided'}
# District: {applicant.get('district') or 'Not provided'}
# Phone: {applicant.get('phone') or 'Not provided'}
# Annual Income: {income_text}
# Occupation: {application.get('occupation') or 'Not provided'}


# NOTICE
# ------
# This is a draft application prepared from the
# information provided by the citizen.

# It has not been submitted to any government authority.
# """


#         st.download_button(
#             label="⬇️ Download Application Draft",
#             data=application_text,
#             file_name="application_draft.txt",
#             mime="text/plain"
#         )


# # ============================================================
# # Government Information Search — Tavily
# # ============================================================

# st.divider()

# st.subheader(
#     "🔎 Government Scheme Information Search"
# )

# st.write(
#     "Search for the latest government scheme information "
#     "using web sources through Tavily."
# )


# # ------------------------------------------------------------
# # Search Input
# # ------------------------------------------------------------

# government_query = st.text_input(
#     "Enter your question",
#     placeholder="Example: PM-KISAN latest eligibility",
#     key="government_search_query"
# )


# # ------------------------------------------------------------
# # Search Button
# # ------------------------------------------------------------

# if st.button(
#     "🔎 Search Government Information",
#     key="government_search_button"
# ):

#     if not government_query.strip():

#         st.warning(
#             "Please enter a search question."
#         )

#     else:

#         try:

#             with st.spinner(
#                 "🔍 Searching government information..."
#             ):

#                 search_result = (
#                     search_government_information(
#                         government_query.strip()
#                     )
#                 )

#         except Exception as e:

#             st.error(
#                 "⚠️ Unable to search government information."
#             )

#             search_result = None


#         # ----------------------------------------------------
#         # Display Search Results
#         # ----------------------------------------------------
#         if search_result:

#             st.markdown("### 📚 Government Information Results")

#             try:
#                 results = json.loads(search_result)
#             except Exception:
#                 results = []

#             # --------------------------------------------------------
#             # Display list of results
#             # --------------------------------------------------------

#             if isinstance(results, list):

#                 if len(results) == 0:

#                     st.info(
#                         "No search results were found."
#                     )

#                 else:

#                     for index, result in enumerate(
#                         results,
#                         start=1
#                     ):

#                         title = result.get(
#                             "title",
#                             "Untitled"
#                         )

#                         content = result.get(
#                             "content",
#                             ""
#                         )

#                         url = result.get(
#                             "url",
#                             ""
#                         )

#                         st.markdown(
#                             f"### {index}. {title}"
#                         )

#                         if content:

#                             st.write(
#                                 content
#                             )

#                         if url:

#                             st.markdown(
#                                 f"🔗 [View Source]({url})"
#                             )

#                         st.divider()

#             # --------------------------------------------------------
#             # Display single result
#             # --------------------------------------------------------

#             elif isinstance(results, dict):

#                 title = results.get(
#                     "title",
#                     "Untitled"
#                 )

#                 content = results.get(
#                     "content",
#                     ""
#                 )

#                 url = results.get(
#                     "url",
#                     ""
#                 )

#                 st.markdown(
#                     f"### 📄 {title}"
#                 )

#                 if content:

#                     st.write(
#                         content
#                     )

#                 if url:

#                     st.markdown(
#                         f"🔗 [View Source]({url})"
#                     )

#             # --------------------------------------------------------
#             # Fallback
#             # --------------------------------------------------------

#             else:

#                 st.write(
#                     search_result
#                 )

#         else:

#             st.warning(
#                 "No information was returned from the search."
#             )

import json
import streamlit as st

from profile_validator import get_missing_fields
from profile_extractor import extract_profile

from mcp_client import (
    check_eligibility,
    get_documents,
    create_application,
    search_government_information
)

from translations import get_text


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Citizen Scheme Eligibility Assistant",
    page_icon="🏛️",
    layout="wide"
)


# ============================================================
# Language Selection
# ============================================================

LANGUAGES = {
    "English": "en",
    "தமிழ்": "ta",
    "हिन्दी": "hi",
    "తెలుగు": "te",
    "ಕನ್ನಡ": "kn",
    "മലയാളം": "ml"
}

selected_language = st.selectbox(
    "🌐 Select Language",
    list(LANGUAGES.keys()),
    index=0
)

language_code = LANGUAGES[selected_language]


# ============================================================
# Translation Helper
# ============================================================

def t(key):
    return get_text(
        language_code,
        key
    )


# ============================================================
# Reset Application
# ============================================================

def reset_application():

    st.session_state.profile = None
    st.session_state.eligibility_data = None
    st.session_state.documents = None
    st.session_state.waiting_for = None
    st.session_state.messages = []
    st.session_state.last_question = None
    st.session_state.application_data = None
    st.session_state.selected_scheme = None
    st.session_state.previous_selected_scheme = None


# ============================================================
# Helper Function
# ============================================================

def add_message(role, content):

    st.session_state.messages.append(
        {
            "role": role,
            "content": content
        }
    )


# ============================================================
# Get Relevant Extra Fields
# ============================================================

def get_relevant_extra_fields(profile):

    occupation = profile.get("occupation")

    fields = []

    if occupation == "farmer":

        fields = [
            ("landholding", "landholding in acres"),
            ("crop", "main crop you grow")
        ]

    elif occupation == "student":

        fields = [
            ("academic_merit", "academic marks or percentage"),
            ("course_type", "course type"),
            ("school_type", "school type")
        ]

    elif occupation == "artisan":

        fields = [
            ("artisan_trade", "artisan trade")
        ]

    elif occupation == "street vendor":

        fields = [
            ("street_vendor", "whether you are a street vendor")
        ]

    elif occupation in [
        "businessman",
        "businesswoman",
        "self-employed"
    ]:

        fields = [
            ("business_status", "business status")
        ]

    return fields


# ============================================================
# Session State
# ============================================================

if "profile" not in st.session_state:
    st.session_state.profile = None

if "eligibility_data" not in st.session_state:
    st.session_state.eligibility_data = None

if "documents" not in st.session_state:
    st.session_state.documents = None

if "waiting_for" not in st.session_state:
    st.session_state.waiting_for = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_question" not in st.session_state:
    st.session_state.last_question = None

if "application_data" not in st.session_state:
    st.session_state.application_data = None

if "selected_scheme" not in st.session_state:
    st.session_state.selected_scheme = None

if "previous_selected_scheme" not in st.session_state:
    st.session_state.previous_selected_scheme = None


# ============================================================
# Application Title
# ============================================================

st.title(
    t("title")
)

st.write(
    t("description")
)


# ============================================================
# Start New Application
# ============================================================

if st.button(
    t("new_application")
):

    reset_application()

    st.rerun()


st.divider()


# ============================================================
# Chat Input
# ============================================================

st.subheader(
    "💬 Tell us what you need"
)

user_message = st.chat_input(
    "Example: I am a 45-year-old farmer from Tamil Nadu "
    "with an income of ₹1.5 lakh."
)


# ============================================================
# Process New User Message
# ============================================================

if user_message:

    add_message(
        "user",
        user_message
    )

    # --------------------------------------------------------
    # Extract / Update Profile
    # --------------------------------------------------------

    if st.session_state.profile is None:

        profile = extract_profile(
            user_message
        )

        st.session_state.profile = profile

    else:

        profile = st.session_state.profile

        new_profile = extract_profile(
            user_message
        )

        for field in profile:

            if new_profile.get(field) is not None:

                profile[field] = new_profile[field]

        st.session_state.profile = profile


    # --------------------------------------------------------
    # STEP 1: Check Basic Profile Information
    # --------------------------------------------------------

    profile = st.session_state.profile

    missing_fields = get_missing_fields(
        profile
    )


    if missing_fields:

        field = missing_fields[0]

        st.session_state.waiting_for = field

        question = (
            f"Could you please provide your {field}?"
        )

        if st.session_state.last_question != field:

            add_message(
                "assistant",
                question
            )

            st.session_state.last_question = field


    else:

        # ----------------------------------------------------
        # STEP 2: Check Relevant Extra Information
        # ----------------------------------------------------

        extra_fields = get_relevant_extra_fields(
            profile
        )

        missing_extra_fields = []

        for field, display_name in extra_fields:

            value = profile.get(field)

            if value is None or value == "":

                missing_extra_fields.append(
                    (field, display_name)
                )


        # ----------------------------------------------------
        # Ask Relevant Extra Question
        # ----------------------------------------------------

        if missing_extra_fields:

            field, display_name = (
                missing_extra_fields[0]
            )

            st.session_state.waiting_for = field


            questions = {

                "landholding":
                    "How many acres of agricultural land do you own or cultivate?",

                "crop":
                    "What is the main crop you grow?",

                "academic_merit":
                    "What was your latest academic percentage or marks?",

                "course_type":
                    "What course are you currently studying?",

                "school_type":
                    "Did you study in a government school or private school?",

                "artisan_trade":
                    "What traditional artisan trade do you practice?",

                "street_vendor":
                    "Are you currently working as a street vendor?",

                "business_status":
                    "Do you already have a business, or are you planning to start one?"
            }


            question = questions.get(
                field,
                f"Could you please provide your {display_name}?"
            )


            if (
                st.session_state.last_question
                != field
            ):

                add_message(
                    "assistant",
                    question
                )

                st.session_state.last_question = field


        else:

            # ------------------------------------------------
            # ALL REQUIRED INFORMATION AVAILABLE
            # ------------------------------------------------

            st.session_state.waiting_for = None
            st.session_state.last_question = None

            profile = st.session_state.profile

            confirmation = (
                "✅ Thanks! I have collected the "
                "following information:\n\n"

                f"**Age:** "
                f"{profile.get('age')}\n\n"

                f"**Occupation:** "
                f"{profile.get('occupation').title()}\n\n"

                f"**State:** "
                f"{profile.get('state')}\n\n"

                f"**Annual Income:** "
                f"₹{profile.get('income'):,.0f}\n\n"

                "🔍 I will now check which schemes "
                "may match your profile."
            )


            add_message(
                "assistant",
                confirmation
            )


            st.session_state.selected_scheme = None

            st.session_state.previous_selected_scheme = None

            st.session_state.documents = None

            st.session_state.application_data = None


            # ------------------------------------------------
            # Check Eligibility Through MCP
            # ------------------------------------------------

            try:

                with st.spinner(
                    "🔍 Checking available schemes..."
                ):

                    result = check_eligibility(
                        st.session_state.profile
                    )

            except Exception:

                st.error(
                    "⚠️ Unable to check scheme eligibility. "
                    "Please try again."
                )

                result = None


            # ------------------------------------------------
            # Convert MCP Response
            # ------------------------------------------------

            if result is not None:

                try:

                    eligibility_data = json.loads(
                        result
                    )

                except Exception:

                    st.error(
                        "⚠️ Received an unexpected response "
                        "from the scheme service."
                    )

                    eligibility_data = None

            else:

                eligibility_data = None


            st.session_state.eligibility_data = (
                eligibility_data
            )


# ============================================================
# Display Chat History
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# ============================================================
# Display Extracted Profile
# ============================================================

if st.session_state.profile:

    with st.expander(
        t("extracted_profile")
    ):

        st.json(
            st.session_state.profile
        )


# ============================================================
# Display Eligibility
# ============================================================

if st.session_state.eligibility_data:

    st.subheader(
        t("eligibility_results")
    )

    eligibility = (
        st.session_state.eligibility_data
    )

    matches = eligibility.get(
        "matches",
        []
    )


    if matches:

        st.write(
            "Based on the information provided, "
            "the following schemes may match your profile:"
        )


        scheme_names = [
            match["scheme"]
            for match in matches
        ]


        # ----------------------------------------------------
        # Scheme Selection
        # ----------------------------------------------------

        selected_scheme = st.selectbox(
            t("select_scheme"),
            scheme_names
        )


        # ----------------------------------------------------
        # Detect Scheme Change
        # ----------------------------------------------------

        if (
            st.session_state.previous_selected_scheme
            is not None
            and
            st.session_state.previous_selected_scheme
            != selected_scheme
        ):

            st.session_state.documents = None

            st.session_state.application_data = None


        st.session_state.selected_scheme = (
            selected_scheme
        )

        st.session_state.previous_selected_scheme = (
            selected_scheme
        )


        # ----------------------------------------------------
        # Find Selected Scheme
        # ----------------------------------------------------

        selected_match = None

        for match in matches:

            if match["scheme"] == selected_scheme:

                selected_match = match

                break


        # ----------------------------------------------------
        # Display Selected Scheme
        # ----------------------------------------------------

        if selected_match:

            st.markdown(
                f"### 🏛️ {selected_match['scheme']}"
            )


            if selected_match.get(
                "description"
            ):

                st.write(
                    selected_match["description"]
                )


            st.write(
                f"**{t('status')}:** 🟢 Potentially Eligible"
            )


            st.markdown(
                f"#### {t('why_eligible')}"
            )


            for reason in selected_match.get(
                "reasons",
                []
            ):

                st.write(
                    f"✅ {reason}"
                )


    else:

        st.warning(
            "No potential scheme matches were found "
            "based on the information provided."
        )


    # --------------------------------------------------------
    # Government Disclaimer
    # --------------------------------------------------------

    if eligibility.get("message"):

        st.info(
            eligibility["message"]
        )


# ============================================================
# Display Required Documents
# ============================================================

if (
    st.session_state.selected_scheme
    and st.session_state.eligibility_data
):

    scheme_name = (
        st.session_state.selected_scheme
    )


    st.subheader(
        t("required_documents")
    )


    st.write(
        f"Documents commonly required for "
        f"**{scheme_name}**:"
    )


    st.info(
        "The document list is based on the available "
        "scheme information. The concerned government "
        "authority may request additional documents."
    )


    # --------------------------------------------------------
    # Get Documents Button
    # --------------------------------------------------------

    if st.button(
        t("get_documents")
    ):

        try:

            with st.spinner(
                "📄 Fetching required documents..."
            ):

                documents = get_documents(
                    scheme_name
                )

        except Exception:

            st.error(
                "⚠️ Unable to retrieve the required "
                "documents. Please try again."
            )

            documents = None


        if (
            documents is not None
            and isinstance(documents, str)
        ):

            try:

                documents = json.loads(
                    documents
                )

            except Exception:

                documents = documents.splitlines()


        st.session_state.documents = (
            documents
        )


    # --------------------------------------------------------
    # Display Documents
    # --------------------------------------------------------

    if st.session_state.documents:

        st.markdown(
            "### 📋 Document Checklist"
        )

        for document in (
            st.session_state.documents
        ):

            st.checkbox(
                document,
                value=False
            )


# ============================================================
# Create Application Draft
# ============================================================

if st.session_state.selected_scheme:

    scheme_name = (
        st.session_state.selected_scheme
    )


    st.subheader(
        t("application")
    )


    st.write(
        f"Prepare a draft application for "
        f"**{scheme_name}** using the information "
        f"collected during the conversation."
    )


    # --------------------------------------------------------
    # Create Draft Button
    # --------------------------------------------------------

    if st.button(
        t("create_application")
    ):

        try:

            with st.spinner(
                "📝 Preparing application..."
            ):

                application = create_application(
                    st.session_state.profile,
                    scheme_name
                )

        except Exception:

            st.error(
                "⚠️ Unable to create the application "
                "draft. Please try again."
            )

            application = None


        # ----------------------------------------------------
        # Convert MCP JSON Response
        # ----------------------------------------------------

        if application is not None:

            try:

                application_data = json.loads(
                    application
                )

                st.session_state.application_data = (
                    application_data
                )

            except Exception:

                st.session_state.application_data = {
                    "raw": application
                }


    # --------------------------------------------------------
    # Display Application Draft
    # --------------------------------------------------------

    if st.session_state.application_data:

        application = (
            st.session_state.application_data
        )


        st.success(
            "Application draft created successfully!"
        )


        # ====================================================
        # Scheme Information
        # ====================================================

        st.markdown(
            "### 🏛️ Scheme Information"
        )


        st.write(
            f"**Scheme:** "
            f"{application.get('scheme_name', scheme_name)}"
        )


        st.write(
            "**Status:** Draft"
        )


        st.divider()


        # ====================================================
        # Applicant Information
        # ====================================================

        st.markdown(
            "### 👤 Applicant Information"
        )


        applicant = application.get(
            "applicant",
            {}
        )


        col1, col2 = st.columns(2)


        with col1:

            st.write(
                f"**Name:** "
                f"{applicant.get('name') or 'Not provided'}"
            )

            st.write(
                f"**Age:** "
                f"{applicant.get('age') or 'Not provided'}"
            )

            st.write(
                f"**Gender:** "
                f"{applicant.get('gender') or 'Not provided'}"
            )

            st.write(
                f"**Phone:** "
                f"{applicant.get('phone') or 'Not provided'}"
            )


        with col2:

            st.write(
                f"**State:** "
                f"{applicant.get('state') or 'Not provided'}"
            )

            st.write(
                f"**District:** "
                f"{applicant.get('district') or 'Not provided'}"
            )


            income = application.get(
                "income"
            )


            if income is not None:

                st.write(
                    f"**Annual Income:** "
                    f"₹{income:,.0f}"
                )

            else:

                st.write(
                    "**Annual Income:** "
                    "Not provided"
                )


            st.write(
                f"**Occupation:** "
                f"{application.get('occupation') or 'Not provided'}"
            )


        st.divider()


        # ====================================================
        # Draft Notice
        # ====================================================

        st.info(
            "This is a draft application prepared from "
            "the information provided in the conversation. "
            "It has not been submitted to any government authority."
        )


        # ====================================================
        # Download Application Draft
        # ====================================================

        income = application.get(
            "income"
        )


        if income is not None:

            income_text = f"₹{income:,.0f}"

        else:

            income_text = "Not provided"


        application_text = f"""
CITIZEN SCHEME APPLICATION DRAFT
================================

Scheme Information
------------------
Scheme: {application.get('scheme_name', scheme_name)}
Status: Draft


Applicant Information
---------------------
Name: {applicant.get('name') or 'Not provided'}
Age: {applicant.get('age') or 'Not provided'}
Gender: {applicant.get('gender') or 'Not provided'}
State: {applicant.get('state') or 'Not provided'}
District: {applicant.get('district') or 'Not provided'}
Phone: {applicant.get('phone') or 'Not provided'}
Annual Income: {income_text}
Occupation: {application.get('occupation') or 'Not provided'}


NOTICE
------
This is a draft application prepared from the
information provided by the citizen.

It has not been submitted to any government authority.
"""


        st.download_button(
            label="⬇️ Download Application Draft",
            data=application_text,
            file_name="application_draft.txt",
            mime="text/plain"
        )


# ============================================================
# Government Information Search — Tavily
# ============================================================

st.divider()

st.subheader(
    t("government_search")
)

st.write(
    t("search_description")
)


# ------------------------------------------------------------
# Search Input
# ------------------------------------------------------------

government_query = st.text_input(
    t("enter_question"),
    placeholder="Example: PM-KISAN latest eligibility",
    key="government_search_query"
)


# ------------------------------------------------------------
# Search Button
# ------------------------------------------------------------

if st.button(
    t("search_button"),
    key="government_search_button"
):

    if not government_query.strip():

        st.warning(
            t("enter_question_warning")
        )

    else:

        try:

            with st.spinner(
                t("searching")
            ):

                search_result = (
                    search_government_information(
                        government_query.strip()
                    )
                )

        except Exception:

            st.error(
                "⚠️ Unable to search government information."
            )

            search_result = None


        # ----------------------------------------------------
        # Display Search Results
        # ----------------------------------------------------

        if search_result:

            st.markdown(
                f"### {t('search_results')}"
            )


            try:

                results = json.loads(
                    search_result
                )

            except Exception:

                results = []


            # ------------------------------------------------
            # List of Results
            # ------------------------------------------------

            if isinstance(results, list):

                if len(results) == 0:

                    st.info(
                        t("no_results")
                    )

                else:

                    for index, result in enumerate(
                        results,
                        start=1
                    ):

                        title = result.get(
                            "title",
                            "Untitled"
                        )

                        content = result.get(
                            "content",
                            ""
                        )

                        url = result.get(
                            "url",
                            ""
                        )


                        st.markdown(
                            f"### {index}. {title}"
                        )


                        if content:

                            st.write(
                                content
                            )


                        if url:

                            st.markdown(
                                f"🔗 [{t('view_source')}]({url})"
                            )


                        st.divider()


            # ------------------------------------------------
            # Single Result
            # ------------------------------------------------

            elif isinstance(results, dict):

                title = results.get(
                    "title",
                    "Untitled"
                )

                content = results.get(
                    "content",
                    ""
                )

                url = results.get(
                    "url",
                    ""
                )


                st.markdown(
                    f"### 📄 {title}"
                )


                if content:

                    st.write(
                        content
                    )


                if url:

                    st.markdown(
                        f"🔗 [{t('view_source')}]({url})"
                    )


            # ------------------------------------------------
            # Fallback
            # ------------------------------------------------

            else:

                st.write(
                    search_result
                )


        else:

            st.warning(
                t("no_information")
            )

