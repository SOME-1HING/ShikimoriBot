from pyrogram import filters,enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from Shikimori import pbot, APOD_API_KEY
import requests

@pbot.on_message(filters.command('apod'))
async def apod(_, message):
    result = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + APOD_API_KEY).json()
    img = result['hdurl']
    title = result['title']
    copyright = result['copyright']
    url = 'https://apod.nasa.gov/apod/'
    text = f'<b>Title:</b> {title}\n\n<b>Credits:</b> {copyright}'
    
    await message.reply_photo(img, caption=text, reply_markup=InlineKeyboardMarkup(
        [    
            [InlineKeyboardButton("More Info" , url=url)]

        ]), parse_mode=enums.ParseMode.HTML, reply_to_message_id=message.id)

__mod_name__ = "NASA"

__help__ = """
Use `/apod` to get Picture of the Day by NASA.
"""
