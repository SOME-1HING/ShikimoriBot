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

from pyrogram import filters
from pyrogram.types import Message

from Shikimori import pbot as app



__mod_name__ = "Games 🎮"
__help__ = """
Use these commands and try to score.\n\n
 ❍ `/dice` - Dice 🎲\n
 ❍ `/dart` - Dart 🎯\n
 ❍ `/basket` - Basket Ball 🏀\n
 ❍ `/bowling` - Bowling Ball 🎳\n
 ❍ `/football` - Football ⚽\n
 ❍ `/slot` - Spin slot machine 🎰
"""

@app.on_message(filters.command("dice"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎲")

@app.on_message(filters.command("dart"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎯")

@app.on_message(filters.command("basket"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🏀")

@app.on_message(filters.command("bowling"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎳")

@app.on_message(filters.command("football"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "⚽")

@app.on_message(filters.command("slot"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎰")
