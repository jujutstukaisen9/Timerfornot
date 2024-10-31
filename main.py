import asyncio
from datetime import datetime, timedelta
from pyrogram import Client

# Replace these with your own values
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "YOUR_CHANNEL_ID"  # e.g., -1001234567890

# Create a Pyrogram Client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def send_message():
    async with app:
        while True:
            now = datetime.now()
            # Check if the current time is in IST
            if now.hour % 2 == 0 and now.minute == 0:  # Every 2 hours at the start of the hour
                await app.send_message(CHANNEL_ID, "This is a scheduled message sent every 2 hours!")
                await asyncio.sleep(60 * 60)  # Sleep for an hour to avoid multiple messages
            await asyncio.sleep(60)  # Check every minute

if __name__ == "__main__":
    asyncio.run(send_message())
