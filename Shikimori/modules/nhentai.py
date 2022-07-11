from turtle import up
from hentai import Hentai, Format, Tag
from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext
from telegraph import Telegraph

from Shikimori import SUPPORT_CHAT, dispatcher

# def _generate_anchor_tags(tags: list[Tag]) -> str:
#     """
#     Generate comma separated anchor tags for a given list of Tag objects
#     :param tags: List of Tag objects
#     :return: comma separated anchor tags
#     """
#     return ", ".join(f'<a href="{tag.url}">{tag.name}</a>' for tag in tags)



# def sauce(update: Update, context: CallbackContext) -> None:
#     """
#     Fetch the doujin for all the sauces given by user, make telegraph article and send it to user for easy reading
#     :param update: object representing the incoming update.
#     :param context: object containing data about the command call.
#     """
#     # check if any args were given
#     if not context.args:
#         update.effective_message.reply_text("Please give some codes to fetch, this cat can't read your mind...")
#         return

#     # check if exception for sauce is added in current chat
#     exception = update.effective_chat.type

#     # iterate over each given sauce and fetch the doujin
#     for digits in context.args:
#         try:
#             code = int(digits)
#         except ValueError:
#             update.effective_message.reply_markdown(
#                 f"If you don't know that sauce codes must be only digits, you shouldn't be using this command. "
#                 f"`{digits}` is not a sauce, just a sign of your ignorance."
#             )
#             continue

#         # check if doujin exists
#         if not Hentai.exists(code):
#             update.effective_message.reply_markdown(
#                 f"Doujin for `{code}` doesn't exist, Donald... Please don't use your nuclear launch codes here 😿"
#             )
#             continue

#         # Fetch doujin data
#         doujin = Hentai(code)

#         # get image tags
#         image_tags = "\n".join(f'<img src="{image_url}">' for image_url in doujin.image_urls)

#         # create telegraph article for the doujin
#         telegraph = Telegraph()
#         telegraph.create_account(short_name="neko-chan-telebot")
#         article_path = telegraph.create_page(doujin.title(Format.Pretty), html_content=image_tags)["path"]

#         # make dict with data to be displayed for the doujin
#         data = {
#             "Code": f'<a href="https://telegra.ph/{article_path}">{code}</a>',
#             "Title": f'<a href="{doujin.url}">{doujin.title(Format.Pretty)}</a>',
#             "Tags": _generate_anchor_tags(doujin.tag),
#             "Characters": _generate_anchor_tags(doujin.character),
#             "Parodies": _generate_anchor_tags(doujin.parody),
#             "Artists": _generate_anchor_tags(doujin.artist),
#             "Groups": _generate_anchor_tags(doujin.group),
#             "Languages": _generate_anchor_tags(doujin.language),
#             "Categories": _generate_anchor_tags(doujin.category),
#         }

#         # add details to the reply to be sent to the user
#         text_blob = "\n\n".join(f"{key}\n{value}" for key, value in data.items())

#         # button with nhentai link
#         markup = InlineKeyboardMarkup.from_button(InlineKeyboardButton(text="Link to nHentai", url=doujin.url))

#         # send message
#         update.message.reply_text(
#             text_blob,
#             reply_markup=markup,
#             parse_mode=ParseMode.HTML
#         )


def sause(update: Update, context: CallbackContext):
    try:
        args = update.effective_message.text.split(None, 1)
        user_id = update.effective_message.from_user.id
        message = update.effective_message
        if len(args) >= 2:
            for digits in context.args:
                try:
                    code = int(digits)
                except ValueError:
                    update.effective_message.reply_text(
                        f"If you don't know that sauce codes must be only digits, you shouldn't be using this command. \n`{digits}` is not a sauce, just a sign of your ignorance.", parse_mode=ParseMode.MARKDOWN
                    )
                    continue
                if not Hentai.exists(code):
                    update.effective_message.reply_text(
                        f"Doujin for `{code}` doesn't exist, Donald... Please don't use your nuclear launch codes here 😿", parse_mode=ParseMode.MARKDOWN
                    )
                    continue

                doujin = Hentai(code)
                update.effective_message.reply_text(doujin.title(Format.Pretty))

        else:
            message.reply_text(
                    f"*No code input!* Use `/sause <code>`", parse_mode=ParseMode.MARKDOWN
                )
            return
    except:
        update.effective_message.reply_text(
            f"*ERROR!!! Contact @{SUPPORT_CHAT}*",
            parse_mode=ParseMode.MARKDOWN,
        )

__help__ = """
- /sauce `<digits list>` : Read a doujin from nhentai.net in telegram instant preview by giving it's code. 
You can give multiple codes, and it will fetch all those doujins. 
If you don't have an exception set for your chat, it'll send it to you in your private chat.
"""

__mod_name__ = "Nhentai"

# create handlers
dispatcher.add_handler(CommandHandler("sauce", sauce, run_async=True))