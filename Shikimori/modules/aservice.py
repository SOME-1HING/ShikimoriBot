# Written By SOME-1HING for Shikimori
# Kang With Proper Credits

import asyncio
from pyrogram import filters

from Shikimori import DRAGONS, pbot
from Shikimori.pyrogramee.telethonbasics import is_admin
import Shikimori.modules.sql.antiservice_sql as sql
from Shikimori.core.decorators.errors import capture_err
import json
import re
import os
import html
import requests
from Shikimori import AI_API_KEY as api

from time import sleep
from telegram import ParseMode
from telegram import (CallbackQuery, Chat, MessageEntity, InlineKeyboardButton,
                      InlineKeyboardMarkup, Message, ParseMode, Update, Bot, User)
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler,
                          DispatcherHandlerStop, Filters, MessageHandler,
                          run_async)
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.utils.helpers import mention_html, mention_markdown, escape_markdown

from Shikimori.modules.helper_funcs.filters import CustomFilters
from Shikimori.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from Shikimori import  dispatcher, updater, SUPPORT_CHAT
from Shikimori.modules.log_channel import loggable

bot_name = f"{dispatcher.bot.first_name}"

__mod_name__ = "AntiService"
__help__ = """
Plugin to delete service messages in a chat!

/antiservice [ON|OFF]
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


@pbot.on_message(filters.service & filters.group)
@capture_err
async def del_service(_, message):
    chat_id = message.chat.id
    try:
        is_aservice = sql.is_aservice(chat_id)
        if not is_aservice:
            return
        await asyncio.sleep(1)
        await message.delete()
        return

    except Exception as e:
        return print("anti-service - " + str(e))


CHATBOTK_HANDLER = CommandHandler("antiservice", aservice, run_async = True)
ADD_CHAT_HANDLER = CallbackQueryHandler(aservice_add, pattern=r"aservice_add", run_async = True)
RM_CHAT_HANDLER = CallbackQueryHandler(aservice_rem, pattern=r"aservice_rem", run_async = True)

dispatcher.add_handler(ADD_CHAT_HANDLER)
dispatcher.add_handler(CHATBOTK_HANDLER)
dispatcher.add_handler(RM_CHAT_HANDLER)

__handlers__ = [
    ADD_CHAT_HANDLER,
    CHATBOTK_HANDLER,
    RM_CHAT_HANDLER,
]