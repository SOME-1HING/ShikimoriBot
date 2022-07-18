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

import random
import Shikimori.strings.truth_and_dare_string as truth_and_dare_string
from Shikimori import dispatcher
from telegram import Update
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext

def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))

def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))

def wyr(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(truth_and_dare_string.WYR))


def tord(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TORD))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)
TORD_HANDLER = DisableAbleCommandHandler("tord", tord, run_async=True)
WYR_HANDLER = DisableAbleCommandHandler(("rather", "wyr"), wyr, run_async=True)


dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(TORD_HANDLER)
dispatcher.add_handler(WYR_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__mod_name__ = "Truth or Dare"
__help__ = """
*Truth or Dare*
 ❍ `/truth` : Asks a question
 ❍ `/dare` : Tells a task to do
 ❍ `/tord` : Can either be a truth or dare
 ❍ `/rather` or `/wyr`: Would you rather?
"""
