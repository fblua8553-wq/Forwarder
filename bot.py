import os
import re
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ভেরিয়েবলগুলো এনভায়রনমেন্ট থেকে সরাসরি নিন
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
session_str = os.environ.get('SESSION_STRING')
target_id = os.environ.get('TARGET_ID') # এটি আপনার টার্গেট আইডি

# ক্লায়েন্ট ইনিশিয়ালাইজ করুন
client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(chats='Testalifxfyr74_bot'))
async def handler(event):
    msg = event.raw_text
    match = re.search(r'Body:\n(.*?)\n.*Date/Time:', msg, re.DOTALL)
    
    if match:
        extracted_body = match.group(1).strip()
        # সরাসরি মেসেজ পাঠান
        await client.send_message(target_id, extracted_body)

print("Bot is running...")
client.start()
client.run_until_disconnected()
