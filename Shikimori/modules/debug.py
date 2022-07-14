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

import time

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler
from telegram.error import BadRequest

from Shikimori import telethn, dispatcher
from Shikimori.modules.helper_funcs.chat_status import dev_plus

@dev_plus
def logs(update: Update, context: CallbackContext):
    chat = update.effective_chat
    user = update.effective_user
    with open("shikimori_logs.txt", "rb") as f:
        context.bot.send_document(document=f, filename=f.name, chat_id=user.id)
    if chat.type != chat.PRIVATE:
        msg = update.effective_message
        hmm = msg.reply_text("`Logs sent. Check your pm.`", parse_mode=ParseMode.MARKDOWN)
        time.sleep(10)
        try:
            msg.delete()
            hmm.delete()
        except BadRequest:
            pass

LOG_HANDLER = CommandHandler(("logs", "log"), logs, run_async=True)
dispatcher.add_handler(LOG_HANDLER)

__mod_name__ = "Debug"
__command_list__ = ["debug"]
