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

import requests
import random
import Shikimori.strings.animal_facts_string as animal_facts
from Shikimori import dispatcher
from telegram import Update
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext


def animalfact(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(animal_facts.ANIMAL_FACTS))

def cats(update, context):
    msg = update.effective_message
    try:
        url = f'https://aws.random.cat/meow'
        result = requests.get(url).json()
        img = result['file']
        msg.reply_photo(photo=img)
    except:        
        url = f'https://aws.random.cat/meow'
        result = requests.get(url).json()
        img = result['file']
        msg.reply_photo(photo=img)

ANIMALFACT_HANDLER = DisableAbleCommandHandler("animalfacts", animalfact, run_async=True)
dispatcher.add_handler(ANIMALFACT_HANDLER)
CAT_HANDLER = DisableAbleCommandHandler(("cats", "cat"), cats, run_async=True)
dispatcher.add_handler(CAT_HANDLER)

__mod_name__ = "Animals"
__help__ = """
   ➢ `/animalfacts` - To Get random animal facts.
   ➢ `/cats` - To Get Random Photo of Cats.
   ➢ `/goose`*:* Sends Random Goose pic.
   ➢ `/woof`*:* Sends Random Woof pic.
   ➢ `/lizard`*:* Sends Random Lizard GIFs.
"""