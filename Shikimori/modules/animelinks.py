from telegram import ParseMode
from pyrogram import filters

from Shikimori import pbot
from Shikimori.Extras.errors import capture_err
from Shikimori.modules.animedev import client, exceptions

@pbot.on_message(filters.command('anilink'))
@capture_err
async def search_anime(_, message):
    if len(message.command) != 2:
        await message.reply_text("/anilink anime name")
        return
    animename = message.text.split(None, 1)[1]
    try:
        anime = client.search(animename)
        text = f'''
                Anime Title: {anime['AnimeTitle']}

                Anime Link: {anime['AnimeLink']}

                Anime Image: {anime['AnimeImg']}

                Search Query: {anime['Search_Query']}
                '''
    except exceptions.NotFound as e:
        text = "Not Found"
        return
    await message.reply_photo(text, parse_mode= ParseMode.MARKUP)


