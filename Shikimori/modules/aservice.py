# Written By SOME-1HING for Shikimori
# Kang With Proper Credits

import asyncio
from pyrogram import filters

from Shikimori import pbot
from Shikimori.modules.helper_funcs.anonymous import user_admin
import Shikimori.modules.sql.antiservice_sql as sql

__mod_name__ = "AntiService"
__help__ = """
Plugin to delete service messages in a chat!

/antiservice [ON|OFF]
"""

@user_admin
@pbot.on_message(filters.command("antiservice") & filters.group)
async def aservice_state(_, message):
    try:
        usage = "**Usage:**\n/antiservice [ON|OFF]"
        if len(message.command) != 2:
            return await message.reply_text(usage)
        chat_id = message.chat.id
        state = message.text.split(None, 1)[1].strip()
        state = state.lower()
        if state == "on":
            is_aservice = sql.is_aservice(chat_id)
            if not is_aservice:
                sql.set_aservice(chat_id)
                await message.reply_text("Enabled AntiService System. I will Delete Service Messages from Now on.")
            else:
                await message.reply_text("AntiService System is already on.")
        elif state == "off":
            is_aservice = sql.is_aservice(chat_id)
            if not is_aservice:
                await message.reply_text("AntiService System is already disabled.")
                return ""
            else:
                sql.rem_aservice(chat_id)
            await message.reply_text("Disabled AntiService System. I won't Be Deleting Service Message from Now on.")
        else:
            await message.reply_text(usage)
    except Exception as e:
        return print("aservice - " + str(e))

@pbot.on_message(filters.service & filters.group)
async def del_service(_, message):
    chat_id = message.chat.id
    try:
        is_aservice = sql.is_aservice(chat_id)
        if not is_aservice:
            return
        await asyncio.sleep(1)
        await message.delete()
        return

    except Exception as e:
        return print("anti-service - " + str(e))
