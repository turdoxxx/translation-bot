# Requier Modules 
from pyrogram import Client ,enums
import os 

# Requier Bot Plugins 
from Utils import databesas
# Check DIrs 
if not os.path.exists('./.session'): # sessions Drictore
    os.mkdir('./.session')

if not os.path.exists('./databesas'): # Databesas Dirctory
    os.mkdir('./databesas')

# databesas 
databesas = databesas.Databesas()


# Config Class
class Config:
    API_KEY   : str = "7867069654:AAFh2xtQyTqgsRnnIaDOm4B2dK0SsiXsw34" # Her Bot Token
    API_HASH  : str = "c1a5d9335f001bd966ad9618473f6526" # Her Telegram Api Hash
    API_ID    : int = 12787419 # her Api Id
    SUDO     : int  = 1847435573 # hey Sudo ID 
    CHANNLS  : list = ['radfx2'] # her Bot Channls
    

# Client Start 

app = Client(
    name='./.session/rad', 
    bot_token=Config.API_KEY, 
    api_hash=Config.API_HASH,
    api_id=Config.API_ID, 
    plugins=dict(root='Plugins'),
    parse_mode=enums.ParseMode.DEFAULT
    
)
