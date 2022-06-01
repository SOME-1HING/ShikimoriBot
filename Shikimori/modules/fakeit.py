import os

import requests
from faker import Faker
from faker.providers import internet
from telethon import events

from Shikimori.pyrogramee.telethonbasics import is_admin
from Shikimori import telethn as pbot

@pbot.on(events.NewMessage(pattern="/fakegen$"))
async def hi(event):
    if event.fwd_from:
        return
    if event.is_group:
        if not await is_admin(event, event.message.sender_id):
            await event.reply("`You Should Be Admin To Do This!`")
            return
    fake = Faker()
    print("FAKE DETAILS GENERATED\n")
    name = str(fake.name())
    fake.add_provider(internet)
    address = str(fake.address())
    ip = fake.ipv4_private()
    cc = fake.credit_card_full()
    email = fake.ascii_free_email()
    job = fake.job()
    android = fake.android_platform_token()
    pc = fake.chrome()
    await event.reply(
        f"<b><u> Fake Information Generated</b></u>\n<b>Name :-</b><code>{name}</code>\n\n<b>Address:-</b><code>{address}</code>\n\n<b>IP ADDRESS:-</b><code>{ip}</code>\n\n<b>credit card:-</b><code>{cc}</code>\n\n<b>Email Id:-</b><code>{email}</code>\n\n<b>Job:-</b><code>{job}</code>\n\n<b>android user agent:-</b><code>{android}</code>\n\n<b>Pc user agent:-</b><code>{pc}</code>",
        parse_mode="HTML",
    )


@pbot.on(events.NewMessage(pattern="/picgen$"))
async def _(event):
    URL = "https://thispersondoesnotexist.com/image"
    await pbot.send_img(event.chat_id, URL)



__mod_name__ = "Fake info"

__help__ = """
*Commands:*
- /fakegen : Generates Fake Information
- /picgen : generate a fake pic
"""
