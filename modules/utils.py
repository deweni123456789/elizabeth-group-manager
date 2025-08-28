from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def developer_button(text="Contact Developer"):
    """
    Returns an inline keyboard with developer contact.
    """
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text, url="https://t.me/deweni2")]]
    )
