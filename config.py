import os

API_ID = int(os.getenv("API_ID", 5047271))
API_HASH = os.getenv("API_HASH", "047d9ed308172e637d4265e1d9ef0c27")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8400227620:AAEje87350ILP5lJxMeb57rOn9K8yBY1f2o")
ADMIN_USERS = {int(x) for x in os.getenv("ADMIN_USERS","").split(",") if x}
FORCE_CHANNEL = os.getenv("FORCE_CHANNEL", "@Slmusicmania")
LOG_CHAT_ID = int(os.getenv("LOG_CHAT_ID", 0))

ENABLE_WELCOME = os.getenv("ENABLE_WELCOME", "1") == "1"
ENABLE_AUTOMOD = os.getenv("ENABLE_AUTOMOD", "1") == "1"
