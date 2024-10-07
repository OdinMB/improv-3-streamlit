import streamlit as st
import os
import base64
from settings import APP_NAME, CONFLUENCE_PAGE, DEVELOPER, PARTNERS

from dotenv import load_dotenv
load_dotenv()

st.set_page_config(
    page_title=APP_NAME + " - AI Improv Session", 
    page_icon="img/favicon-32x32.png",
    layout="centered", 
    initial_sidebar_state="auto", 
    menu_items=None
)

# --- PAGE SETUP ---
app_page = st.Page(
    page="views/start.py",
    title="App",
    icon=":material/assignment_turned_in:",
    default=True,
)
manual_page = st.Page(
    page="views/manual.py",
    title="Manual",
    icon=":material/assignment:",
)
explanation_page = st.Page(
    page="views/explanation.py",
    title="Technical explanation",
    icon=":material/developer_board:",
)

# --- NAVIGATION ---
pg = st.navigation(
    {
        APP_NAME: [app_page],
        "Documentation": [manual_page, explanation_page],
    }
)
pg.run()

st.logo(
    image="img/AILab.png", 
    link=CONFLUENCE_PAGE,
)

# --- workaround to display image with link ---

def get_img_with_href(local_img_path, target_url, width="100%", centered=False, styles=""):
    img_format = os.path.splitext(local_img_path)[-1].replace(".", "")
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f"""
    {'<div style="text-align: center">' if centered else ''}<a href="{target_url}">
        <img src="data:image/{img_format};base64,{bin_str}" style="width: {width}; {styles}" />
    </a>{'</div>' if centered else ''}"""
    return html_code

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# logo_html = get_img_with_href("img/AppLogo.jpg", CONFLUENCE_PAGE, "200px", True, "margin-top: 0.5em; margin-bottom: 0.5em")
# st.sidebar.markdown(logo_html, unsafe_allow_html=True)

# st.sidebar.markdown(f"<h2 style='text-align: center; padding-top: 0; margin-top: 0;'>{APP_NAME}</h2>", unsafe_allow_html=True)

# st.sidebar.markdown(f"""\
#     [Confluence page]({CONFLUENCE_PAGE})   
#     [Feedback](https://forms.office.com/r/tRvXcxpZQ8)  
#     [Report a problem](https://jira.ashoka.org/servicedesk/customer/portal/30/create/289)  

#     ---                    
# """)

st.sidebar.info(f"""\
    Developer: {DEVELOPER}  
    Partners: {PARTNERS}
""")

# --- STYLES ---
st.html("""\
<style>
    [data-testid="stSidebar"][aria-expanded="true"]{
        min-width: 275px;
        max-width: 275px;
    }
        
    div[data-testid="stSidebarHeader"] > a > img, 
    div[data-testid="collapsedControl"] > a > img {
        height: auto;
        width: 90px;
        margin-top: 10px
    }
    div[data-testid="stSidebarHeader"] > a > img {
            margin-left: 65px;
    }
            
    .stButton>button {
        border-radius: 100px;
    }
    @media screen and (max-width: 767px) {
        .hide-on-mobile {
            display: none;
        }
    }
    @media screen and (min-width: 768px) {
        .hide-on-large_screen {
            display: none;
        }
    }
    .centered {
        text-align: center;
        width: 100%;
    }
</style>
""")