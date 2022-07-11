import asyncio
import Shikimori.modules.sql.nsfw_sql as sql
from janda import Nhentai
import json
from Shikimori import pbot, dispatcher
from telegram import InlineKeyboardButton, ParseMode, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

async def sauce(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    args = update.effective_message.text.split(None, 1)
    if not update.effective_chat.type != "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
           return await message.reply_text("NSFW is not activated")

    try:   
        code = int(args[1])
        nh = Nhentai()
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
        buttons = [
        [
            InlineKeyboardButton(text="Visit", url=source),
        ],
        [
            InlineKeyboardButton(text="❌ Close", callback_data="close_reply_"),
        ],
        ]

        return await message.reply_photo(photo=cover,caption=caption, reply_markup=InlineKeyboardMarkup(buttons))
    except ValueError:
            return await message.reply_text("/sauce code")
    except:
        return await message.reply_text("Not Found")


def close_reply_(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "close_reply_":
        query.message.delete()

close_reply_handler = CallbackQueryHandler(
        close_reply_, pattern=r"close_reply_", run_async=True
    )
dispatcher.add_handler(close_reply_handler)

SAUCE_HANDLER = CommandHandler("sauce", sauce, run_async = True)

dispatcher.add_handler(SAUCE_HANDLER)