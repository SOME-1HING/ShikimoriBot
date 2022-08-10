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
from Shikimori import SUPPORT_CHAT
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

def github(update: Update, context: CallbackContext):
    if len(message.command) != 2:
        update.effective_message.reply_text("/github Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
        result = request.json()
        try:
            m = message.reply_text("`Searching.....`")
            url = result['html_url']
            name = result['name']
            company = result['company']
            bio = result['bio']
            created_at = result['created_at']
            avatar_url = result['avatar_url']
            blog = result['blog']
            location = result['location']
            repositories = result['public_repos']
            followers = result['followers']
            following = result['following']
            caption = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`"""
            update.effective_message.reply_photo(avatar_url, caption=caption,reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Profile",
                                url=url,
                            ),
                        ],
                    ],
                ), parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            print(str(e))
            update.effective_message.reply_text(f"ERROR!! Contact @{SUPPORT_CHAT}")
            pass

git_handler = CommandHandler(("git", "github"), uchiha, run_async = True)
dispatcher.add_handler(git_handler)

__mod_name__ = "Github 🐱‍💻"
__help__ = """
Here is help for Github

 ❍ `/github` <username> - Get information from a profile on GitHub.
 ❍ `/git` <username> - Get information from a profile on GitHub.
"""
