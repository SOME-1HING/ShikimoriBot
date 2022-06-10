from Shikimori import dispatcher, APOD_API_KEY
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
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
    text = f'Title: {title}\n\nCredits: {copyright}'
    
    update.effective_message.reply_photo(img, caption=text, reply_markup=InlineKeyboardMarkup(
        [    
            [InlineKeyboardButton("More Info" , url=url)]

        ]))

apod_handler = CommandHandler("apod", apod, run_async = True)
dispatcher.add_handler(apod_handler)

__mod_name__ = "NASA"

__help__ = """
Use `/apod` to get Picture of the Day by NASA.
"""
