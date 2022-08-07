"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

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

PHOTO = "https://telegra.ph/file/7cb643db87efa3a111744.jpg"

network_name = NETWORK_USERNAME.lower()

if network_name == "uchihaxnetwork":
    def uchiha(update: Update, context: CallbackContext):

        TEXT = f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [❟❛❟ 𝖀𝖈𝖍𝖎𝖍𝖆 ❟❛❟ 𝘕𝘌𝘛𝘞𝘖𝘙𝘒](https://t.me/UchihaXNetwork/70),
𝖀𝖈𝖍𝖎𝖍𝖆 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤 𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙂𝙤 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮, 𝙞𝙛 𝙞𝙩 𝙙𝙧𝙖𝙬𝙨 𝙮𝙤𝙪𝙧 𝙖𝙩𝙩𝙚𝙣𝙩𝙞𝙤𝙣.
"""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="❟❛❟ 𝖀𝖈𝖍𝖎𝖍𝖆 ❟❛❟ 𝙉𝙚𝙩𝙬𝙤𝙧𝙠", url="https://t.me/UchihaXNetwork/70")],
                    [
                    InlineKeyboardButton(text="★彡[ᴜꜱᴇʀ ᴛᴀɢ]彡★", url="https://t.me/UchihaXNetwork/74"),
                    InlineKeyboardButton(text="★彡[ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘ]彡★", url="https://t.me/Uchihashrine")
                    ],
                ]
            ),
        )


    uchiha_handler = CommandHandler(("uchiha", "network", "net"), uchiha, run_async = True)
    dispatcher.add_handler(uchiha_handler)

    __help__ = """
    ──「❟❛❟ 𝖀𝖈𝖍𝖎𝖍𝖆 ❟❛❟ 𝘕𝘌𝘛𝘞𝘖𝘙𝘒」──                         
    
    ❂ /uchiha: Get information about our community! Using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "❟❛❟ 𝖀𝖈𝖍𝖎𝖍𝖆 ❟❛❟"
