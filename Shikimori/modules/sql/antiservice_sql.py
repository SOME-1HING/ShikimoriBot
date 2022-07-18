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

import threading
from sqlalchemy import Column, String
from Shikimori.modules.sql import BASE, SESSION

class ANTISERVICEChats(BASE):
    __tablename__ = "antiservice_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

ANTISERVICEChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_aservice(chat_id):
    try:
        chat = SESSION.query(ANTISERVICEChats).get(str(chat_id))
        if chat:
            return True
        else:
            return False
    finally:
        SESSION.close()

def set_aservice(chat_id):
    with INSERTION_LOCK:
        aservicechat = SESSION.query(ANTISERVICEChats).get(str(chat_id))
        if not aservicechat:
            aservicechat = ANTISERVICEChats(str(chat_id))
        SESSION.add(aservicechat)
        SESSION.commit()

def rem_aservice(chat_id):
    with INSERTION_LOCK:
        aservicechat = SESSION.query(ANTISERVICEChats).get(str(chat_id))
        if aservicechat:
            SESSION.delete(aservicechat)
        SESSION.commit()
