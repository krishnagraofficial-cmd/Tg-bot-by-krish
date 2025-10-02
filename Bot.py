from telethon import TelegramClient, events
import os

# Load from environment variables (we will add these in Render)
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

source_chat_id = int(os.getenv("SOURCE_CHAT_ID"))
target_chat_id = int(os.getenv("TARGET_CHAT_ID"))

# Start bot client
client = TelegramClient('forwardbot', api_id, api_hash).start(bot_token=bot_token)

# Event handler: When a new message arrives in source chat, forward it
@client.on(events.NewMessage(chats=source_chat_id))
async def handler(event):
    await client.forward_messages(target_chat_id, event.message)

print("🚀 Bot is running...")
client.run_until_disconnected()
