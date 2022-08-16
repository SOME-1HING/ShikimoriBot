"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

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

import aiohttp
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
from Shikimori import pbot
from Shikimori.Extras.errors import capture_err

@pbot.on_message(filters.command(['pokedex', 'pokemon']))
@capture_err
async def PokeDex(_, message):
    if len(message.command) != 2:
        await message.reply_text("/pokedex Pokemon Name")
        return
    pokemon = message.text.split(None, 1)[1]
    pokedex = f'https://some-random-api.ml/pokedex?pokemon={pokemon}'
    async with aiohttp.ClientSession() as session:
        async with session.get(pokedex) as request:
            if request.status == 404:
                return await message.reply_text("Wrong Pokemon Name")

            result = await request.json()
            try:
                pokemon = result['name']
                pokedex = result['id']
                type = result['type']
                poke_img = f"https://img.pokemondb.net/artwork/large/{pokemon}.jpg"
                abilities = result['abilities']
                height = result['height']
                weight = result['weight']
                gender = result['gender']
                stats = result['stats']
                description = result['description']
                caption = f"""
======[ 【Ｐｏｋéｄｅｘ】 ]======

╒═══「 **{pokemon.upper()}** 」

**Pokedex ➢** `{pokedex}`
**Type ➢** {type}
**Abilities ➢** {abilities}
**Height ➢** `{height}`
**Weight ➢** `{weight}`
**Gender ➢** {gender}

**Stats ➢** 
{stats}

**Description ➢** __{description}__
"""

                for ch in ["[", "]", "{", "}", ":"]:
                    if ch in caption:
                        caption = caption.replace(ch, "") 


                caption = caption.replace("'", "`")
                caption = caption.replace("`hp`", "× HP : ")
                caption = caption.replace(", `attack`", "\n× Attack : ")
                caption = caption.replace(", `defense`", "\n× Defense : ")
                caption = caption.replace(", `sp_atk`", "\n× Special Attack : ")
                caption = caption.replace(", `sp_def`", "\n× Special Defanse : ")
                caption = caption.replace(", `speed`", "\n× Speed : ")
                caption = caption.replace(", `total`", "\n× Total : ")

                try:
                    link = f"https://www.pokemon.com/us/pokedex/{pokemon}"
                    button = InlineKeyboard(row_width=1)
                    button.add(InlineKeyboardButton(text="More Info", url=link))
                    await message.reply_photo(photo=poke_img, caption=caption, reply_markup=button)

                except:
                    await message.reply_photo(photo=poke_img, caption=caption)

            except Exception as e:
                print(str(e))
                pass


__mod_name__ = "Pokedex"
__help__ = """
**Here is help for Pokedex**

`/pokedex` <pokemon name> - Get information about the pokemon.
`/pokemon` <pokemon name> - Get information about the pokemon.
"""