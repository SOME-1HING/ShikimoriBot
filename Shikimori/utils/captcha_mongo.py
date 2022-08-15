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

from pymongo import MongoClient

from Shikimori.vars import MONGO_DB_URI


class manage_db:
    def __init__(self):
        self.db = MongoClient(MONGO_DB_URI)["captcha"]
        self.chats = self.db["Chats"]

    def chat_in_db(self, chat_id):
        chat = self.chats.find_one({"chat_id": chat_id})
        return chat

    def add_chat(self, chat_id, captcha):
        if self.chat_in_db(chat_id):
            return 404
        self.chats.insert_one({"chat_id": chat_id, "captcha": captcha})
        return 200

    def delete_chat(self, chat_id):
        self.chats.delete_many({"chat_id": chat_id})
        return True
