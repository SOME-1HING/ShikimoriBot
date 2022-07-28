import os
import datetime
import time

from telethon import events
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext, CommandHandler
from telegram.error import BadRequest

from Shikimori import telethn, dispatcher
from Shikimori.modules.helper_funcs.chat_status import dev_plus

DEBUG_MODE = False

@dev_plus
def debug(update: Update, context: CallbackContext):
    global DEBUG_MODE
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message
    print(DEBUG_MODE)
    if len(args) > 1:
        if args[1] in ("yes", "on"):
            DEBUG_MODE = True
            message.reply_text("Debug mode is now on.")
        elif args[1] in ("no", "off"):
            DEBUG_MODE = False
            message.reply_text("Debug mode is now off.")
    else:
        if DEBUG_MODE:
            message.reply_text("Debug mode is currently on.")
        else:
            message.reply_text("Debug mode is currently off.")


@telethn.on(events.NewMessage(pattern="[/!].*"))
async def i_do_nothing_yes(event):
    global DEBUG_MODE
    if DEBUG_MODE:
        print(f"-{event.from_id} ({event.chat_id}) : {event.text}")
        if os.path.exists("updates.txt"):
            with open("updates.txt", "r") as f:
                text = f.read()
            with open("updates.txt", "w+") as f:
                f.write(text + f"\n-{event.from_id} ({event.chat_id}) : {event.text}")
        else:
            with open("updates.txt", "w+") as f:
                f.write(
                    f"- {event.from_id} ({event.chat_id}) : {event.text} | {datetime.datetime.now()}",
                )

support_chat = os.getenv("SUPPORT_CHAT")

@dev_plus
def logs(update: Update, context: CallbackContext):
    chat = update.effective_chat
    user = update.effective_user
    with open("bot_logs.txt", "rb") as f:
        context.bot.send_document(document=f, filename=f.name, chat_id=user.id)
    if chat.type != chat.PRIVATE:
        msg = update.effective_message
        hmm = msg.reply_text("`Logs sent. Check your pm.`", parse_mode=ParseMode.MARKDOWN)
        time.sleep(10)
        try:
            msg.delete()
            hmm.delete()
        except BadRequest:
            pass

LOG_HANDLER = CommandHandler(("logs", "log"), logs, run_async=True)
dispatcher.add_handler(LOG_HANDLER)

DEBUG_HANDLER = CommandHandler("debug", debug, run_async=True)
dispatcher.add_handler(DEBUG_HANDLER)

__mod_name__ = "Debug"
__command_list__ = ["debug"]
__handlers__ = [DEBUG_HANDLER]
