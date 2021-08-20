import os

import requests

# Environments for telegram bot
TOKEN = os.environ['INPUT_TOKEN']
CHAT_ID = os.environ['INPUT_TO']
MESSAGE = os.environ['INPUT_MESSAGE']
PAGE_PREVIEW = os.environ['INPUT_DISABLE_WEB_PAGE_PREVIEW']
BRANCH_NAME = os.environ['BRANCH_NAME']

# Static request
REQUEST = f'https://api.telegram.org/bot{TOKEN}/'


# def check_branch_name(branch_name):
#     if branch_name != 'master' or branch_name != '1.10'

def send_message(chat_id, message,
                 disable_web_page_preview=False, markdown='MakrdownV2'):
    edit_message = message.replace('-', '\\-').replace('_', '\\_')

    print(os.environ["GITHUB_REF"])

    send_message_url = REQUEST + 'sendMessage'
    send_message_data = {
        'chat_id': chat_id,
        'parse_mode': markdown,
        'disable_web_page_preview': disable_web_page_preview,
        'text': edit_message,
    }

    response = requests.post(send_message_url, send_message_data)
    print(response.json())
    return response.json()


if __name__ == '__main__':
    send_message(CHAT_ID, MESSAGE, PAGE_PREVIEW)
