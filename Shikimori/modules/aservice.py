# Written By SOME-1HING for Shikimori
# Kang With Proper Credits

import asyncio
from pyrogram import filters

from Shikimori import DRAGONS, pbot
import Shikimori.modules.sql.antiservice_sql as sql
import re
import html
from telegram import ParseMode
from telegram import (CallbackQuery, Chat, MessageEntity, InlineKeyboardButton,
                      InlineKeyboardMarkup, Message, ParseMode, Update, Bot, User)
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler)
from telegram.utils.helpers import mention_html

from Shikimori.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from Shikimori import  dispatcher
from Shikimori.modules.log_channel import loggable

__mod_name__ = "AntiService"
__help__ = """
Plugin to delete service messages in a chat!

/antiservice
"""



@user_admin_no_reply
@loggable
def aservice_rem(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"aservice_rem\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = sql.rem_aservice(chat.id)
        if is_kuki:
            is_kuki = sql.rem_aservice(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"ANTI_SERVICE_DISABLED\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                f"Disabled AntiService System. I won't Be Deleting Service Message from Now on.",
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin_no_reply
@loggable
def aservice_add(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"aservice_add\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = sql.set_aservice(chat.id)
        if is_kuki:
            is_kuki = sql.set_aservice(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"ANTI_SERVICE_ENABLE\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                f"Enabled AntiService System. I will Delete Service Messages from Now on.",
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin
@loggable
def aservice(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message
    msg = "Choose an option"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Enable",
            callback_data="aservice_add({})")],
       [
        InlineKeyboardButton(
            text="Disable",
            callback_data="aservice_rem({})")]])
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


@pbot.on_message(filters.service)
async def del_service(_, message):
    chat_id = message.chat.id
    try:
        is_aservice = sql.is_aservice(chat_id)
        if is_aservice:
            await asyncio.sleep(10)
            await message.delete()
    except Exception as e:
        print("anti-service - " + str(e))


ANTISERVICE_HANDLER = CommandHandler("antiservice", aservice, run_async = True)
ADD_ASERVICE_HANDLER = CallbackQueryHandler(aservice_add, pattern=r"aservice_add", run_async = True)
RM_ASEVICE_HANDLER = CallbackQueryHandler(aservice_rem, pattern=r"aservice_rem", run_async = True)

dispatcher.add_handler(ADD_ASERVICE_HANDLER)
dispatcher.add_handler(ANTISERVICE_HANDLER)
dispatcher.add_handler(RM_ASEVICE_HANDLER)

__handlers__ = [
    ADD_ASERVICE_HANDLER,
    ANTISERVICE_HANDLER,
    RM_ASEVICE_HANDLER,
]