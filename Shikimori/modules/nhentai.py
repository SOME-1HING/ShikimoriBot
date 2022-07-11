from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
import asyncio
import Shikimori.modules.sql.nsfw_sql as sql
from janda import Nhentai, resolve
import json
from Shikimori import pbot

@pbot.on_message(filters.command("sauce"))
async def sauce(_, message):
    chat_id = message.chat.id
    if not message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
           return await message.reply_text("NSFW is not activated")
            
    if len(message.command) != 2:
        await message.reply_text("/sauce code")
        return
    nh = Nhentai()
    code = message.text.split(None, 1)[1]
    code = int(code)
    data = await nh.get(code)
    json_acceptable_string = data.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    await asyncio.sleep(0.6)
    res = d["data"]
    artist = res["artist"]
    id = res["id"]
    image = res["image"]
    cover = image[0]
    language = res["language"]
    num_favorites = res["num_favorites"]
    num_pages = res["num_pages"]
    title = res["title"]
    source = d["source"]
    parodies = res["parodies"]

    if parodies== None:
        parodies ="Original"

    artist= str(artist)

    for ch in ["[", "]", "'"]:
        artist = artist.replace(ch, "")

    caption=f"""
Title➢ {title}
id ➢ {id}
Artist ➢ {artist}
Lang ➢ {language}
Parodies ➢ {parodies}
Source ➢ {source}
Fav➢ {num_favorites}
Pages ➢ {num_pages}
    """
    button = InlineKeyboard(row_width=1)
    button.add(InlineKeyboardButton(text="Visit", url=source))

    return await message.reply_photo(photo=cover,caption=caption, reply_markup=button)
