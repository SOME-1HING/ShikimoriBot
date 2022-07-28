"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import datetime
import platform
import time
from psutil import cpu_percent, virtual_memory, disk_usage, boot_time
from platform import python_version

from telegram import __version__ as ptbver, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import CommandHandler
from telegram.helpers import escape_markdown
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
    
from Shikimori import (
    SUPPORT_CHAT,
    UPDATE_CHANNEL,
    dispatcher,
    StartTime,
    STATS_IMG,
)
from Shikimori.__main__ import STATS
from Shikimori.modules.helper_funcs.chat_status import sudo_plus


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@sudo_plus
def stats(update, context):
    uptime = datetime.datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    botuptime = get_readable_time((time.time() - StartTime))
    status = "*╒═══「 System statistics 」*\n\n"
    status += "*➢ System Start time:* " + str(uptime) + "\n"
    uname = platform.uname()
    status += "*➢ System:* " + str(uname.system) + "\n"
    status += "*➢ Node name:* " + escape_markdown(str(uname.node)) + "\n"
    status += "*➢ Release:* " + escape_markdown(str(uname.release)) + "\n"
    status += "*➢ Machine:* " + escape_markdown(str(uname.machine)) + "\n"
    mem = virtual_memory()
    cpu = cpu_percent()
    disk = disk_usage("/")
    status += "*➢ CPU:* " + str(cpu) + " %\n"
    status += "*➢ RAM:* " + str(mem[2]) + " %\n"
    status += "*➢ Storage:* " + str(disk[3]) + " %\n\n"
    status += "*➢ Python Version:* " + python_version() + "\n"
    status += "*➢ Python-Telegram-Bot:* " + str(ptbver) + "\n"
    status += "*➢ Telethon Version:* " + str(tlhver) + "\n"
    status += "*➢ Pyrogram Version:* " + str(pyrover) + "\n"
    status += "*➢ Uptime:* " + str(botuptime) + "\n"
    try:
        if STATS_IMG:
            update.effective_message.reply_photo(
                STATS_IMG,
                status
                + "\n𝕭𝖔𝖙 𝖘𝖙𝖆𝖙𝖎𝖘𝖙𝖎𝖈𝖘:\n"
                + "\n".join([mod.__stats__() for mod in STATS]),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [                  
                            InlineKeyboardButton(
                                    text="REPO",
                                    url="https://github.com/SOME-1HING/ShikimoriBot"),
                        ]
                    ]
                ),
            )
        else:
            update.effective_message.reply_text(
                status
                + "\n𝕭𝖔𝖙 𝖘𝖙𝖆𝖙𝖎𝖘𝖙𝖎𝖈𝖘:\n"
                + "\n".join([mod.__stats__() for mod in STATS]),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [                  
                            InlineKeyboardButton(
                                    text="REPO",
                                    url="https://github.com/SOME-1HING/ShikimoriBot"),
                        ]
                    ]
                ),
            )

    except BaseException:
        update.effective_message.reply_text(
            (
                (
                    (
                        "\n*Bot statistics*:\n"
                        + "\n".join(mod.__stats__() for mod in STATS)
                    )
                    + f"\n\n✦ [Support](https://t.me/{SUPPORT_CHAT}) | ✦ [Updates](https://t.me/{UPDATE_CHANNEL})\n\n"
                )
            ),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                  [                  
                       InlineKeyboardButton(
                                text="REPO",
                                url="https://github.com/SOME-1HING/ShikimoriBot"),
                     ] 
                ]
            ),
        )

STATS_HANDLER = CommandHandler(["stats", "statistics"], stats, block=False)
dispatcher.add_handler(STATS_HANDLER)

__handlers__ = [
    STATS_HANDLER
]
