import threading
from sqlalchemy import Column, String
from Shikimori.modules.sql import BASE, SESSION
class ChatBot_chats(BASE):
    __tablename__ = "chatbot_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

ChatBot_chats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()

def is_chatbot(chat_id):
    try:
        chat = SESSION.query(ChatBot_chats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()

def set_chatbot(chat_id):
    with INSERTION_LOCK:
        ai_chats = SESSION.query(ChatBot_chats).get(str(chat_id))
        if not ai_chats:
            ai_chats = ChatBot_chats(str(chat_id))
        SESSION.add(ai_chats)
        SESSION.commit()

def rem_chatbot(chat_id):
    with INSERTION_LOCK:
        ai_chats = SESSION.query(ChatBot_chats).get(str(chat_id))
        if ai_chats:
            SESSION.delete(ai_chats)
        SESSION.commit()


def get_all_chatbot_chats():
    try:
        return SESSION.query(ChatBot_chats.chat_id).all()
    finally:
        SESSION.close()
