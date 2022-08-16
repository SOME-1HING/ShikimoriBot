# Written By SOME-1HING for Shikimori
# Kang With Proper Credits


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


import re
import Shikimori.modules.sql.karma_sql as ksql
from Shikimori.modules.sql import log_channel_sql as logsql
import html
from telegram import ParseMode
from telegram import (CallbackQuery, Chat, InlineKeyboardButton,
                      InlineKeyboardMarkup, ParseMode, Update, User)
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler)
from telegram.utils.helpers import mention_html

from Shikimori.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from Shikimori import  dispatcher
from Shikimori.modules.log_channel import loggable



@user_admin_no_reply
@loggable
def rem_karma(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    bot = context.bot
    match = re.match(r"rem_karma\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = ksql.rem_karma(chat.id)
        if is_kuki:
            is_kuki = ksql.rem_karma(user_id)
            LOG = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"KARMA_DISABLED\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
            log_channel = logsql.get_chat_log_channel(chat.id)
            if log_channel:
                return bot.send_message(
                log_channel,
                LOG,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
            return
        else:
            update.effective_message.edit_text(
                f"Disabled Karma System.",
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin_no_reply
@loggable
def add_karma(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    bot = context.bot
    match = re.match(r"add_karma\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = ksql.set_karma(chat.id)
        if is_kuki:
            is_kuki = ksql.set_karma(user_id)
            LOG =f"""
<b>{html.escape(chat.title)}:</b>\n"
KARMA_ENABLE\n"
<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"""
            log_channel = logsql.get_chat_log_channel(chat.id)
            if log_channel:
                return bot.send_message(
                log_channel.id,
                LOG,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
            return
        else:
            update.effective_message.edit_text(
                f"Enabled Karma System.",
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin
@loggable
def karma_status(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message
    msg = "Choose an option"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Enable",
            callback_data="add_karma({})")],
       [
        InlineKeyboardButton(
            text="Disable",
            callback_data="rem_karma({})")]])
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )

KARMA_STATUS_HANDLER = CommandHandler("karma", karma_status, run_async = True)
ADD_KARMA_HANDLER = CallbackQueryHandler(add_karma, pattern=r"add_karma", run_async = True)
RM_KARMA_HANDLER = CallbackQueryHandler(rem_karma, pattern=r"rem_karma", run_async = True)

dispatcher.add_handler(ADD_KARMA_HANDLER)
dispatcher.add_handler(KARMA_STATUS_HANDLER)
dispatcher.add_handler(RM_KARMA_HANDLER)

__handlers__ = [
    ADD_KARMA_HANDLER,
    KARMA_STATUS_HANDLER,
    RM_KARMA_HANDLER,
]