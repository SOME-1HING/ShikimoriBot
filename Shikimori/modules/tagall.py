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

from Shikimori import telethn
from Shikimori.events import register as tomori


@tomori(pattern="^/(all|mentionall|tagall|utag) ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Tagged by an admin"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()

@tomori(pattern="^@(all|mentionall|tagall|utag) ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Tagged by an admin"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


# @tomori(pattern="^/users ?(.*)")
# async def _(event):
#     if event.fwd_from:
#         return
#     mentions = "Users : "
#     chat = await event.get_input_chat()
#     async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
#         mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
#     reply_message = None
#     if event.reply_to_msg_id:
#         reply_message = await event.get_reply_message()
#         await reply_message.reply(mentions)
#     else:
#         await event.reply(mentions)
#     await event.delete()


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
