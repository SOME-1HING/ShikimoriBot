import threading
from sqlalchemy import Column, String
from Shikimori.modules.sql import BASE, SESSION

class KARMAChats(BASE):
    __tablename__ = "karma_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

KARMAChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_karma(chat_id):
    try:
        chat = SESSION.query(KARMAChats).get(str(chat_id))
        if chat:
            return True
        else:
            return False
    finally:
        SESSION.close()

def set_karma(chat_id):
    with INSERTION_LOCK:
        nsfwchat = SESSION.query(KARMAChats).get(str(chat_id))
        if not nsfwchat:
            nsfwchat = KARMAChats(str(chat_id))
        SESSION.add(nsfwchat)
        SESSION.commit()

def rem_karma(chat_id):
    with INSERTION_LOCK:
        nsfwchat = SESSION.query(KARMAChats).get(str(chat_id))
        if nsfwchat:
            SESSION.delete(nsfwchat)
        SESSION.commit()


def get_all_karma_chats():
    try:
        return SESSION.query(KARMAChats.chat_id).all()
    finally:
        SESSION.close()
