"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from Shikimori.imports.animedev import client as animedev_client, exceptions
from Shikimori.events import register
from Shikimori import telethn
from Shikimori.vars import SUPPORT_CHAT
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


