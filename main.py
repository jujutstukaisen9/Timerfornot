import os
import time
from datetime import datetime, timedelta
from pyrogram import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Create a Pyrogram Client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Function to send message to the channel
def send_message():
    with app:
        app.send_message(CHANNEL_ID, "This is a scheduled message every 2 hours!")

# Function to calculate the next scheduled time
def get_next_run_time():
    now = datetime.now()
    next_run = now + timedelta(hours=2)
    next_run = next_run.replace(minute=0, second=0, microsecond=0)
    return next_run

if __name__ == "__main__":
    next_run_time = get_next_run_time()
    
    while True:
        current_time = datetime.now()
        if current_time >= next_run_time:
            send_message()
            next_run_time = get_next_run_time()
        time.sleep(60)  # Check every minute
