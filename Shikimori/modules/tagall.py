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

from Shikimori import telethn
from Shikimori.events import register as tomori


@tomori(pattern="^/(all|mentionall|tagall|utag) ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Tagged by an admin"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 99999999):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        try:
            await event.send_text(event.chat_id, mentions, reply_to=event.reply_to_msg_id)
        except:
            await event.reply(mentions)
    await event.reply(mentions)

@tomori(pattern="^@(all|mentionall|tagall|utag) ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Tagged by an admin"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 99999999):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        try:
            await event.send_text(event.chat_id, mentions, reply_to=event.reply_to_msg_id)
        except:
            await event.reply(mentions)
    await event.reply(mentions)

__mod_name__ = "TagAll"
__help__ = """
*Tag All*
 ❍ `/users` : Get txt file of all users in your group.
 ❍ `/all` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `/tagall` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `/utag` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `/mentionall` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@all` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@tagall` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@utag` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@mentionall` : (reply to message or add another message) To mention all members in your group, without exception.
"""
