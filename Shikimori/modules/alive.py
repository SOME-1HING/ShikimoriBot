import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Shikimori.events import register
from Shikimori import telethn as tbot


PHOTO = "https://telegra.ph/file/b7759b3636989914441fc.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Zoro Robot.** \n\n"
  TEXT += "⚪ **I'm Working Properly** \n\n"
  TEXT += f"⚪ **My Owner : [【🌀 长工尺工丅口 🌀】](https://t.me/asta_est)** \n\n"
  TEXT += f"⚪ **I am Powered by : [【XYZ】»Network«](https://t.me/TeamXYZNetwork)** \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Updates", "https://t.me/rukaxUpdates"), Button.url("Support", "https://t.me/tyranteyeeee")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

__mod_name__ = "Alive ✨"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
