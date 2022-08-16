from Shikimori.mongo import db

nsfwchatsdb = db.nsfwchats

def is_nsfw(chat_id: int) -> bool:
    nsfwchat = nsfwchatsdb.find_one({"chat_id": chat_id})
    if nsfwchat:
        return True
    return False

def set_nsfw(chat_id):
    nsfwchat = is_nsfw(chat_id)
    if nsfwchat:
        return
    return nsfwchatsdb.insert_one({"chat_id": chat_id})

def rem_nsfw(chat_id):
    nsfwchat = is_nsfw(chat_id)
    if not nsfwchat:
        return
    return nsfwchatsdb.delete_one({"chat_id": chat_id})