from pyrogram import filters
from pyrogram.types import Message
import re
import config

# Example: bad words list
BAD_WORDS = ["badword1", "badword2", "spamword"]

def register(app):
    @app.on_message(filters.group)
    async def automod_filter(client, message: Message):
        # Skip admins
        if message.from_user and message.from_user.id in config.ADMIN_USERS:
            return

        # 1️⃣ Check for bad words
        text = message.text or ""
        if any(bad_word.lower() in text.lower() for bad_word in BAD_WORDS):
            try:
                await message.delete()
                await message.reply_text(f"⚠️ {message.from_user.mention}, your message contains banned words!")
            except:
                pass
            return

        # 2️⃣ Check for links (basic)
        if re.search(r"(https?://|t\.me/)", text):
            try:
                await message.delete()
                await message.reply_text(f"⚠️ {message.from_user.mention}, links are not allowed!")
            except:
                pass
            return

        # 3️⃣ Example: spam detection (long repeated text)
        if len(text) > 300:  # very long message
            try:
                await message.delete()
                await message.reply_text(f"⚠️ {message.from_user.mention}, message too long!")
            except:
                pass
