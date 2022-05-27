import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Shikimori.events import register
from Shikimori import telethn as tbot


PHOTO = "https://telegra.ph/file/2b04f7812f22b983f8a10.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Shikomori Robot.** \n\n"
  TEXT += "⚪ **I'm Working Properly** \n\n"
  TEXT += f"⚪ **My 'Boyfriend' and original 'Creator' : [Yash](https://github.com/SOME-1HING)**\n\n"
  TEXT += f"⚪ **My Owner : [Sneha](https://t.me/Sneha_UwU_OwO)** \n\n"
  TEXT += f"⚪ **My Manager : [【V๏ɪ፝֟𝔡】](https://t.me/VoidAryan)** \n\n"
  TEXT += f"⚪ **I am Powered by : [【V๏ɪ፝֟𝔡】»Network«](https://t.me/VoidxNetwork)** \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Updates", "https://t.me/Shikimori_bot_Updates"), Button.url("Support", "https://t.me/Shikimori_bot_Support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

__mod_name__ = "Alive"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
