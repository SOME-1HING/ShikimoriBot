from Shikimori.modules.imgeditor import photo
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
import asyncio
import re
import Shikimori.modules.sql.nsfw_sql as sql
from janda import Nhentai, resolve
import json
from Shikimori import pbot, dispatcher
from math import ceil

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
    source = d["source"]
    parodies = res["parodies"]
    tags = res["tags"]
    j = res["optional_title"]
    title = j["english"]


    if parodies== None:
        parodies ="Original"

    artist= str(artist)
    tags = str(tags)

    for ch in ["[", "]", "'"]:
        artist = artist.replace(ch, "")
        tags = tags.replace(ch, "")

    caption=f"""
**Title➢ {title}**

**id ➢** `{id}`
**Artist ➢ {artist.capitalize()}
Lang ➢ {language.capitalize()}

Parodies ➢ `{parodies}`
Tags ➢** `{tags}`

**Fav ➢** ❤️`{num_favorites}`
**Pages ➢** `{num_pages}`
    """
    img_url = f"https://i.nhentai.net/galleries/{id}/"

    source_button = InlineKeyboardButton(text="Visit", url=source)

    buttons = [
    [
        InlineKeyboardButton(text="❮", callback_data="back_n"),
        InlineKeyboardButton(text="CLOSE", callback_data="close_n"),
        InlineKeyboardButton(text="❯", callback_data="next_n"),
    ],
    [
        source_button
    ],
    ]

    return await message.reply_photo(photo=cover,caption=caption, reply_markup=InlineKeyboardMarkup(buttons))



@pbot.on_callback_query()
async def close_(client: pbot, query: CallbackQuery):
    if query.data == "close_n":
        await query.message.delete()

@pbot.on_callback_query()
async def button_n(client: pbot, query: CallbackQuery):
    next_n = re.match(r"next_n", query.data)
    back_n = re.match(r"back_n", query.data)
    i = 1
    while i != (int(sauce.num_pages)-1):
        if next_n:
            await query.message.edit_photo(photo= f"{sauce.img_url}/{i}", )
            source = sauce.source_button
            buttons = [
            [
                InlineKeyboardButton(text="❮", callback_data="back_n"),
                InlineKeyboardButton(text="CLOSE", callback_data="close_n"),
                InlineKeyboardButton(text="❯", callback_data="next_n"),
            ],
            [
                source
            ],
            ]
            i = i+1
        elif back_n:
            await query.message.edit_photo(photo= f"{sauce.img_url}/{i}", )
            source = sauce.source_button
            buttons = [
            [
                InlineKeyboardButton(text="❮", callback_data="back_n"),
                InlineKeyboardButton(text="CLOSE", callback_data="close_n"),
                InlineKeyboardButton(text="❯", callback_data="next_n"),
            ],
            [
                source
            ],
            ]
            i = i-1
