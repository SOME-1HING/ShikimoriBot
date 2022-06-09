from Shikimori.mongo import client as db_x

chatbot_ai = db_x["chatbot_chats"]

def set_chatbot(chat_id):
    stark = chatbot_ai.find_one({"chat_id": chat_id})
    if stark:
        return False
    chatbot_ai.insert_one({"chat_id": chat_id})
    return True

def rem_chatbot(chat_id):
    stark = chatbot_ai.find_one({"chat_id": chat_id})
    if not stark:
        return False
    chatbot_ai.delete_one({"chat_id": chat_id})
    return True
