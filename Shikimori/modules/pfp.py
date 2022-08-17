"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

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
            await borg.send_message("Reply to user mate")
