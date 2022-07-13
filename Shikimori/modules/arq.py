from pyrogram import filters
from Shikimori.utils.pastebin import paste
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Shikimori import pbot
from Shikimori.utils.arqapi import arq

@pbot.on_message(filters.command("torrent"))
async def torrent_func(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/torrent [QUERY]")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]
    hmm = await arq.torrent(query)
    torrent = hmm.result[0]
    name = torrent["name"]
    upload = torrent["uploaded"]
    size = torrent["size"]
    seeds = torrent["seeds"]
    leechs = torrent["leechs"]
    magnet = torrent["magnet"]

    text = f"Title - **{name}**\n"
    text += f"Uploaded By - `{upload}`\n"
    text += f"Size - `{size}`\n"
    text += f"Seeds - `{seeds}`  Leechs - `{leechs}`\n\n"
    text += f"Torrent Magnet - `{magnet}`\n"

    await m.edit(text)   

@pbot.on_message(filters.command("yt"))
async def ytarq(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n\n`/yt [QUERY]`")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]

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
  