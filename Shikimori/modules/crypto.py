from Shikimori.core.sections import section
import requests
from Shikimori.utils.http import get
from Shikimori import dispatcher
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

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
        return message.effective_message.reply_text(
            "[ERROR]: INVALID CURRENCY",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    body = {i.upper(): j for i, j in result.get(currency).items()}

    text = section(
        "Current Crypto Rates For " + currency.upper(),
        body,
    )
    message.effective_message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))

CRYPTO_HANDLER = CommandHandler("crypto", crypto, run_async=True)

dispatcher.add_handler(CRYPTO_HANDLER)

__handlers__ = [
    CRYPTO_HANDLER
]


__mod_name__ = "Crypto"
__help__ = """
   ➢ `/crypto` [currency] :Get Real Time value from currency given.
"""