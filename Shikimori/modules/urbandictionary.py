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

import requests
from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext



def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    args = context.args
    if len(args) == 0:
        return message.reply_text("/ud [word]")
        
    text = message.text[len('/ud '):]
    results = requests.get(
        f'https://api.urbandictionary.com/v0/define?term={text}').json()
    try:
        reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "No results found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


UD_HANDLER = DisableAbleCommandHandler(["ud"], ud, run_async=True)

dispatcher.add_handler(UD_HANDLER)

__command_list__ = ["ud"]
__handlers__ = [UD_HANDLER]

__mod_name__ = "Urban Dictionary"
__help__ = """
*Urban Dictionary*
 ❍ `/ud` : Search for word in Urban Dictionary
"""
