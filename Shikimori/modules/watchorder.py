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
		await telethn.send_text(event.chat_id, text = f'Watchorder of {animename}: \n```{data}```',parse_mode='html', reply_to=event.id)
	except Exception as e:
		await event.reply(f'*Error*: Contact @{SUPPORT_CHAT}.\nERROR: {e}')
		return

