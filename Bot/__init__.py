import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', 21755892)) #API ID
API_HASH = environ.get('API_HASH', '86e4ee550e25c840f888feb042663545') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '6387970018:AAH92XPk4loqOZ82zfp-oK5fmFgGK7-wYHA') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://1234:1234@cluster0.hvaceqn.mongodb.net/?retryWrites=true&w=majority') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', 6440253535)) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', -1001958343978))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', -1001817757798))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', 2)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
