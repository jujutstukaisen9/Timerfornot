import asyncio
import datetime
from pyrogram import Client

# Replace these with your actual values
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
CHANNEL_ID = "YOUR_CHANNEL_ID"  # e.g., -1001234567890 or @your_channel_username

# Create a Pyrogram Client
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

async def send_message():
    while True:
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))  # IST
        # Send message every 2 hours
        if now.minute == 0:
            await app.send_message(CHANNEL_ID, "This is a scheduled message.")
        
        # Wait for 60 seconds before checking again
        await asyncio.sleep(60)

async def main():
    async with app:
        await send_message()

if __name__ == "__main__":
    asyncio.run(main())
