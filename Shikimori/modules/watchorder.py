import requests

from Shikimori import pbot as pgram
from pyrogram import filters
from bs4 import BeautifulSoup

@pgram.on_message(filters.command("watchorder", f"watchorder@micchon_shikimori_bot"))
def watchorderx(_,message):

	anime = message.text.replace(message.text.split(' ')[0], '')

	res = requests.get(f'https://chiaki.site/?/tools/autocomplete_series&term={anime}').json()

	data = None

	id_ = res[0]['id']

	res_ = requests.get(f'https://chiaki.site/?/tools/watch_order/id/{id_}').text

	soup = BeautifulSoup(res_ , 'html.parser')

	anime_names = soup.find_all('span' , class_='wo_title')

	for x in anime_names:

		data = f"{data}\n{x.text}" if data else x.text
	message.reply_text(f'Watchorder of {anime}: \n```{data}```')

__mod_name__ = "VC Player 🎧"
__help__ = """
*VC Player*
 • `/pause` - To pause the playback.
 • `/resume` - To resuming the playback You've paused.
 • `/skip` - To skipping the player.
 • `/end` - For end the playback.
 • `/play` <query /reply audio> - Playing music via YouTube.
 • `/playlist` - To playing a playlist of groups or your personal playlist
"""

