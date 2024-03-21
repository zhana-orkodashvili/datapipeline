import logging
import requests


class DiscordHandler(logging.Handler):
    """ Discord custom handler to send logs to discord channel using webhook """
    def __init__(self, webhook_url):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record):
        log = self.format(record)
        payload = {
            "content": log
        }
        try:
            response = requests.post(self.webhook_url, data=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.handleError(record)
            print("Error sending log message to Discord: %s", str(e))



class MessageFilter(logging.Filter):
    """ Message filter function to filter out messages containing secret/private info """
    def __init__(self, words_to_filter):
        super().__init__()
        self.words_to_filter = words_to_filter

    def filter(self, record):
        for w in self.words_to_filter:
            if w.lower() in record.msg.lower():
                return False
        return True
