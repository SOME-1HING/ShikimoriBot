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

import os
from pyrogram import filters
from pyrogram.types import Message

from Shikimori import DEV_USERS
from Shikimori import pbot as app
from Shikimori.core.sections import section


async def get_user_info(user, already=False):
    if not already:
        user = await app.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    dc_id = user.dc_id
    photo_id = user.photo.big_file_id if user.photo else None
    is_sudo = user_id in DEV_USERS
    body = {
        "ID": user_id,
        "DC": dc_id,
        "Name": [first_name],
        "Username": [("@" + username) if username else None],
        "Mention": [mention],
        "Sudo": is_sudo,
    }
    caption = section("User info", body)
    return [caption, photo_id]


async def get_chat_info(chat, already=False):
    if not already:
        chat = await app.get_chat(chat)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    type_ = chat.type
    is_scam = chat.is_scam
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    link = f"[Link](t.me/{username})" if username else None
    dc_id = chat.dc_id
    photo_id = chat.photo.big_file_id if chat.photo else None
    body = {
        "ID": chat_id,
        "DC": dc_id,
        "Type": type_,
        "Name": [title],
        "Username": [("@" + username) if username else None],
        "Mention": [link],
        "Members": members,
        "Scam": is_scam,
        "Restricted": is_restricted,
        "Description": [description],
    }
    caption = section("Chat info", body)
    return [caption, photo_id]


@app.on_message(filters.command("uinfo"))
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("Processing...")

    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(
            info_caption, disable_web_page_preview=True
        )
    photo = await app.download_media(photo_id)

    await message.reply_photo(
        photo, caption=info_caption, quote=False
    )
    await m.delete()
    os.remove(photo)


@app.on_message(filters.command("cinfo"))
async def chat_info_func(_, message: Message):
    try:
        if len(message.command) > 2:
            return await message.reply_text(
                "**Usage:**cinfo <chat id/username>"
            )

        if len(message.command) == 1:
            chat = message.chat.id
        elif len(message.command) == 2:
            chat = message.text.split(None, 1)[1]

        m = await message.reply_text("Processing...")

        info_caption, photo_id = await get_chat_info(chat)
        if not photo_id:
            return await m.edit(
                info_caption, disable_web_page_preview=True
            )

        photo = await app.download_media(photo_id)
        await message.reply_photo(
            photo, caption=info_caption, quote=False
        )

        await m.delete()
        os.remove(photo)
    except Exception as e:
        await m.edit(e)


__mod_name__ = "SecInfo"
