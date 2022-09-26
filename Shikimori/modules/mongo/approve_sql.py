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

from typing import Dict, List

from Shikimori.mongo import db

approval = db.approval

def approve(chat_id, user_id):
    return approval.update_one({"chat_id": str(chat_id)}, {"$set": {"user_id" : user_id}}, upsert=True)

def is_approved(chat_id, user_id):
    is_approv = approval.find_one({"chat_id": chat_id, "user_id": user_id})
    return bool(is_approv)

def disapprove(chat_id, user_id):
    return approval.delete_one({"chat_id": chat_id, "user_id": user_id})

def get_approved(chat_id: int) -> Dict[str, int]:
    _approved = approval.find_one({"chat_id": chat_id})
    if not _approved:
        return {}
    return _approved["filters"]


def list_approved(chat_id: int) -> List[str]:
    _approved = []
    for _filter in get_approved(chat_id):
        _approved.append(_filter)
    return _approved
