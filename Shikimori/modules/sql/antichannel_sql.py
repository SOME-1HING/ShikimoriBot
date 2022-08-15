from Shikimori.mongo import db

antichanneldb = db.antichannel

async def is_achannel(chat_id: int) -> bool:
    chat = antichanneldb.find_one({"chat_id": chat_id})
    if not chat:
        return True
    return False

def set_achannel(chat_id):
    is_achannel = is_achannel(chat_id)
    if not is_achannel:
        return
    return antichanneldb.insert_one({"chat_id": chat_id})

def rem_achannel(chat_id):
    is_achannel = is_achannel(chat_id)
    if is_achannel:
        return
    return antichanneldb.delete_one({"chat_id": chat_id})