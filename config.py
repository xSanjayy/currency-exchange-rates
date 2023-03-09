from pathlib import Path
from dotenv import load_dotenv
import os

class Config:
    if Path('.env').exists():
        load_dotenv()
        BOT_TOKEN = os.getenv('bot_token', "")
    else:
        BOT_TOKEN = "" # Enter your bot token here.