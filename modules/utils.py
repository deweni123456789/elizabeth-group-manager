# shared helpers
from pyrogram.types import Message

async def reply_text_or_chat(msg: Message, text: str):
    try:
        await msg.reply_text(text)
    except:
        await msg.chat.send_message(text)
