import http
import aiohttp

from telegram import ParseMode

from Shikimori import pbot
from Shikimori.Extras.errors import capture_err


@pbot.on_message(filters.command('anilink'))
@capture_err
async def animelink(_, message):
    if len(message.command) != 2:
        await message.reply_text("/anilink anime name")
        return
    aniname = message.text.split(None, 1)[1]
    URL = f'https://9anime.dev/{aniname}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            try:
                caption = URL
            except Exception as e:
                print(str(e))
                pass
    await message.reply_text(caption=caption, parse_mode= ParseMode.MARKUP)


    