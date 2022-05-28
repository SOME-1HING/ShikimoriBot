from typing import Optional

from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.error import BadRequest
from telegram.ext import Filters, MessageHandler, run_async

from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler

from Shikimori.modules.helper_funcs.alternate import send_message


def send(update, context):
	args = update.effective_message.text.split(None, 1)
	creply = args[1]
	send_message(update.effective_message, creply)
	
	
		

__help__ = """The Send Module Allows you to send a custom message to users in a chat
/snd :Send the given message
Note - /snd Hi will send the message hi to the chat"""

__mod_name__ = "Send"


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send, run_async = True)
dispatcher.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["snd"]
__handlers__ = [
    ADD_CCHAT_HANDLER
]
