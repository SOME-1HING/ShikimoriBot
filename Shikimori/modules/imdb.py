    
import requests
from bs4 import BeautifulSoup
import re
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Shikimori import SUPPORT_CHAT, pbot
from Shikimori.Extras.errors import capture_err



@pbot.on_message(filters.command("imdb"))
@capture_err
async def imdb(_, message):
    movie_name = message.text.split(None, 1)[1]
    remove_space = movie_name.split(" ")
    final_name = "+".join(remove_space)
    page = requests.get(
        "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + final_name + "&s=all"
    )
    str(page.status_code)
    soup = BeautifulSoup(page.content, "lxml")
    odds = soup.findAll("tr", "odd")
    mov_title = odds[0].findNext("td").findNext("td").text
    mov_link = (
        "http://www.imdb.com/" + odds[0].findNext("td").findNext("td").a["href"]
    )
    page1 = requests.get(mov_link)
    soup = BeautifulSoup(page1.content, "lxml")
    if soup.find("div", "poster"):
        poster = soup.find("div", "poster").img["src"]
    else:
        poster = ""
    if soup.find("div", "title_wrapper"):
        pg = soup.find("div", "title_wrapper").findNext("div").text
        mov_details = re.sub(r"\s+", " ", pg)
    else:
        mov_details = ""
    credits = soup.findAll("div", "credit_summary_item")
    director = credits[0].a.text
    if len(credits) == 1:
        writer = "Not available"
        stars = "Not available"
    elif len(credits) > 2:
        writer = credits[1].a.text
        actors = [x.text for x in credits[2].findAll("a")]
        actors.pop()
        stars = actors[0] + "," + actors[1] + "," + actors[2]
    else:
        writer = "Not available"
        actors = []
        for x in credits[1].findAll("a"):
            actors.append(x.text)
        actors.pop()
        stars = actors[0] + "," + actors[1] + "," + actors[2]
    if soup.find("div", "inline canwrap"):
        story_line = soup.find("div", "inline canwrap").findAll("p")[0].text
    else:
        story_line = "Not available"
    info = soup.findAll("div", "txt-block")
    if info:
        mov_country = []
        mov_language = []
        for node in info:
            a = node.findAll("a")
            for i in a:
                if "country_of_origin" in i["href"]:
                    mov_country.append(i.text)
                elif "primary_language" in i["href"]:
                    mov_language.append(i.text)
    if soup.findAll("div", "ratingValue"):
        for r in soup.findAll("div", "ratingValue"):
            mov_rating = r.strong["title"]
    else:
        mov_rating = "Not available"
    lol = f"Movie - {mov_title}\n Click to see more"
    msg = (
        "<a href=" + poster + ">&#8203;</a>"
        "<b>Title : </b><code>"
        + mov_title
        + "</code>\n<code>"
        + mov_details
        + "</code>\n<b>Rating : </b><code>"
        + mov_rating
        + "</code>\n<b>Country : </b><code>"
        + mov_country[0]
        + "</code>\n<b>Language : </b><code>"
        + mov_language[0]
        + "</code>\n<b>Director : </b><code>"
        + director
        + "</code>\n<b>Writer : </b><code>"
        + writer
        + "</code>\n<b>Stars : </b><code>"
        + stars
        + "</code>\n<b>IMDB Url : </b>"
        + mov_link
        + "\n<b>Story Line : </b>"
        + story_line
    )
    
    await message.reply_text(msg)