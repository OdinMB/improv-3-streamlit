import streamlit as st
from settings import APP_NAME, CONFLUENCE_PAGE

st.markdown(f"""\
# How It Works

For more information, visit the [Confluence page]({CONFLUENCE_PAGE}) of {APP_NAME}.
""")

# This app helps you find colleagues at Ashoka who are relevant to your specific needs or interests.

# ## Steps

# 1. **You enter a query**: 
#    Tell the app what kind of colleagues you're looking for or what topic you're interested in.

# 2. **The app searches for relevant colleagues**: 
#    It looks through a large database of information about Ashoka colleagues, including their objectives and activities.

# 3. **Initial results are gathered**: 
#    The app finds colleagues whose information closely matches your query.

# 4. **AI evaluates the relevance**: 
#    For each potential match, an AI (Claude 3 Haiku) carefully considers how relevant the colleague is to your query. It provides reasons why the colleague might be relevant, potential limitations, and a relevance score.

# 5. **Results are presented**: 
#    You see a list of the most relevant colleagues, along with details about why they're a good match for your query.

# 6. **Optional summary**: 
#    If you want, you can ask the app to generate an overall summary of the top results. A more advanced AI (Claude 3.5 Sonnet) will create this summary, highlighting the most relevant colleagues and any patterns it notices.

# ### "Thorough Search" Mode

# If you select the "I want a more thorough search" option:

# - The app performs a deeper, more extensive search through the colleague database.
# - It creates variations of your original query to capture a wider range of potentially relevant results. For example, if you search for "finding individual donors," the app might also look for "ASN", "fundraising", or "E2".
# - You receive a larger set of final results.

# ## Key Components

# 1. **Colleague Database**: 
#    A structured collection of information about Ashoka colleagues, including their objectives, activities, and other relevant details.

# 2. **Smart Search System**: 
#    A technology that understands the meaning behind your query and finds matching information in the colleague database.

# 3. **AI Evaluation**: 
#    Artificial Intelligence models that assess how well each potential colleague matches your query.

# 4. **Results Organizer**: 
#    A system that groups and sorts the results to present them in a clear, understandable way.

# 5. **Summary Generator**: 
#    An advanced AI that can create an overall summary of the search results when requested.

# ## Technologies

# We use several advanced technologies to make this app work:

# - **Streamlit**: Creates the user interface you see and interact with.
# - **FAISS**: A powerful tool for searching through large amounts of information quickly.
# - **LangChain**: Helps us work efficiently with AI language models.
# - **Anthropic's Claude AI Models**: 
#   - Claude 3 Haiku: A quick-thinking AI for evaluating relevance and creating query variations.
#   - Claude 3.5 Sonnet: A more advanced AI for generating comprehensive summaries.
# - **Python**: The programming language that ties everything together.
