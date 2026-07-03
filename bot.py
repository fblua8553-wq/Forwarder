import os
import asyncio
import re
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# কনফিগারেশন
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
session_str = os.environ.get('SESSION_STRING')
target_id = int(os.environ.get('TARGET_ID'))
source_bot = 'Testapifefrrhbot'  # সোর্স বট

client = TelegramClient(StringSession(session_str), api_id, api_hash)

# প্রসেস করা মেসেজের আইডি ট্র্যাক করুন (ডুপ্লিকেট এড়াতে)
processed_ids = set()

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # নিজের মেসেজ ইগনোর
    if event.out:
        return
    
    # ডুপ্লিকেট চেক
    if event.id in processed_ids:
        return
    processed_ids.add(event.id)
    
    # মেমরি লিমিট (শেষ ১০০০টি রাখা)
    if len(processed_ids) > 1000:
        processed_ids.clear()
    
    chat = await event.get_chat()
    
    # সোর্স বট চেক
    if getattr(chat, 'username', None) == source_bot:
        msg = event.raw_text
        
        # রিপ্লেসমেন্ট
        new_msg = msg.replace('@Axit_dev & @MeNoFace', '@Anonymous_XZ & @WW_Owner')
        
        # অতিরিক্ত: 'Body:' অংশ এক্সট্রাক্ট (যদি প্রয়োজন)
        body_match = re.search(r'Body:\s*\n(.*?)\n', msg, re.DOTALL)
        if body_match:
            new_msg = body_match.group(1).strip()
        
        # পাঠান
        if new_msg and new_msg != msg:
            try:
                await client.send_message(target_id, new_msg)
                print(f"✅ [{event.date}] মেসেজ ফরওয়ার্ড: {new_msg[:40]}...")
            except Exception as e:
                print(f"❌ এরর: {e}")

async def main():
    await client.start()
    me = await client.get_me()
    print(f"✅ {me.first_name} হিসেবে লগইন সফল!")
    print("🤖 বট চালু আছে, মেসেজের জন্য অপেক্ষা করছে...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
