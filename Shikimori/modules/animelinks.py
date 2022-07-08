from Shikimori.modules.animedev import client as animedev_client, exceptions
from Shikimori.events import register
from Shikimori import telethn, SUPPORT_CHAT
from telethon import Button


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
        await event.reply(f'*Error*: Contact @{SUPPORT_CHAT}.\nERROR: {e}')
        return
    text = f'''
<b>Anime Title:</b> <code>{anime['AnimeTitle']}</code>
    '''
    button_list = [[Button.url('Download Link', anime['AnimeLink'])], [Button.url('Search Query', anime['Search_Query'])]]
    
    await telethn.send_file(event.chat_id, anime['AnimeImg'], caption=text, buttons=button_list, parse_mode='html', reply_to=event.id)


