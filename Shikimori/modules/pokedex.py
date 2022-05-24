
import aiohttp
from pyrogram import filters
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
Pokemon: {pokemon}
Pokedex: {pokedex}
Type: {type.replace('[', '').replace(']', '').replace("'", '')}
Abilities: {abilities.replace('[', '').replace(']', '').replace("'", '')}
Height: {height}
Weight: {weight}
Gender: {gender.replace('[', '').replace(']', '').replace("'", '')}
Stats: {stats.replace("{'", "\n").replace('}', '').replace("'", '').replace(',', '\n')}
Description: {description}"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=poke_img, caption=caption)


__mod_name__ = "Pokedex"
__help__ = """
Here is help for Pokedex

/pokedex <pokemon name> - Get information about the pokemon.
/pokemon <pokemon name> - Get information about the pokemon.
"""