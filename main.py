from pyrogram import Client
import config
import logging

logging.basicConfig(level=logging.INFO)

app = Client(
    "bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# import all modules
from modules import (
    moderation, welcome, automod, logger_mod, filters_mod,
    infractions, captcha, starboard, scheduled_messages,
    anti_raid, backup, economy, polls_quiz,
    stickers_manager, welcome_image, music_player, force_sub
)

modules = [
    moderation, welcome, automod, logger_mod, filters_mod,
    infractions, captcha, starboard, scheduled_messages,
    anti_raid, backup, economy, polls_quiz,
    stickers_manager, welcome_image, music_player, force_sub
]

for m in modules:
    try:
        m.register(app)
        logging.info(f"Registered module: {m.__name__}")
    except Exception as e:
        logging.exception(f"Failed to register module {m.__name__}: {e}")

if __name__ == "__main__":
    logging.info("Starting bot...")
    app.run()
