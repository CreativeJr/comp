from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 4926633)
API_HASH = config("API_HASH", default="be7b1d39ac5116d22701f8b6ac956785")
BOT_TOKEN = config("BOT_TOKEN", default="be7b1d39ac5116d22701f8b6ac956785")
BOT_UN = config("BOT_UN", default="@Privatecompressor_bot")

Drone = TelegramClient('bot', 4926633, "be7b1d39ac5116d22701f8b6ac956785").start(bot_token="be7b1d39ac5116d22701f8b6ac956785") 
