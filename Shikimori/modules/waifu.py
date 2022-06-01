import requests
from pyrogram import filters
from Shikimori import pbot
from Shikimori.Extras.errors import capture_err

@pbot.on_message(filters.command('waifu'))
@capture_err
async def ann(_, message):
    url = f'https://api.animeepisode.org/waifu/'
    result = requests.get(url).json()
    try:
        anime = result['Anime_name']
        name = result['Character_Name']
        img = result['Character_Image']
        caption = f"""
Name: {name}
Anime: {anime}
"""
    except Exception as e:
        print(str(e))
        pass
    await message.reply_photo(photo=img, caption=caption)
