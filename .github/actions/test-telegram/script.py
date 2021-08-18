import os

import requests

# Environments for telegram bot
TOKEN = os.environ['INPUT_TOKEN']
CHAT_ID = os.environ['INPUT_TO']
MESSAGE = os.environ['INPUT_MESSAGE']


# Static request
REQUEST = f'https://api.telegram.org/bot{TOKEN}/'


def send_message(chat_id, message):
    edit_message = message.replace('-', '\\-').replace('_', '\\_')

    send_message_url = REQUEST + 'sendMessage'
    send_message_data = {
        'chat_id': chat_id,
        'parse_mode': 'MarkdownV2',
        'disable_web_page_preview': 'true',
        'text': edit_message,
    }

    response = requests.post(send_message_url, send_message_data)
    print(response.json())
    return response.json()


if __name__ == '__main__':
    send_message(CHAT_ID, MESSAGE)
