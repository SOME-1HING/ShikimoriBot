"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import json
import requests
import random

from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from Shikimori.strings.animequotes_string import QUOTES_IMG
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import ParseMode, Update, InlineKeyboardMarkup, InlineKeyboardButton

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
