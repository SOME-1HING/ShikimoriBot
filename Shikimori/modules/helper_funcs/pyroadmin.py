from Shikimori import pbot
from pyrogram import filters

async def is_pyroadmin(_, message):
    try:
        user = await message.user
        if user.is_admin:
            return True
        else:
            return False
    except:
        return False


@pbot.on_message(filters.command("checkl"))
async def checkl(_, message):
    try:
        if is_pyroadmin:
            return await message.reply_text("yes")
        elif not is_pyroadmin:
            return await message.rely_text("no")
        else:
            return await message.reply_text("error")
    except Exception as e:
        print(e)



@pbot.on_message(filters.command("checkw"))
async def checkw(_, message):
    await message.reply_text("hmm")
    user = await message.user
    try:
        if user.is_admin:
            return await message.reply_text("yes")
        elif not user.is_admin:
            return await message.reply_text("no")
        else:
            return await message.reply_text("error")
    except Exception as e:
        print(e)