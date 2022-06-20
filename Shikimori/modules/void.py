from Shikimori import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/ef075f11c9d091b1cafa0.jpg"



def kaizen(update: Update, context: CallbackContext):

    TEXT = f"Welcome to **[【ᴋᴀɪᴢᴇɴ】 ✧Network✧](https://t.me/Kaizen_Network)** \n\n◈ Kaizen is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈"

    update.effective_message.reply_photo(
        PHOTO, caption= TEXT,
        parse_mode=ParseMode.MARKDOWN,

            reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(text="【About ᴋᴀɪᴢᴇɴ】", url="https://t.me/Kaizen_Network/8"),
                InlineKeyboardButton(text="【Owner Sama】", url="https://t.me/Just_itachi_uchiha")
                ],
                [InlineKeyboardButton(text="【ᴋᴀɪᴢᴇɴ】Network", url="https://t.me/Kaizen_Network")]
            ]
        ),
    )


void_handler = CommandHandler("kaizen", kaizen, run_async = True)
dispatcher.add_handler(kaizen_handler)

__help__ = """
 ──「Kaizen Network」──                         
 
❂ /kaizen: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
   
__mod_name__ = "【Kaizen】"
