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

Rules = db.rules

def set_rules(chat_id, rules_text):
    rules = Rules.find_one({"chat_id": chat_id})
    if not rules:
        rules = Rules(str(chat_id))
    rules.rules = rules_text
    return Rules.update_one({"chat_id": chat_id}, {"$set": {"rules" : rules_text}}, upsert=True)


def get_rules(chat_id):
    rules = Rules.find_one({"chat_id": chat_id})
    if rules:
        rules_text = Rules.rules
    return rules_text

def num_chats() -> int:
    bl = Rules.find({"chat_id": {"$gt": 0}})
    bl = bl.to_list(length=100000)
    return len(bl)


def migrate_chat(old_chat_id, new_chat_id):
    chat = Rules.find_one({"chat_id": old_chat_id})
    if chat:
        chat.chat_id = str(new_chat_id)
