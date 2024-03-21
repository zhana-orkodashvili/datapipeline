import logging
from logging_custom import DiscordHandler
from logging_custom import MessageFilter

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - Line: %(lineno)d"
)

# Formatters
default_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - Line: %(lineno)d")
custom_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# The root logger
root_logger = logging.getLogger()

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(custom_formatter)
root_logger.addHandler(console_handler)

# File handler for all logs
all_logs_file_handler = logging.FileHandler(filename="logs.log")
all_logs_file_handler.setLevel(logging.DEBUG)
all_logs_file_handler.setFormatter(default_formatter)
root_logger.addHandler(all_logs_file_handler)

# File handler for only error level logs
errors_file_handler = logging.FileHandler(filename="error_logs.txt")
errors_file_handler.setLevel(logging.ERROR)
errors_file_handler.setFormatter(default_formatter)
root_logger.addHandler(errors_file_handler)

# Discord handler
discord_webhook_url = "https://discord.com/api/webhooks/1219748387084308686/4YSc9snTiKezv9rioGeQKIY6JN3AwJmijsdhnsWOe2XWS70VhA1vRrrcDYliHvW38E8N"
discord_handler = DiscordHandler(discord_webhook_url)
discord_handler.setLevel(logging.INFO)
discord_handler.setFormatter(custom_formatter)
discord_handler.addFilter(MessageFilter(["password", "secret"]))
root_logger.addHandler(discord_handler)
