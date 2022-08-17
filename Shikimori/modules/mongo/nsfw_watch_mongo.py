from Shikimori.mongo import db

Nsfwatchdb = db.Nsfwatch

def is_nsfwatch_indb(chat_id):
    nsfwm = Nsfwatchdb.find_one({"chat_id": chat_id})
    if not nsfwm:
        return False
    else:
        return True

def add_nsfwm(chat_id):
    nsfwm = is_nsfwatch_indb(chat_id)
    if nsfwm:
        return
    else:
        return Nsfwatchdb.insert_one({"chat_id": chat_id})

def rm_nsfwm(chat_id):
    nsfwm = is_nsfwatch_indb(chat_id)
    if not nsfwm:
        return
    else:
        return Nsfwatchdb.delete_one({"chat_id": chat_id})