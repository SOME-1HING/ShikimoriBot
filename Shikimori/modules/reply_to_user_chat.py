# This module is made by https://github.com/SOME-1HING/

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

# You are free to use this module. But don't delete this commented text. Thank you.

from Shikimori import dispatcher, MEDIA_BYE, MEDIA_GM, MEDIA_GN, MEDIA_HELLO
from telegram.constants import ParseMode
from telegram.ext import Filters, MessageHandler
import time

IMG_GM = MEDIA_GM.split(".")
gm_id = IMG_GM[-1]

IMG_GN = MEDIA_GM.split(".")
gn_id = IMG_GN[-1]

IMG_HELLO = MEDIA_GM.split(".")
hello_id = IMG_HELLO[-1]

IMG_BYE = MEDIA_BYE.split(".")
bye_id = IMG_BYE[-1]

def goodnight(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        if gn_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_GN, caption = f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gn_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_GN, caption = f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gn_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_GN, caption = f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Good Night:* {user1}"
            message.reply_text(reply)

    except:
        reply = f"*Good Night:* {user1}"
        message.reply_text(reply)

    time.sleep(5)


def goodmorning(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        if gm_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_GM, caption = f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_GM, caption = f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_GM, caption = f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Good Morning:* {user1}"
            message.reply_text(reply)
    except:
        reply = f"*Good Morning:* {user1}"
        message.reply_text(reply)
    
    time.sleep(5)

def hello(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        if gm_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_HELLO, caption = f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_HELLO, caption = f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_HELLO, caption = f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Hello* {user1}"
            message.reply_text(reply)
    except:
        reply = f"*Hello* {user1}"
        message.reply_text(reply)

    time.sleep(5)

def bye(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        if bye_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif bye_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif bye_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Bye!!* {user1}"
            message.reply_text(reply)
    except:
        reply = f"*Bye!!* {user1}"
        message.reply_text(reply)
    
    time.sleep(5)



GDMORNING_HANDLER = MessageHandler(
    Filters.regex("(?i)(good morning|goodmorning)"), goodmorning, friendly="goodmorning", run_async = True
)
GDNIGHT_HANDLER = MessageHandler(
    Filters.regex("(?i)(good night|goodnight)"), goodnight, friendly="goodnight", run_async = True
)
BYE_HANDLER = MessageHandler(
    Filters.regex("(?i)(bye|brb|afk)"), bye, friendly="bye", run_async = True
)
HELLO_HANDLER = MessageHandler(
    Filters.regex("(?i)(hello)"), hello, friendly="hello", run_async = True
)

dispatcher.add_handler(GDMORNING_HANDLER)
dispatcher.add_handler(GDNIGHT_HANDLER)
dispatcher.add_handler(HELLO_HANDLER)
dispatcher.add_handler(BYE_HANDLER)
