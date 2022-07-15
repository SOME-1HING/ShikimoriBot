"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

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

from asyncio import Lock, create_task
from time import time

from pyrogram import filters
from pyrogram.types import Message

from wbb import BOT_ID, SUDOERS, USERBOT_PREFIX, app2
from wbb.core.sections import bold, section, w

tasks = {}
TASKS_LOCK = Lock()
arrow = lambda x: (x.text if x else "") + "\n`→`"


def all_tasks():
    return tasks


async def add_task(
        taskFunc,
        task_name,
        *args,
        **kwargs,
):
    async with TASKS_LOCK:
        global tasks

        task_id = (list(tasks.keys())[-1] + 1) if tasks else 0

        task = create_task(
            taskFunc(*args, **kwargs),
            name=task_name,
        )
        tasks[task_id] = task, int(time())
    return task, task_id


async def rm_task(task_id=None):
    global tasks

    async with TASKS_LOCK:
        for key, value in list(tasks.items()):
            if value[0].done() or value[0].cancelled():
                del tasks[key]

        if (task_id is not None) and (task_id in tasks):
            task = tasks[task_id][0]

            if not task.done():
                task.cancel()

            del tasks[task_id]


async def _get_tasks_text():
    await rm_task()  # Clean completed tasks
    if not tasks:
        return f"{arrow('')} No pending task"

    text = bold("Tasks") + "\n"

    for i, task in enumerate(list(tasks.items())):
        indent = w * 4

        t, started = task[1]
        elapsed = round(time() - started)
        info = t._repr_info()

        id = task[0]
        text += section(
            f"{indent}Task {i}",
            body={
                "Name": t.get_name(),
                "Task ID": id,
                "Status": info[0].capitalize(),
                "Origin": info[2].split("/")[-1].replace(">", ""),
                "Running since": f"{elapsed}s",
            },
            indent=8,
        )
    return text


@app2.on_message(
    SUDOERS
    & ~filters.forwarded
    & ~filters.via_bot
    & filters.command("lsTasks", prefixes=USERBOT_PREFIX)
)
async def task_list(_, message: Message):
    if message.from_user.is_self:
        await message.delete()

    results = await app2.get_inline_bot_results(
        BOT_ID,
        "tasks",
    )
    await app2.send_inline_bot_result(
        message.chat.id,
        results.query_id,
        results.results[0].id,
        hide_via=True,
    )
