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

import time
from Shikimori.modules.helper_funcs.readable_time import get_readable_time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.utils.helpers import escape_markdown
from telegram.ext import CallbackContext, CallbackQueryHandler
from Shikimori.vars import ANIME_NAME, BOT_USERNAME, NETWORK, NETWORK_USERNAME, PM_START_TEXT, START_MEDIA, SUPPORT_CHAT, UPDATE_CHANNEL
from Shikimori import StartTime, dispatcher
import Shikimori.modules.sql.users_sql as sql

bot_name = f"{dispatcher.bot.first_name}"

IMG_START = START_MEDIA.split(".")
start_id = IMG_START[-1]

buttons = [
    [
        InlineKeyboardButton(
            text=f" Add {bot_name} to your Group", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="❓About", callback_data="Shikimori_"),
        InlineKeyboardButton(text=" 💬Commands", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="🚨Support Grp", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="❗Updates", url=f"https://t.me/{UPDATE_CHANNEL}"),
   
    ], 
]

network_name = NETWORK_USERNAME.lower()

try:
    if network_name == "uchihaxnetwork":
        HMMM = InlineKeyboardButton(text="❟❛❟ 𝖀𝖈𝖍𝖎𝖍𝖆 ❟❛❟ 𝙉𝙚𝙩𝙬𝙤𝙧𝙠", callback_data="sern_")
    elif NETWORK:
        HMMM = InlineKeyboardButton(text=f"{NETWORK}", url=f"https://t.me/{NETWORK_USERNAME}")
    else:
        HMMM = None
except:
    HMMM = None

def Shikimori_about_callback(update, context):
    query = update.callback_query
    if query.data == "Shikimori_":
        query.message.edit_text(
            text=f"๏ I'm *{bot_name}*, a powerful group management bot built to help you manage your group easily."
            "\n• I can restrict users."
            "\n• I can greet users with customizable welcome messages and even set a group's rules."
            "\n• I have an advanced anti-flood system."
            "\n• I can warn users until they reach max warns, with each predefined actions such as ban, mute, kick, etc."
            "\n• I have a note keeping system, blacklists, and even predetermined replies on certain keywords."
            "\n• I check for admins' permissions before executing any command and more stuffs",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="Github", callback_data="github_"),
                    InlineKeyboardButton(text="License", callback_data="license_"),
                    ],
                    [
                    HMMM,
                    InlineKeyboardButton(text="Documentation", url="https://some1hing.gitbook.io/shikimori-bot/"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="home_"),
                    ],
                ]
            ),
        )

def git_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "github_":
        query.message.edit_text(
            text=f"Orginal Repositiory created by [SOME1HING](https://github.com/SOME-1HING) on [github](https://github.com/SOME-1HING/ShikimoriBot) for [Shikimori Bot](https://t.me/micchon_shikimori_bot)",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="Repo", url="https://github.com/SOME-1HING/ShikimoriBot"),
                    InlineKeyboardButton(text="Creator", url="https://github.com/SOME-1HING"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_"),
                    ],
                ]
            ),
        )
def home_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "home_":
        first_name = update.effective_user.first_name
        users = f"{sql.num_users}"
        uptime = get_readable_time((time.time() - StartTime))
        chats = f"{sql.num_chats}"
        first_name = update.effective_user.first_name
        start_text = PM_START_TEXT.format(escape_markdown(first_name), bot_name, ANIME_NAME, users, chats, uptime)
        query.message.delete()
        try:
            if start_id in ("jpeg", "jpg", "png"):
                query.edit_photo(
                    START_MEDIA, caption = start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
            )
            elif start_id in ("mp4", "mkv"):
                update.effective_message.reply_video(
                START_MEDIA, caption = start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
            )
            elif start_id in ("gif", "webp"):
                update.effective_message.reply_animation(
                START_MEDIA, caption = start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
            )
            else:
                update.effective_message.reply_text(start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,)

        except:
            update.effective_message.reply_text(start_text, reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,)
    

def sern_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "sern_":
        query.message.edit_text(
            text=f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [❟❛❟ 𝖀𝖈𝖍𝖎𝖍𝖆 ❟❛❟ 𝘕𝘌𝘛𝘞𝘖𝘙𝘒](https://t.me/UchihaXNetwork/70),
𝖀𝖈𝖍𝖎𝖍𝖆 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤 𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙂𝙤 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮, 𝙞𝙛 𝙞𝙩 𝙙𝙧𝙖𝙬𝙨 𝙮𝙤𝙪𝙧 𝙖𝙩𝙩𝙚𝙣𝙩𝙞𝙤𝙣.""", parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=False,
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

def license_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "license_":
        query.message.edit_text(
            text=f"\n\n_{bot_name}'s licensed under the GNU General Public License v3.0_",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="License", url="https://github.com/SOME-1HING/ShikimoriBot/blob/master/LICENSE"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_"),
                    ],
                ]
            ),
        )

about_callback_handler = CallbackQueryHandler(
        Shikimori_about_callback, pattern=r"Shikimori_", run_async=True
    )
license_call_back_handler = CallbackQueryHandler(
    license_call_back, pattern=r"license_", run_async=True
)
git_call_back_handler = CallbackQueryHandler(
    git_call_back, pattern=r"github_", run_async=True
)
sern_call_back_handler = CallbackQueryHandler(
    sern_call_back, pattern=r"sern_", run_async=True
)
home_handler = CallbackQueryHandler(
    home_back, pattern=r"home_", run_async=True
)

dispatcher.add_handler(sern_call_back_handler)
dispatcher.add_handler(home_handler)
dispatcher.add_handler(git_call_back_handler)
dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(license_call_back_handler)
