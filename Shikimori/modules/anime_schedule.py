"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    Ryu120 [https://github.com/Ryu120] 

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

from pyrogram import filters
import requests
from Shikimori import pbot

@pbot.on_message(filters.command('latest'))
def schedule(_, message):
    results = requests.get('https://subsplease.org/api/?f=schedule&h=true&tz=Japan').json()
    text = None
    for result in results['schedule']:
        title = result['title']
        time = result['time']
        aired = bool(result['aired'])
        title = f"**[{title}](https://subsplease.org/shows/{result['page']})**" if not aired else f"**~~[{title}](https://subsplease.org/shows/{result['page']})~~**"
        data = f"{title} - **{time}**"
        
        if text:
            text = f"{text}\n{data}"
        else:
            text = data

    message.reply_text(f"**Today's Schedule:**\nTime-Zone: Tokyo (GMT +9)\n\n{text}")


__mod_name__ = "Schedule"

__help__ = """
 ❍ `/latest`: to see latest anime episode
"""
