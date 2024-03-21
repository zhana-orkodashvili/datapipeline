import json
import logging
import requests


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
        for w in self.words_to_filter:
            if w in record.msg:
                return False
        return True
