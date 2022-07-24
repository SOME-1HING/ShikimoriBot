# This module is made by https://github.com/SOME-1HING/

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

# You are free to use this module. But don't delete this commented text. Thank you.

from Shikimori import dispatcher, MEDIA_BYE, MEDIA_GM, MEDIA_GN, MEDIA_HELLO
import Shikimori.modules.sql.chatbot_sql as sql
from telegram import ParseMode
from telegram.ext import Filters, MessageHandler
import time

IMG_GM = MEDIA_GM.split(".")
gm_id = IMG_GM[-1]

IMG_GN = MEDIA_GM.split(".")
gn_id = IMG_GN[-1]

IMG_HELLO = MEDIA_HELLO.split(".")
hello_id = IMG_HELLO[-1]

IMG_BYE = MEDIA_BYE.split(".")
bye_id = IMG_BYE[-1]

def goodnight(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    chat_id = update.effective_chat.id
    is_kuki = sql.is_kuki(chat_id)
    if not is_kuki:
        return
    try:
        if gn_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_GN, caption = f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gn_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_GN, caption = f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gn_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_GN, caption = f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Good Night:* {user1}"
            message.reply_text(reply)

    except:
        reply = f"*Good Night:* {user1}"
        message.reply_text(reply)

    time.sleep(5)


def goodmorning(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    chat_id = update.effective_chat.id
    is_kuki = sql.is_kuki(chat_id)
    if not is_kuki:
        return
    try:
        if gm_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_GM, caption = f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_GM, caption = f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_GM, caption = f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Good Morning:* {user1}"
            message.reply_text(reply)
    except:
        reply = f"*Good Morning:* {user1}"
        message.reply_text(reply)
    
    time.sleep(5)

def hello(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    chat_id = update.effective_chat.id
    is_kuki = sql.is_kuki(chat_id)
    if not is_kuki:
        return
    try:
        if hello_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_HELLO, caption = f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif hello_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_HELLO, caption = f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif hello_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_HELLO, caption = f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Hello* {user1}"
            message.reply_text(reply)
    except:
        reply = f"*Hello* {user1}"
        message.reply_text(reply)

    time.sleep(5)

def bye(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    chat_id = update.effective_chat.id
    is_kuki = sql.is_kuki(chat_id)
    if not is_kuki:
        return
    try:
        if bye_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif bye_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif bye_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Bye!!* {user1}"
            message.reply_text(reply)
    except:
        reply = f"*Bye!!* {user1}"
        message.reply_text(reply)
    
    time.sleep(5)



GDMORNING_HANDLER = MessageHandler(
    Filters.regex("(?i)(good morning|goodmorning)"), goodmorning, friendly="goodmorning", run_async = True
)
GDNIGHT_HANDLER = MessageHandler(
    Filters.regex("(?i)(good night|goodnight)"), goodnight, friendly="goodnight", run_async = True
)
BYE_HANDLER = MessageHandler(
    Filters.regex("(?i)(bye|brb|afk)"), bye, friendly="bye", run_async = True
)
HELLO_HANDLER = MessageHandler(
    Filters.regex("(?i)(hello)"), hello, friendly="hello", run_async = True
)

dispatcher.add_handler(GDMORNING_HANDLER)
dispatcher.add_handler(GDNIGHT_HANDLER)
dispatcher.add_handler(HELLO_HANDLER)
dispatcher.add_handler(BYE_HANDLER)
