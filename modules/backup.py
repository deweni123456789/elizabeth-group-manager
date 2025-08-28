from pyrogram import filters
from pyrogram.types import Message
from .utils import developer_button
import config

def register(app):
    @app.on_message(filters.private)
    async def force_sub_check(client, message: Message):
        user = message.from_user
        try:
            member = await client.get_chat_member(config.FORCE_CHANNEL, user.id)
            if member.status in ["member", "administrator", "creator"]:
                return
        except:
            pass

        await message.reply_text(
            "You must join our channel to use the bot!",
            reply_markup=developer_button()
        )
