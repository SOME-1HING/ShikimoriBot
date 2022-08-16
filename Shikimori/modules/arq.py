from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Shikimori import pbot, arq
from Shikimori.vars import SUPPORT_CHAT

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


@pbot.on_message(filters.command("spellcheck"))
async def spellcheck_func(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/spellcheck [QUERY]")

    query = message.text.strip().split(None, 1)[1]

    try:
        spellcheck = await arq.spellcheck(query)
        # spellcheck = hmm.result[0]
        corrected = spellcheck["corrected"]
        corrections = spellcheck["corrections"]

        text = f"corrected - **{corrected}**\n"
        text += f"corrections - `{corrections}`\n"

        await message.reply_text(text)   
    
    except:
        await message.reply_text(f"Check your query. And if the function doesn't work, contact @{SUPPORT_CHAT}")

@pbot.on_message(filters.command("phub"))
async def phub(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n\n`/phub [QUERY]`")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]

    try:
        hmm = await arq.pornhub(query)
        result = hmm.result[0]
        thumbs = result["thumbnails"]
        thumb= thumbs[0]
        thumb = thumb + ".jpg"
        title = result["title"]
        rating = result["rating"]
        Duration = result["duration"]
        views = result["views"]
        url = result["url"]
        category = result["category"]
        views = views.replace('.', ",")
        views = views.replace("Aufrufe", "")

        text = f"Title 🎩 - **{title}**\n"
        text += f"Duration 🕔 - `{Duration}`\n"
        text += f"Views 👀 - `{views}`\n"
        text += f"Category 📺 - `{category}`\n"
        text += f"Rating 📺 - `{rating}`\n"
        link = f"https://youtube.com{url}"
        text += f"{url}"

        buttons = [
            [
                InlineKeyboardButton(text="Visit", url=link),
            ],]
        await m.delete()
        return await message.reply_photo(thumb ,caption = text, 
        #reply_markup=InlineKeyboardMarkup(buttons)
        )
    
    except:
        await m.edit(f"ERROR!!! Contact @{SUPPORT_CHAT}")