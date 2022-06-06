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
    update.effective_message.reply_photo(random.choice(waifu_string.WAIFUS))
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
WAIFUINFO_HANDLER = CommandHandler('waifu', waifu, run_async=True)
dispatcher.add_handler(WAIFUINFO_HANDLER)

#  Buttons for /help .
__mod_name__ = 'Waifu'  # *IF YOU WANT* EDIT NAME OF BUTTON IN '/help'


# *IF YOU WANT* EDIT MESSAGE FOR HELP OF THIS MODULE.
__help__ = '''
❍ `/waifu` : Gives random image of waifu.  
❍ `/waifu` : Gives random image of waifu.  
'''

# DON'T EDIT
__handlers__ = [WAIFUINFO_HANDLER]