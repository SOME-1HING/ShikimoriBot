import threading
from sqlalchemy import Column, String
from Shikimori.modules.sql import BASE, SESSION

class ANTICHANNELChats(BASE):
    __tablename__ = "antichannel_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

ANTICHANNELChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_achannel(chat_id):
    try:
        chat = SESSION.query(ANTICHANNELChats).get(str(chat_id))
        if chat:
            return True
        else:
            return False
    finally:
        SESSION.close()

def set_aservice(chat_id):
    with INSERTION_LOCK:
        achannnelchat = SESSION.query(ANTICHANNELChats).get(str(chat_id))
        if not achannnelchat:
            achannnelchat = ANTICHANNELChats(str(chat_id))
        SESSION.add(achannnelchat)
        SESSION.commit()

def rem_aservice(chat_id):
    with INSERTION_LOCK:
        achannnelchat = SESSION.query(ANTICHANNELChats).get(str(chat_id))
        if achannnelchat:
            SESSION.delete(achannnelchat)
        SESSION.commit()