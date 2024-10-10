from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_PERSONAL_KEY")  
REPO_NAME = 'Kaden-Barker/synergy_infrastructure' 
BRANCH_NAME = 'main'  
FILE_PATH = 'xmlFiles/index.xml'  # Currently hard coded file that is to be uploaded
TARGET_PATH = 'xmlFiles/index.xml'  # The destination path in the repo


# authenticate to GitHub using the access token
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# read the contents of the XML file
with open(FILE_PATH, 'r') as file:
    content = file.read()

# check if the file already exists in the repo
try:
    contents = repo.get_contents(TARGET_PATH, ref=BRANCH_NAME)
    
    # If the file exists, update it -- really just replaces the contents
    repo.update_file(contents.path, "Updating XML file", content, contents.sha, branch=BRANCH_NAME)
    print(f"Updated {TARGET_PATH} in {REPO_NAME} on branch {BRANCH_NAME}.")
except:
    # create a new file
    repo.create_file(TARGET_PATH, "Adding new XML file", content, branch=BRANCH_NAME)
    print(f"Created {TARGET_PATH} in {REPO_NAME} on branch {BRANCH_NAME}.")
