import requests
from pyrogram import filters
from Shikimori import pbot
from Shikimori.Extras.errors import capture_err

@pbot.on_message(filters.command('ann'))
@capture_err
async def ann(_, message):
    url = f'https://api.animeepisode.org/waifu/animenews.php'
    result = requests.get(url).json()
    try:
        title = result['Post_title']
        description = result['Description']
        img = result['Post_image']
        url = result['Post_url']
        caption = f"""
Title: {title}
Description: {description}
url: {url}
"""
    except Exception as e:
        print(str(e))
        pass
    await message.reply_photo(photo=img, caption=caption)
