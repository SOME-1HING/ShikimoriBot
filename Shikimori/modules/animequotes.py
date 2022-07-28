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

import json
import requests
import random

from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from Shikimori.strings.animequotes_string import QUOTES_IMG
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode

def anime_quote():
    url = "https://animechan.vercel.app/api/random"
    # since text attribute returns dictionary like string
    response = requests.get(url)
    try:
        dic = json.loads(response.text)
    except Exception:
        pass
    quote = dic["quote"]
    character = dic["character"]
    anime = dic["anime"]
    return quote, character, anime


def quotes(update: Update, context: CallbackContext):
    message = update.effective_message
    quote, character, anime = anime_quote()
    msg = f"<i>❝{quote}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Change🔁",
            callback_data="change_quote")]])
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )

def change_quote(update: Update, context: CallbackContext):
    message = update.effective_message
    quote, character, anime = anime_quote()
    msg = f"<i>❝{quote}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Change🔁",
            callback_data="quote_change")]])
    message.edit_text(msg, reply_markup=keyboard,
                      parse_mode=ParseMode.HTML)
 
 
def animequotes(update: Update, context: CallbackContext):
    message = update.effective_message
    keyboard = [[InlineKeyboardButton(text="Change", callback_data="changek_quote")]]
    message.reply_photo(random.choice(QUOTES_IMG),reply_markup=InlineKeyboardMarkup(keyboard))

def changek_quote(update: Update, context: CallbackContext):
    message = update.effective_message
    keyboard = [[InlineKeyboardButton(text="Change", callback_data="quotek_change")]]
    message.reply_photo(random.choice(QUOTES_IMG),reply_markup=InlineKeyboardMarkup(keyboard))

ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes, run_async = True)
QUOTES_HANDLER = DisableAbleCommandHandler("quote", quotes, run_async = True)

CHANGE_QUOTE = CallbackQueryHandler(
    change_quote, pattern=r"change_.*")
QUOTE_CHANGE = CallbackQueryHandler(
    change_quote, pattern=r"quote_.*")
CHANGEK_QUOTE = CallbackQueryHandler(
    changek_quote, pattern=r"changek_.*")
QUOTEK_CHANGE = CallbackQueryHandler(
    changek_quote, pattern=r"quotek_.*")

dispatcher.add_handler(CHANGE_QUOTE)
dispatcher.add_handler(QUOTE_CHANGE)
dispatcher.add_handler(CHANGEK_QUOTE)
dispatcher.add_handler(QUOTEK_CHANGE)
dispatcher.add_handler(ANIMEQUOTES_HANDLER)
dispatcher.add_handler(QUOTES_HANDLER)

__command_list__ = [

    "animequotes",
    "quote"

]

__handlers__ = [

    ANIMEQUOTES_HANDLER,
    QUOTES_HANDLER

]

__mod_name__ = "AnimeQuotes"
__help__ = """
*Anime Quotes & Quotes*

 ❍ `/animequotes` - gives a random anime quote
 ❍ `/quote` - gives a random quote
"""
