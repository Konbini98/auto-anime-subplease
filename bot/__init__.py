import os
import libtorrent as lt
import logging
import time
from pymongo import MongoClient
from pyromod import listen
import asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client

class Config(object):
  BOT_TOKEN = str("5833103468:AAF3bnqY-y8Ld44KGskBO43SocsjUR-DDNE")
  API_ID = int(22681384)
  API_HASH = str("14ae45755537c723aab0564a80d723a9")
  DOWNLOAD_LOCATION = str("bot/downloads/")
  LOG_CHANNEL = "uploadanimechan"
  UPDATES_CHANNEL = "mainanimechan"
  DOWNLOAD_DIR = "downloads/"
  AUTH_USERS = [5840630594]
  BOT_USERNAME = "AutoAnimeV4Bot"
  SESSION_STRING = ""
  DATABASE_URL = 'mongodb+srv://autoani:autoani@autoanime.x7uprzw.mongodb.net/?retryWrites=true&w=majority'
  
cluster = MongoClient(Config.DATABASE_URL)
db = cluster[Config.BOT_USERNAME]
collection = db["data"]
queue = db["queue"]
channels = db["channels"]
  
LOG_FILE_NAME = f"BOT@Log.txt"

if os.path.exists(LOG_FILE_NAME):
    with open(LOG_FILE_NAME, "r+") as f_d:
        f_d.truncate(0)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=2097152000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
LOGS = logging.getLogger(__name__)  

bot = Client("Airing", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

if not Config.DOWNLOAD_DIR.endswith("/"):
  Config.DOWNLOAD_DIR = str() + "/"
if not os.path.isdir(Config.DOWNLOAD_DIR):
  os.makedirs(Config.DOWNLOAD_DIR)
  
os.makedirs('torrent/')  
ses = lt.session()
ses.listen_on(6881, 6891)
