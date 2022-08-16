"""
STATUS: Code check is pending.
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

import html

from telegram import Update
from telegram.ext import CallbackContext, Filters
from telegram.utils.helpers import mention_html

from Shikimori.modules.log_channel import loggable
from Shikimori.modules.helper_funcs.decorators import Shikimoricmd

import Shikimori.modules.sql.logger_sql as sql
from Shikimori.modules.helper_funcs.anonymous import user_admin as u_admin, AdminPerms


@Shikimoricmd(command="announce", pass_args=True)
@u_admin(AdminPerms.CAN_CHANGE_INFO)
@loggable
def announcestat(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    if chat.type == "private":
        return
    args = context.args
    if len(args) > 0:
        u = update.effective_user
        message = update.effective_message
        user = update.effective_user
        if args[0].lower() in ["on", "yes", "true"]:
            sql.enable_chat_log(update.effective_chat.id)
            update.effective_message.reply_text(
                "I've enabled announcemets in this group. Now any admin actions in your group will be announced."
            )
            logmsg = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"#ANNOUNCE_TOGGLED\n"
                f"Admin actions announcement has been <b>enabled</b>\n"
                f"<b>Admin:</b> {mention_html(user.id, user.first_name) if not message.sender_chat else message.sender_chat.title}\n "
            )
            return logmsg
        elif args[0].lower() in ["off", "no", "false"]:
            sql.disable_chat_log(update.effective_chat.id)
            update.effective_message.reply_text(
                "I've disabled announcemets in this group. Now admin actions in your group will not be announced."
            )
            logmsg = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"#ANNOUNCE_TOGGLED\n"
                f"Admin actions announcement has been <b>disabled</b>\n"
                f"<b>Admin:</b> {mention_html(user.id, user.first_name) if not message.sender_chat else message.sender_chat.title}\n "
            )
            return logmsg
    else:
        update.effective_message.reply_text(
            "Give me some arguments to choose a setting! on/off, yes/no!\n\n"
            "Your current setting is: {}\n"
            "When True, any admin actions in your group will be announced."
            "When False, admin actions in your group will not be announced.".format(
                sql.does_chat_log(update.effective_chat.id))
        )
        return ''


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)
