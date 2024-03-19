import logging_setup

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "defaultFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - Line: %(lineno)d"
        },
        "customFormatter": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M"
        }
    },
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "defaultFormatter",
            "filename": "error_logs.txt"
        },
        "discordHandler": {
            "class": "logging_setup.DiscordHandler",
            "level": "INFO",
            "formatter": "customFormatter",
            "filters": ["messageFilter"],
            "webhook_url": "https://discord.com/api/webhooks/1219748387084308686/4YSc9snTiKezv9rioGeQKIY6JN3AwJmijsdhnsWOe2XWS70VhA1vRrrcDYliHvW38E8N"
        }
    },
    "filters": {
        "messageFilter": {
            "()": "logging_setup.MessageFilter",
            "words_to_filter": ["password", "secret"]
        }
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["fileHandler", "discordHandler"]
        }
    }
}

