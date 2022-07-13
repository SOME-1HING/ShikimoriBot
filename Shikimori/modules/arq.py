from pyrogram import filters
from Shikimori.utils.pastebin import paste
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Shikimori import pbot
from Shikimori.utils.arqapi import arq

@pbot.on_message(filters.command("lyrics"))
async def lyrics_func(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/lyrics [QUERY]")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]
    song = await arq.lyrics(query)
    lyrics = song.result
    if len(lyrics) < 4095:
        return await m.edit(f"__{lyrics}__")
    lyrics = await paste(lyrics)
    await m.edit(f"**LYRICS_TOO_LONG:** [URL]({lyrics})")

@pbot.on_message(filters.command("ytarq"))
async def ytarq(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/lyrics [QUERY]")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]

    hmm = await arq.youtube(query)
    videos = hmm.result[0]
    thumbs = videos["thumbnails"]
    thumb= thumbs[0]
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
    link = f"https://youtube.com{url}\n\n"

    buttons = [
        [
            InlineKeyboardButton(text="Visit", url=link),
        ],]
    m.delete()
    return await message.reply_photo(thumb ,text, reply_markup=InlineKeyboardMarkup(buttons))
  