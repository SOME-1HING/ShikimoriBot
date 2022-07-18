"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

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

import os
from time import sleep

from Shikimori import DEV_USERS, dispatcher
from Shikimori.modules.helper_funcs.extraction import extract_user
from Shikimori.modules.sql.users_sql import get_user_com_chats
from telegram import Update
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CallbackContext, CommandHandler, Filters

def get_user_common_chats(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message
    user = extract_user(msg, args)
    if not user:
        msg.reply_text("I share no common chats with the void.")
        return
    common_list = get_user_com_chats(user)
    if not common_list:
        msg.reply_text("No common chats with this user!")
        return
    name = bot.get_chat(user).first_name
    text = f"<b>Common chats with {name}</b>\n"
    for chat in common_list:
        try:
            chat_name = bot.get_chat(chat).title
            chat_limk = bot.get_chat(chat).username
            sleep(0.3)
            text += f"• Name :- {chat_name} \n Username :- @{chat_limk} \n"
        except BadRequest:
            pass
        except Unauthorized:
            pass
        except RetryAfter as e:
            sleep(e.retry_after)

    if len(text) < 4096:
        msg.reply_text(text, parse_mode="HTML")
    else:
        with open("common_chats.txt", "w") as f:
            f.write(text)
        with open("common_chats.txt", "rb") as f:
            msg.reply_document(f)
        os.remove("common_chats.txt")


COMMON_CHATS_HANDLER = CommandHandler(
    "getchats", get_user_common_chats, filters=Filters.user(DEV_USERS), run_async = True
)

dispatcher.add_handler(COMMON_CHATS_HANDLER)
