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

from Shikimori.core.sections import section
import requests
from Shikimori import dispatcher
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

def crypto(update: Update, context: CallbackContext):
    message = update.effective_message
    args = context.args
    if len(args) == 0:
        return message.reply_text("/crypto [currency]")

    currency = message.text.split(None, 1)[1].lower()

    buttons = [
        [
            InlineKeyboardButton(text = "Available Currencies", url ="https://plotcryptoprice.herokuapp.com"),
        ],
    ]

    try:
        url = f'https://x.wazirx.com/wazirx-falcon/api/v2.0/crypto_rates'
        result = requests.get(url).json()
    except Exception:
        return message.reply_text("[ERROR]: Something went wrong.")

    if currency not in result:
        return update.effective_message.reply_text(
            "[ERROR]: INVALID CURRENCY",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    body = {i.upper(): j for i, j in result.get(currency).items()}

    text = section(
        "Current Crypto Rates For " + currency.upper(),
        body,
    )
    update.effective_message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), parse_mode=ParseMode.MARKDOWN)

CRYPTO_HANDLER = CommandHandler("crypto", crypto, run_async=True)

dispatcher.add_handler(CRYPTO_HANDLER)

__handlers__ = [
    CRYPTO_HANDLER
]


__mod_name__ = "Crypto 🪙"
__help__ = """
   ➢ `/crypto` [currency] :Get Real Time value from currency given.
"""