import html

from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleMessageHandler
from telegram import ChatPermissions, ParseMode, Update
from telegram.ext import CallbackContext, Filters, run_async

IMG_GM = "https://telegra.ph/file/fff37608fa21d9d3d0b39.jpg"
IMG_GN = "https://telegra.ph/file/1862c7260109e24ed4715.jpg"


def goodnight(update: Update, context: CallbackContext):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        update.effective_message.reply_photo(
            IMG_GN,f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
    except:
        reply = f"*Good Night:* {user1}"
        message.reply_text(reply)


def goodmorning(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        update.effective_message.reply_photo(
            IMG_GM,f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
    except:
        reply = f"*Good Morning:* {user1}"
        message.reply_text(reply)



GDMORNING_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(good morning|gm|goodmorning)"), goodmorning, friendly="goodmorning", run_async = True
)
GDNIGHT_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(good night|gn|goodnight)"), goodnight, friendly="goodnight", run_async = True
)

dispatcher.add_handler(GDMORNING_HANDLER)
dispatcher.add_handler(GDNIGHT_HANDLER)
