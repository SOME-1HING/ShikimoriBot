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

aservice = db.aservice

def is_aservice(chat_id: int) -> bool:
    chat = aservice.find_one({"chat_id": chat_id})
    if chat:
        return True
    return False

def set_aservice(chat_id):
    aservice = aservice(chat_id)
    if aservice:
        return
    return aservice.insert_one({"chat_id": chat_id})

def rem_aservice(chat_id):
    aservice = aservice(chat_id)
    if not aservice:
        return
    return aservice.delete_one({"chat_id": chat_id})