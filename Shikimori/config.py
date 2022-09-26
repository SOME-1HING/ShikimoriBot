# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

def get_user_list(config, key):
    with open("{}/Shikimori/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):

    BOT_TOKEN = "5420636798:AAFER5x9yRdK8oYRqSVCHF1c9tdLkrt_CEs" # Your bot token. Get one from @BotFather duh
    API_ID = 10604413 # Get API_ID from my.telegram.org, used for telethon based modules.
    API_HASH = "436125698b225fa2fa1d662717c7283f" # Get API_HASH from my.telegram.org, used for telethon based modules.
    OWNER_ID = 886906981 # Your user ID as an integer.
    OWNER_USERNAME = "Aug0felix" # Your username, witthout @.
    BOT_USERNAME = "Riasxprobot" # Username of your bot without the @
    BOT_ID = 5420636798 # to get your bot_id using other bot or userbot
    SUPPORT_CHAT = "riasxprobotsupport" # Your Telegram support group chat username where your users will go and bother you. 
    MONGO_DB_URI = "mongodb+srv://sukuna:sukuna@sukuna.vipbn9a.mongodb.net/?retryWrites=true&w=majority" # Required for database connections.
    LOG_CHANNEL = -1001387369837 # Event logs channel to note down important bot level events, recommend to make this public. ex: '-123456'
    CASH_API_KEY = "hmm" # Required for currency converter. Get yours from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = "hmm" # Required for timezone information. Get yours from https://timezonedb.com/api
    API_WEATHER = "hmm" # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    DATABASE_URL = "postgresql://rwfyrnwp:FhUHv-L_YsdP8HsxcdVsa_Jxhk_AgPsL@ruby.db.elephantsql.com/rwfyrnwp" # Put sql based database link. Recommended to use Elephant SQL.
    FUNC_DB_URL = "postgresql://jjcsdkwx:h8DmIhk_WlCSVUn6iebybPV8VB79Vkt6@suleiman.db.elephantsql.com/jjcsdkwx" # Put sql based database link. Recommended to use Elephant SQL. MUST BE DIFFERENT THAN DATABSE_URL
    ARQ_API = "KOLCYM-IRNQFC-UWCOKJ-BYJZVB-ARQ" # Get this from @ARQRobot.
    WALL_API = "hmm" # Required for wallpaper. Get your's from https://wall.alphacoders.com/ by writting a email to them.
    ERROR_LOG_CHANNEL = -1001387369837 # Event logs channel to note down important bot level events, recommend to make this public. ex: '-123456'
    REDIS_URL = "redis://Augstun:AUGSTUN_1924bot@redis-19250.c12.us-east-1-4.ec2.cloud.redislabs.com:19250/Augstun-free-db" # Paste your redis url in format redis://<username of admin role>:<password of admin role>@<endoint url>/<database name>
    ANIME_NAME = "High School DxD" # If your bot is based on some anime, type the name of anime. Otherwise, manually edit PM_START_TEXT in start.py
    START_MEDIA = "https://telegra.ph/file/7a8d43abca0f6b215978d.mp4" # Paste link of your media(img, video or gif) that you want to show in /start. Otherwise put None.
    UPDATE_CHANNEL = "riasxprobotupdates" # Leave it as it is, or if you have your own update channel, put channel username without @.
    APOD_API_KEY = "hmm" # Get yours from https://api.nasa.gov/ to get NASA's picture of the day.
    ALIVE_MEDIA = "https://te.legra.ph/file/d58aa2637c4bfcaceb393.mp4" # Paste link of your media(img, video or gif) that you want to show in /alive. Otherwise put None.
    AI_API_KEY = "SOME1HING_privet_990022" # AI API key, get from @tyranteyeeee.
    STATS_IMG = "https://telegra.ph/file/545d005429aecdeec7388.jpg" # Paste image link for /stats. Otherwise keep it blank.
    NETWORK = "【V๏ɪ፝֟𝔡】»Network«" # If your bot is connected to a network, Type the Network name. Only type one Network name. Otherwise leave it blank, or just leave【V๏ɪ፝֟𝔡】»Network«
    NETWORK_USERNAME = "VoidxNetwork" # If you have put a netowrk name, you also have to put its username without @
    OWNER_WELCOME_MEDIA = "hmm" # URL of media that you want to show when owner of bot joins any chat. Supported file types (jpg, png, gif, webp, mkv, mp4)
    INLINE_IMG = "https://telegra.ph/file/8cec66d01df8c0071ebaa.jpg" # URL of image for inline querry. Must be a still image.

    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = "hmm"
    HEROKU_API_KEY = "hmm"
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    LOGGER = True
    LOAD = []
    NO_LOAD = []
    DEL_CMDS = True
    BAN_STICKER = []
    WEBHOOK = False
    URL = None
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
    CERT_PATH = None
    PORT = 5000
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
