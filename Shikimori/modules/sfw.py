import nekos
from Shikimori import dispatcher
from telegram.ext import CommandHandler


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

def slap(update, context):
    msg = update.effective_message
    target = "slap"
    msg.reply_video(nekos.img(target))

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
SLAP_HANDLER = CommandHandler("slap", slap, run_async=True)
LIZARD_HANDLER = CommandHandler("lizard", lizard, run_async=True)
SPANK_HANDLER = CommandHandler("spank", spank, run_async=True)
GOOSE_HANDLER = CommandHandler("goose", goose, run_async=True)
WOOF_HANDLER = CommandHandler("woof", woof, run_async=True)
NGIF_HANDLER = CommandHandler("ngif", ngif, run_async=True)

dispatcher.add_handler(LIZARD_HANDLER)
dispatcher.add_handler(NGIF_HANDLER)
dispatcher.add_handler(GOOSE_HANDLER)
dispatcher.add_handler(WOOF_HANDLER)
dispatcher.add_handler(SPANK_HANDLER)
dispatcher.add_handler(GECG_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
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
    SPANK_HANDLER,
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
   ➢ `/cringe
"""

