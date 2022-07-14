"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

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

import os

from gtts import gTTS
from gtts import gTTSError
from telethon import *
from telethon.tl.types import *

from Shikimori import *

from Shikimori import telethn as tbot
from Shikimori.events import register


@register(pattern="^/tts (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply(
            "Invalid Syntax\nFormat `/tts lang | text`\nFor eg: `/tts en | hello`"
        )
        return
    text = text.strip()
    lan = lan.strip()
    try:
        tts = gTTS(text, tld="com", lang=lan)
        tts.save("k.mp3")
    except AssertionError:
        await event.reply(
            "The text is empty.\n"
            "Nothing left to speak after pre-precessing, "
            "tokenizing and cleaning."
        )
        return
    except ValueError:
        await event.reply("Language is not supported.")
        return
    except RuntimeError:
        await event.reply("Error loading the languages dictionary.")
        return
    except gTTSError:
        await event.reply("Error in Google Text-to-Speech API request!")
        return
    with open("k.mp3", "r"):
        await tbot.send_file(
            event.chat_id, "k.mp3", voice_note=True, reply_to=reply_to_id
        )
        os.remove("k.mp3")
