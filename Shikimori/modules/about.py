import time
from Shikimori.modules.helper_funcs.readable_time import get_readable_time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.utils.helpers import escape_markdown
from telegram.ext import CallbackContext, CallbackQueryHandler
from Shikimori.modules.start import PM_START_TEXT, buttons
from Shikimori import StartTime, dispatcher

bot_name = f"{dispatcher.bot.first_name}"

def Shikimori_about_callback(update, context):
    query = update.callback_query
    if query.data == "Shikimori_":
        query.message.edit_text(
            text=f"๏ I'm *{bot_name}*, a powerful group management bot built to help you manage your group easily."
            "\n• I can restrict users."
            "\n• I can greet users with customizable welcome messages and even set a group's rules."
            "\n• I have an advanced anti-flood system."
            "\n• I can warn users until they reach max warns, with each predefined actions such as ban, mute, kick, etc."
            "\n• I have a note keeping system, blacklists, and even predetermined replies on certain keywords."
            "\n• I check for admins' permissions before executing any command and more stuffs",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="Github", callback_data="github_"),
                    InlineKeyboardButton(text="License", callback_data="license_"),
                    ],
                    [
                    InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】✧Network✧", callback_data="void_"),
                    InlineKeyboardButton(text="Documentation", url="https://some1hing.gitbook.io/shikimori-bot/"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_back"),
                    ],
                ]
            ),
        )

    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "Hello *{}*! Nice to meet you!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT
     
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

def git_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "github_":
        query.message.edit_text(
            text=f"Orginal Repositiory created by [SOME1HING](https://github.com/SOME-1HING) on [github](https://github.com/SOME-1HING/ShikimoriBot) for [Shikimori Bot](https://t.me/micchon_shikimori_bot)",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="Repo", url="https://github.com/SOME-1HING/ShikimoriBot"),
                    InlineKeyboardButton(text="Creator", url="https://github.com/SOME-1HING"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_"),
                    ],
                ]
            ),
        )
    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "Hello *{}*! Nice to meet you!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT
    
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

def void_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "void_":
        query.message.edit_text(
            text=f"๏ The Shikimori Repo is originally under Void Network. The bot made by this repo may or may not be under Void Network.\n\nWelcome to **[【V๏ɪ፝֟𝔡】 ✧Network✧](https://t.me/voidxnetwork)** \n\n◈ Void is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=False,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(text="【Usertag】", url="https://t.me/void_network/103"),
                InlineKeyboardButton(text="【Owner Sama】", url="https://t.me/voidxtoxic")
                ],
                [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】Network", url="https://t.me/voidxnetwork")],
                [InlineKeyboardButton(text="Back", callback_data="Shikimori_")]
            ]
            ),
        )
    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "Hello *{}*! Nice to meet you!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT
    
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

def license_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "license_":
        query.message.edit_text(
            text=f"\n\n_{bot_name}'s licensed under the GNU General Public License v3.0_",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="License", url="https://github.com/SOME-1HING/ShikimoriBot/blob/master/LICENSE"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_"),
                    ],
                ]
            ),
        )
    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "Hello *{}*! Nice to meet you!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT
    
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )
about_callback_handler = CallbackQueryHandler(
        Shikimori_about_callback, pattern=r"Shikimori_", run_async=True
    )
license_call_back_handler = CallbackQueryHandler(
    license_call_back, pattern=r"license_", run_async=True
)
git_call_back_handler = CallbackQueryHandler(
    git_call_back, pattern=r"github_", run_async=True
)
void_call_back_handler = CallbackQueryHandler(
    void_call_back, pattern=r"void_", run_async=True
)

dispatcher.add_handler(void_call_back_handler)
dispatcher.add_handler(git_call_back_handler)
dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(license_call_back_handler)