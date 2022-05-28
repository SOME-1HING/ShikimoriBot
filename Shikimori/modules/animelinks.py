from telegram import ParseMode
from pyrogram import filters

from Shikimori import pbot
from Shikimori.Extras.errors import capture_err
from Shikimori.modules.animedev import client, exceptions

@pbot.on_message(filters.command('anilink'))
@capture_err
async def search_anime(_, message):
    if len(message.command) <= 1:
        await message.reply_text("/anilink anime name")
        return
    animename = message.text.split()[1:]
    try:
        anime = client.search(animename)
        text = f'''
                *Anime Title*: {anime['AnimeTitle']}

                *Anime Link*: {anime['AnimeLink']}

                *Search Query*: {anime['Search_Query']}
                '''
        await message.reply_photo(photo=anime['AnimeImg'], caption=text)
    except exceptions.NotFound as e:
        text = "Not Found"
        await message.reply_text(caption=text)


