import os

import requests


# GitHub Environment Variables
EVENT_NAME = os.environ['GITHUB_EVENT_NAME']
BRANCH_NAME = os.environ['GITHUB_HEAD_REF']
REPOSITORY = os.environ['GITHUB_REPOSITORY']
RUN_ID = os.environ['GITHUB_RUN_ID']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

# URL to make an API request, to get JOB ID
URL = f"https://api.github.com/repos/{REPOSITORY}/actions/runs/{RUN_ID}/jobs"

# Headers to make request
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Bearer": f"{GITHUB_TOKEN}",
}


def parse_branch_name(event_name):
    """Method that gets correct branch name

    If event name is equal to pull request, then save
    initial state of branch name. Else, update branch name
    and save it to GITHUB_ENV where all GitHub environment_variables
    are stored, exclude default ones.

    Args:
        event_name (str): Event name of when workflow is running
    """
    branch_name = os.environ['GITHUB_REF']
    if event_name != 'pull_request':
        branch_name = branch_name.split('/')[-1]

    # Storing result in $GITHUB_ENV
    os.system(f"echo BRANCH_NAME={branch_name} | tee -a $GITHUB_ENV")


def get_job_id():
    """Method that gets job id

    Making an API request to api.github and getting an
    job id to directly follow to workflow run.
    Saving job id to a GITHUB_ENV
    """
    response = requests.get(URL, headers=HEADERS)  # Making an request
    JOB_ID = response.json()['jobs'][0]['id']  # Getting Job ID

    # Storing result in $GITHUB_ENV
    os.system(f'echo JOB_ID={JOB_ID} | tee -a $GITHUB_ENV')


if __name__ == '__main__':
    parse_branch_name(EVENT_NAME)
    get_job_id()
    print(os.environ.items())
