# Made By Mozila kang .

import asyncio
from Shikimori import pbot as app, OWNER_ID
from Shikimori.utils.errors import capture_err
from pyrogram import *
from pyrogram.types import *
import Shikimori.modules.sql.users_sql as sql

from pymongo import MongoClient

MONGO_DB_URL = ""

worddb = MongoClient(MONGO_DB_URL) 
k = worddb["Shikimori"]["live_stats"]


@app.on_message(
    filters.text
    & ~filters.private,
)
async def live(client: Client, message: Message):
    is_live = k.find_one({"live": "stats"})
    users = f"{sql.num_users()}"
    chats = f"{sql.num_chats()}"
    captionk =  f"Live Shikimori Stats\n♡ 𝐔𝐬𝐞𝐫𝐬 {sql.num_users()}\n\n♡ 𝐂𝐡𝐚𝐭𝐬:{sql.num_chats()}"
    if not is_live:     
        k.insert_one({"live": "stats", "user": users, "chat": chats})
        await app.edit_message_text(chat_id=-1001605084393, message_id=39, text=captionk, disable_web_page_preview=True)
    if is_live:       
        is_live2 = k.find_one({"live": "stats", "user": users, "chat": chats})
        if not is_live2:       
            k.update_one({"live": "stats"}, {"$set": {"user": users, "chat": chats}})
            # editing chat_id and message id
            await app.edit_message_text(chat_id=-1001605084393, message_id=39, text=captionk, disable_web_page_preview=True)
   
  
