# Written By SOME-1HING for Shikimori
# Kang With Proper Credits


import Shikimori.modules.sql.antichannel_sql as sql
import re
import Shikimori.modules.sql.antiservice_sql as ssql
import Shikimori.modules.sql.karma_sql as ksql
from Shikimori.modules.sql import log_channel_sql as logsql
import html
from telegram import ParseMode
from telegram import (CallbackQuery, Chat, InlineKeyboardButton,
                      InlineKeyboardMarkup, ParseMode, Update, User)
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler, MessageHandler, Filters)
from telegram.utils.helpers import mention_html

from Shikimori.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from Shikimori import  dispatcher
from Shikimori.modules.log_channel import loggable

@user_admin_no_reply
@loggable
def achannel_rem(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    bot = context.bot
    match = re.match(r"achannel_rem\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = sql.rem_achannel(chat.id)
        if is_kuki:
            is_kuki = sql.rem_achannel(user_id)
            LOG = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"ANTI_CHANNEL_DISABLED\n"
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
                f"Disabled AntiCHannel System.",
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin_no_reply
@loggable
def achannel_add(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    bot = context.bot
    match = re.match(r"achannel_add\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = sql.set_achannel(chat.id)
        if is_kuki:
            is_kuki = sql.set_achannel(user_id)
            LOG = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"ANTI_CHANNEL_ENABLE\n"
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
                f"Enabled AntiChannel System.",
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin
@loggable
def achannel(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message
    msg = "Choose an option"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Enable",
            callback_data="achannel_add({})")],
       [
        InlineKeyboardButton(
            text="Disable",
            callback_data="achannel_rem({})")]])
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )

def eliminate_channel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    bot = context.bot
    if not sql.is_achannel(chat.id):
        return
    if message.sender_chat and message.sender_chat.type == "channel" and not message.is_automatic_forward:
        message.delete()
        sender_chat = message.sender_chat
        bot.ban_chat_sender_chat(sender_chat_id=sender_chat.id, chat_id=chat.id)

ANTICHANNEL_HANDLER = CommandHandler("antichannel", achannel, run_async = True)
ADD_CHANNEL_HANDLER = CallbackQueryHandler(achannel_add, pattern=r"achannel_add", run_async = True)
RM_CHANNEL_HANDLER = CallbackQueryHandler(achannel_rem, pattern=r"achannel_rem", run_async = True)
CHANNEL_ELI_HANDLER = MessageHandler(
    Filters.all & ~Filters.status_update & Filters.chat_type.groups, eliminate_channel, run_async = True
)

dispatcher.add_handler(ADD_CHANNEL_HANDLER)
dispatcher.add_handler(ANTICHANNEL_HANDLER)
dispatcher.add_handler(RM_CHANNEL_HANDLER)
dispatcher.add_handler(CHANNEL_ELI_HANDLER)

__handlers__ = [
    ADD_CHANNEL_HANDLER,
    ANTICHANNEL_HANDLER,
    RM_CHANNEL_HANDLER,
    CHANNEL_ELI_HANDLER
]



__mod_name__ = "AntiChannel"
__help__ = """
Plugin to delete service messages in a chat!

/antichannel [ON|OFF]
"""


@user_admin_no_reply
@loggable
def aservice_rem(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    bot = context.bot
    match = re.match(r"aservice_rem\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = ssql.rem_aservice(chat.id)
        if is_kuki:
            is_kuki = ssql.rem_aservice(user_id)
            LOG = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"ANTI_SERVICE_DISABLED\n"
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
                f"Disabled AntiService System. I won't Be Deleting Service Message from Now on.",
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin_no_reply
@loggable
def aservice_add(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    bot = context.bot
    match = re.match(r"aservice_add\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = ssql.set_aservice(chat.id)
        if is_kuki:
            is_kuki = ssql.set_aservice(user_id)
            LOG = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"ANTI_SERVICE_ENABLE\n"
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