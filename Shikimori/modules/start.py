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
import re
from Shikimori.__main__ import HELPABLE, IMPORTED, USER_SETTINGS, CHAT_SETTINGS
from Shikimori.modules.helper_funcs.readable_time import get_readable_time
from Shikimori import (
    dispatcher,
    StartTime,
)
from Shikimori.vars import (
    BOT_USERNAME,
    OWNER_USERNAME,
    UPDATE_CHANNEL,
    SUPPORT_CHAT,
    ANIME_NAME,
    START_MEDIA,)
from Shikimori.modules.helper_funcs.misc import paginate_modules
from Shikimori.modules.helper_funcs.chat_status import is_user_admin
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import escape_markdown

bot_name = f"{dispatcher.bot.first_name}"

IMG_START = START_MEDIA.split(".")
start_id = IMG_START[-1]

PM_START_TEXT = """
\n◍ I'ᴍ Kᴀᴏʀɪ Mɪʏᴀᴢᴏɴᴏ Fʀᴏᴍ Yᴏᴜʀ Lɪᴇ Iɴ Aᴘʀɪʟ
◍ I'ᴍ Hɪɢʜʟʏ Aᴅᴠᴀɴᴄᴇ Gʀᴏᴜᴘ Mᴀɴᴀɢᴇᴍᴇɴᴛ Bᴏᴛ 
────────────────────────
× Uᴘᴛɪᴍᴇ: {}
────────────────────────
✪ Hɪᴛ /help Tᴏ Sᴇᴇ Mʏ Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs.
"""

HELP_STRINGS = """
Click on the button bellow to get description about specifics command."""

buttons = [
    [
        InlineKeyboardButton(
            text=f"➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ ➕", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="Uᴘᴅᴀᴛᴇ", url=f"https://t.me/{UPDATE_CHANNEL}"),
    ], 
    [
        InlineKeyboardButton(text=f"Mʏ Hᴜsʙᴀɴᴅ", url=f"t.me/{OWNER_USERNAME}"),
    ],
]

def start(update: Update, context: CallbackContext):
    args = context.args
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_STRINGS)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split("_", 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id,
                    HELPABLE[mod].__help__,
                    InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="Go Back", callback_data="help_back")]]
                    ),
                )

            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, False)
                else:
                    send_settings(match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name
            uptime = get_readable_time((time.time() - StartTime))
            hmm = "◍ Hᴇʟʟᴏ *{}*!".format(escape_markdown(first_name))
            HMM = hmm + PM_START_TEXT.format(uptime)
            try:
                if start_id in ("jpeg", "jpg", "png"):
                    update.effective_message.reply_photo(
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
    else:
        start_buttons = [
                 [
                    InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
                    InlineKeyboardButton(text="Uᴘᴅᴀᴛᴇ", url=f"https://t.me/{UPDATE_CHANNEL}")
                 ]
                ]
        chat_id = update.effective_chat.id
        first_name = update.effective_user.first_name
        chat_name = dispatcher.bot.getChat(chat_id).title
        start_text= "*Hey {}, I'm here for you at {} since :* `{}`\n".format(escape_markdown(first_name), escape_markdown(chat_name), uptime)
        try:
            if start_id in ("jpeg", "jpg", "png"):
                update.effective_message.reply_photo(
                    START_MEDIA, caption = start_text, reply_markup=InlineKeyboardMarkup(start_buttons),
                parse_mode=ParseMode.MARKDOWN,
            )
            elif start_id in ("mp4", "mkv"):
                update.effective_message.reply_video(
                START_MEDIA, caption = start_text, reply_markup=InlineKeyboardMarkup(start_buttons),
                parse_mode=ParseMode.MARKDOWN,
            )
            elif start_id in ("gif", "webp"):
                update.effective_message.reply_animation(
                START_MEDIA, caption = start_text, reply_markup=InlineKeyboardMarkup(start_buttons),
                parse_mode=ParseMode.MARKDOWN,
            )
            else:
                update.effective_message.reply_text(start_text, reply_markup=InlineKeyboardMarkup(start_buttons),
                parse_mode=ParseMode.MARKDOWN,)

        except:
            update.effective_message.reply_text(start_text, reply_markup=InlineKeyboardMarkup(start_buttons),
                parse_mode=ParseMode.MARKDOWN,)

start_handler = CommandHandler("start", start, run_async=True)
dispatcher.add_handler(start_handler)

def send_settings(chat_id, user_id, user=False):
    if user:
        if USER_SETTINGS:
            settings = "\n\n".join(
                "*{}*:\n{}".format(mod.__mod_name__, mod.__user_settings__(user_id))
                for mod in USER_SETTINGS.values()
            )
            dispatcher.bot.send_message(
                user_id,
                "These are your current settings:" + "\n\n" + settings,
                parse_mode=ParseMode.MARKDOWN,
            )

        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any user specific settings available :'(",
                parse_mode=ParseMode.MARKDOWN,
            )

    else:
        if CHAT_SETTINGS:
            chat_name = dispatcher.bot.getChat(chat_id).title
            dispatcher.bot.send_message(
                user_id,
                text="Which module would you like to check {}'s settings for?".format(
                    chat_name
                ),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )
        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any chat settings available :'(\nSend this "
                "in a group chat you're admin in to find its current settings!",
                parse_mode=ParseMode.MARKDOWN,
            )

def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    dispatcher.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=keyboard,
    )