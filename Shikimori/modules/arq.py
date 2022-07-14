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

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Shikimori import SUPPORT_CHAT, pbot
from Shikimori.utils.arqapi import arq

@pbot.on_message(filters.command("torrent"))
async def torrent_func(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/torrent [QUERY]")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]

    try:
        hmm = await arq.torrent(query)
        torrent = hmm.result[0]
        name = torrent["name"]
        upload = torrent["uploaded"]
        size = torrent["size"]
        seeds = torrent["seeds"]
        leechs = torrent["leechs"]
        magnet = torrent["magnet"]

        text = f"Title - **{name}**\n"
        text += f"Uploaded On - `{upload}`\n"
        text += f"Size - `{size}`\n"
        text += f"Seeds - `{seeds}`  Leechs - `{leechs}`\n\n"
        text += f"Torrent Magnet - `{magnet}`\n"

        await m.edit(text)   
    
    except:
        await m.edit(f"Check your query. And if the function doesn't work, contact @{SUPPORT_CHAT}")

@pbot.on_message(filters.command("yt"))
async def ytarq(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n\n`/yt [QUERY]`")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]

    try:
        hmm = await arq.youtube(query)
        videos = hmm.result[0]
        thumbs = videos["thumbnails"]
        thumb= thumbs[0]
        thumb = thumb + ".jpg"
        title = videos["title"]
        channel = videos["channel"]
        Duration = videos["duration"]
        views = videos["views"]
        url = videos["url_suffix"]
        views = views.replace('.', ",")
        views = views.replace("Aufrufe", "")

        text = f"Title 🎩 - **{title}**\n"
        text += f"Duration 🕔 - `{Duration}`\n"
        text += f"Views 👀 - `{views}`\n"
        text += f"Channel 📺 - `{channel}`\n"
        link = f"https://youtube.com{url}"

        buttons = [
            [
                InlineKeyboardButton(text="Visit", url=link),
            ],]
        await m.delete()
        return await message.reply_photo(thumb ,caption = text, reply_markup=InlineKeyboardMarkup(buttons))
    
    except:
        await m.edit(f"ERROR!!! Contact @{SUPPORT_CHAT}")