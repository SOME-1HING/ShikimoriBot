from telegram import InlineKeyboardButton
from Shikimori.modules.animedev import client as animedev_client, exceptions
from Shikimori.events import register
from Shikimori import telethn

@register(pattern='/anilink')
async def animelink(event):
    animename = event.message.message.split()
    if len(animename) <= 1:
        await event.reply('/anilink anime name')
        return
    try:
        anime = animedev_client.search(' '.join(animename[1:]))
        anime['Search_Query'] = anime['Search_Query'].replace(' ', '+')
    except exceptions.NotFound:
        await event.reply('Anime not found.')
        return
    except Exception as e:
        await event.reply(f'*Error*: Contact @tyranteyeeee.\nERROR: {e}')
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
    
    await telethn.send_file(event.chat_id, anime['AnimeImg'], caption=text, buttons = buttons)


