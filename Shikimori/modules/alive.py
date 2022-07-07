import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Shikimori.events import register
from Shikimori import telethn as tbot
from Shikimori import ALIVE_MEDIA, UPDATE_CHANNEL, SUPPORT_CHAT


PHOTO = ALIVE_MEDIA

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Hinata Shoyo Robot.** \n\n"
  TEXT += "⚪ **I'm Working Properly** \n\n"
  TEXT += f"⚪ **My Owner : [Himanshu Mishra](https://t.me/madarauchiha_TheSageOfSixPaths)** \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Updates", f"https://t.me/{UPDATE_CHANNEL}"), Button.url("Support", f"https://t.me/{SUPPORT_CHAT}")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

__mod_name__ = "Alive ✨"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
