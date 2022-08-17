from Shikimori.mongo import db

nsfwchatsdb = db.nsfwchats

def is_nsfw(chat_id):
    nsfwchat = nsfwchatsdb.find_one({"chat_id": chat_id})
    if not nsfwchat:
        return False
    else:
        return True

def set_nsfw(chat_id):
    nsfwchat = is_nsfw(chat_id)
    if nsfwchat:
        return
    else:
        return nsfwchatsdb.insert_one({"chat_id": chat_id})

def rem_nsfw(chat_id):
    nsfwchat = is_nsfw(chat_id)
    if not nsfwchat:
        return
    else:
        return nsfwchatsdb.delete_one({"chat_id": chat_id})