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
        nsfwchat = SESSION.query(ANTISERVICEChats).get(str(chat_id))
        if not nsfwchat:
            nsfwchat = ANTISERVICEChats(str(chat_id))
        SESSION.add(nsfwchat)
        SESSION.commit()

def rem_aservice(chat_id):
    with INSERTION_LOCK:
        nsfwchat = SESSION.query(ANTISERVICEChats).get(str(chat_id))
        if nsfwchat:
            SESSION.delete(nsfwchat)
        SESSION.commit()


def get_all_aservice_chats():
    try:
        return SESSION.query(ANTISERVICEChats.chat_id).all()
    finally:
        SESSION.close()
