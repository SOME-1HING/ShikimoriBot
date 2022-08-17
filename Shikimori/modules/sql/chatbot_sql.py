"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

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

chatbotdb = db.chatbot

def is_chatbot(chat_id):
    chatbot = chatbotdb.find_one({"chat_id": chat_id})
    if not chatbot:
        return False
    else:
        return True

def add_chatbot(chat_id):
    chatbot = is_chatbot(chat_id)
    if chatbot:
        return
    else:
        return chatbotdb.insert_one({"chat_id": chat_id})

def rm_chatbot(chat_id):
    chatbot = is_chatbot(chat_id)
    if not chatbot:
        return
    else:
        return chatbotdb.delete_one({"chat_id": chat_id})
