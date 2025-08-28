from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import config

def register(app):
    @app.on_message(filters.private)
    async def force_sub(client, message: Message):
        user = message.from_user
        try:
            member = await client.get_chat_member(config.FORCE_CHANNEL, user.id)
            if member.status in ["member", "administrator", "creator"]:
                return
        except:
            pass
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Join Channel ✅", url=f"https://t.me/{config.FORCE_CHANNEL.lstrip('@')}")]]
        )
        await message.reply_text("You must join our channel to use the bot!", reply_markup=keyboard)
