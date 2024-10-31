import asyncio
from datetime import datetime, time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from pyrogram import Client, filters
from tzlocal import get_localzone

# Set up bot with your own credentials
api_id = "3847632"
api_hash = "1a9708f807ddd06b10337f2091c67657"
bot_token = "6433673225:AAHnxVRkTnps4z_KbdClWdyFETR9dlCCRpM"

# Set your channel username or ID (format like -1001234567890 for private channels)
channel_id = "-1001835361439‎"

# Define time zone (IST - Indian Standard Time)
time_zone = "Asia/Kolkata"

app = Client("alarm_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Initialize scheduler
scheduler = AsyncIOScheduler(timezone=time_zone)


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("Hello! I will send alarms to the designated channel at specified times.")


# Alarm message sending function
async def send_alarm_message():
    await app.send_message(channel_id, "⏰ This is a scheduled alarm message!")


def schedule_alarms():
    # Set up all specified times for IST
    for hour in range(0, 24, 2):
        # Scheduling alarms at specified hours in IST
        scheduler.add_job(
            send_alarm_message,
            trigger=CronTrigger(hour=hour, minute=0, timezone=time_zone)
        )


# Starting the scheduler when bot starts
@app.on_startup
async def startup_scheduler():
    schedule_alarms()
    scheduler.start()
    print("Scheduler started, alarms set for every 2 hours in IST.")


# Running the bot
app.run()
