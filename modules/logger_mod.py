from pyrogram import filters
from pyrogram.types import Message

def register(app):
    @app.on_message()
    async def log_messages(client, message: Message):
        # Simple console log
        print(f"[LOG] {message.chat.title if message.chat else message.chat.id}: {message.text}")
