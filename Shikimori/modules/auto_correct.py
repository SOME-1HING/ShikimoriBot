from Shikimori import dispatcher
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update

from Shikimori import arq

def autocorrect_bot(update: Update, context: CallbackContext):
    message = update.effective_message
    if not message.reply_to_message:
        return message.reply_text("Reply to a text message.")
    reply = message.reply_to_message
    text = reply.text or reply.caption
    if not text:
        return message.reply_text("Reply to a text message.")
    data = arq.spellcheck(text)
    if not data.ok:
        return message.reply_text("Something wrong happened.")
    result = data.result
    message.reply_text(result.corrected or "Empty")

AUTOCORRECT_HANDLER = CommandHandler("autocorrect", autocorrect_bot, run_async=True)

dispatcher.add_handler(AUTOCORRECT_HANDLER)

__handlers__ = [
    AUTOCORRECT_HANDLER
]

__mod_name__ = "Auto Correct"
__name__ = """
   ➢ `/autocorrect` : Reply to a message to show correct spelling.

"""