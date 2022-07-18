"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits: 
    Void [https://github.com/Voidxtoxic/]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from Shikimori import NETWORK_USERNAME, dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/f9b0895ae78578fda9202.jpg"


if NETWORK_USERNAME == "VoidxNetwork":
    def void(update: Update, context: CallbackContext):

        TEXT = f"Welcome to **[【V๏ɪ፝֟𝔡】 ✧Network✧](https://t.me/voidxnetwork)** \n\n◈ Void is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈"

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="【Usertag】", url="https://t.me/void_network/103"),
                    InlineKeyboardButton(text="【Owner Sama】", url="https://t.me/voidxtoxic")
                    ],
                    [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】Network", url="https://t.me/voidxnetwork")]
                ]
            ),
        )


    void_handler = CommandHandler("void", void, run_async = True)
    dispatcher.add_handler(void_handler)

    __help__ = """
    ──「Void Network」──                         
    
    ❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "【ᴠᴏɪᴅ】"
