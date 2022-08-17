"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging
import sys
import time
from Shikimori.vars import OWNER_ID, DEV_USERS, DEMONS, DRAGONS, TOKEN, WORKERS, API_HASH, API_ID, WOLVES, ARQ_API_KEY, TIGERS
from pyrogram import Client, filters
from aiohttp import ClientSession
import telegram.ext as tg
from telethon import TelegramClient
from Python_ARQ import ARQ
from telethon.sessions import MemorySession

StartTime = time.time()

# enable logging
FORMAT = "[Shikimori] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("bot_logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger('ptbcontrib.postgres_persistence.postgrespersistence').setLevel(logging.WARNING)

LOGGER = logging.getLogger('[Shikimori]')
LOGGER.info("Shikimori is starting. | Built by SOME1HING. | Licensed under GPLv3.")
LOGGER.info("Handled by: github.com/SOME-1HING (t.me/SOME1HING)")

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
session = ClientSession()
print("[INFO]: AIOHTTP SESSION INITIALIZED")

# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ("https://arq.hamker.in", ARQ_API_KEY, session)
print("[INFO]: ARQ CLIENT INITIALIZED")

# Pyrogram CLient
print("[INFO]: INITIALIZING PYROGRAM CLIENT")
pbot = Client("ShikimoriPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
print("[INFO]: PYROGRAM CLIENT INITIALIZED")

# PTB Client
print("[INFO]: INITIALIZING PTB CLIENT")
defaults = tg.Defaults(run_async=True)
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
dispatcher = updater.dispatcher
print("[INFO]: PTB CLIENT INITIALIZED")

# Telethon Client
print("[INFO]: INITIALIZING TELETHON CLIENT")
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
print("[INFO]: TELETHON CLIENT INITIALIZED")

# Updating Sudo list
DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
SUDOERS = filters.user()
DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from Shikimori.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler


