from time import perf_counter
from cachetools import TTLCache
from threading import RLock
from Shikimori import (
    DEV_USERS,
    DRAGONS,
)
from pyrogram.types import Chat, ChatMember
from pyrogram import enums
from Shikimori import pbot

# stores admemes in memory for 10 min.
ADMIN_CACHE = TTLCache(maxsize=512, ttl=60 * 10, timer=perf_counter)
THREAD_LOCK = RLock()

def is_user_pyro_admin(chat: Chat, user_id: int, member: ChatMember = None) -> bool:
    if (
        chat.type == "private"
        or user_id in DRAGONS
        or user_id in DEV_USERS
        or user_id in [777000, 1087968824]
    ):
        return True
    if not member:
        with THREAD_LOCK:
            try:
                return user_id in ADMIN_CACHE[chat.id]
            except KeyError:
                chat_admins = pbot.get_chat_members(chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
                admin_list = [x.user.id for x in chat_admins]
                ADMIN_CACHE[chat.id] = admin_list
                return user_id in admin_list
    else:
        return member.status in ("administrator", "creator")