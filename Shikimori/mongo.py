import asyncio
import sys
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Shikimori import MONGO_DB_URI
from Shikimori.confing import get_int_key, get_str_key
from Shikimori.utils.logger import log

MONGO_PORT = get_int_key("27017")
MONGO_DB_URI = get_str_key("MONGO_URI")
MONGO_DB = "DaisyX"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["senkurobot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    print(log.critical("Can't connect to mongodb! Exiting..."))
