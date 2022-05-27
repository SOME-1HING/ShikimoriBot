from animedev import client, exceptions
from telegram import ParseMode
from Shikimori import dispatcher
from telegram.ext import CommandHandler


async def search_anime(anime_name):
    if len(anime_name.command) <= 1:
        await anime_name.reply_text("/anilink anime name")
        return

    try:
        anime = client.search(anime_name)
        text = f'''
        Anime Title: {anime['AnimeTitle']}

        Anime Link: {anime['AnimeLink']}

        Anime Image: {anime['AnimeImg']}

        Search Query: {anime['Search_Query']}
        '''
    except exceptions.NotFound as e:
        print(e)
        pass
    await anime_name.reply_text(caption=text, parse_mode= ParseMode.MARKUP)


ANILINK_HANDLER = CommandHandler("anilink", search_anime, run_async=True)


dispatcher.add_handler(ANILINK_HANDLER)

__handlers__ = [
    ANILINK_HANDLER
    ]