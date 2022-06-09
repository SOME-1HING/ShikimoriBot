import json
import re
import requests
import Shikimori.modules.sql.chatbot_sql as sql
from Shikimori import AI_API_KEY as api
from Shikimori import pbot
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@pbot.on_message(filters.command('chatbot'))
async def chatbot(_, message):
    user_id = message.from_user.id
    member = await pbot.get_chat_member(message.chat.id, user_id)
    if member.status == "administrator" or "creator":
        text = "Choose an option"
        await message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(
            [    
               [InlineKeyboardButton("Enable" , callback_data="add_chat"),
               InlineKeyboardButton("Disable" , callback_data="remove_chat")]
            ]),
            parse_mode=enums.ParseMode.HTML)
    else:
        await message.reply_text("Only admins can use this command.")

@pbot.on_callback_query(filters.regex("add_chat"))
async def add_ai(client: pbot, query: CallbackQuery, message) -> str:
    user_id = message.from_user.id
    member = await pbot.get_chat_member(message.chat.id, user_id)
    if member.status == "administrator" or "creator":
        chat = message.chat
        is_chatbot = sql.set_chatbot(chat.id)
        if is_chatbot:
             await message.edit_text(
                 "Shikimori Chatbot enable by {}.".format(message.from_user.mention),
                 parse_mode=enums.ParseMode.HTML,
             )
        else:
            await pbot.answer_callback_query(CallbackQuery.id, "Already chatbot is enabled.")
    else:
        text = "Only admins can click this button."
        await pbot.answer_callback_query(CallbackQuery.id, text, show_alert=True)

@pbot.on_callback_query(filters.regex("remove_chat"))
async def remove_ai(client: pbot, query: CallbackQuery, message) -> str:
    user_id = message.from_user.id
    member = await pbot.get_chat_member(message.chat.id, user_id)
    if member.status == "administrator" or "creator":
        chat = message.chat
        is_chatbot = sql.rem_chatbot(chat.id)
        if is_chatbot:
             await message.edit_text(
                 "Shikimori Chatbot disable by {}.".format(message.from_user.mention),
                 parse_mode=enums.ParseMode.HTML,
             )
        else:
            await pbot.answer_callback_query(CallbackQuery.id, "Already chatbot is disabled.")
    else:
        text = "Only admins can click this button."
        await pbot.answer_callback_query(CallbackQuery.id, text, show_alert=True)

@pbot.on_message(filters.text, group=8)
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

__mod_name__ = "ChatBot"
__help__ = """
*Admins only Commands*:
  `/Chatbot`*:* Shows chatbot control panel

*Thx @mizuhara_chan1 for the API*
"""