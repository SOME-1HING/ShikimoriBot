# Module rewritten by https://github.com/SOME-1HING from the original module by rozari0

import requests
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

def cats(update, context):
    try:
        msg = update.effective_message
        url = f'https://thatcopy.pw/catapi/rest/'
        result = requests.get(url).json()
        if len(msg.command)<2:
            img = result['url']
            msg.reply_photo(img)
        else:
            img = result['webpurl']
            msg.reply_photo(img)
    except:        
            msg.reply_text("ERROR")

ANIMALFACT_HANDLER = DisableAbleCommandHandler("animalfacts", animalfact, run_async=True)
dispatcher.add_handler(ANIMALFACT_HANDLER)
DOGFACT_HANDLER = DisableAbleCommandHandler("dogfacts", dogfacts, run_async=True)
dispatcher.add_handler(DOGFACT_HANDLER)
RANDOMCAT_HANDLER = DisableAbleCommandHandler("randomcat", randomcat, run_async=True)
dispatcher.add_handler(RANDOMCAT_HANDLER)
CAT_HANDLER = DisableAbleCommandHandler("cats", cats, run_async=True)
dispatcher.add_handler(CAT_HANDLER)


__mod_name__ = "Animal facts"
__help__ = """
   ➢ `/animalfacts` - To Get random animal facts.

credits: rozari0   

   ➢ `/dogfacts` - To Get Facts About Dog.  
   ➢ `/randomcat` - To Get Random Photo of Cat.
   ➢ `/cats` - To Get Photo of Cat. Use **/cats -s** to get photo as sticker.

"""