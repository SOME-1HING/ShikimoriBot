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

import flag
from countryinfo import CountryInfo
from Shikimori import dispatcher, telethn as borg
from Shikimori.events import register

bot_name = f"{dispatcher.bot.first_name}"


@register(pattern="^/country (.*)")
async def msg(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    lol = input_str
    country = CountryInfo(lol)
    try:
        a = country.info()
    except:
        await event.reply("Country Not Avaiable Currently")
    name = a.get("name")
    bb = a.get("altSpellings")
    hu = ""
    for p in bb:
        hu += p + ",  "

    area = a.get("area")
    borders = ""
    hell = a.get("borders")
    for fk in hell:
        borders += fk + ",  "

    call = ""
    WhAt = a.get("callingCodes")
    for what in WhAt:
        call += what + "  "

    capital = a.get("capital")
    currencies = ""
    fker = a.get("currencies")
    for FKer in fker:
        currencies += FKer + ",  "

    HmM = a.get("demonym")
    geo = a.get("geoJSON")
    pablo = geo.get("features")
    Pablo = pablo[0]
    PAblo = Pablo.get("geometry")
    EsCoBaR = PAblo.get("type")
    iso = ""
    iSo = a.get("ISO")
    for hitler in iSo:
        po = iSo.get(hitler)
        iso += po + ",  "
    fla = iSo.get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)

    languages = a.get("languages")
    lMAO = ""
    for lmao in languages:
        lMAO += lmao + ",  "

    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tik = a.get("timezones")
    tom = ""
    for jerry in tik:
        tom += jerry + ",   "

    GOT = a.get("tld")
    lanester = ""
    for targaryen in GOT:
        lanester += targaryen + ",   "

    wiki = a.get("wiki")

    caption = f"""<b><u>Information Gathered Successfully</b></u>
<b>
Country Name:- {name}
Alternative Spellings:- {hu}
Country Area:- {area} square kilometers
Borders:- {borders}
Calling Codes:- {call}
Country's Capital:- {capital}
Country's currency:- {currencies}
Country's Flag:- {okie}
Demonym:- {HmM}
Country Type:- {EsCoBaR}
ISO Names:- {iso}
Languages:- {lMAO}
Native Name:- {nonive}
population:- {waste}
Region:- {reg}
Sub Region:- {sub}
Time Zones:- {tom}
Top Level Domain:- {lanester}
wikipedia:- {wiki}</b>

Gathered By {bot_name} ✨.</b>
"""

    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
    )

    await event.delete()
