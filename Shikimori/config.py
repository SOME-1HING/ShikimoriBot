# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

from Shikimori import HEROKU_API_KEY, HEROKU_APP_NAME, REDIS_URL, SS_TOKEN, SS_USERNAME


def get_user_list(config, key):
    with open("{}/Senku/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 123456  # integer value, dont use ""
    API_HASH = "awoo"
    TOKEN = "BOT_TOKEN"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1606221784  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "SOME1HING"
    SUPPORT_CHAT = "tyranteyeeee"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001432609692
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001150905176
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    SS_TOKEN = (
        "awoo"  # Required for taking screenshot. Get your's from https://nocodeapi.com/docs/screenshot-api
    )
    SS_USERNAME = (
        "awoo"  # Required for taking screenshot. Get your's from https://nocodeapi.com/docs/screenshot-api
    )
    MESSAGE_DUMP = -1001501815938  # needed to make sure 'save from' messages persist
    MAINDEV_ID = 2088106582  # The main dev that is responsible for fixing heroku vars. If owners is only going to set vars, Paste Owner ID here
    HEROKU_API_KEY = 2088106582  # Your Heroku API key, get it from 'https://dashboard.heroku.com/account
    HEROKU_APP_NAME = (
        "awoo"  # Enter the Heroku app name here (Must an exact same name with your input above)
    )
    ARQ_API = "awoo"
    APOD_API_KEY = "awoo"
    REDIS_URL = "awoo"
    ANIME_NAME = "Shikimori's Not Just a Cutie"
    START_MEDIA = "https://telegra.ph/file/9235d57807362b4e227a3.mp4"
    BOT_USERNAME = "micchon_shikimori_bot"
    UPDATE_CHANNEL = "Shikimori_bot_Updates"
    ALIVE_MEDIA = "https://telegra.ph/file/2b04f7812f22b983f8a10.mp4"
    BOT_ID = 5169508699
    STATS_IMG = "awoo"
    NETWORK_USERNAME = "VoidxNetwork"
    NETWORK = "【V๏ɪ፝֟𝔡】»Network«"
    MEDIA_GM = "https://telegra.ph/file/fff37608fa21d9d3d0b39.jpg"
    MEDIA_GN = "https://telegra.ph/file/1862c7260109e24ed4715.jpg"
    MEDIA_HELLO = "https://telegra.ph/file/f3f2dc386a33e37f6cb05.png"
    MEDIA_BYE = "https://telegra.ph/file/061054c8f73fe7ffbf6aa.mp4"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
