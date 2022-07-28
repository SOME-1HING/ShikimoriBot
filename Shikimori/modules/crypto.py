"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

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

from Shikimori.core.sections import section
import requests
from Shikimori import dispatcher
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode

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

CRYPTO_HANDLER = CommandHandler("crypto", crypto, block=False)

dispatcher.add_handler(CRYPTO_HANDLER)

__handlers__ = [
    CRYPTO_HANDLER
]


__mod_name__ = "Crypto 🪙"
__help__ = """
   ➢ `/crypto` [currency] :Get Real Time value from currency given.
"""
