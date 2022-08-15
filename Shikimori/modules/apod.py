"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

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

from Shikimori import dispatcher
from Shikimori.vars import APOD_API_KEY
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import (
    CallbackContext,
    CommandHandler,
)
import requests

def apod(update: Update, context: CallbackContext):
    url = 'https://apod.nasa.gov/apod/'
    result = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + APOD_API_KEY).json()
    img = result['hdurl']
    title = result['title']
    if result['copyright']:       
        copyright = result['copyright']
        text = f'<b>Title: <u>{title}</u></b>\n\n<i>Credits: {copyright}</i>'
    else:
        text = f'<b>Title: <u>{title}</u></b>'
    
    update.effective_message.reply_photo(img, caption=text, reply_markup=InlineKeyboardMarkup(
        [    
            [InlineKeyboardButton("More Info" , url=url)]

        ]),
        parse_mode=ParseMode.HTML)

apod_handler = CommandHandler("apod", apod, run_async = True)
dispatcher.add_handler(apod_handler)

__mod_name__ = "NASA"

__help__ = """
Use `/apod` to get Picture of the Day by NASA.
"""
