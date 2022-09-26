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

afkdb = db.afk

def is_user_afk(userid):
    is_afk = afkdb.find_one({"user_id": userid})
    return bool(is_afk)

def start_afk(userid, reason, time):
    return afkdb.update_one({"user_id": userid}, {"$set": {"reason" : reason, "time" : time}}, upsert=True)

def afk_reason(userid):
    user = strb(userid)
    if user:
        return user["reason"]

def afk_time(userid):
    user = strb(userid)
    if user:
        return user["time"]

def end_afk(userid):
    afkdb.delete_one({"user_id": userid})
    return True
    

# Helpers
def strb(user_id):
    return afkdb.find_one({"user_id": user_id})
