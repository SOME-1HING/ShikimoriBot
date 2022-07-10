from datetime import datetime
from email import message

from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from Shikimori import DEV_USERS, OWNER_ID, STATS_IMG, pbot
from Shikimori import (
    OWNER_ID,
    OWNER_USERNAME,
    SUPPORT_CHAT,
)
from Shikimori.utils.errors import capture_err


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@pbot.on_message(filters.command("bug"))
@capture_err
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username} / `{msg.chat.id}`")
    else:
        chat_username = (f"Private Group / `{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)
    bug_report = f"""
**#BUG : ** **@{OWNER_USERNAME}**
**From User : ** **{mention}**
**User ID : ** **{user_id}**
**Group : ** **{chat_username}**
**Bug Report : ** **{bugs}**
**Event Stamp : ** **{datetimes}**"""

    
    if msg.chat.type != "private":
        if user_id == OWNER_ID:
            if bugs:
                await msg.reply_text(
                    "❎ <b>Why owner of bot reporting a bug?? Go fix yourself</b>",
                )
                return
            else:
                await msg.reply_text(
                    "❎ <b>Why owner of bot reporting a bug?? Go fix yourself</b>"
                )
        elif user_id != OWNER_ID:
            if bugs:
                await msg.reply_text(
                    f"<b>Bug Report : {bugs}</b>\n\n"
                    "✅ <b>The bug was successfully reported to the support group!</b>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Close", callback_data=f"close_reply")
                            ]
                        ]
                    )
                )
            await pbot.send_photo(
                SUPPORT_CHAT,
                photo=STATS_IMG,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "➡ View Bug", url=f"{msg.link}")
                        ],
                        [
                            InlineKeyboardButton(
                                "❌ Close", callback_data="close_send_photo")
                        ]
                    ]
                )
            )
        else:
            await msg.reply_text(
                f"❎ <b>No bug to Report!</b> Use `/bug <information>`",
            )
    else:
        await msg.reply_text(f"❎ <b>This command only works in groups.</b>\n\n Visit @{SUPPORT_CHAT} to report bugs related to bot's pm.")

@pbot.on_callback_query(filters.regex("close_reply"))
async def close_reply(client: pbot, query: CallbackQuery):
    await query.message.delete()

@pbot.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(client: pbot, query: CallbackQuery):
    user_id = query.from_user.id
    if user_id not in DEV_USERS :
        return await query.message(
            "Only developers can close Bug reports.", show_alert=True
        )
    else:
        await query.message.delete()
        

__mod_name__ = "Bug"

__help__ = """
*Bug*
 ❍ `/bug` <information>: Reports bug to support group.
"""