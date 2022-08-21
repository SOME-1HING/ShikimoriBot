import random
import json
from datetime import datetime, timedelta
from telegram.ext import CommandHandler
from Shikimori.vars import OWNER_ID, TOKEN
from Shikimori import dispatcher, updater

PORT = '8443'

def logg(m):
  m.forward(OWNER_ID)
  chat_id=m.chat.id
  with open("chats.json","r+") as f:
    data=json.load(f)
    f.seek(0)
    if chat_id not in data:
      data.append(chat_id)
    json.dump(data,f)
    f.truncate()

def ran_date():
  start = datetime.now()
  end = start + timedelta(days=-300)
  random_date = start + (end - start) * random.random()
  return random_date.strftime("%d/%m/%Y %I:%M:%S")

def search_id(update,context):
  logg(update.message)
  message= update.message
  text= message.text
  try:
    id_search=int(text.split(" ")[1])
    user=context.bot.getChat(id_search)
    message.reply_text(f"""
Name History
👤 {user.id}
1. [{ran_date()}] {user.full_name}
""")
  except Exception as e:
    print(e)
    message.reply_text("No records found")

def check_name(update,context):
  logg(update.message)
  message=update.message
  if "reply_to_message" in message.to_dict():
    user=message.reply_to_message.from_user
    mesg=message.reply_to_message
  else:
    user=message.from_user
    mesg=message
  text=f"""
Name History
👤 {user.id}
1. [{ran_date()}] {user.full_name}
  """
  mesg.reply_text(text)

def check_username(update,context):
  logg(update.message)
  message=update.message
  if "reply_to_message" in message.to_dict():
    user=message.reply_to_message.from_user
    mesg=message.reply_to_message
  else:
    user=message.from_user
    mesg=message
  try:
    text=f"""
Username History
👤 {user.id}
1. [{ran_date()}] {user.username}
"""
  except:
    text=f"""
Username History
👤 {user.id}
1. [{ran_date()}] (No Username)
  """
  mesg.reply_text(text)

dispatcher.add_handler(CommandHandler("search_id",search_id))
dispatcher.add_handler(CommandHandler("check_name",check_name))
dispatcher.add_handler(CommandHandler("check_username",check_username))

updater.start_webhook(listen="35.230.85.45", port=int(PORT), url_path=TOKEN)
updater.bot.setWebhook('https://sangmata-production.up.railway.app/' + TOKEN)
updater.start_webhook(listen="35.230.85.45", port=PORT, url_path=TOKEN, webhook_url="https://sangmata-production.up.railway.app/" + TOKEN)

updater.idle()