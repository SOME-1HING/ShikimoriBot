
from enum import Enum
import functools

from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup

from Shikimori import DEV_USERS, DRAGONS, dispatcher

class AdminPerms(Enum):
    CAN_RESTRICT_MEMBERS = 'can_restrict_members'
    CAN_PROMOTE_MEMBERS = 'can_promote_members'
    CAN_INVITE_USERS = 'can_invite_users'
    CAN_DELETE_MESSAGES = 'can_delete_messages'
    CAN_CHANGE_INFO = 'can_change_info'
    CAN_PIN_MESSAGES = 'can_pin_messages'


class ChatStatus(Enum):
    CREATOR = "creator"
    ADMIN = "administrator"


anon_callbacks = {}
anon_callback_messages = {}


def user_admin(permission: AdminPerms):
    def wrapper(func):
        @functools.wraps(func)
        def awrapper(update: Update, context: CallbackContext, *args, **kwargs):
            nonlocal permission
            if update.effective_chat.type == 'private':
                return func(update, context, *args, **kwargs)
            message = update.effective_message
            is_anon = bool(update.effective_message.sender_chat)

            if is_anon:
                callback_id = f'anoncb/{message.chat.id}/{message.message_id}/{permission.value}'
                anon_callbacks[(message.chat.id, message.message_id)] = ((update, context), func)
                anon_callback_messages[(message.chat.id, message.message_id)] = (
                    message.reply_text("Seems like you're anonymous, click the button below to prove your identity",
                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Prove identity',
                                                                                                callback_data=callback_id)]]))).message_id
                # send message with callback f'anoncb{callback_id}'
            else:
                user_id = message.from_user.id
                chat_id = message.chat.id
                mem = context.bot.get_chat_member(chat_id=chat_id, user_id=user_id)
                if getattr(mem, permission.value) is True or mem.status == "creator" or user_id in DRAGONS:
                    return func(update, context, *args, **kwargs)
                else:
                    return message.reply_text(f"You lack the permission: `{permission.name}`",
                                              parse_mode=ParseMode.MARKDOWN)

        return awrapper

    return wrapper

