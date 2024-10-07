import os

APP_NAME = "NGO Academy Improv Session"
# AI Lab page
CONFLUENCE_PAGE = ""

DEVELOPER = "Odin"
PARTNERS = "NGO Academy Improv Session Audience"

CREATE_LOG_FILES = False

# Get the directory of the current script (which is in the project root folder)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(SCRIPT_DIR, 'files')
LOGS_DIR = os.path.join(SCRIPT_DIR, 'logs')
DATA_DIR = os.path.join(SCRIPT_DIR, 'data')

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR, exist_ok=True)

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR, exist_ok=True)