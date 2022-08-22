## Made By @Yash-Sharma-1807
## telegram.dog/YASH_SHARMA_1807?start=papa

import os
from random import choice
from Shikimori.events import register
from Shikimori.modules.helper_funcs.quoteapi import quotely
from Shikimori.modules.helper_funcs.quotes import process

col_list = ("black", "white", "magenta", "blue", "red", "yellow", "cyan")

@register(pattern="^/q(?: |$)(.*)")
async def quott_(event):
    if not event.is_reply:
        return await event.reply("Please reply to a message")
    msg = await event.reply("`Creating quote please wait.`")
    try:
        match = event.pattern_match.group(1).strip()
        reply = await event.get_reply_message()
        replied_to, reply_ = None, None
        if match:
            spli_ = match.split(maxsplit=1)
            if (spli_[0] in ["r", "reply"]) or (
                spli_[0].isdigit() and int(spli_[0]) in range(1, 21)
            ):
                if spli_[0].isdigit():
                    if int(spli_[0]) >= 21:
                        return await event.reply("I can't quote more than 20,message at once.")
                    if not event.client._bot:
                        reply_ = await event.client.get_messages(
                            event.chat_id,
                            min_id=event.reply_to_msg_id - 1,
                            reverse=True,
                            limit=int(spli_[0]),
                        )
                    else:
                        id_ = reply.id
                        reply_ = []
                        for msg_ in range(id_, id_ + int(spli_[0])):
                            msh = await event.client.get_messages(event.chat_id, ids=msg_)
                            if msh:
                                reply_.append(msh)
                else:
                    replied_to = await reply.get_reply_message()
                try:
                    match = spli_[1]
                except IndexError:
                    match = None
        user = None
        if not reply_:
            reply_ = reply
        if match:
            match = match.split(maxsplit=1)
        if match:
            if match[0].startswith("@") or match[0].isdigit():
                try:
                    match_ = await event.client.parse_id(match[0])
                    user = await event.client.get_entity(match_)
                except ValueError:
                    pass
                match = match[1] if len(match) == 2 else None
            else:
                match = match[0]
        if match == "random":
            match = choice(col_list)
      
        file = await quotely.create_quotly(
            reply_, bg=match, reply=replied_to, sender=user
        )
        message = await reply.reply("", file=file)
        os.remove(file)
        try:
            await msg.delete()
        except:
            pass
        return message
    except:
        if event.fwd_from:
            return
        reply = await event.get_reply_message()
        msg = reply.message
        repliedreply = await reply.get_reply_message()
        user = (
            await event.client.get_entity(reply.forward.sender) if reply.fwd_from
            else reply.sender)
        res, canvas = await process(msg, user, event.client, reply, repliedreply)
        if not res:
            return
        canvas.save('sticker.webp')
        await event.client.send_file(event.chat_id, "sticker.webp", reply_to=event.reply_to_msg_id)
        os.remove('sticker.webp')
        try:
            await msg.delete()
        except:
            pass    

__mod_name__ = "Quotly"

__help__ = """
> `/q` *:* To quote a message.
"""