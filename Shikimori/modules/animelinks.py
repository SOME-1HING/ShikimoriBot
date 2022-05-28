from Shikimori import pbot
from telegram import InlineKeyboardButton
from Shikimori.modules.animedev import client as animedev_client, exceptions
from pyrogram import filters

@pbot.on_message(filters.command('anilink'))
async def animelink(_, message):
    animename = message.message.split()
    if len(animename) <= 1:
        await message.reply('/anilink anime name')
        return
    try:
        anime = animedev_client.search(' '.join(animename[1:]))
        anime['Search_Query'] = anime['Search_Query'].replace(' ', '+')
    except exceptions.NotFound:
        await message.reply('Anime not found.')
        return
    except Exception as e:
        await message.reply(f'*Error*: Contact @tyranteyeeee.\nERROR: {e}')
        return
    text = f'''
                *Anime Title*: {anime['AnimeTitle']}

                *Search Query*: {anime['Search_Query']}
                '''
    buttons = [
    [
        InlineKeyboardButton(
            text="Link", url= anime['AnimeLink']),
    ],
    [
        InlineKeyboardButton(text="Search Query", url= anime['Search_Query']),
    ],
]
    await message.reply_photo(anime['AnimeImg'], caption=text, buttons = buttons, parse_mode='html')


