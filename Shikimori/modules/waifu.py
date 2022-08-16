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

# Created By: https://telegram.dog/SOME1_HING 
# Assisted By: https://telegram.dog/SastaDev from https://telegram.dog/SastaNetwork

# Imports from external libraries. (DON'T EDIT)
import requests
from telegram import ParseMode
from telegram.ext import CommandHandler

import random
# Imports dispatcher = updater.dispatcher from __init__.py (*MUST EDIT* CHANGE MODULE NAME TO THE FOLDER NAME OF MODULES IN YOUR BOT)
from Shikimori import dispatcher

# Main code, Credit to https://github.com/itspro-dev for making the API. 

def waifu(update, context):
    try:
        msg = update.effective_message
        # API (DON'T EDIT)
        url = f'https://api.animeepisode.org/waifu/'
        result = requests.get(url).json()
        img = result['Character_Image']
        # Message (EDIT THIS PART AS HTML *IF YOU WANT*)
        text = f'''
<b>Name :</b> <code>{result['Character_Name']}</code>
        
<b>Anime :</b> <code>{result['Anime_name']}</code>
'''
        msg.reply_photo(photo=img, caption=text, parse_mode=ParseMode.HTML)

    except Exception as e:
        text = f'<b>Error</b>: <code>' + e + '</code>'
        msg.reply_text(text, parse_mode=ParseMode.HTML)


# Code Handler (YOU CAN CHANGE 'waifu' TO ANY 'cmd' FOR THIS TO BE WORKED AS '/cmd' *IF YOU WANT*.)
WAIFUINFO_HANDLER = CommandHandler('waifuinfo', waifu, run_async=True)
dispatcher.add_handler(WAIFUINFO_HANDLER)

#  Buttons for /help .
__mod_name__ = 'Waifus'  # *IF YOU WANT* EDIT NAME OF BUTTON IN '/help'


# *IF YOU WANT* EDIT MESSAGE FOR HELP OF THIS MODULE.
__help__ = '''
*Get waifu images*

   ➢ `/waifu`*:* Sends limited but best Waifu image. *RECOMMENDED*
   ➢ `/waifuinfo`*:* Gives random image of waifu with info. 
   ➢ `/waifus`*:* Sends Random Waifu image.
   ➢ `/swaifu`*:* Sends Random Waifu image.

   *NSFW CONTENT*
   ➢ `/nsfwwaifu`
   ➢ `/nwaifu`  
'''

# DON'T EDIT
__handlers__ = [WAIFUINFO_HANDLER]