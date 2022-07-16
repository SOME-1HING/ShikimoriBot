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

@is_pyroadmin
@pbot.on_message(filters.command("check"))
async def check(_, message):
    if is_pyroadmin:
        return await message.reply_text("yes")
    elif not is_pyroadmin:
        return await message.rely_text("no")
    else:
        return await message.reply_text("error")