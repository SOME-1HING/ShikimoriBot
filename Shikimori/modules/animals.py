"""
MIT License

Copyright (c) 2021 rozari0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# Module rewritten by https://github.com/SOME-1HING


import random
from Shikimori import pbot
from pyrogram import filters
from Shikimori.core.decorators.errors import capture_err
from Shikimori.utils.http import get
import Shikimori.modules.animal_facts_string as animal_facts
from Shikimori import dispatcher
from telegram import ParseMode, Update, Bot
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def animalfact(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(animal_facts.ANIMAL_FACTS))


@pbot.on_message(filters.command("dogfacts"))
@capture_err
async def dogfacts(client, message):
    message = await message.reply_text("`Getting dog facts...`")
    fact = await get("https://dog-facts-api.herokupbot.com/api/v1/resources/dogs?number=1")
    return await message.reply_text(fact[0]["fact"])

@pbot.on_message(filters.command("randomcat"))
@capture_err
async def randomcat(_, message):
    cat = await get("https://aws.random.cat/meow")
    await message.reply_photo(cat["file"])

@pbot.on_message(filters.command("cats"))
@capture_err
async def cats(_, message):
    cat = await get("https://thatcopy.pw/catapi/rest/")
    if len(message.command)<2:
        return await message.reply_photo(cat["url"])
    else:
        return await message.reply_sticker(cat["webpurl"])

ANIMALFACT_HANDLER = DisableAbleCommandHandler("animalfacts", animalfact, run_async=True)
dispatcher.add_handler(ANIMALFACT_HANDLER)

__mod_name__ = "Animal facts"
__help__ = """
   ➢ `/animalfacts` - To Get random animal facts.

credits: rozari0   

   ➢ `/dogfacts` - To Get Facts About Dog.  
   ➢ `/randomcat` - To Get Random Photo of Cat.
   ➢ `/cats` - To Get Photo of Cat. Use **/cats -s** to get photo as sticker.

"""