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

PHOTO = "https://telegra.ph/file/43d9fb78973ec724c41e5.jpg"

network_name = NETWORK_USERNAME.lower()

if network_name == "Anteiku_cafe_fed":
    def anteiku(update: Update, context: CallbackContext):

        TEXT = f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [ΛПƬΣ𝐈𝐊Ц Federations](https://t.me/Anteiku_cafe_fed/47),
ΛПƬΣ𝐈𝐊Ц ɪꜱ ᴀɴ ᴀɴɪᴍᴇ ʙᴀꜱᴇᴅ ʟᴇᴀɢᴜᴇ ᴏꜰ ɢʀᴇᴀᴛ ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴏʀꜱ 
ᴀɴᴅ ᴅɪʟɪɢᴇɴᴛ ɢᴜʏꜱ ᴄᴏɴꜱɪꜱᴛᴇɴᴛʟʏ ᴡᴏʀᴋɪɴɢ ꜰᴏʀ ᴀ ᴍᴏᴛɪᴠᴇ ᴛᴏ ꜱᴛᴏᴘ ᴛʜᴇ 
ᴛᴏxɪᴄɪᴛʏ ᴀɴᴅ ꜱᴘʀᴇᴀᴅ ʟᴏᴠᴇ, ᴘᴇᴀᴄᴇ ᴀɴᴅ ʜᴀʀᴍᴏɴʏ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ. 
ᴏᴜʀ ᴍᴏᴛᴛᴏ ɪꜱ - ꜱᴇʀᴇɴɪᴛʏ ᴀʙᴏᴠᴇ ɢʀᴇᴀᴛɴᴇꜱꜱ. ᴅɪɢ ɪɴᴛᴏ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ 
ᴀɴᴅ ɢʀᴏᴜᴘꜱ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴀɴᴅ ᴊᴏɪɴ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ 
ɪꜰ ɪᴛ ᴀᴄᴄᴇɴᴛᴜᴀᴛᴇꜱ ᴛʜᴇ ᴘᴜʀᴘᴏꜱᴇ.
"""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="ΛПƬΣ𝐈𝐊Ц Federations", url="https://t.me/Anteiku_cafe_fed/47")],
                    [
                    InlineKeyboardButton(text="ᴜꜱᴇʀ ᴛᴀɢ", url="https://t.me/Anteiku_cafe_fed/38"),
                    InlineKeyboardButton(text="ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘ", url="https://t.me/Anteiku_cafe_fed")
                    ],
                ]
            ),
        )


    anteiku_handler = CommandHandler(("anteiku", "federation", "net"), anteiku, run_async = True)
    dispatcher.add_handler(anteiku_handler)

    __help__ = """
    ──「ΛПƬΣ𝐈𝐊Ц Federations」──                         
    
    ❂ /anteiku : Get information about our community! Using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "ΛПƬΣ𝐈𝐊Ц "
