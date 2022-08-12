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
from Shikimori import ANIME_NAME, BOT_USERNAME, NETWORK, NETWORK_USERNAME, START_MEDIA, SUPPORT_CHAT, UPDATE_CHANNEL, StartTime, dispatcher

bot_name = f"{dispatcher.bot.first_name}"

PM_START_TEXT = f"""
\nI am *{bot_name}* , a group management bot based on the anime *{ANIME_NAME}*![ ]({START_MEDIA})

*Click on the Commands Button below to go through my commands.*
"""

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
    if network_name == "sernxnetwork":
        HMMM = InlineKeyboardButton(text="⡷⠂SΞЯИ⠐⢾ THE ORGANIZATION✧", callback_data="sern_")
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
                (
                    [
                    InlineKeyboardButton(text="Github", callback_data="github_"),
                    InlineKeyboardButton(text="License", callback_data="license_"),
                    ],
                    [
                    HMMM,
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_back"),
                    ],
                ]
            ),
        )

    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "Hello *{}*! Nice to meet you!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT
     
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

def git_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "github_":
        query.message.edit_text(
            text=f"Repositiory created by [Alonebots](https://github.com/Alonebots) on [github](https://github.com/Alonebots/Gojo-bot) for [GOJO Bot](https://t.me/Gojoa_satoru_bot)",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    InlineKeyboardButton(text="Creator", url="https://github.com/Alonebots"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_"),
                    ],
            )
    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "Hello *{}*! Nice to meet you!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT
    
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

def sern_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "sern_":
        query.message.edit_text(
            text=f"ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ 𝘚𝘌𝘙𝘕𝘹𝘕𝘦𝘵𝘸𝘰𝘳𝘬 (http://t.me/sernxnetwork), 𝙎𝙀𝙍𝙉 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤 𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙂𝙤 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮, 𝙞𝙛 𝙞𝙩 𝙙𝙧𝙖𝙬𝙨 𝙮𝙤𝙪𝙧 𝙖𝙩𝙩𝙚𝙣𝙩𝙞𝙤𝙣.",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=False,
            reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="⡷⠂SΞЯИ⠐⢾ THE ORGANIZATION", url="https://t.me/sernxnetwork")],
                [
                InlineKeyboardButton(text="★彡[ᴜꜱᴇʀ ᴛᴀɢ]彡★", url="https://t.me/SERNXNETWORK/31"),
                InlineKeyboardButton(text="★彡[ᴏᴜʀ ꜱᴛᴀꜰꜰ]彡★", url="https://t.me/SERNXNETWORK/38")
                ],
                [InlineKeyboardButton(text="Back", callback_data="Shikimori_")]
            ]
            ),
        )
    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "Hello *{}*! Nice to meet you!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT
    
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
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
    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "Hello *{}*! Nice to meet you!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT
    
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
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

dispatcher.add_handler(sern_call_back_handler)
dispatcher.add_handler(git_call_back_handler)
dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(license_call_back_handler)
