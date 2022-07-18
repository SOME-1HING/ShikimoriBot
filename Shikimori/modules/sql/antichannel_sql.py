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

from sqlalchemy import Boolean
from sqlalchemy.sql.sqltypes import String
from sqlalchemy import Column

from Shikimori.modules.sql import BASE, SESSION


class AntiChannelSettings(BASE):
    __tablename__ = "anti_channel_settings"
    
    chat_id = Column(String(14), primary_key=True)
    setting = Column(Boolean, default=False, nullable=False)

    def __init__(self, chat_id: int, disabled: bool):
        self.chat_id = str(chat_id)
        self.setting = disabled

    def __repr__(self):
        return "<Antiflood setting {} ({})>".format(self.chat_id, self.setting)


AntiChannelSettings.__table__.create(checkfirst=True)
ANTICHANNEL_SETTING_LOCK = threading.RLock()

def enable_antichannel(chat_id: int):
    with ANTICHANNEL_SETTING_LOCK:
        chat = SESSION.query(AntiChannelSettings).get(str(chat_id))
        if not chat:
            chat = AntiChannelSettings(str(chat_id), True)

        chat.setting = True
        SESSION.add(chat)
        SESSION.commit()


def disable_antichannel(chat_id: int):
    with ANTICHANNEL_SETTING_LOCK:
        chat = SESSION.query(AntiChannelSettings).get(str(chat_id))
        if not chat:
            chat = AntiChannelSettings(str(chat_id), False)

        chat.setting = False
        SESSION.add(chat)
        SESSION.commit()


def antichannel_status(chat_id: int) -> bool:
    with ANTICHANNEL_SETTING_LOCK:
        d = SESSION.query(AntiChannelSettings).get(str(chat_id))
        if not d:
            return False
        return d.setting




def migrate_chat(old_chat_id, new_chat_id):
    with ANTICHANNEL_SETTING_LOCK:
        chat = SESSION.query(AntiChannelSettings).get(str(old_chat_id))
        if chat:
            chat.chat_id = new_chat_id
            SESSION.add(chat)

        SESSION.commit()
