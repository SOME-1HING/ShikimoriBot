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
                stats = stats.replace(", `hp`", "HP = ")
                stats = stats.replace(", `attack`", "\nAttack = ")
                stats = stats.replace(", `defense`", "\nDefense = ")
                stats = stats.replace(", `sp_atk`", "\nSpecial Attack = ")
                stats = stats.replace(", `sp_def`", "\nSpecial Defanse = ")
                stats = stats.replace(", `speed`", "\nSpeed = ")
                stats = stats.replace(", `total`", "\nTotal = ")
                caption = f"""
**Pokemon =>** {pokemon.upper()}
**Pokedex =>** `{pokedex}`
**Type =>** {type}
**Abilities =>** {abilities}
**Height =>** `{height}`
**Weight =>** `{weight}`
**Gender =>** {gender}
**Stats =>** 
{stats}

**Description =>** __{description}__
"""
                for ch in ["[", "]", "{", "}", ":"]:
                    if ch in caption:
                        caption = caption.replace(ch, "") 


                caption = caption.replace("'", "`")

            except Exception as e:
                print(str(e))
                pass

    try:
        link = f"https://www.pokemon.com/us/pokedex/{pokemon}"
        button = InlineKeyboard(row_width=1)
        button.add(InlineKeyboardButton(text="More Info", url=link))
        await message.reply_photo(photo=poke_img, caption=caption)

    except:
        await message.reply_photo(photo=poke_img, caption=caption)


__mod_name__ = "Pokedex"
__help__ = """
**Here is help for Pokedex**

`/pokedex` <pokemon name> - Get information about the pokemon.
`/pokemon` <pokemon name> - Get information about the pokemon.
"""