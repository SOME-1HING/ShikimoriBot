# Voics Chatbot Module Credits Pranav Ajay 🐰Github = Red-Aura 🐹 Telegram= @madepranav
# @lyciachatbot support Now
import os

import aiofiles
import aiohttp
from pyrogram import filters

from Shikimori import pbot as LYCIA


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data


async def ai_lycia(url):
    ai_name = "Lycia.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(ai_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return ai_name


@LYCIA.on_message(filters.command("voicebot"))
async def Lycia(_, message):
    if len(message.command) < 2:
        await message.reply_text("`/voicebot` <msg>")
        return
    text = message.text.split(None, 1)[1]
    lycia = text.replace(" ", "%20")
    m = await message.reply_text("`Thinking....`")
    try:
        L = await fetch(
            f"https://api.affiliateplus.xyz/api/chatbot?message={lycia}&botname=Shasa&ownername=@Simpleboy787&user=1"
        )
        chatbot = L["message"]
        VoiceAi = f"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=hi"
        name = "Shikimori"
    except Exception as e:
        await m.edit(str(e))
        return
    LyciaVoice = await ai_lycia(VoiceAi)
    await m.edit("`Replying...`")
    await message.reply_audio(audio=LyciaVoice, title=chatbot, performer=name)
    os.remove(LyciaVoice)
    await m.delete()



__help__ = """
 • `/voicebot` <msg> : Shikimori replies to your chat.

 Made By @SimpleBoy787
"""

__mod_name__ = "Voice Bot"