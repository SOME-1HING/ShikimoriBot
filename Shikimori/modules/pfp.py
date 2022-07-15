"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

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

from telethon import *
from telethon.tl.functions.account import *
from telethon.tl.functions.channels import *
from telethon.tl.functions.photos import *
from telethon.tl.types import *
from Shikimori.events import register
from Shikimori import telethn as borg
from html import *
import logging

logger = logging.getLogger(__name__)



if 1 == 1:
    name = "Profile Photos"
    client = borg

    @register(pattern=("/pfp"))
    async def PPScmd(event):
#        """Gets the profile photos of replied users, channels or chats"""
        try:
            id = "".join(event.raw_text.split(maxsplit=2)[1:]) 
            user = await event.get_reply_message()
            if user:
                photos = await event.client.get_profile_photos(user.sender)
            else:
                photos = await event.client.get_profile_photos(event.chat_id)
            if id.strip() == "":
                try:
                    await event.client.send_file(event.chat.id, photos)
                except a:
                    photo = await event.client.download_profile_photo(event.chat_id)
                    await borg.send_file(event.chat.id, photo)
            else:
                try:
                    id = int(id)
                    if id <= 0:
                        await event.edit("<code>ID number you entered is invalid</code>")
                        return
                except:
                    await event.edit("<code>ID number you entered is invalid</code>")
                    return
                if int(id) <= (len(photos)):
                    send_photos = await event.client.download_media(photos[id - 1])
                    await borg.send_file(event.chat.id, send_photos)
                else:
                    await event.edit("<code>No photo found with that id</code>")
                    return
        except:
            await borg.send_text("Reply to user mate")
