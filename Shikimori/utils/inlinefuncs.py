# import asyncio
# import os
# import sys
# from html import escape
# from re import sub as re_sub
# from sys import version as pyver
# from time import ctime, time
# import socket
# import ffmpeg
# import youtube_dl
# from urllib.parse import urlparse
# from time import time
# from fuzzysearch import find_near_matches
# from motor import version as mongover
# from pykeyboard import InlineKeyboard
# from pyrogram import __version__ as pyrover
# from pyrogram import filters
# from pyrogram.raw.functions import Ping
# from pyrogram.types import (CallbackQuery, 
#                             InlineKeyboardButton,
#                             InlineQueryResultArticle,
#                             InlineQueryResultPhoto,
#                             InputTextMessageContent)
# from search_engine_parser import GoogleSearch

# from Shikimori import (
#     ALIVE_MEDIA,
#     DEV_USERS,
#     LOG_CHANNEL, 
#     BOT_USERNAME,
#     STATS_IMG,
#     SUPPORT_CHAT,
# )
# from Shikimori.__main__ import bot_name
# from Shikimori import pbot as app 
# from Shikimori import arq
# from Shikimori.core.keyboard import ikb
# from Shikimori.utils.pluginhelper import convert_seconds_to_minutes as time_convert, fetch
# from Shikimori.core.tasks import _get_tasks_text, all_tasks, rm_task
# from Shikimori.core.types import InlineQueryResultCachedDocument
# from Shikimori.modules.info import get_chat_info, get_user_info
# from Shikimori.modules.song import download_youtube_audio
# from Shikimori.utils.functions import test_speedtest
# from Shikimori.utils.pastebin import paste

# MESSAGE_DUMP_CHAT = LOG_CHANNEL

# keywords_list = [
#     "alive",
#     "image",
#     "wall",
#     "tmdb",
#     "lyrics",
#     "exec",
#     "speedtest",
#     "search",
#     "ping",
#     "webss",
#     "fakegen",
#     "gsearch",
#     "paste",
#     "tr",
#     "ud",
#     "yt",
#     "info",
#     "google",
#     "gh",
#     "torrent",
#     "pokedex",
#     "saavn",
#     "wiki",
#     "music",
#     "ytmusic",
# ]

# is_downloading = False


# def get_file_extension_from_url(url):
#     url_path = urlparse(url).path
#     basename = os.path.basename(url_path)
#     return basename.split(".")[-1]


# def download_youtube_audio(url: str):
#     global is_downloading
#     with youtube_dl.YoutubeDL(
#         {
#             "format": "bestaudio",
#             "writethumbnail": True,
#             "quiet": True,
#         }
#     ) as ydl:
#         info_dict = ydl.extract_info(url, download=False)
#         if int(float(info_dict["duration"])) > 600:
#             is_downloading = False
#             return []
#         ydl.process_info(info_dict)
#         audio_file = ydl.prepare_filename(info_dict)
#         basename = audio_file.rsplit(".", 1)[-2]
#         if info_dict["ext"] == "webm":
#             audio_file_opus = basename + ".opus"
#             ffmpeg.input(audio_file).output(
#                 audio_file_opus, codec="copy", loglevel="error"
#             ).overwrite_output().run()
#             os.remove(audio_file)
#             audio_file = audio_file_opus
#         thumbnail_url = info_dict["thumbnail"]
#         thumbnail_file = (
#             basename
#             + "."
#             + get_file_extension_from_url(thumbnail_url)
#         )
#         title = info_dict["title"]
#         performer = info_dict["uploader"]
#         duration = int(float(info_dict["duration"]))
#     return [title, performer, duration, audio_file, thumbnail_file]



# async def _netcat(host, port, content):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((host, int(port)))
#     s.sendall(content.encode())
#     s.shutdown(socket.SHUT_WR)
#     while True:
#         data = s.recv(4096).decode("utf-8").strip("\n\x00")
#         if not data:
#             break
#         return data
#     s.close()


# async def paste(content):
#     link = await _netcat("ezup.dev", 9999, content)
#     return link

# async def inline_help_func(__HELP__):
#     buttons = InlineKeyboard(row_width=4)
#     buttons.add(
#         *[
#             (InlineKeyboardButton(text=i, switch_inline_query_current_chat=i))
#             for i in keywords_list
#         ]
#     )
#     answerss = [
#         InlineQueryResultArticle(
#             title="Inline Commands",
#             description="Help Related To Inline Usage.",
#             input_message_content=InputTextMessageContent(
#                 "**__Click A Button To Get Started.__**"
#             ),
#             thumb_url=f"{STATS_IMG}",
#             reply_markup=buttons,
#         ),
#     ]
#     answerss = await alive_function(answerss)
#     return answerss


# async def alive_function(answers):
#     buttons = InlineKeyboard(row_width=2)
#     bot_state = "Dead" if not await app.get_me() else "Alive"
#     buttons.add(
#         InlineKeyboardButton("Main bot", url=f"https://t.me/{BOT_USERNAME}"),
#         InlineKeyboardButton(
#             "Go Inline!", switch_inline_query_current_chat=""
#         ),
#     )

#     msg = f"""
# **[{bot_name} Bot ❤️](https://t.me/{SUPPORT_CHAT}):**
# **MainBot:** `{bot_state}`
# **Python:** `{pyver.split()[0]}`
# **Pyrogram:** `{pyrover}`
# **MongoDB:** `{mongover}`
# **Platform:** `{sys.platform}`
# **Profiles:** [BOT](t.me/{BOT_USERNAME})
# """
#     answers.append(
#         InlineQueryResultArticle(
#             title="Alive",
#             description="Check Bot's Stats",
#             thumb_url=f"{STATS_IMG}",
#             input_message_content=InputTextMessageContent(
#                 msg, disable_web_page_preview=True
#             ),
#             reply_markup=buttons,
#         )
#     )
#     return answers


# async def translate_func(answers, lang, tex):
#     result = await arq.translate(tex, lang)
#     if not result.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=result.result,
#                 input_message_content=InputTextMessageContent(result.result),
#             )
#         )
#         return answers
#     result = result.result
#     msg = f"""
# __**Translated from {result.src} to {result.dest}**__
# **INPUT:**
# {tex}
# **OUTPUT:**
# {result.translatedText}"""
#     answers.extend(
#         [
#             InlineQueryResultArticle(
#                 title=f"Translated from {result.src} to {result.dest}.",
#                 description=result.translatedText,
#                 input_message_content=InputTextMessageContent(msg),
#             ),
#             InlineQueryResultArticle(
#                 title=result.translatedText,
#                 input_message_content=InputTextMessageContent(
#                     result.translatedText
#                 ),
#             ),
#         ]
#     )
#     return answers


# async def urban_func(answers, text):
#     results = await arq.urbandict(text)
#     if not results.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=results.result,
#                 input_message_content=InputTextMessageContent(results.result),
#             )
#         )
#         return answers
#     results = results.result[0:48]
#     for i in results:
#         clean = lambda x: re_sub(r"[\[\]]", "", x)
#         msg = f"""
# **Query:** {text}
# **Definition:** __{clean(i.definition)}__
# **Example:** __{clean(i.example)}__"""

#         answers.append(
#             InlineQueryResultArticle(
#                 title=i.word,
#                 description=clean(i.definition),
#                 input_message_content=InputTextMessageContent(msg),
#             )
#         )
#     return answers


# async def google_search_func(answers, text):
#     gresults = await GoogleSearch().async_search(text)
#     limit = 0
#     for i in gresults:
#         if limit > 48:
#             break
#         limit += 1

#         try:
#             msg = f"""
# [{i['titles']}]({i['links']})
# {i['descriptions']}"""

#             answers.append(
#                 InlineQueryResultArticle(
#                     title=i["titles"],
#                     description=i["descriptions"],
#                     input_message_content=InputTextMessageContent(
#                         msg, disable_web_page_preview=True
#                     ),
#                 )
#             )
#         except KeyError:
#             pass
#     return answers


# async def wall_func(answers, text):
#     results = await arq.wall(text)
#     if not results.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=results.result,
#                 input_message_content=InputTextMessageContent(results.result),
#             )
#         )
#         return answers
#     results = results.result[0:48]
#     for i in results:
#         answers.append(
#             InlineQueryResultPhoto(
#                 photo_url=i.url_image,
#                 thumb_url=i.url_thumb,
#                 caption=f"[Source]({i.url_image})",
#             )
#         )
#     return answers


# async def torrent_func(answers, text):
#     results = await arq.torrent(text)
#     if not results.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=results.result,
#                 input_message_content=InputTextMessageContent(results.result),
#             )
#         )
#         return answers
#     results = results.result[0:48]
#     for i in results:
#         title = i.name
#         size = i.size
#         seeds = i.seeds
#         leechs = i.leechs
#         upload_date = i.uploaded
#         magnet = i.magnet
#         caption = f"""
# **Title:** __{title}__
# **Size:** __{size}__
# **Seeds:** __{seeds}__
# **Leechs:** __{leechs}__
# **Uploaded:** __{upload_date}__
# **Magnet:** `{magnet}`"""

#         description = f"{size} | {upload_date} | Seeds: {seeds}"
#         answers.append(
#             InlineQueryResultArticle(
#                 title=title,
#                 description=description,
#                 input_message_content=InputTextMessageContent(
#                     caption, disable_web_page_preview=True
#                 ),
#             )
#         )
#         pass
#     return answers


# async def youtube_func(answers, text):
#     results = await arq.youtube(text)
#     if not results.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=results.result,
#                 input_message_content=InputTextMessageContent(results.result),
#             )
#         )
#         return answers
#     results = results.result[0:48]
#     for i in results:
#         buttons = InlineKeyboard(row_width=1)
#         video_url = f"https://youtube.com{i.url_suffix}"
#         buttons.add(InlineKeyboardButton("Watch", url=video_url))
#         caption = f"""
# **Title:** {i.title}
# **Views:** {i.views}
# **Channel:** {i.channel}
# **Duration:** {i.duration}
# **Uploaded:** {i.publish_time}
# **Description:** {i.long_desc}"""
#         description = (
#             f"{i.views} | {i.channel} | {i.duration} | {i.publish_time}"
#         )
#         answers.append(
#             InlineQueryResultArticle(
#                 title=i.title,
#                 thumb_url=i.thumbnails[0],
#                 description=description,
#                 input_message_content=InputTextMessageContent(
#                     caption, disable_web_page_preview=True
#                 ),
#                 reply_markup=buttons,
#             )
#         )
#     return answers


# async def lyrics_func(answers, text):
#     song = await arq.lyrics(text)
#     if not song.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=song.result,
#                 input_message_content=InputTextMessageContent(song.result),
#             )
#         )
#         return answers
#     lyrics = song.result
#     song = lyrics.splitlines()
#     song_name = song[0]
#     artist = song[1]
#     if len(lyrics) > 4095:
#         lyrics = await paste(lyrics)
#         lyrics = f"**LYRICS_TOO_LONG:** [URL]({lyrics})"

#     msg = f"**__{lyrics}__**"

#     answers.append(
#         InlineQueryResultArticle(
#             title=song_name,
#             description=artist,
#             input_message_content=InputTextMessageContent(msg),
#         )
#     )
#     return answers

# async def paste_func(answers, text):
#     start_time = time()
#     url = await paste(text)
#     msg = f"__**{url}**__"
#     end_time = time()
#     answers.append(
#         InlineQueryResultArticle(
#             title=f"Pasted In {round(end_time - start_time)} Seconds.",
#             description=url,
#             input_message_content=InputTextMessageContent(msg),
#         )
#     )
#     return answers



# async def saavn_func(answers, text):
#     buttons_list = []
#     results = await arq.saavn(text)
#     if not results.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=results.result,
#                 input_message_content=InputTextMessageContent(results.result),
#             )
#         )
#         return answers
#     results = results.result
#     for count, i in enumerate(results):
#         buttons = InlineKeyboard(row_width=1)
#         buttons.add(InlineKeyboardButton("Download | Play", url=i.media_url))
#         buttons_list.append(buttons)
#         duration = await time_convert(i.duration)
#         caption = f"""
# **Title:** {i.song}
# **Album:** {i.album}
# **Duration:** {duration}
# **Release:** {i.year}
# **Singers:** {i.singers}"""
#         description = f"{i.album} | {duration} " + f"| {i.singers} ({i.year})"
#         answers.append(
#             InlineQueryResultArticle(
#                 title=i.song,
#                 input_message_content=InputTextMessageContent(
#                     caption, disable_web_page_preview=True
#                 ),
#                 description=description,
#                 thumb_url=i.image,
#                 reply_markup=buttons_list[count],
#             )
#         )
#     return answers


# async def wiki_func(answers, text):
#     data = await arq.wiki(text)
#     if not data.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=data.result,
#                 input_message_content=InputTextMessageContent(data.result),
#             )
#         )
#         return answers
#     data = data.result
#     msg = f"""
# **QUERY:**
# {data.title}
# **ANSWER:**
# __{data.answer}__"""
#     answers.append(
#         InlineQueryResultArticle(
#             title=data.title,
#             description=data.answer,
#             input_message_content=InputTextMessageContent(msg),
#         )
#     )
#     return answers


# async def speedtest_init(query):
#     answers = []
#     user_id = query.from_user.id
#     if user_id not in DEV_USERS:
#         msg = "**ERROR**\n__THIS FEATURE IS ONLY FOR DEV USERS__"
#         answers.append(
#             InlineQueryResultArticle(
#                 title="ERROR",
#                 description="THIS FEATURE IS ONLY FOR SUDO USERS",
#                 input_message_content=InputTextMessageContent(msg),
#             )
#         )
#         return answers
#     msg = "**Click The Button Below To Perform A Speedtest**"
#     button = InlineKeyboard(row_width=1)
#     button.add(
#         InlineKeyboardButton(text="Test", callback_data="test_speedtest")
#     )
#     answers.append(
#         InlineQueryResultArticle(
#             title="Click Here",
#             input_message_content=InputTextMessageContent(msg),
#             reply_markup=button,
#         )
#     )
#     return answers


# # CallbackQuery for the function above


# @app.on_callback_query(filters.regex("test_speedtest"))
# async def test_speedtest_cq(_, cq):
#     if cq.from_user.id not in DEV_USERS:
#         return await cq.answer("This Isn't For You!")
#     inline_message_id = cq.inline_message_id
#     await app.edit_inline_text(inline_message_id, "**Testing**")
#     loop = asyncio.get_running_loop()
#     download, upload, info = await loop.run_in_executor(None, test_speedtest)
#     msg = f"""
# **Download:** `{download}`
# **Upload:** `{upload}`
# **Latency:** `{info['latency']} ms`
# **Country:** `{info['country']} [{info['cc']}]`
# **Latitude:** `{info['lat']}`
# **Longitude:** `{info['lon']}`
# """
#     await app.edit_inline_text(inline_message_id, msg)


# async def ping_func(answers):
#     ping = Ping(ping_id=app.rnd_id())
#     t1 = time()
#     await app.send(ping)
#     t2 = time()
#     ping = f"{str(round((t2 - t1) * 1000, 2))} ms"
#     answers.append(
#         InlineQueryResultArticle(
#             title=ping,
#             input_message_content=InputTextMessageContent(f"__**{ping}**__"),
#         )
#     )
#     return answers


# async def yt_music_func(answers, url):
#     if "http" not in url:
#         url = (await arq.youtube(url)).result[0]
#         url = f"https://youtube.com{url.url_suffix}"
#     loop = asyncio.get_running_loop()
#     music = await loop.run_in_executor(None, download_youtube_audio, url)
#     if not music:
#         msg = "**ERROR**\n__MUSIC TOO LONG__"
#         answers.append(
#             InlineQueryResultArticle(
#                 title="ERROR",
#                 description="MUSIC TOO LONG",
#                 input_message_content=InputTextMessageContent(msg),
#             )
#         )
#         return answers
#     (
#         title,
#         performer,
#         duration,
#         audio,
#         thumbnail,
#     ) = music
#     m = await app.send_audio(
#         MESSAGE_DUMP_CHAT,
#         audio,
#         title=title,
#         duration=duration,
#         performer=performer,
#         thumb=thumbnail,
#     )
#     os.remove(audio)
#     os.remove(thumbnail)
#     answers.append(
#         InlineQueryResultCachedDocument(title=title, file_id=m.audio.file_id)
#     )
#     return answers


# async def info_inline_func(answers, peer):
#     not_found = InlineQueryResultArticle(
#         title="PEER NOT FOUND",
#         input_message_content=InputTextMessageContent("PEER NOT FOUND"),
#     )
#     try:
#         user = await app.get_users(peer)
#         caption, _ = await get_user_info(user, True)
#     except IndexError:
#         try:
#             chat = await app.get_chat(peer)
#             caption, _ = await get_chat_info(chat, True)
#         except Exception:
#             return [not_found]
#     except Exception:
#         return [not_found]

#     answers.append(
#         InlineQueryResultArticle(
#             title="Found Peer.",
#             input_message_content=InputTextMessageContent(
#                 caption, disable_web_page_preview=True
#             ),
#         )
#     )
#     return answers


# async def tmdb_func(answers, query):
#     response = await arq.tmdb(query)
#     if not response.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=response.result,
#                 input_message_content=InputTextMessageContent(response.result),
#             )
#         )
#         return answers
#     results = response.result[:49]
#     for result in results:
#         if not result.poster and not result.backdrop:
#             continue
#         if not result.genre:
#             genre = None
#         else:
#             genre = " | ".join(result.genre)
#         description = result.overview[0:900] if result.overview else "None"
#         caption = f"""
# **{result.title}**
# **Type:** {result.type}
# **Rating:** {result.rating}
# **Genre:** {genre}
# **Release Date:** {result.releaseDate}
# **Description:** __{description}__
# """
#         buttons = InlineKeyboard(row_width=1)
#         buttons.add(
#             InlineKeyboardButton(
#                 "Search Again",
#                 switch_inline_query_current_chat="tmdb",
#             )
#         )
#         answers.append(
#             InlineQueryResultPhoto(
#                 photo_url=result.backdrop
#                 if result.backdrop
#                 else result.poster,
#                 caption=caption,
#                 title=result.title,
#                 description=f"{genre} • {result.releaseDate} • {result.rating} • {description}",
#                 reply_markup=buttons,
#             )
#         )
#     return answers


# async def image_func(answers, query):
#     results = await arq.image(query)
#     if not results.ok:
#         answers.append(
#             InlineQueryResultArticle(
#                 title="Error",
#                 description=results.result,
#                 input_message_content=InputTextMessageContent(results.result),
#             )
#         )
#         return answers
#     results = results.result[:49]
#     buttons = InlineKeyboard(row_width=2)
#     buttons.add(
#         InlineKeyboardButton(
#             text="Search again",
#             switch_inline_query_current_chat="image",
#         ),
#     )
#     for i in results:
#         answers.append(
#             InlineQueryResultPhoto(
#                 title=i.title,
#                 photo_url=i.url,
#                 thumb_url=i.url,
#                 reply_markup=buttons,
#             )
#         )
#     return answers


# async def pokedexinfo(answers, pokemon):
#     Pokemon = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
#     result = await fetch(Pokemon)
#     buttons = InlineKeyboard(row_width=1)
#     buttons.add(
#         InlineKeyboardButton("Pokedex", switch_inline_query_current_chat="pokedex")
#     )
#     pokemon = result['name']
#     pokedex = result['id']
#     type = result['type']
#     poke_img = f"https://img.pokemondb.net/artwork/large/{pokemon}.jpg"
#     abilities = result['abilities']
#     height = result['height']
#     weight = result['weight']
#     gender = result['gender']
#     stats = result['stats']
#     description = result['description']

#     caption = f"""
# ======[ 【Ｐｏｋéｄｅｘ】 ]======

# ╒═══「 **{pokemon.upper()}** 」

# **Pokedex ➢** `{pokedex}`
# **Type ➢** {type}
# **Abilities ➢** {abilities}
# **Height ➢** `{height}`
# **Weight ➢** `{weight}`
# **Gender ➢** {gender}

# **Stats ➢** 
# {stats}

# **Description ➢** __{description}__
# """

#     for ch in ["[", "]", "{", "}", ":"]:
#         if ch in caption:
#             caption = caption.replace(ch, "") 


#     caption = caption.replace("'", "`")
#     caption = caption.replace("`hp`", "× HP : ")
#     caption = caption.replace(", `attack`", "\n× Attack : ")
#     caption = caption.replace(", `defense`", "\n× Defense : ")
#     caption = caption.replace(", `sp_atk`", "\n× Special Attack : ")
#     caption = caption.replace(", `sp_def`", "\n× Special Defanse : ")
#     caption = caption.replace(", `speed`", "\n× Speed : ")
#     caption = caption.replace(", `total`", "\n× Total : ")

#     try:
#         link = f"https://www.pokemon.com/us/pokedex/{pokemon}"
#         button = InlineKeyboard(row_width=1)
#         button.add(InlineKeyboardButton(text="More Info", url=link))
#         answers.append(InlineQueryResultPhoto(photo=poke_img, caption=caption, reply_markup=button))

#     except:
#         answers.append(InlineQueryResultArticle(photo=poke_img, caption=caption))
        
#     return answers


# async def execute_code(query):
#     text = query.query.strip()
#     offset = int((query.offset or 0))
#     answers = []
#     languages = (await arq.execute()).result
#     if len(text.split()) == 1:
#         answers = [
#             InlineQueryResultArticle(
#                 title=lang,
#                 input_message_content=InputTextMessageContent(lang),
#             )
#             for lang in languages
#         ][offset : offset + 25]
#         await query.answer(
#             next_offset=str(offset + 25),
#             results=answers,
#             cache_time=1,
#         )
#     elif len(text.split()) == 2:
#         text = text.split()[1].strip()
#         languages = list(
#             filter(
#                 lambda x: find_near_matches(text, x, max_l_dist=1),
#                 languages,
#             )
#         )
#         answers.extend(
#             [
#                 InlineQueryResultArticle(
#                     title=lang,
#                     input_message_content=InputTextMessageContent(lang),
#                 )
#                 for lang in languages
#             ][:49]
#         )
#     else:
#         lang = text.split()[1]
#         code = text.split(None, 2)[2]
#         response = await arq.execute(lang, code)
#         if not response.ok:
#             answers.append(
#                 InlineQueryResultArticle(
#                     title="Error",
#                     input_message_content=InputTextMessageContent(
#                         response.result
#                     ),
#                 )
#             )
#         else:
#             res = response.result
#             stdout, stderr = escape(res.stdout), escape(res.stderr)
#             output = stdout or stderr
#             out = "STDOUT" if stdout else ("STDERR" if stderr else "No output")

#             msg = f"""
# **{lang.capitalize()}:**
# ```{code}```
# **{out}:**
# ```{output}```
#             """
#             answers.append(
#                 InlineQueryResultArticle(
#                     title="Executed",
#                     description=output[:20],
#                     input_message_content=InputTextMessageContent(msg),
#                 )
#             )
#     await query.answer(results=answers, cache_time=1)


# async def task_inline_func(user_id):
#     if user_id not in DEV_USERS:
#         return

#     tasks = all_tasks()
#     text = await _get_tasks_text()
#     keyb = None

#     if tasks:
#         keyb = ikb(
#             {i: f"cancel_task_{i}" for i in list(tasks.keys())},
#             row_width=4,
#         )

#     return [
#         InlineQueryResultArticle(
#             title="Tasks",
#             reply_markup=keyb,
#             input_message_content=InputTextMessageContent(
#                 text,
#             ),
#         )
#     ]


# @app.on_callback_query(filters.regex("^cancel_task_"))
# async def cancel_task_button(_, query: CallbackQuery):
#     user_id = query.from_user.id

#     if user_id not in DEV_USERS:
#         return await query.answer("This is not for you.")

#     task_id = int(query.data.split("_")[-1])
#     await rm_task(task_id)

#     tasks = all_tasks()
#     text = await _get_tasks_text()
#     keyb = None

#     if tasks:
#         keyb = ikb({i: f"cancel_task_{i}" for i in list(tasks.keys())})

#     await app.edit_inline_text(
#         query.inline_message_id,
#         text,
#     )

#     if keyb:
#         await app.edit_inline_reply_markup(
#             query.inline_message_id,
#             keyb,
#         )

# #--------------------


# """
# Kang With Credits:

# A Huge Thanks To @TheHamkerCat for this Inline Module
# Make Sure to Check out!

# """

import asyncio
import os
import sys
from html import escape
from re import sub as re_sub
from sys import version as pyver
from time import ctime, time
import ffmpeg
import youtube_dl
from urllib.parse import urlparse
from fuzzysearch import find_near_matches
from motor import version as mongover
from pykeyboard import InlineKeyboard
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.raw.functions import Ping
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineQueryResultArticle,
                            InlineQueryResultPhoto,
                            InputTextMessageContent)
from search_engine_parser import GoogleSearch

from Shikimori import DEV_USERS
from Shikimori import LOG_CHANNEL
from Shikimori import pbot as app 
from Shikimori.modules import arq
from Shikimori.core.keyboard import ikb
from Shikimori.core.tasks import _get_tasks_text, all_tasks, rm_task
from Shikimori.core.types import InlineQueryResultCachedDocument
from Shikimori.modules.info import get_chat_info, get_user_info
from Shikimori.utils.functions import test_speedtest
from Shikimori.utils.pastebin import paste

MESSAGE_DUMP_CHAT = LOG_CHANNEL

BOT_USERNAME = ""
keywords_list = [
    "image",
    "wall",
    "tmdb",
    "lyrics",
    "exec",
    "speedtest",
    "search",
    "ping",
    "tr",
    "ud",
    "yt",
    "info",
    "google",
    "torrent",
    "wiki",
    "music",
    "ytmusic",
]


async def inline_help_func(__help__):
    buttons = InlineKeyboard(row_width=4)
    buttons.add(
        *[
            (
                InlineKeyboardButton(
                    text=i, switch_inline_query_current_chat=i
                )
            )
            for i in keywords_list
        ]
    )
    answerss = [
        InlineQueryResultArticle(
            title="Inline Commands",
            description="Help Related To Inline Usage.",
            input_message_content=InputTextMessageContent(
                "Click a button to get started."
            ),
            thumb_url="https://telegra.ph/file/a03660425cd749faf0a4a.jpg",
            reply_markup=buttons,
        ),
    ]
    answerss = await alive_function(answerss)
    return answerss

def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


def download_youtube_audio(url: str):
    global is_downloading
    with youtube_dl.YoutubeDL(
        {
            "format": "bestaudio",
            "writethumbnail": True,
            "quiet": True,
        }
    ) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        if int(float(info_dict["duration"])) > 600:
            is_downloading = False
            return []
        ydl.process_info(info_dict)
        audio_file = ydl.prepare_filename(info_dict)
        basename = audio_file.rsplit(".", 1)[-2]
        if info_dict["ext"] == "webm":
            audio_file_opus = basename + ".opus"
            ffmpeg.input(audio_file).output(
                audio_file_opus, codec="copy", loglevel="error"
            ).overwrite_output().run()
            os.remove(audio_file)
            audio_file = audio_file_opus
        thumbnail_url = info_dict["thumbnail"]
        thumbnail_file = (
            basename
            + "."
            + get_file_extension_from_url(thumbnail_url)
        )
        title = info_dict["title"]
        performer = info_dict["uploader"]
        duration = int(float(info_dict["duration"]))
    return [title, performer, duration, audio_file, thumbnail_file]


async def alive_function(answers):
    buttons = InlineKeyboard(row_width=2)
    bot_state = "Dead" if not await app.get_me() else "Alive"
    buttons.add(
        InlineKeyboardButton("Main bot", url=f"https://t.me/lunatapibot"),
        InlineKeyboardButton(
            "Go Inline!", switch_inline_query_current_chat=""
        ),
    )

    msg = f"""
**[Shikimori](https://t.me/):**
**RoBot:** `{bot_state}`
**UserBot:** `Alive`
**Python:** `{pyver.split()[0]}`
**Pyrogram:** `{pyrover}`
**MongoDB:** `{mongover}`
**Platform:** `{sys.platform}`
**Profiles:** [BOT](https://t.me/) | [UBOT](https://t.me/Ryu_God)
"""
    answers.append(
        InlineQueryResultArticle(
            title="Alive",
            description="Check Shikimori Stats",
            thumb_url="https://telegra.ph/file/fbb803ea2af74de745362.jpg",
            input_message_content=InputTextMessageContent(
                msg, disable_web_page_preview=True
            ),
            reply_markup=buttons,
        )
    )
    asnwers = await about_function(answers)
    return answers

async def about_function(answers):
    buttons = InlineKeyboard(row_width=2)
    bot_state = "Dead" if not await app.get_me() else "About"
    buttons.add(
        InlineKeyboardButton("Support", url=f"https://t.me/"),
        InlineKeyboardButton("Channel", url=f"https://t.me/"),
    )

    msg = f"""
[Shikimori✨](https://t.me/) 
   Maintained by [X](t.me/Ryu_God) [Y](t.me/TheBlacklinen) 
Built with using python-telegram-bot v13.7 Running on Python 3.9.7
"""
    answers.append(
        InlineQueryResultArticle(
            title="About",
            description="About Shikimori",
            thumb_url="https://telegra.ph/file/fbb803ea2af74de745362.jpg",
            input_message_content=InputTextMessageContent(
                msg, disable_web_page_preview=True
            ),
            reply_markup=buttons,
        )
    )
    return answers


async def translate_func(answers, lang, tex):
    result = await arq.translate(tex, lang)
    if not result.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=result.result,
                input_message_content=InputTextMessageContent(
                    result.result
                ),
            )
        )
        return answers
    result = result.result
    msg = f"""
__**Translated from {result.src} to {result.dest}**__

**INPUT:**
{tex}

**OUTPUT:**
{result.translatedText}"""
    answers.extend(
        [
            InlineQueryResultArticle(
                title=f"Translated from {result.src} to {result.dest}.",
                description=result.translatedText,
                input_message_content=InputTextMessageContent(msg),
            ),
            InlineQueryResultArticle(
                title=result.translatedText,
                input_message_content=InputTextMessageContent(
                    result.translatedText
                ),
            ),
        ]
    )
    return answers


async def urban_func(answers, text):
    results = await arq.urbandict(text)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[0:48]
    for i in results:
        clean = lambda x: re_sub(r"[\[\]]", "", x)
        msg = f"""
**Query:** {text}

**Definition:** __{clean(i.definition)}__

**Example:** __{clean(i.example)}__"""

        answers.append(
            InlineQueryResultArticle(
                title=i.word,
                description=clean(i.definition),
                input_message_content=InputTextMessageContent(msg),
            )
        )
    return answers


async def google_search_func(answers, text):
    gresults = await GoogleSearch().async_search(text)
    limit = 0
    for i in gresults:
        if limit > 48:
            break
        limit += 1

        try:
            msg = f"""
[{i['titles']}]({i['links']})
{i['descriptions']}"""

            answers.append(
                InlineQueryResultArticle(
                    title=i["titles"],
                    description=i["descriptions"],
                    input_message_content=InputTextMessageContent(
                        msg, disable_web_page_preview=True
                    ),
                )
            )
        except KeyError:
            pass
    return answers


async def wall_func(answers, text):
    results = await arq.wall(text)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[0:48]
    for i in results:
        answers.append(
            InlineQueryResultPhoto(
                photo_url=i.url_image,
                thumb_url=i.url_thumb,
                caption=f"[Source]({i.url_image})",
            )
        )
    return answers


async def torrent_func(answers, text):
    results = await arq.torrent(text)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[0:48]
    for i in results:
        title = i.name
        size = i.size
        seeds = i.seeds
        leechs = i.leechs
        upload_date = i.uploaded
        magnet = i.magnet
        caption = f"""
**Title:** __{title}__
**Size:** __{size}__
**Seeds:** __{seeds}__
**Leechs:** __{leechs}__
**Uploaded:** __{upload_date}__
**Magnet:** `{magnet}`"""

        description = f"{size} | {upload_date} | Seeds: {seeds}"
        answers.append(
            InlineQueryResultArticle(
                title=title,
                description=description,
                input_message_content=InputTextMessageContent(
                    caption, disable_web_page_preview=True
                ),
            )
        )
        pass
    return answers


async def youtube_func(answers, text):
    results = await arq.youtube(text)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[0:48]
    for i in results:
        buttons = InlineKeyboard(row_width=1)
        video_url = f"https://youtube.com{i.url_suffix}"
        buttons.add(InlineKeyboardButton("Watch", url=video_url))
        caption = f"""
**Title:** {i.title}
**Views:** {i.views}
**Channel:** {i.channel}
**Duration:** {i.duration}
**Uploaded:** {i.publish_time}
**Description:** {i.long_desc}"""
        description = f"{i.views} | {i.channel} | {i.duration} | {i.publish_time}"
        answers.append(
            InlineQueryResultArticle(
                title=i.title,
                thumb_url=i.thumbnails[0],
                description=description,
                input_message_content=InputTextMessageContent(
                    caption, disable_web_page_preview=True
                ),
                reply_markup=buttons,
            )
        )
    return answers


async def lyrics_func(answers, text):
    song = await arq.lyrics(text)
    if not song.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=song.result,
                input_message_content=InputTextMessageContent(
                    song.result
                ),
            )
        )
        return answers
    lyrics = song.result
    song = lyrics.splitlines()
    song_name = song[0]
    artist = song[1]
    if len(lyrics) > 4095:
        lyrics = await paste(lyrics)
        lyrics = f"**Lyrics too Long:** [URL]({lyrics})"

    msg = f"__{lyrics}__"

    answers.append(
        InlineQueryResultArticle(
            title=song_name,
            description=artist,
            input_message_content=InputTextMessageContent(msg),
        )
    )
    return answers


async def tg_search_func(answers, text, user_id):
    if user_id not in DEV_USERS:
        msg = "**ERROR**\n__Only For Devs__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="Only For Devs",
                input_message_content=InputTextMessageContent(msg),
            )
        )
        return answers
    if str(text)[-1] != ":":
        msg = "**ERROR**\n__Put A ':' After The Text To Search__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="Put A ':' After The Text To Search",
                input_message_content=InputTextMessageContent(msg),
            )
        )

        return answers
    text = text[0:-1]
    async for message in app.search_global(text, limit=49):
        buttons = InlineKeyboard(row_width=2)
        buttons.add(
            InlineKeyboardButton(
                text="Origin",
                url=message.link
                if message.link
                else "https://t.me/telegram",
            ),
            InlineKeyboardButton(
                text="Search again",
                switch_inline_query_current_chat="search",
            ),
        )
        name = (
            message.from_user.first_name
            if message.from_user.first_name
            else "NO NAME"
        )
        caption = f"""
**Query:** {text}
**Name:** {str(name)} [`{message.from_user.id}`]
**Chat:** {str(message.chat.title)} [`{message.chat.id}`]
**Date:** {ctime(message.date)}
**Text:** >>

{message.text.markdown if message.text else message.caption if message.caption else '[NO_TEXT]'}
"""
        result = InlineQueryResultArticle(
            title=name,
            description=message.text if message.text else "[NO_TEXT]",
            reply_markup=buttons,
            input_message_content=InputTextMessageContent(
                caption, disable_web_page_preview=True
            ),
        )
        answers.append(result)
    return answers


async def music_inline_func(answers, query):
    chat_id = -1001574867550
    group_invite = "https://t.me/TedeMusicCache"
    try:
        messages = [
            m
            async for m in app.search_messages(
                chat_id, query, filter="audio", limit=100
            )
        ]
    except Exception as e:
        print(e)
        msg = f"You Need To Join Here With Your Bot And Userbot To Get Cached Music.\n{group_invite}"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="Click Here To Know More.",
                input_message_content=InputTextMessageContent(
                    msg, disable_web_page_preview=True
                ),
            )
        )
        return answers
    messages_ids_and_duration = []
    for f_ in messages:
        messages_ids_and_duration.append(
            {
                "message_id": f_.message_id,
                "duration": f_.audio.duration if f_.audio.duration else 0,
            }
        )
    messages = list(
        {v["duration"]: v for v in messages_ids_and_duration}.values()
    )
    messages_ids = [ff_["message_id"] for ff_ in messages]
    messages = await app.get_messages(chat_id, messages_ids[0:48])
    return [
        InlineQueryResultCachedDocument(
            file_id=message_.audio.file_id,
            title=message_.audio.title,
        )
        for message_ in messages
    ]



async def wiki_func(answers, text):
    data = await arq.wiki(text)
    if not data.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=data.result,
                input_message_content=InputTextMessageContent(
                    data.result
                ),
            )
        )
        return answers
    data = data.result
    msg = f"""
**QUERY:**
{data.title}

**ANSWER:**
__{data.answer}__"""
    answers.append(
        InlineQueryResultArticle(
            title=data.title,
            description=data.answer,
            input_message_content=InputTextMessageContent(msg),
        )
    )
    return answers


async def speedtest_init(query):
    answers = []
    user_id = query.from_user.id
    if user_id not in DEV_USERS:
        msg = "**ERROR**\n__THIS FEATURE IS ONLY FOR DEVS__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="THIS FEATURE IS ONLY FOR DEVS",
                input_message_content=InputTextMessageContent(msg),
            )
        )
        return answers
    msg = "**Click The Button Below To Perform A Speedtest**"
    button = InlineKeyboard(row_width=1)
    button.add(
        InlineKeyboardButton(
            text="Start!", callback_data="test_speedtest"
        )
    )
    answers.append(
        InlineQueryResultArticle(
            title="Click Here",
            input_message_content=InputTextMessageContent(msg),
            reply_markup=button,
        )
    )
    return answers


@app.on_callback_query(filters.regex("test_speedtest"))
async def test_speedtest_cq(_, cq):
    if cq.from_user.id not in DEV_USERS:
        return await cq.answer("This Isn't For You!")
    inline_message_id = cq.inline_message_id
    await app.edit_inline_text(inline_message_id, "**Testing**")
    loop = asyncio.get_running_loop()
    download, upload, info = await loop.run_in_executor(
        None, test_speedtest
    )
    msg = f"""
**Download:** `{download}`
**Upload:** `{upload}`
**Latency:** `{info['latency']} ms`
**Country:** `{info['country']} [{info['cc']}]`
**Latitude:** `{info['lat']}`
**Longitude:** `{info['lon']}`
"""
    await app.edit_inline_text(inline_message_id, msg)


async def ping_func(answers):
    ping = Ping(ping_id=app.rnd_id())
    t1 = time()
    await app.send(ping)
    t2 = time()
    ping = f"{str(round((t2 - t1) * 1000, 2))} ms"
    answers.append(
        InlineQueryResultArticle(
            title=ping,
            input_message_content=InputTextMessageContent(
                f"__**{ping}**__"
            ),
        )
    )
    return answers


async def yt_music_func(answers, url):
    if "http" not in url:
        url = (await arq.youtube(url)).result[:10]
        url = f"https://youtube.com{url.url_suffix}"
    loop = asyncio.get_running_loop()
    music = await loop.run_in_executor(
        None, download_youtube_audio, url
    )
    if not music:
        msg = "**ERROR**\n__MUSIC TOO LONG__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="MUSIC TOO LONG",
                input_message_content=InputTextMessageContent(msg),
            )
        )
        return answers
    (
        title,
        performer,
        duration,
        audio,
        thumbnail,
    ) = music
    m = await app.send_audio(
        LOG_CHANNEL,
        audio,
        title=title,
        duration=duration,
        performer=performer,
        thumb=thumbnail,
    )
    os.remove(audio)
    os.remove(thumbnail)
    answers.append(
        InlineQueryResultCachedDocument(
            title=title, file_id=m.audio.file_id
        )
    )
    return answers


async def info_inline_func(answers, peer):
    not_found = InlineQueryResultArticle(
        title="PEER NOT FOUND",
        input_message_content=InputTextMessageContent(
            "PEER NOT FOUND"
        ),
    )
    try:
        user = await app.get_users(peer)
        caption, _ = await get_user_info(user, True)
    except IndexError:
        try:
            chat = await app.get_chat(peer)
            caption, _ = await get_chat_info(chat, True)
        except Exception:
            return [not_found]
    except Exception:
        return [not_found]

    answers.append(
        InlineQueryResultArticle(
            title="Found Peer.",
            input_message_content=InputTextMessageContent(
                caption, disable_web_page_preview=True
            ),
        )
    )
    return answers


async def tmdb_func(answers, query):
    response = await arq.tmdb(query)
    if not response.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=response.result,
                input_message_content=InputTextMessageContent(
                    response.result
                ),
            )
        )
        return answers
    results = response.result[:49]
    for result in results:
        if not result.poster and not result.backdrop:
            continue
        if not result.genre:
            genre = None
        else:
            genre = " | ".join(result.genre)
        description = (
            result.overview[0:900] if result.overview else "None"
        )
        caption = f"""
**{result.title}**
**Type:** {result.type}
**Rating:** {result.rating}
**Genre:** {genre}
**Release Date:** {result.releaseDate}
**Description:** __{description}__
"""
        buttons = InlineKeyboard(row_width=1)
        buttons.add(
            InlineKeyboardButton(
                "Search Again",
                switch_inline_query_current_chat="tmdb",
            )
        )
        answers.append(
            InlineQueryResultPhoto(
                photo_url=result.backdrop
                if result.backdrop
                else result.poster,
                caption=caption,
                title=result.title,
                description=f"{genre} • {result.releaseDate} • {result.rating} • {description}",
                reply_markup=buttons,
            )
        )
    return answers


async def image_func(answers, query):
    results = await arq.image(query)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[:49]
    buttons = InlineKeyboard(row_width=2)
    buttons.add(
        InlineKeyboardButton(
            text="Search again",
            switch_inline_query_current_chat="image",
        ),
    )
    for i in results:
        answers.append(
            InlineQueryResultPhoto(
                title=i.title,
                photo_url=i.url,
                thumb_url=i.url,
                reply_markup=buttons,
            )
        )
    return answers


async def execute_code(query):
    text = query.query.strip()
    offset = int((query.offset or 0))
    answers = []
    languages = (await arq.execute()).result
    if len(text.split()) == 1:
        answers = [
            InlineQueryResultArticle(
                title=lang,
                input_message_content=InputTextMessageContent(lang),
            )
            for lang in languages
        ][offset : offset + 25]
        await query.answer(
            next_offset=str(offset + 25),
            results=answers,
            cache_time=1,
        )
    elif len(text.split()) == 2:
        text = text.split()[1].strip()
        languages = list(
            filter(
                lambda x: find_near_matches(text, x, max_l_dist=1),
                languages,
            )
        )
        answers.extend(
            [
                InlineQueryResultArticle(
                    title=lang,
                    input_message_content=InputTextMessageContent(
                        lang
                    ),
                )
                for lang in languages
            ][:49]
        )
    else:
        lang = text.split()[1]
        code = text.split(None, 2)[2]
        response = await arq.execute(lang, code)
        if not response.ok:
            answers.append(
                InlineQueryResultArticle(
                    title="Error",
                    input_message_content=InputTextMessageContent(
                        response.result
                    ),
                )
            )
        else:
            res = response.result
            stdout, stderr = escape(res.stdout), escape(res.stderr)
            output = stdout or stderr
            out = (
                "STDOUT"
                if stdout
                else ("STDERR" if stderr else "No output")
            )

            msg = f"""
**{lang.capitalize()}:**
```{code}```

**{out}:**
```{output}```
            """
            answers.append(
                InlineQueryResultArticle(
                    title="Executed",
                    description=output[:20],
                    input_message_content=InputTextMessageContent(
                        msg
                    ),
                )
            )
    await query.answer(results=answers, cache_time=1)


async def task_inline_func(user_id):
    if user_id not in DEV_USERS:
        return

    tasks = all_tasks()
    text = await _get_tasks_text()
    keyb = None

    if tasks:
        keyb = ikb(
            {i: f"cancel_task_{i}" for i in list(tasks.keys())},
            row_width=4,
        )

    return [
        InlineQueryResultArticle(
            title="Tasks",
            reply_markup=keyb,
            input_message_content=InputTextMessageContent(
                text,
            ),
        )
    ]


@app.on_callback_query(filters.regex("^cancel_task_"))
async def cancel_task_button(_, query: CallbackQuery):
    user_id = query.from_user.id

    if user_id not in DEV_USERS:
        return await query.answer("This is not for you.")

    task_id = int(query.data.split("_")[-1])
    await rm_task(task_id)

    tasks = all_tasks()
    text = await _get_tasks_text()
    keyb = None

    if tasks:
        keyb = ikb(
            {i: f"cancel_task_{i}" for i in list(tasks.keys())}
        )

    await app.edit_inline_text(
        query.inline_message_id,
        text,
    )

    if keyb:
        await app.edit_inline_reply_markup(
            query.inline_message_id,
            keyb,
        )
