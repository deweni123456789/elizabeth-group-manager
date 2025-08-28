from pyrogram import filters
from pyrogram.types import Message, ChatPermissions
import config

def register(app):
    @app.on_message(filters.command("ban") & filters.user(config.ADMIN_USERS))
    async def ban_user(client, message: Message):
        if not message.reply_to_message:
            await message.reply_text("Reply to a user to ban.")
            return
        target = message.reply_to_message.from_user
        await client.kick_chat_member(message.chat.id, target.id)
        await message.reply_text(f"Banned {target.mention}")
