"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import time
from telethon import events

from Shikimori import telethn, DEV_USERS
from Shikimori.modules.helper_funcs.telethn.chatstatus import (
    can_delete_messages,
    user_is_admin,
)


async def purge_messages(event):
    start = time.perf_counter()
    if event.from_id is None:
        return

    if (
        not await user_is_admin(
            user_id=event.sender_id,
            message=event,
        )
        and event.from_id not in DEV_USERS
    ):
        await event.reply("Only Admins are allowed to use this command")
        return

    if not await can_delete_messages(message=event):
        await event.reply("Can't seem to purge the message")
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to a message to select where to start purging from.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    try:
        await event.client.delete_messages(event.chat_id, messages)
    except:
        pass
    time_ = time.perf_counter() - start
    text = f"Purged Successfully in {time_:0.2f} Second(s)"
    await event.respond(text, parse_mode="markdown")

async def delete_messages(event):
    if event.from_id is None:
        return

    if (
        not await user_is_admin(
            user_id=event.sender_id,
            message=event,
        )
        and event.from_id not in DEV_USERS
    ):
        await event.reply("Only Admins are allowed to use this command")
        return

    if not await can_delete_messages(message=event):
        await event.reply("Can't seem to delete this?")
        return

    message = await event.get_reply_message()
    if not message:
        await event.reply("Whadya want to delete?")
        return
    chat = await event.get_input_chat()
    del_message = [message, event.message]
    await event.client.delete_messages(chat, del_message)

PURGE_HANDLER = purge_messages, events.NewMessage(pattern="^[!/]purge$")
DEL_HANDLER = delete_messages, events.NewMessage(pattern="^[!/]del$")

telethn.add_event_handler(*PURGE_HANDLER)
telethn.add_event_handler(*DEL_HANDLER)

__mod_name__ = "Purges"
__command_list__ = ["del", "purge"]
__handlers__ = [PURGE_HANDLER, DEL_HANDLER]
