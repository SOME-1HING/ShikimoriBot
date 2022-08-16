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
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
from Shikimori import pbot
from Shikimori.Extras.errors import capture_err

@pbot.on_message(filters.command(['pokedex', 'pokemon']))
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