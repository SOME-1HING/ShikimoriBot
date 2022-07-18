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

import wikipedia
from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext
from wikipedia.exceptions import DisambiguationError, PageError


def wiki(update: Update, context: CallbackContext):
    msg = (
        update.effective_message.reply_to_message
        if update.effective_message.reply_to_message
        else update.effective_message
    )
    res = ""
    if msg == update.effective_message:
        search = msg.text.split(" ", maxsplit=1)[1]
    else:
        search = msg.text
    try:
        res = wikipedia.summary(search)
    except DisambiguationError as e:
        update.message.reply_text(
            "Disambiguated pages found! Adjust your query accordingly.\n<i>{}</i>".format(
                e
            ),
            parse_mode=ParseMode.HTML,
        )
    except PageError as e:
        update.message.reply_text(
            "<code>{}</code>".format(e), parse_mode=ParseMode.HTML
        )
    if res:
        result = f"<b>{search}</b>\n\n"
        result += f"<i>{res}</i>\n"
        result += f"""<a href="https://en.wikipedia.org/wiki/{search.replace(" ", "%20")}">Read more...</a>"""
        if len(result) > 4000:
            with open("result.txt", "w") as f:
                f.write(f"{result}\n\nUwU OwO OmO UmU")
            with open("result.txt", "rb") as f:
                context.bot.send_document(
                    document=f,
                    filename=f.name,
                    reply_to_message_id=update.message.message_id,
                    chat_id=update.effective_chat.id,
                    parse_mode=ParseMode.HTML,
                )
        else:
            update.message.reply_text(
                result, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            )


WIKI_HANDLER = DisableAbleCommandHandler("wiki", wiki, run_async = True)
dispatcher.add_handler(WIKI_HANDLER)

__help__ = """
Wiki module:

× `/wiki` <query>: Gets Wikipedia article about query

""" 

__mod_name__ = "Wiki"
