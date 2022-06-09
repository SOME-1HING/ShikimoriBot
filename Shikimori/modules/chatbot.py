api = 'itspro3243354'

import json
import re
import requests
import Shikimori.modules.sql.chatbot_sql as sql
from Shikimori import pbot
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Shikimori.modules.sql.chatbot_sql import (
    is_karma_on,
    karma_off,
    karma_on,
) 


@pbot.on_message(filters.command('chatbot'))
async def chatbot(client, message):
    if message.sender_chat:
        await message.reply_text('come from user account bro')
        return
    user_id = message.from_user.id
    member = await pbot.get_chat_member(message.chat.id, user_id)
    if str(member.status) in ["ChatMemberStatus.ADMINISTRATOR" , "ChatMemberStatus.OWNER"]:
        text = "Choose an option"
        await message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(
            [    
               [InlineKeyboardButton("Enable" , callback_data="add_chat"),
               InlineKeyboardButton("Disable" , callback_data="remove_chat")]
            ]))
    else:
        await message.reply_text("Only admins can use this command.")

@pbot.on_callback_query(filters.regex("add_chat"))
async def add_ai(client, callback_query) -> str:
    message = callback_query.message
    user_id = callback_query.from_user.id
    chat_id = message.chat.id
    member = await pbot.get_chat_member(message.chat.id, user_id)
    if str(member.status) in ["ChatMemberStatus.ADMINISTRATOR" , "ChatMemberStatus.OWNER"]:
        await karma_on(chat_id)
        await callback_query.message.edit_text(
                 "Bot's chatbot had been enabled by {}.".format(callback_query.from_user.mention),
             )
    else:
        text = "Only admins can click this button."
        await callback_query.answer(text, show_alert=True)

@pbot.on_callback_query(filters.regex("remove_chat"))
async def remove_ai(client, callback_query):
    message = callback_query.message
    user_id = callback_query.from_user.id
    chat_id = message.chat.id
    member = await pbot.get_chat_member(message.chat.id, user_id)
    if str(member.status) in ["ChatMemberStatus.ADMINISTRATOR" , "ChatMemberStatus.OWNER"]:
        await karma_off(chat_id)
        await callback_query.message.edit_text(
                 "Bot's chatbot has been disabled by {}.".format(message.from_user.mention),
             )
    else:
        text = "Only admins can click this button."
        await callback_query.answer(text, show_alert=True)

@pbot.on_message(filters.text, group=8)
async def chatbot(client, message):
    chat_id = message.chat.id
    if not is_karma_on(message.chat.id):
        return
    Message = message.text
    await pbot.send_chat_action(chat_id, enums.ChatAction.TYPING)
    url = requests.get('http://itsprodev.cf/chatbot/?api=' + api + '&message=' + Message)
    reply = json.loads(url.text)
    text = reply['reply']
    await message.reply_text(text)

mod_name = "ChatBot"
help = """
*Admins only Commands*:
  /Chatbot*:* Shows chatbot control panel
*Thx @mizuhara_chan1 for the API*
"""