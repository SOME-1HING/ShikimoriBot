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
from pyrogram import filters

from Shikimori import dispatcher, pbot
from Shikimori.modules.disable import DisableAbleCommandHandler
from Shikimori.modules.helper_funcs.anonymous import user_admin
from Shikimori.modules.sql.antichannel_sql import antichannel_status, disable_antichannel, enable_antichannel
from Shikimori.modules.log_channel import loggable

@user_admin
@loggable
@pbot.on_message(filters.command("antichannel"))
async def set_antichannel(_, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        await message.reply_text("This command only works in groups.")
        return
    if len(message.command) < 2:
        return await message.reply_text(
        f"Antichannel setting is currently {antichannel_status(chat_id)}\n\n**Usage:**\n/antichannel [ON/OFF]"
    )
    query = message.text.strip().split(None, 1)[1]
    query = query.lower()
    if ["on", "enable", "yes"] in query:
        enable_antichannel(chat_id)
        await message.reply_text(f"Enabled antichannel!!")
        return
    elif ["off", "disable", "no"] in query:
        enable_antichannel(chat_id)
        await message.reply_text(f"Disabled antichannel!!")
    else:
        return await message.reply_text("**Usage:**\n/antichannel [ON/OFF]")

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