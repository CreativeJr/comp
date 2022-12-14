from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default="4926633", cast=int)
API_HASH = config("API_HASH", default="be7b1d39ac5116d22701f8b6ac956785")
BOT_TOKEN = config("BOT_TOKEN", default="5202925982:AAGn_FROGTtB9hdsjtzA6IHNC4uDMigHpOw")
BOT_UN = config("BOT_UN", default="@Privatecompressor_bot")
AUTH_USERS = config("AUTH_USERS", default="1022568191", cast=int)
LOG_CHANNEL = config("LOG_CHANNEL", default="@vidcom")
LOG_ID = config("LOG_ID", default="-1001887884003")
FORCESUB = config("FORCESUB", default=None)
FORCESUB_UN = config("FORCESUB_UN", default=None)
ACCESS_CHANNEL = config("ACCESS_CHANNEL", default=None)
MONGODB_URI = config("MONGODB_URI", default="mongodb+srv://unzipper:unzipper@cluster0.fc8uopr.mongodb.net/?retryWrites=true&w=majority")

Drone = TelegramClient('bot', 4926633, "be7b1d39ac5116d22701f8b6ac956785").start(bot_token="5202925982:AAGn_FROGTtB9hdsjtzA6IHNC4uDMigHpOw") 
