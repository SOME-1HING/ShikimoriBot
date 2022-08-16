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

import threading
from sqlalchemy import Column, String, UnicodeText, func, distinct
from Shikimori.modules.sql_2 import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger

class Approvals(BASE):
    __tablename__ = "approval"
    chat_id = Column(String(14), primary_key=True)
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, chat_id, user_id):
        self.chat_id = str(chat_id)  # ensure string
        self.user_id = user_id

    def __repr__(self):
        return "<Approve %s>" % self.user_id


Approvals.__table__.create(checkfirst=True)

APPROVE_INSERTION_LOCK = threading.RLock()


def approve(chat_id, user_id):
    with APPROVE_INSERTION_LOCK:
        approve_user = Approvals(str(chat_id), user_id)
        SESSION.add(approve_user)
        SESSION.commit()


def is_approved(chat_id, user_id):
    try:
        return SESSION.query(Approvals).get((str(chat_id), user_id))
    finally:
        SESSION.close()


def disapprove(chat_id, user_id):
    with APPROVE_INSERTION_LOCK:
        disapprove_user = SESSION.query(Approvals).get((str(chat_id), user_id))
        if disapprove_user:
            SESSION.delete(disapprove_user)
            SESSION.commit()
            return True
        else:
            SESSION.close()
            return False


def list_approved(chat_id):
    try:
        return (
            SESSION.query(Approvals)
            .filter(Approvals.chat_id == str(chat_id))
            .order_by(Approvals.user_id.asc())
            .all()
        )
    finally:
        SESSION.close()
