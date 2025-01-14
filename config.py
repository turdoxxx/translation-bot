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
    API_KEY   : str = "<API_KEY>" # Her Bot Token
    API_HASH  : str = "abcdf1223455" # Her Telegram Api Hash
    API_ID    : int = 1234567 # her Api Id
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