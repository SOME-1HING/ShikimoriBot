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

PHOTO = "https://telegra.ph/file/7fe35e97609829443206e.jpg"

network_name = NETWORK_USERNAME.lower()

if network_name == "sernxnetwork":
    def sern(update: Update, context: CallbackContext):

        TEXT = f"""
        ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ 𝘚𝘌𝘙𝘕𝘹𝘕𝘦𝘵𝘸𝘰𝘳𝘬 (http://t.me/sernxnetwork),
  𝙎𝙀𝙍𝙉 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤
𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙂𝙤 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚
            𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮,
              𝙞𝙛 𝙞𝙩 𝙙𝙧𝙖𝙬𝙨 𝙮𝙤𝙪𝙧 𝙖𝙩𝙩𝙚𝙣𝙩𝙞𝙤𝙣."""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="⡷⠂SΞЯИ⠐⢾ THE ORGANIZATION", url="https://t.me/sernxnetwork")],
                    [
                    InlineKeyboardButton(text="★彡[ᴜꜱᴇʀ ᴛᴀɢ]彡★", url="https://t.me/SERNXNETWORK/31"),
                    InlineKeyboardButton(text="★彡[ᴏᴜʀ ꜱᴛᴀꜰꜰ]彡★", url="https://t.me/SERNXNETWORK/38")
                    ],
                ]
            ),
        )


    sern_handler = CommandHandler("sern", sern, run_async = True)
    dispatcher.add_handler(sern_handler)

    __help__ = """
    ──「⡷⠂SΞЯИ⠐⢾ The Organization」──                         
    
    ❂ /sern: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "⡷⠂SΞЯИ⠐⢾"
