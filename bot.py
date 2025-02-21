import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Chat IDs (replace with actual chat IDs)
SOURCE_CHAT = int(os.getenv("SOURCE_CHAT"))
DEST_CHAT = int(os.getenv("DEST_CHAT"))

# Create a Telegram Client
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward_message(event):
    await bot.send_message(DEST_CHAT, event.message)

print("🚀 Bot is running...")

bot.run_until_disconnected()
