"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

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

import requests
from Shikimori.events import register
from Shikimori import telethn
from Shikimori.vars import SUPPORT_CHAT
from bs4 import BeautifulSoup

@register(pattern='/watchorder')
async def watchorder(event):
	animename = event.message.message.replace(event.text.split(' ')[0], '')
	if len(animename) <= 1:
		await event.reply('/watchorder anime name')
		return
	try:
		res = requests.get(f'https://chiaki.site/?/tools/autocomplete_series&term={animename}').json()
		data = None
		id_ = res[0]['id']
		res_ = requests.get(f'https://chiaki.site/?/tools/watch_order/id/{id_}').text
		soup = BeautifulSoup(res_ , 'html.parser')
		anime_names = soup.find_all('span' , class_='wo_title')
		for x in anime_names:
			data = f"{data}\n{x.text}" if data else x.text
		await telethn.send_message(event.chat_id, f'Watchorder of <b>{animename}:</b> \n\n<tt>{data}</tt>',parse_mode='html', reply_to=event.id)
	except Exception as e:
		await event.reply(f'*Error*: Contact @{SUPPORT_CHAT}.\nERROR: {e}')
		return

