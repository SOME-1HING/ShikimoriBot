"""
STATUS: Code check is pending.
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import html

from telegram import Update
from telegram.ext import CallbackContext
from telegram.utils.helpers import mention_html

from Shikimori.modules.log_channel import loggable
from Shikimori.modules.helper_funcs.decorators import Shikimoricmd

import Shikimori.modules.sql.logger_sql as sql
from Shikimori.modules.helper_funcs.anonymous import user_admin as u_admin, AdminPerms


@Shikimoricmd(command="announce", pass_args=True)
@u_admin(AdminPerms.CAN_CHANGE_INFO)
@loggable
def announcestat(update: Update, context: CallbackContext) -> str:
    args = context.args
    if len(args) > 0:
        u = update.effective_user
        message = update.effective_message
        chat = update.effective_chat
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
