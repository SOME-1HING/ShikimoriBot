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

antichanneldb = db.antichannel

def antichannel_status(chat_id):
    is_achannel = antichanneldb.find_one({"chat_id": chat_id})
    if not is_achannel:
        return False
    else:
        return True

def enable_antichannel(chat_id):
    is_achannel = antichannel_status(chat_id)
    if is_achannel:
        return
    else:
        return antichanneldb.insert_one({"chat_id": chat_id})

def disable_antichannel(chat_id):
    is_achannel = antichannel_status(chat_id)
    if not is_achannel:
        return
    else:
        return antichanneldb.delete_one({"chat_id": chat_id})