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

from Shikimori.modules.helper_funcs.telethn import IMMUNE_USERS, telethn
from Shikimori import DRAGONS
from telethon.tl.types import ChannelParticipantsAdmins


async def user_is_ban_protected(user_id: int, message):
    status = False
    if message.is_private or user_id in (IMMUNE_USERS):
        return True

    async for user in telethn.iter_participants(
        message.chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if user_id == user.id:
            status = True
            break
    return status


async def user_is_admin(user_id: int, message):
    status = False
    if message.is_private:
        return True

    async for user in telethn.iter_participants(
        message.chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if user_id == user.id or user_id in DRAGONS:
            status = True
            break
    return status


async def is_user_admin(user_id: int, chat_id):
    status = False
    async for user in telethn.iter_participants(
        chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if user_id == user.id or user_id in DRAGONS:
            status = True
            break
    return status


async def saitama_is_admin(chat_id: int):
    status = False
    saitama = await telethn.get_me()
    async for user in telethn.iter_participants(
        chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if saitama.id == user.id:
            status = True
            break
    return status


async def is_user_in_chat(chat_id: int, user_id: int):
    status = False
    async for user in telethn.iter_participants(chat_id):
        if user_id == user.id:
            status = True
            break
    return status


async def can_change_info(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.change_info
    return status


async def can_ban_users(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.ban_users
    return status


async def can_pin_messages(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.pin_messages
    return status


async def can_invite_users(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.invite_users
    return status


async def can_add_admins(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.add_admins
    return status


async def can_delete_messages(message):

    if message.is_private:
        return True
    if message.chat.admin_rights:
        status = message.chat.admin_rights.delete_messages
        return status
    return False
