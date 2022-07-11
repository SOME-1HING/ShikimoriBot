from datetime import datetime
from Shikimori import DEV_USERS, OWNER_ID, STATS_IMG
from Shikimori import (
    OWNER_ID,
    OWNER_USERNAME,
    SUPPORT_CHAT,
    dispatcher
)
import time
from telegram import InlineKeyboardButton, ParseMode, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

def bug(update: Update, context: CallbackContext):
    try:
        args = update.effective_message.text.split(None, 1)
        user_id = update.effective_message.from_user.id
        message = update.effective_message
        msg_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
        if user_id == OWNER_ID:
            message.reply_text(
                    "❎ *Why owner of bot reporting a bug?? Go fix yourself*", parse_mode=ParseMode.MARKDOWN
                )
            return
        if update.effective_chat.type == "private":
            update.effective_message.reply_text(f"❎ *This command only works in public groups.*\n\n Visit @{SUPPORT_CHAT} to report bugs related to bot's pm.", parse_mode=ParseMode.MARKDOWN)
            return
        
        if len(args) >= 2:
            bugs = args[1]
            if message.chat.username:
                link_chat_id = message.chat.username
                message_link = f"https://t.me/{link_chat_id}/{msg_id}"
            else:
                update.effective_message.reply_text(f"❎ *This command only works in public groups.*\n\n Visit @{SUPPORT_CHAT} to report bugs related to bot's pm.", parse_mode=ParseMode.MARKDOWN)
                return
        else:
            message.reply_text(
                    f"❎ *No bug to Report!* Use `/bug <information>`", parse_mode=ParseMode.MARKDOWN
                )
            return
            
        first_name = update.effective_user.first_name
        user = message.from_user
        mention = f"[{first_name}](tg://user?id={user.id}) [Shikimori Bot](https://t.me/micchon_shikimori_bot)"
        datetimes_fmt = "%d-%m-%Y"
        datetimes = datetime.utcnow().strftime(datetimes_fmt)
        bug_report = f"""
*#BUG :  @{OWNER_USERNAME}
From User :  {mention}
User ID :  {user_id}
Group :  @{link_chat_id}
Bug Report :  {bugs}
Event Stamp :  {datetimes}*
"""

        if user_id != OWNER_ID:
            message.reply_text(
                f"*Bug Report : {bugs}*\n\n"
                "✅ *The bug was successfully reported to the support group!*",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="❌ Close",
                                callback_data="close_reply_"
                            )
                        ]
                    ]
                ),
                parse_mode=ParseMode.MARKDOWN
            )
            dispatcher.bot.send_photo(
                f"@{SUPPORT_CHAT}",
                photo=STATS_IMG,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="➡ View Bug",
                                url=f"{message_link}",
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="❌ Close",
                                callback_data="close_send_photo_"
                            )
                        ]
                    ]
            ),
            parse_mode=ParseMode.MARKDOWN,
            )
    except:
        update.effective_message.reply_text(
            f"*ERROR!!! Contact @{SUPPORT_CHAT}*",
            parse_mode=ParseMode.MARKDOWN,
        )

def close_reply(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "close_reply_":
        query.message.delete()

def close_send_photo(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "close_send_photo_":
        user = update.effective_user
        if user.id in DEV_USERS:
            query.message.delete()
        else:
            msg = update.effective_message.reply_text(
            "Only developers can close Bug reports."
        )
            time.sleep(10)
            msg.delete()
            return

close_reply_handler = CallbackQueryHandler(
        close_reply, pattern=r"close_reply_", run_async=True
    )
close_send_photo_handler = CallbackQueryHandler(
    close_send_photo, pattern=r"close_send_photo_", run_async=True
)

BUG_HANDLER = CommandHandler(("bug", "bugs"), bug, run_async = True)

dispatcher.add_handler(BUG_HANDLER)
dispatcher.add_handler(close_reply_handler)
dispatcher.add_handler(close_send_photo_handler)

__command_list__ = ["bug"]
__handlers__ = [BUG_HANDLER]

__mod_name__ = "Bug"

__help__ = """
*Bug*
 ❍ `/bug` <information>: Reports bug to support group.
"""