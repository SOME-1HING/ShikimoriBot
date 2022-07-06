import datetime
import platform
import time
from psutil import cpu_percent, virtual_memory, disk_usage, boot_time
from platform import python_version

from telegram import ParseMode, __version__ as ptbver, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler
from telegram.utils.helpers import escape_markdown
    
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
    status += "*➢ python-Telegram-Bot:* " + str(ptbver) + "\n"
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

STATS_HANDLER = CommandHandler(["stats", "statistics"], stats, run_async=True)
dispatcher.add_handler(STATS_HANDLER)

__handlers__ = [
    STATS_HANDLER
]