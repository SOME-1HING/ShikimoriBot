from Shikimori.mongo import db

karma_statusdb = db.karma_status

def is_karma(chat_id: int) -> bool:
    karma = karma_statusdb.find_one({"chat_id": chat_id})
    if karma:
        return True
    return False

def set_karma(chat_id):
    karma = is_karma(chat_id)
    if karma:
        return
    return karma_statusdb.insert_one({"chat_id": chat_id})

def rem_karma(chat_id):
    karma = is_karma(chat_id)
    if not karma:
        return
    return karma_statusdb.delete_one({"chat_id": chat_id})
