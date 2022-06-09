import json
import re
import requests
import Shikimori.modules.sql.chatbot_sql as sql
from Shikimori import AI_API_KEY as api
from Shikimori import pbot
from Shikimori.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@user_admin
@pbot.on_message(filters.command('chatbot'))
async def chatbot(_, message):
    text = "Choose an option"
    await message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(
        [    
            [InlineKeyboardButton("Enable" , callback_data="add_chat")],
            [InlineKeyboardButton("Disable" , callback_data="remove_chat")]
        ]),
        parse_mode=enums.ParseMode.HTML)

@user_admin_no_reply
@pbot.on_callback_query(filters.regex("add_chat"))
async def add_ai(client: pbot, query: CallbackQuery, message) -> str:
    user_id = query.from_user.id
    match = re.match(r"add_chat\((.+?)\)", query.data)
    if query.data == "add_chat":
        if match:
            user_id = match.group(1)
            chat= message.chat
            is_chatbot = sql.set_chatbot(chat.id)
            if is_chatbot:
                is_chatbot = sql.set_chatbot(user_id)
            else:
                await pbot.edit_text(
                    "Shikimori Chatbot enable by {}.".format(message.from_user.mention),
                    parse_mode=enums.ParseMode.HTML,
                )

    return ""

@user_admin_no_reply
@pbot.on_callback_query(filters.regex("remove_chat"))
async def remove_ai(client: pbot, query: CallbackQuery, message) -> str:
    user_id = query.from_user.id
    match = re.match(r"remove_chat\((.+?)\)", query.data)
    if query.data == "remove_chat":
        if match:
            user_id = match.group(1)
            chat= message.chat
            is_chatbot = sql.rem_chatbot(chat.id)
            if is_chatbot:
                is_chatbot = sql.rem_chatbot(user_id)
            else:
                await pbot.edit_text(
                    "Shikimori Chatbot disabled by {}.".format(message.from_user.mention),
                    parse_mode=enums.ParseMode.HTML,
                )

    return ""

async def chatbot(_, message):
    chat_id = message.chat.id
    is_chatbot = sql.is_chatbot(chat_id)
    if not is_chatbot:
        return
    if message.text and not message.document:
        Message = message.text
        await pbot.send_chat_action(chat_id, enums.ChatAction.TYPING)
        url = requests.get('http://itsprodev.cf/chatbot/?api=' + api + '&message=' + Message)
        reply = json.loads(url.text)
        text = reply['reply']
        await message.reply_text(text, timeout=60)

__mod_name__ = "ChatBot 🤖"

__help__ = """
*Admins only Commands*:
  ➢ `/Chatbot`*:* Shows chatbot control panel

*Thx @mizuhara_chan1 for the API*
"""