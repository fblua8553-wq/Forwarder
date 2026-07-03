import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# কনফিগারেশন
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
session_str = os.environ.get('SESSION_STRING')
target_name = os.environ.get('TARGET_NAME') # এখানে আপনার টার্গেট ইউজারনেম বা চ্যাটের নাম লিখুন

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    chat = await event.get_chat()
    
    # বট থেকে মেসেজ চেক করা
    if getattr(chat, 'username', None) == 'Testalifxfyr74_bot':
        msg = event.raw_text
        new_msg = msg.replace('@Axit_dev & @MeNoFace', '@Anonymous_XZ & @WW_Owner')
        
        # সব চ্যাট স্ক্যান করে টার্গেট খুঁজে নেওয়া
        async for dialog in client.iter_dialogs():
            if dialog.name == target_name or dialog.entity.username == target_name.replace('@', ''):
                await client.send_message(dialog.id, new_msg)
                print(f"সফলভাবে {target_name}-এ মেসেজ পাঠানো হয়েছে।")
                return

print("Bot is running...")
client.start()
client.run_until_disconnected()
