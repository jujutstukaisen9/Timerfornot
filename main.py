import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from pyrogram import Client, filters, idle
from tzlocal import get_localzone

# Telegram Bot Credentials
api_id = "3847632"
api_hash = "1a9708f807ddd06b10337f2091c67657"
bot_token = "6433673225:AAHnxVRkTnps4z_KbdClWdyFETR9dlCCRpM"
channel_id = "-1001835361439"
time_zone = "Asia/Kolkata"
app = Client("alarm_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
scheduler = AsyncIOScheduler(timezone=time_zone)

@app.on_message(filters.command("test") & filters.private)
async def test_message(client, message):
    await app.send_message(channel_id, "Test message to channel.")

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("Hello! I will send alarms to the designated channel at specified times.")

# Function to send scheduled alarm messages
async def send_alarm_message():
    try:
        await app.send_message(channel_id, "⏰ This is a scheduled alarm message!")
    except PeerIdInvalid:
        print(f"Error: The channel ID {channel_id} is invalid or the bot has not been added to the channel.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to schedule alarms every 2 hours
def schedule_alarms():
    for hour in range(0, 24, 2):  # Runs at 00:00, 02:00, 04:00, etc.
        scheduler.add_job(
            send_alarm_message,
            trigger=CronTrigger(hour=hour, minute=0, timezone=time_zone)
        )

# Main function to start the bot and initialize the scheduler
async def main():
    await app.start()  # Start the bot
    print("Bot started")
    schedule_alarms()  # Schedule the alarms
    scheduler.start()  # Start the scheduler

    # Keep the bot running
    await idle()
    await app.stop()  # Stop the bot when idle stops

# Run the main function within an asyncio event loop
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
