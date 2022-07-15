"""
BSD 2-Clause License

Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2021-2022, Awesome-RJ, [ https://github.com/Awesome-RJ ]
Copyright (c) 2021-2022, Yūki • Black Knights Union, [ https://github.com/Awesome-RJ/CutiepiiRobot ]

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
from telegram import Update, ParseMode
from telegram.ext import Filters, CallbackContext

from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from Shikimori.modules.helper_funcs.anonymous import user_admin
from Shikimori.modules.sql.antichannel_sql import antichannel_status, disable_antichannel, enable_antichannel
from Shikimori.modules.log_channel import loggable

@user_admin
@loggable
async def set_antichannel(update: Update, context: CallbackContext):
    chat = update.effective_chat  
    user = update.effective_user 
    message = update.effective_message 
    args = context.arg
    if update.effective_message.chat.type == "private":
            await message.reply_text(
                update.effective_message,
                "This command is meant to use in group not in PM",
            )
            return
    if len(args) > 0:
        s = args[0].lower()
        if s in ["yes", "on"]:
            enable_antichannel(chat.id)
            await message.reply_text(f"Enabled antichannel in {html.escape(chat.title)}", parse_mode=ParseMode.HTML)
        elif s in ["off", "no"]:
            disable_antichannel(chat.id)
            await message.reply_text(f"Disabled antichannel in {html.escape(chat.title)}", parse_mode=ParseMode.HTML)
        else:
            await update.effective_message.reply_text(f"Unrecognized arguments {s}")
        return
    await message.reply_text(
        f"Antichannel setting is currently {antichannel_status(chat.id)} in {html.escape(chat.title)}", parse_mode=ParseMode.HTML
    )


async def eliminate_channel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    bot = context.bot
    if not antichannel_status(chat.id):
        return
    if message.sender_chat and message.sender_chat.type == "channel" and not message.is_automatic_forward:
        await message.delete()
        sender_chat = message.sender_chat
        await bot.ban_chat_sender_chat(sender_chat_id=sender_chat.id, chat_id=chat.id)


dispatcher.add_handler(DisableAbleCommandHandler("antichannel", set_antichannel, filters=Filters.chat_type.groups))