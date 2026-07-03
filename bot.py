import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# কনফিগারেশন
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
session_str = os.environ.get('SESSION_STRING')
target_id = os.environ.get('TARGET_ID')

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    chat = await event.get_chat()
    
    # শুধুমাত্র নির্দিষ্ট বট থেকে আসা মেসেজ চেক করা
    if getattr(chat, 'username', None) == 'Testapifefrrhbot':
        msg = event.raw_text
        
        # ডেভেলপার নাম পরিবর্তন করার লজিক
        # পুরাতন টেক্সট: @Axit_dev & @MeNoFace
        # নতুন টেক্সট: @Anonymous_XZ & @WW_Owner
        
        new_msg = msg.replace('@Axit_dev & @MeNoFace', '@Anonymous_XZ & @WW_Owner')
        
        # এডিট করে ফরোয়ার্ড করা
        await client.send_message(target_id, new_msg)
        print("মেসেজ এডিট করে ফরোয়ার্ড করা হয়েছে।")

print("Bot is running...")
client.start()
client.run_until_disconnected()
