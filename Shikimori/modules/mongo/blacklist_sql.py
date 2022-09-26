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

from Shikimori.mongo import db

CHAT_BLACKLISTS = {}
CHAT_SETTINGS_BLACKLISTS = {}

blacklist = db.blacklist
blacklistset = db.blacklistset

def add_to_blacklist(chat_id, trigger):
    blacklist.update_one({"chat_id": str(chat_id)}, {"$set": {"trigger" : trigger}}, upsert=True)
    if CHAT_BLACKLISTS.get(str(chat_id), set()) == set():
            CHAT_BLACKLISTS[str(chat_id)] = {trigger}
    else:
        CHAT_BLACKLISTS.get(str(chat_id), set()).add(trigger)

def rm_from_blacklist(chat_id, trigger):
    blacklist_filt = blacklist.find_one({"chat_id": str(chat_id), "trigger" : trigger})
    if blacklist_filt:
        if trigger in CHAT_BLACKLISTS.get(str(chat_id), set()):  # sanity check
            CHAT_BLACKLISTS.get(str(chat_id), set()).remove(trigger)

        blacklist.delete_one({"chat_id": str(chat_id), "trigger" : trigger})
        return True
    return False

def get_chat_blacklist(chat_id):
    return CHAT_BLACKLISTS.get(str(chat_id), set())

def num_blacklist_filters() -> int:
    bl = blacklist.find({"chat_id": {"$gt": 0}})
    bl = bl.to_list(length=100000)
    return len(bl)

def num_blacklist_chat_filters(chat_id) -> int:
    bl = blacklist.find({"chat_id": chat_id})
    bl = bl.to_list(length=100000)
    return len(bl)

def num_blacklist_filter_chats() -> int:
    bl = blacklist.find({"chat_id": {"$gt": 0}})
    bl = bl.to_list(length=100000)
    return len(bl)

def set_blacklist_strength(chat_id, blacklist_type, value):
    # for blacklist_type
    # 0 = nothing
    # 1 = delete
    # 2 = warn
    # 3 = mute
    # 4 = kick
    # 5 = ban
    # 6 = tban
    # 7 = tmute
    global CHAT_SETTINGS_BLACKLISTS
    curr_setting = blacklist.find_one({"chat_id": str(chat_id)})
    if not curr_setting:
        blacklistset.update_one({"chat_id": str(chat_id)}, {"$set": {"trigger" : int(blacklist_type), "value" : value}}, upsert=True)

    curr_setting.blacklist_type = int(blacklist_type)
    curr_setting.value = str(value)
    CHAT_SETTINGS_BLACKLISTS[str(chat_id)] = {
        "blacklist_type": int(blacklist_type),
        "value": value,
    }

    blacklistset.update_one(curr_setting, upsert=True)

def get_blacklist_setting(chat_id):
    setting = CHAT_SETTINGS_BLACKLISTS.get(str(chat_id))
    if setting:
        return setting["blacklist_type"], setting["value"]
    return 1, "0"


def __load_chat_blacklists():
    global CHAT_BLACKLISTS
    chats = blacklist.find({"chat_id": {"$gt": 0}})
    for (chat_id,) in chats:  # remove tuple by ( ,)
        CHAT_BLACKLISTS[chat_id] = []

    all_filters = blacklist.find({"chat_id": {"$gt": 0}}, {"trigger": {"$gt": 0}})
    for x in all_filters:
        CHAT_BLACKLISTS[x.chat_id] += [x.trigger]

    CHAT_BLACKLISTS = {x: set(y) for x, y in CHAT_BLACKLISTS.items()}


def __load_chat_settings_blacklists():
    chats_settings = blacklistset.find({"chat_id": {"$gt": 0}})
    for x in chats_settings:  # remove tuple by ( ,)
        CHAT_SETTINGS_BLACKLISTS[x.chat_id] = {
            "blacklist_type": x.blacklist_type,
            "value": x.value,
        }

def migrate_chat(old_chat_id, new_chat_id):
    chat_filters = blacklist.find({"chat_id": old_chat_id})
    for filt in chat_filters:
            filt.chat_id = str(new_chat_id)


__load_chat_blacklists()
__load_chat_settings_blacklists()


