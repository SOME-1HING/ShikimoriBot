
from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext
from telegraph import Telegraph
from Shikimori import pbot
from pyrogram import filters
from Shikimori.Extras.errors import capture_err
from Shikimori import SUPPORT_CHAT, dispatcher

from NHentai import NHentai, NHentaiAsync

nhentai = NHentai()

nhentai_async = NHentaiAsync()

@pbot.on_message(filters.command("sauce"))
@capture_err
async def sauce(_, message):
    popular = await nhentai_async.get_popular_now()
    return await message.reply_text(popular)

# def sauce(update: Update, context: CallbackContext):
#     try:
#         args = update.effective_message.text.split(None, 1)
#         user_id = update.effective_message.from_user.id
#         message = update.effective_message
#         Doujin = nhentai.get_random()
#     except:
#         update.effective_message.reply_text(
#             f"*ERROR!!! Contact @{SUPPORT_CHAT}*",
#             parse_mode=ParseMode.MARKDOWN,
#         )

__help__ = """
- /sauce `<digits list>` : Read a doujin from nhentai.net in telegram instant preview by giving it's code. 
You can give multiple codes, and it will fetch all those doujins. 
If you don't have an exception set for your chat, it'll send it to you in your private chat.
"""

__mod_name__ = "Nhentai"









# try:
#         args = update.effective_message.text.split(None, 1)
#         user_id = update.effective_message.from_user.id
#         message = update.effective_message
#         if len(args) >= 2:
#             for digits in context.args:
#                 try:
#                     code = int(digits)
#                 except ValueError:
#                     update.effective_message.reply_text(
#                         f"If you don't know that sauce codes must be only digits, you shouldn't be using this command. \n`{digits}` is not a sauce, just a sign of your ignorance.", parse_mode=ParseMode.MARKDOWN
#                     )
#                     continue
#                 doujin = Hentai(code)
#                 if not Hentai.exists(doujin.id):
#                     update.effective_message.reply_text(
#                         f"Doujin for `{code}` doesn't exist, Donald... Please don't use your nuclear launch codes here 😿", parse_mode=ParseMode.MARKDOWN
#                     )
#                     continue

                
#                 update.effective_message.reply_text(f"{doujin.artist}")

#         else:
#             message.reply_text(
#                     f"*No code input!* Use `/sauce <code>`", parse_mode=ParseMode.MARKDOWN
#                 )
#             return
#     except:
#         update.effective_message.reply_text(
#             f"*ERROR!!! Contact @{SUPPORT_CHAT}*",
#             parse_mode=ParseMode.MARKDOWN,
#         )