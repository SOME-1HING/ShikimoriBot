import nekos
from Shikimori import dispatcher
from telegram.ext import CommandHandler

url_sfw = "https://api.waifu.pics/sfw/" 

def waifu(update, context):
    msg = update.effective_message
    img = f"{url_sfw}blowjob"
    msg.reply_photo(photo=img)

def neko(update, context):
    msg = update.effective_message
    img = f"{url_sfw}neko"
    msg.reply_photo(photo=img)

def shinobu(update, context):
    msg = update.effective_message
    img = f"{url_sfw}shinobu"
    msg.reply_photo(photo=img)

def megumin(update, context):
    msg = update.effective_message
    img = f"{url_sfw}megumin"
    msg.reply_photo(photo=img)

def bully(update, context):
    msg = update.effective_message
    img = f"{url_sfw}bully"
    msg.reply_animation(photo=img)

def cuddle(update, context):
    msg = update.effective_message
    img = f"{url_sfw}cuddle"
    msg.reply_animation(photo=img)

def cry(update, context):
    msg = update.effective_message
    img = f"{url_sfw}cry"
    msg.reply_animation(photo=img)

def hug(update, context):
    msg = update.effective_message
    img = f"{url_sfw}hug"
    msg.reply_animation(photo=img)

def awoo(update, context):
    msg = update.effective_message
    img = f"{url_sfw}awoo"
    msg.reply_animation(photo=img)

def kiss(update, context):
    msg = update.effective_message
    img = f"{url_sfw}kiss"
    msg.reply_animation(photo=img)

def lick(update, context):
    msg = update.effective_message
    img = f"{url_sfw}lick"
    msg.reply_animation(photo=img)

def pat(update, context):
    msg = update.effective_message
    img = f"{url_sfw}pat"
    msg.reply_animation(photo=img)

def smug(update, context):
    msg = update.effective_message
    img = f"{url_sfw}smug"
    msg.reply_animation(photo=img)

def bonk(update, context):
    msg = update.effective_message
    img = f"{url_sfw}bonk"
    msg.reply_animation(video=img)

def yeet(update, context):
    msg = update.effective_message
    img = f"{url_sfw}yeet"
    msg.reply_animation(video=img)

def blush(update, context):
    msg = update.effective_message
    img = f"{url_sfw}blush"
    msg.reply_animation(video=img)

def smile(update, context):
    msg = update.effective_message
    img = f"{url_sfw}smile"
    msg.reply_animation(video=img)

def wave(update, context):
    msg = update.effective_message
    img = f"{url_sfw}wave"
    msg.reply_animation(video=img)

def highfive(update, context):
    msg = update.effective_message
    img = f"{url_sfw}highfive"
    msg.reply_animation(video=img)

def handhold(update, context):
    msg = update.effective_message
    img = f"{url_sfw}handhold"
    msg.reply_animation(video=img)

def nom(update, context):
    msg = update.effective_message
    img = f"{url_sfw}nom"
    msg.reply_animation(video=img)

def bite(update, context):
    msg = update.effective_message
    img = f"{url_sfw}bite"
    msg.reply_animation(video=img)


def glomp(update, context):
    msg = update.effective_message
    img = f"{url_sfw}glomp"
    msg.reply_animation(video=img)

def slap(update, context):
    msg = update.effective_message
    img = f"{url_sfw}slap"
    msg.reply_animation(video=img)

def killgif(update, context):
    msg = update.effective_message
    img = f"{url_sfw}kill"
    msg.reply_animation(video=img)

def kickgif(update, context):
    msg = update.effective_message
    img = f"{url_sfw}kick"
    msg.reply_animation(video=img)

def happy(update, context):
    msg = update.effective_message
    img = f"{url_sfw}happy"
    msg.reply_animation(video=img)

def wink(update, context):
    msg = update.effective_message
    img = f"{url_sfw}wink"
    msg.reply_animation(video=img)

def poke(update, context):
    msg = update.effective_message
    img = f"{url_sfw}poke"
    msg.reply_animation(video=img)

def dance(update, context):
    msg = update.effective_message
    img = f"{url_sfw}dance"
    msg.reply_animation(video=img)

def cringe(update, context):
    msg = update.effective_message
    img = f"{url_sfw}cringe"
    msg.reply_animation(video=img)

################
def wallpaper(update, context):
    msg = update.effective_message
    target = "wallpaper"
    msg.reply_photo(nekos.img(target))

def tickle(update, context):
    msg = update.effective_message
    target = "tickle"
    msg.reply_video(nekos.img(target))

def ngif(update, context):
    msg = update.effective_message
    target = "ngif"
    msg.reply_video(nekos.img(target))

def feed(update, context):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))

def gasm(update, context):
    msg = update.effective_message
    target = "gasm"
    msg.reply_photo(nekos.img(target))

def avatar(update, context):
     msg = update.effective_message
     target = "avatar"
     msg.reply_photo(nekos.img(target))


def foxgirl(update, context):
    msg = update.effective_message
    target = "fox_girl"
    msg.reply_photo(nekos.img(target))

def gecg(update, context):
    msg = update.effective_message
    target = "gecg"
    msg.reply_photo(nekos.img(target))

def lizard(update, context):
    msg = update.effective_message
    target = "lizard"
    msg.reply_photo(nekos.img(target))

def spank(update, context):
    msg = update.effective_message
    target = "spank"
    msg.reply_video(nekos.img(target))    

def goose(update, context):
    msg = update.effective_message
    target = "goose"
    msg.reply_photo(nekos.img(target))

def woof(update, context):
    msg = update.effective_message
    target = "woof"
    msg.reply_photo(nekos.img(target))       

WALLPAPER_HANDLER = CommandHandler("wallpaper", wallpaper, run_async=True)
TICKLE_HANDLER = CommandHandler("tickle", tickle, run_async=True)
FEED_HANDLER = CommandHandler("feed", feed, run_async=True)
GASM_HANDLER = CommandHandler("gasm", gasm, run_async=True)
AVATAR_HANDLER = CommandHandler("avatar", avatar, run_async=True)
FOXGIRL_HANDLER = CommandHandler("foxgirl", foxgirl, run_async=True)
GECG_HANDLER = CommandHandler("gecg", gecg, run_async=True)
LIZARD_HANDLER = CommandHandler("lizard", lizard, run_async=True)
GOOSE_HANDLER = CommandHandler("goose", goose, run_async=True)
WOOF_HANDLER = CommandHandler("woof", woof, run_async=True)
NGIF_HANDLER = CommandHandler("ngif", ngif, run_async=True)

WAIFUS_HANDLER = CommandHandler("waifus", waifu, run_async=True)
NEKO_HANDLER = CommandHandler("neko", neko, run_async=True)
SHINOBU_HANDLER = CommandHandler("shinobu", shinobu, run_async=True)
MEGUMIN_HANDLER = CommandHandler("megumin", megumin, run_async=True)
BULLY_HANDLER = CommandHandler("bully", bully, run_async=True)
CUDDLE_HANDLER = CommandHandler("cuddle", foxgirl, run_async=True)
CRY_HANDLER = CommandHandler("cry", cry, run_async=True)
HUG_HANDLER = CommandHandler("hug", hug, run_async=True)
AWOO_HANDLER = CommandHandler("awoo", awoo, run_async=True)
KISS_HANDLER = CommandHandler("kiss", kiss, run_async=True)
LICK_HANDLER = CommandHandler("lick", lick, run_async=True)
PAT_HANDLER = CommandHandler("pat", pat, run_async=True)





SMUG_HANDLER = CommandHandler("smug", smug, run_async=True)
BONK_HANDLER = CommandHandler("bonk", bonk, run_async=True)
YEET_HANDLER = CommandHandler("yeet", yeet, run_async=True)
BLUSH_HANDLER = CommandHandler("blush", blush, run_async=True)
SMILE_HANDLER = CommandHandler("smile", smile, run_async=True)
WAVE_HANDLER = CommandHandler("wave", wave, run_async=True)
HIGHFIVE_HANDLER = CommandHandler("highfive", highfive, run_async=True)
HANDHOLD_HANDLER = CommandHandler("handhold", handhold, run_async=True)
NOM_HANDLER = CommandHandler("nom", nom, run_async=True)
BITE_HANDLER = CommandHandler("bite", bite, run_async=True)
GLOMP_HANDLER = CommandHandler("glomp", glomp, run_async=True)


SLAP_HANDLER = CommandHandler("slap", slap, run_async=True)
KILLGIF_HANDLER = CommandHandler("killgif", killgif, run_async=True)
HAPPY_HANDLER = CommandHandler("happy", happy, run_async=True)
WINK_HANDLER = CommandHandler("wink", wink, run_async=True)
POKE_HANDLER = CommandHandler("poke", poke, run_async=True)
DANCE_HANDLER = CommandHandler("dance", dance, run_async=True)
CRINGE_HANDLER = CommandHandler("cringe", cringe, run_async=True)



dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(KILLGIF_HANDLER)
dispatcher.add_handler(HAPPY_HANDLER)
dispatcher.add_handler(WINK_HANDLER)
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(DANCE_HANDLER)
dispatcher.add_handler(CRINGE_HANDLER)


dispatcher.add_handler(SMUG_HANDLER)
dispatcher.add_handler(BONK_HANDLER)
dispatcher.add_handler(YEET_HANDLER)
dispatcher.add_handler(BLUSH_HANDLER)
dispatcher.add_handler(SMILE_HANDLER)
dispatcher.add_handler(WAVE_HANDLER)
dispatcher.add_handler(HIGHFIVE_HANDLER)
dispatcher.add_handler(HANDHOLD_HANDLER)
dispatcher.add_handler(NOM_HANDLER)
dispatcher.add_handler(BITE_HANDLER)
dispatcher.add_handler(GLOMP_HANDLER)




dispatcher.add_handler(AWOO_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(KISS_HANDLER)
dispatcher.add_handler(LICK_HANDLER)
dispatcher.add_handler(CRY_HANDLER)
dispatcher.add_handler(HUG_HANDLER)
dispatcher.add_handler(WAIFUS_HANDLER)
dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(SHINOBU_HANDLER)
dispatcher.add_handler(MEGUMIN_HANDLER)
dispatcher.add_handler(BULLY_HANDLER)
dispatcher.add_handler(CUDDLE_HANDLER)

dispatcher.add_handler(LIZARD_HANDLER)
dispatcher.add_handler(NGIF_HANDLER)
dispatcher.add_handler(GOOSE_HANDLER)
dispatcher.add_handler(WOOF_HANDLER)
dispatcher.add_handler(GECG_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(GASM_HANDLER)
dispatcher.add_handler(AVATAR_HANDLER)
dispatcher.add_handler(FOXGIRL_HANDLER)

__handlers__ = [
    SLAP_HANDLER,
    LIZARD_HANDLER,
    GOOSE_HANDLER,
    WOOF_HANDLER,
    WALLPAPER_HANDLER,
    TICKLE_HANDLER,
    FEED_HANDLER,
    GASM_HANDLER,
    AVATAR_HANDLER,
    GECG_HANDLER,
    FOXGIRL_HANDLER,
]



__mod_name__ = "SFW"
__help__ = """
*Commands* *:*  
   ➢ `/neko`*:*Sends Random SFW Neko source Images.
   ➢ `/ngif`*:*Sends Random Neko GIFs.
   ➢ `/tickle`*:*Sends Random Tickle GIFs.
   ➢ `/feed`*:*Sends Random Feeding GIFs.
   ➢ `/gasm`*:*Sends Random Orgasm Stickers.
   ➢ `/avatar`*:*Sends Random Avatar Stickers.
   ➢ `/waifus`*:* Sends Random Waifu Stickers.
   ➢ `/kiss`*:* Sends Random Kissing GIFs.
   ➢ `/cuddle`*:* Sends Random Cuddle GIFs.
   ➢ `/foxgirl`*:* Sends Random FoxGirl source Images.
   ➢ `/smug`*:* Sends Random Smug GIFs.
   ➢ `/gecg`*:* IDK
   ➢ `/slap`*:* Sends Random Slap GIFs.

*Some more SFW commands :*
   ➢ `/shinobu`
   ➢ `/megumin`
   ➢ `/bully`
   ➢ `/cry`
   ➢ `/awoo`
   ➢ `/lick`
   ➢ `/pat`
   ➢ `/bonk`
   ➢ `/yeet`
   ➢ `/blush`
   ➢ `/smile`
   ➢ `/wave`
   ➢ `/highfive`
   ➢ `/handhold`
   ➢ `/nom`
   ➢ `/bite`
   ➢ `/glomp`
   ➢ `/slapgif`
   ➢ `/kill`
   ➢ `/kick`
   ➢ `/happy`
   ➢ `/wink`
   ➢ `/poke`
   ➢ `/dance`
   ➢ `/cringe`
"""

