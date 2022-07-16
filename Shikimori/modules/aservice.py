# Written By SOME-1HING for Shikimori
# Kang With Proper Credits

import asyncio
from pyrogram import filters

from Shikimori import DRAGONS, pbot
import Shikimori.modules.sql.antiservice_sql as ssql

__mod_name__ = "AntiService"
__help__ = """
Plugin to delete service messages in a chat!

/antiservice
"""

@pbot.on_message(filters.service)
async def del_service(_, message):
    chat_id = message.chat.id
    try:
        is_aservice = ssql.is_aservice(chat_id)
        if is_aservice:
            await asyncio.sleep(10)
            await message.delete()
    except Exception as e:
        print("anti-service - " + str(e))
