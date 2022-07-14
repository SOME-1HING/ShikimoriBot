"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
