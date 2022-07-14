"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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


