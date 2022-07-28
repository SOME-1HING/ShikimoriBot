"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

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

from Shikimori import dispatcher, APOD_API_KEY
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    CallbackContext,
    CommandHandler,
)
import requests

def apod(update: Update, context: CallbackContext):
    result = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + APOD_API_KEY).json()
    img = result['hdurl']
    title = result['title']
    copyright = result['copyright']
    url = 'https://apod.nasa.gov/apod/'
    text = f'<b>Title: <u>{title}</u></b>\n\n<i>Credits: {copyright}</i>'
    
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
