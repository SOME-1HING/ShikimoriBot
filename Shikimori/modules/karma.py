"""
STATUS: Code is working. ✅
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
import re
import html
from Shikimori.modules.sql import log_channel_sql as logsql
from telegram import ParseMode
from telegram import (CallbackQuery, Chat, InlineKeyboardButton,
                      InlineKeyboardMarkup, ParseMode, Update, User)
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler)
from telegram.utils.helpers import mention_html

from Shikimori.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from Shikimori import  dispatcher
from Shikimori.modules.log_channel import loggable

import asyncio
from pyrogram import filters

from Shikimori import DRAGONS, pbot as app, BOT_ID
import Shikimori.modules.sql.karma_sql as sql
from Shikimori.ex_plugins.dbfunctions import (
    alpha_to_int,
    get_karma,
    get_karmas,
    int_to_alpha,
    is_karma_on,
    karma_off,
    karma_on,
    update_karma,
)      
from Shikimori.utils.filter_groups import karma_negative_group, karma_positive_group
from Shikimori.core.decorators.errors import capture_err

regex_upvote = r"^((?i)\+|\+\+|\+1|thx|thanx|thanks|pro|cool|good|pro|pero|op|nice|noice|best|uwu|owo|right|correct|peru|piro|👍)$"
regex_downvote = r"^(\-|\-\-|\-1|👎|noob|baka|idiot|chutiya|nub|noob|wrong|incorrect|chaprii|chapri|weak)$"




@app.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_upvote)
    & ~filters.via_bot
    & ~filters.bot,
    group=karma_positive_group,
)
@capture_err
async def upvote(_, message):
    chat_id = message.chat.id
    is_karma = sql.is_karma(chat_id)
    if not is_karma:
        return
    if not message.reply_to_message.from_user:
        return
    if not message.from_user:
        return
    if message.reply_to_message.from_user.id == message.from_user.id:
        return
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(
        chat_id, await int_to_alpha(user_id)
    )
    if current_karma:
        current_karma = current_karma['karma']
        karma = current_karma + 1
    else:
        karma = 1
    new_karma = {"karma": karma}
    await update_karma(
        chat_id, await int_to_alpha(user_id), new_karma
    )
    await message.reply_text(
        f"Incremented Karma of {user_mention} By 1 \nTotal Points: {karma}"
    )

@app.on_message(

    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_downvote)
    & ~filters.via_bot
    & ~filters.bot,
    group=karma_negative_group,
)
@capture_err
async def downvote(_, message):
    is_karma = sql.is_karma(chat_id)
    if not is_karma:
        return
    if not message.reply_to_message.from_user:
        return
    if not message.from_user:
        return
    if message.reply_to_message.from_user.id == message.from_user.id:
        return

    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
    if current_karma:
        current_karma = current_karma["karma"]
        karma = current_karma - 1
    else:
        karma = 1
    new_karma = {"karma": karma}
    await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
    await message.reply_text(
        f"Decremented Karma Of {user_mention} By 1 \nTotal Points: {karma}"
    )


@app.on_message(filters.command("karmastat") & filters.group)
@capture_err
async def karma(_, message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        m = await message.reply_text("`Analyzing Karma...Will Take 10 Seconds`")
        karma = await get_karmas(chat_id)
        if not karma:
            await m.edit("No karma in DB for this chat.")
            return
        msg = f"**Karma list of {message.chat.title}:- **\n"
        limit = 0
        karma_dicc = {}
        for i in karma:
            user_id = await alpha_to_int(i)
            user_karma = karma[i]["karma"]
            karma_dicc[str(user_id)] = user_karma
            karma_arranged = dict(
                sorted(karma_dicc.items(), key=lambda item: item[1], reverse=True)
            )
        if not karma_dicc:
            await m.edit("No karma in DB for this chat.")
            return
        for user_idd, karma_count in karma_arranged.items():
            if limit > 9:
                break
            try:
                user = await app.get_users(int(user_idd))
                await asyncio.sleep(0.8)
            except Exception:
                continue
            first_name = user.first_name
            if not first_name:
                continue
            username = user.username
            msg += f"**{karma_count}**  {(first_name[0:12] + '...') if len(first_name) > 12 else first_name}  `{('@' + username) if username else user_idd}`\n"
            limit += 1
        await m.edit(msg)
    else:
        user_id = message.reply_to_message.from_user.id
        karma = await get_karma(chat_id, await int_to_alpha(user_id))
        karma = karma["karma"] if karma else 0
        await message.reply_text(f"**Total Points**: __{karma}__")

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
        is_kuki = sql.rem_karma(chat.id)
        if is_kuki:
            is_kuki = sql.rem_karma(user_id)
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
        is_kuki = sql.set_karma(chat.id)
        if is_kuki:
            is_kuki = sql.set_karma(user_id)
            LOG = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"KARMA_ENABLE\n"
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

KARMA_STATUS_HANDLER = CommandHandler("antichannel", karma_status, run_async = True)
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

__mod_name__ = "Karma ☯️"
__help__ = """
*Karma*
 ❍ `/karma` [ON][OFF]: To enable / disable Karma system
 ❍ `/karmastat`: Get stats of karma for your chat
 ❍ Reply to any meassage with (`+, +1, thx, thanx, thanks, pro, cool, good,pro, pero, op, nice, noice, best, uwu, owo, right, correct, peru, piro`, 👍) to increse karma of user.
 ❍ Reply to any meassage with (`-, -1, 👎, noob, baka, idiot, chutiya, nub, noob, wrong, incorrect, chaprii, chapri, weak`) to decrease karma of user.
"""
