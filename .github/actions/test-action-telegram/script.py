import os

import requests

# Environments for telegram bot
os.environ['ANDREY'] = "ANDREY420"

TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['TO']
MESSAGE = os.environ['MESSAGE']
PAGE_PREVIEW = os.environ['DISABLE_PAGE_PREVIEW']

# GitHub environment variables
BRANCH_NAME = os.environ['GITHUB_REF']
ACTOR = os.environ['GITHUB_ACTOR']

# Static request
REQUEST = f'https://api.telegram.org/bot{TOKEN}/'


def check_branch_name(branch_name):
    """Checks branch name

    Checking branch name for particular version and tags,
    if branch name contains specific keys e.g [master, 1.10, 2., tags],
    then we should send message to the main telegram channel: @tntcore_ghactions

    Args:
        branch_name (str): String branch name that would be checked

    Returns:
        str: If branch name match,
        it is updating CHAT_ID name after parsing and validating branch name.
        Else, returning Main CHAT_ID - @tntcore_ghactions
    """
    branch_list = [
        branch_name != 'refs/heads/master',
        branch_name != 'refs/heads/1.10',
        not branch_name.startswith('refs/heads/2.'),
        not branch_name.startswith('refs/tags'),
        ]

    # Checks if any of the branch_name are matching branch_list
    if any(branch_list):
        return CHAT_ID + "_" + ACTOR
    return CHAT_ID


def send_message(chat_id, message,
                 disable_web_page_preview=False, markdown='MarkdownV2'):
    """ Sending particular message

    Sending message via telegram bot, to the channel which identified
    by chat_id (int, or username as string).

    Args:
        chat_id ():
        message (str): Message to send
        disable_web_page_preview (bool, optional): If True disable web page preview, False opposite
        markdown (str, optional): Format of message text e.g 'MarkdownV2' or 'HTML'

    Returns:
         dict: Json format of a request. If success ( 200 code ), message was sent
         successfully. Else ( 404 code ) message would not be sent due to an error.
    """

    # Edit message because of MarkdownV2 incompatibilities
    edit_message = message.replace('-', '\\-')\
        .replace('_', '\\_')\
        .replace('.', '\\.')\

    # Preparing data for request
    send_message_url = REQUEST + 'sendMessage'
    send_message_data = {
        'chat_id': chat_id,
        'parse_mode': markdown,
        'disable_web_page_preview': disable_web_page_preview,
        'text': edit_message,
    }

    # Making request to send message via telegram bot
    response = requests.post(send_message_url, send_message_data)

    print(response.json())  # Using this print to display json data

    return response.json()


if __name__ == '__main__':
    chat_id = check_branch_name(BRANCH_NAME)
    send_message(chat_id, MESSAGE, PAGE_PREVIEW,)
