"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

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

import datetime
from typing import List

import requests
from Shikimori import dispatcher
from Shikimori.vars import TIME_API_KEY
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext


def generate_time(to_find: str, findtype: List[str]) -> str:
    data = requests.get(
        f"https://api.timezonedb.com/v2.1/list-time-zone"
        f"?key={TIME_API_KEY}"
        f"&format=json"
        f"&fields=countryCode,countryName,zoneName,gmtOffset,timestamp,dst",
    ).json()

    for zone in data["zones"]:
        for eachtype in findtype:
            if to_find in zone[eachtype].lower():
                country_name = zone["countryName"]
                country_zone = zone["zoneName"]
                country_code = zone["countryCode"]

                if zone["dst"] == 1:
                    daylight_saving = "Yes"
                else:
                    daylight_saving = "No"

                date_fmt = r"%d-%m-%Y"
                time_fmt = r"%H:%M:%S"
                day_fmt = r"%A"
                gmt_offset = zone["gmtOffset"]
                timestamp = (
                    datetime.datetime.now(
                        datetime.timezone.utc,
                    )
                    + datetime.timedelta(seconds=gmt_offset)
                )
                current_date = timestamp.strftime(date_fmt)
                current_time = timestamp.strftime(time_fmt)
                current_day = timestamp.strftime(day_fmt)

                break

    try:
        result = (
            f"<b>Country:</b> <code>{country_name}</code>\n"
            f"<b>Zone Name:</b> <code>{country_zone}</code>\n"
            f"<b>Country Code:</b> <code>{country_code}</code>\n"
            f"<b>Daylight saving:</b> <code>{daylight_saving}</code>\n"
            f"<b>Day:</b> <code>{current_day}</code>\n"
            f"<b>Current Time:</b> <code>{current_time}</code>\n"
            f"<b>Current Date:</b> <code>{current_date}</code>\n"
            '<b>Timezones:</b> <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">List here</a>'
        )
    except:
        result = None

    return result


def gettime(update: Update, context: CallbackContext):
    message = update.effective_message

    try:
        query = message.text.strip().split(" ", 1)[1]
    except:
        message.reply_text("Provide a country name/abbreviation/timezone to find.")
        return
    send_message = message.reply_text(
        f"Finding timezone info for <b>{query}</b>",
        parse_mode=ParseMode.HTML,
    )

    query_timezone = query.lower()
    if len(query_timezone) == 2:
        result = generate_time(query_timezone, ["countryCode"])
    else:
        result = generate_time(query_timezone, ["zoneName", "countryName"])

    if not result:
        send_message.edit_text(
            f"Timezone info not available for <b>{query}</b>\n"
            '<b>All Timezones:</b> <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">List here</a>',
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )
        return

    send_message.edit_text(
        result,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


TIME_HANDLER = DisableAbleCommandHandler("time", gettime, run_async=True)

dispatcher.add_handler(TIME_HANDLER)

__mod_name__ = "Time ⏰"
__help__ = """
*Time*
 ❍ `/time` : To check time of given timezone
"""

__command_list__ = ["time"]
__handlers__ = [TIME_HANDLER]
