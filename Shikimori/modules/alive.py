from Shikimori import ALIVE_MEDIA, UPDATE_CHANNEL, SUPPORT_CHAT, OWNER_USERNAME, dispatcher, NETWORK, NETWORK_USERNAME
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from Shikimori.modules.helper_funcs.extraction import extract_user

PHOTO = ALIVE_MEDIA

def awake(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    buttons = [
        [
        InlineKeyboardButton(
            text="Updates",
            url=f"https://t.me/{UPDATE_CHANNEL}"),
        InlineKeyboardButton(
            text="Support",
            url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
     ]
    
    first_name = update.effective_user.first_name
    user = message.from_user

    TEXT = f"""
    <b>Hi [{first_name}](tg://user?id={user.id}), I'm Shikomori Robot.

    ⚪ I'm Working Properly

    ⚪ My Owner : [{OWNER_USERNAME}](https://t.me/{OWNER_USERNAME})</b>
    """
    if NETWORK:
        TEXT = TEXT + f"\n\n⚪ <b>I am Powered by : [{NETWORK}](https://t.me/{NETWORK_USERNAME}) \n\n" + "Thanks For Adding Me Here ❤️</b>"
    
    else:
        TEXT = TEXT + "\n\n<b>Thanks For Adding Me Here ❤️</b>"

    message.reply_text(
        TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)

ALIVE_HANDLER = DisableAbleCommandHandler("alive", awake, run_async=True)
dispatcher.add_handler(ALIVE_HANDLER)
__command_list__ = ["alive"]
__handlers__ = [
    ALIVE_HANDLER,
]

__mod_name__ = "Alive ✨"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
