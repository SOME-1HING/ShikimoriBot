from Shikimori import telethn as tbot
import os
from Shikimori.events import register
import secureme


@register(pattern="^/encrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        cmd = lel.text
    else:
        cmd = event.pattern_match.group(1)
    Text = cmd
    k = secureme.encrypt(Text)
    await event.reply(k)


@register(pattern="^/decrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        ok = lel.text
    else:
        ok = event.pattern_match.group(1)
    Text = ok
    k = secureme.decrypt(Text)
    await event.reply(k)


__mod_name__ = "Encryption"

___help__ = """
Here is help for Encryption

Note: Only works for text.

/encrypt - Reply to a text message to Encrypt it.
/decrypt - Reply to a text message to Decrypt it.
"""

