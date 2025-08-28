import os

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_USERS = {int(x) for x in os.getenv("ADMIN_USERS","").split(",") if x}
FORCE_CHANNEL = os.getenv("FORCE_CHANNEL", "@YourChannel")
LOG_CHAT_ID = int(os.getenv("LOG_CHAT_ID", 0))

ENABLE_WELCOME = os.getenv("ENABLE_WELCOME", "1") == "1"
ENABLE_AUTOMOD = os.getenv("ENABLE_AUTOMOD", "1") == "1"
