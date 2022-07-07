from os import environ


class EnvironmentConfig:
    """
    Load application environments variables
    This class can be instantiated everywhere in the program to loads the environment parameters
    """

    ENV_DELIMITER = ";"

    def __init__(self):
        self.TELEGRAM_BOT_TOKEN = environ.get("TELEGRAM_BOT_TOKEN")
        if not environ.get("TELEGRAM_BOT_TOKEN"):
            raise EnvironmentError("Missing required env TELEGRAM_BOT_TOKEN")

        # process messages only for these chat_ids, if None do not filter chat id
        self.TELEGRAM_BOT_CHAT_IDS = None
        if chat_ids := environ.get("TELEGRAM_BOT_CHAT_IDS"):
            self.TELEGRAM_BOT_CHAT_IDS = [
                int(i) for i in chat_ids.split(self.ENV_DELIMITER)
            ]

        # based keyword
        self.TELEGRAM_BOT_BASED_KEYWORDS = []
        if chat_ids := environ.get("TELEGRAM_BOT_BASED_KEYWORDS"):
            self.TELEGRAM_BOT_BASED_KEYWORDS = [
                keyword.lower() for keyword in chat_ids.split(self.ENV_DELIMITER)
            ]

        if not self.TELEGRAM_BOT_BASED_KEYWORDS:
            raise EnvironmentError("No TELEGRAM_BOT_BASED_KEYWORDS set")

        self.ENABLE_DEBUG = environ.get("ENABLE_DEBUG", "").lower() in [
            "1",
            "true",
            "t",
            "on",
            "yes",
            "y",
        ]
