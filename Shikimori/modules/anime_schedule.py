# ptb
import requests
from datetime import date
import calendar
from Shikimori import dispatcher
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update


curr_date = date.today()
tody = calendar.day_name[curr_date.weekday()]
today = tody.lower()

def schedule(update: Update, context: CallbackContext):
    message = update.effective_message
    results = requests.get(f'https://api.jikan.moe/v3/schedule/{today}').json()
    count = 0
    text = ''
    for i in results:
        j = results[today][0:7][count]['title']
        text += f'\n{count + 1} {j}'
        count += 1
    message.reply_text(text)

SCHEDULE_HANDLER = CommandHandler(('schedule', 'ongoing', 'latest'), schedule, run_async=True)

dispatcher.add_handler(SCHEDULE_HANDLER)

__handlers__ = [
    SCHEDULE_HANDLER
]


# # pyrogram    
# from pyrogram import filters
# from datetime import date
# import calendar
# from Shikimori import pbot

# curr_date = date.today()
# tody = calendar.day_name[curr_date.weekday()]
# today = tody.lower()

# @pbot.on_message(filters.command('schedule', 'ongoing', 'latest'))
# async def schedule(_, message):
#     results = requests.get(f'https://api.jikan.moe/v3/schedule/{today}').json()
#     count = 0
#     text = ''
#     for i in results:
#         j = results[today][0:7][count]['title']
#         text += f'\n{count + 1} {j}'
#         count += 1
#     await message.reply_text(text)

# # telethon
# from Shikimori import dispatcher, telethn as bot
# from telethon import events
# from datetime import date
# import calendar

# curr_date = date.today()
# tody = calendar.day_name[curr_date.weekday()]
# today = tody.lower()

# @bot.on(events.NewMessage(pattern='/(schedule|ongoing|latest)$)'))
# async def schedule(event):
#     results = requests.get(f'https://api.jikan.moe/v3/schedule/{today}').json()
#     count = 0
#     text = ''
#     for i in results:
#         j = results[today][0:7][count]['title']
#         text += f'\n{count + 1} {j}'
#         count += 1
#     await event.reply(text)
