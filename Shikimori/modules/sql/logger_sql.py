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

from sqlalchemy import Column, String, Boolean

from Shikimori.modules.sql import BASE, SESSION

class LoggerSettings(BASE):
    __tablename__ = "chat_log_settings"
    chat_id = Column(String(14), primary_key=True)
    setting = Column(Boolean, default=False, nullable=False)

    def __init__(self, chat_id, disabled):
        self.chat_id = str(chat_id)
        self.setting = disabled

    def __repr__(self):
        return "<Chat log setting {} ({})>".format(self.chat_id, self.setting)

LoggerSettings.__table__.create(checkfirst=True)

LOG_SETTING_LOCK = threading.RLock()
LOGSTAT_LIST = set()

def enable_chat_log(chat_id):
    with LOG_SETTING_LOCK:
        chat = SESSION.query(LoggerSettings).get(str(chat_id))
        if not chat:
            chat = LoggerSettings(chat_id, True)
        chat.setting = True
        SESSION.add(chat)
        SESSION.commit()
        if str(chat_id) in LOGSTAT_LIST:
            LOGSTAT_LIST.remove(str(chat_id))

def disable_chat_log(chat_id):
    with LOG_SETTING_LOCK:
        chat = SESSION.query(LoggerSettings).get(str(chat_id))
        if not chat:
            chat = LoggerSettings(chat_id, False)

        chat.setting = False
        SESSION.add(chat)
        SESSION.commit()
        LOGSTAT_LIST.add(str(chat_id))

def does_chat_log(chat_id):
    return str(chat_id) not in LOGSTAT_LIST

def __load_chat_log_stat_list():
    global LOGSTAT_LIST
    try:
        LOGSTAT_LIST = {
            x.chat_id for x in SESSION.query(LoggerSettings).all() if not x.setting
        }
    finally:
        SESSION.close()

def migrate_chat(old_chat_id, new_chat_id):
    with LOG_SETTING_LOCK:
        chat = SESSION.query(LoggerSettings).get(str(old_chat_id))
        if chat:
            chat.chat_id = new_chat_id
            SESSION.add(chat)

        SESSION.commit()


# Create in memory userid to avoid disk access
__load_chat_log_stat_list()
