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

import requests
from Shikimori.events import register
from Shikimori import telethn, SUPPORT_CHAT
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

