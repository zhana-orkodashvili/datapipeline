import json
import discord
import logging

import requests

logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - Line: %(lineno)d'
)

_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d"
)

webhook_url = ("https://discord.com/api/webhooks/1219748387084308686"
               "/4YSc9snTiKezv9rioGeQKIY6JN3AwJmijsdhnsWOe2XWS70VhA1vRrrcDYliHvW38E8N")


class DiscordHandler(logging.Handler):
    def __init__(self, webhook_url):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record):
        log_entry = self.format(record)
        payload = {
            "content": log_entry
        }
        headers = {
            "Content-Type": "application/json"
        }
        requests.post(self.webhook_url, data=json.dumps(payload), headers=headers)


class MessageFilter(logging.Filter):
    def __init__(self, words_to_filter):
        super().__init__()
        self.words_to_filter = words_to_filter

    def filter(self, record):
        for word in self.words_to_filter:
            if word in record.msg:
                return False
        return True


