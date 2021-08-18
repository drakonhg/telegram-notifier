import os

import requests

# Environments for telegram bot
TOKEN = os.environ['INPUT_TOKEN']
CHAT_ID = os.environ['INPUT_TO']
MESSAGE = os.environ['INPUT_MESSAGE']
PAGE_PREVIEW = os.environ['INPUT_DISABLE_WEB_PAGE_PREVIEW']


# Static request
REQUEST = f'https://api.telegram.org/bot{TOKEN}/'


def send_message(chat_id, message,
                 disable_web_page_preview=False, markdown='MakrdownV2'):
    edit_message = message.replace('-', '\\-').replace('_', '\\_')

    send_message_url = REQUEST + 'sendMessage'
    send_message_data = {
        'chat_id': chat_id,
        'parse_mode': 'MarkdownV2',
        'disable_web_page_preview': disable_web_page_preview,
        'text': edit_message,
    }

    response = requests.post(send_message_url, send_message_data)
    print(response.json())
    return response.json()


if __name__ == '__main__':
    send_message(CHAT_ID, MESSAGE, PAGE_PREVIEW)
