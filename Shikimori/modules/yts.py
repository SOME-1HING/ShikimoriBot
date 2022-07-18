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

import logging
from pyrogram.types import Message
from Shikimori.imports.youtube_search import YoutubeSearch
from Shikimori import pbot
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)

@pbot.on_message(pyrogram.filters.command("yts"))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/yts `YouTube Video Name`")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("Searching....")
        results = YoutubeSearch(query, max_results=6).to_dict()
        i = 0
        text = ""
        while i < 6:
            text += f"Title 🎩 - {results[i]['title']}\n"
            text += f"Duration 🕔 - {results[i]['duration']}\n"
            text += f"Views 👀 - {results[i]['views']}\n"
            text += f"Channel 📺 - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
        
@pbot.on_message(pyrogram.filters.command(["ytsearch"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/ytsearch `YouTube Video Name`")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("Searching....")
        results = YoutubeSearch(query, max_results=8).to_dict()
        i = 0
        text = ""
        while i < 8:
            text += f"Title 🎩 - {results[i]['title']}\n"
            text += f"Duration 🕔 - {results[i]['duration']}\n"
            text += f"Views 👀 - {results[i]['views']}\n"
            text += f"Channel 📺 - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))    
        
  

__mod_name__ = "YouTube"

__help__ = """
=>> *Youtube Video Searching *
 - `/yts` Video name :  To Search In Youtube Until Max Result Is 4
 - `/ytsearch` Video name :  To Search In Youtube Until Max Result Is 8
"""       
