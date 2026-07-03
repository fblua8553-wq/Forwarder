from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import re

# এনভায়রনমেন্ট ভেরিয়েবল থেকে কনফিগারেশন
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
session_str = os.environ.get('SESSION_STRING')
target_id = os.environ.get('TARGET_ID') # আপনার কাঙ্ক্ষিত আইডি (যেমন: @username বা আইডি নাম্বার)

client = TelegramClient(StringSession(session_str), api_id, api_hash)

# নির্দিষ্ট বটের ইউজারনেম দিয়ে মেসেজ লিসেনিং
@client.on(events.NewMessage(chats='Mypersonal_phone_bot')) 
async def handler(event):
    msg = event.raw_text
    
    # "1000165001_3.jpg" ফরম্যাট অনুযায়ী Body এবং Date/Time এর মাঝের অংশ বের করার Regex লজিক
    match = re.search(r'Body:\n(.*?)\n.*Date/Time:', msg, re.DOTALL)
    
    if match:
        extracted_body = match.group(1).strip()
        
        # মেসেজটি এডিট করে আপনার পছন্দমতো ফরম্যাট করা (যেমন শুধু বডি পাঠানো)
        # যদি অন্য কিছু যোগ করতে চান তবে এখানে করতে পারেন
        await client.send_message(target_id, extracted_body)

client.start()
client.run_until_disconnected()
