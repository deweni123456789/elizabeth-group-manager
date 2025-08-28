from pyrogram import filters
from pyrogram.types import Message
import config

WELCOME_TEXT = "Welcome {first_name}!"

def register(app):
    if not config.ENABLE_WELCOME:
        return

    @app.on_message(filters.new_chat_members)
    async def greet(client, message: Message):
        for u in message.new_chat_members:
            await message.reply_text(WELCOME_TEXT.format(first_name=u.first_name))
