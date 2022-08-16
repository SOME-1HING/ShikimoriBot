from Shikimori.mongo import db

Nsfwatchdb = db.Nsfwatch

def is_nsfwatch_indb(chat_id: int) -> bool:
    nsfwm = Nsfwatchdb.find_one({"chat_id": chat_id})
    if not nsfwm:
        return True
    return False

def add_nsfwatch(chat_id):
    nsfwm = is_nsfwatch_indb(chat_id)
    if not nsfwm:
        return
    return Nsfwatchdb.insert_one({"chat_id": chat_id})

def rmnsfwatch(chat_id):
    nsfwm = is_nsfwatch_indb(chat_id)
    if nsfwm:
        return
    return Nsfwatchdb.delete_one({"chat_id": chat_id})