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

import aiohttp
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Shikimori import SUPPORT_CHAT, pbot
from Shikimori.Extras.errors import capture_err



@pbot.on_message(filters.command(['github', 'git']))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/github Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text(f"ERROR!! Contact @{SUPPORT_CHAT}")

            result = await request.json()
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
                await message.reply_photo(photo=avatar_url, caption=caption,reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Profile",
                                    url=url,
                                ),
                            ],
                        ],
                        disable_web_page_preview=True,
                    ), parse_mode= enums.ParseMode.MARKDOWN)
            except Exception as e:
                print(str(e))
                await message.reply_text(f"ERROR!! Contact @{SUPPORT_CHAT}")
                pass


__mod_name__ = "Github 🐱‍💻"
__help__ = """
Here is help for Github

 ❍ `/github` <username> - Get information from a profile on GitHub.
 ❍ `/git` <username> - Get information from a profile on GitHub.
"""