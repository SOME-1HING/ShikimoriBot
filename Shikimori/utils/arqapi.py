from aiohttp import ClientSession

from Python_ARQ import ARQ

from Shikimori import ARQ_API_URL, ARQ_API_KEY
from Shikimori import pbot

ARQ_API_URL = "https://arq.hamker.in"

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
session = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

app = pbot

