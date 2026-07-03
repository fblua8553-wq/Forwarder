import os
import re
import asyncio
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError

# কনফিগারেশন
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
session_str = os.environ.get('SESSION_STRING')

# target_id .env থেকে string হিসেবে আসে
# যদি এটা numeric chat id হয় (যেমন -100123456789), int এ কনভার্ট করা দরকার
raw_target = os.environ.get('TARGET_ID')
try:
    target_id = int(raw_target)
except (TypeError, ValueError):
    target_id = raw_target  # username হলে string-ই থাকবে (@somechannel)

client = TelegramClient(StringSession(session_str), api_id, api_hash)

SOURCE_BOT_USERNAME = 'Testapifefrrhbot'

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    chat = await event.get_chat()

    # শুধুমাত্র নির্দিষ্ট বট থেকে আসা মেসেজ চেক করা (প্রাইভেট চ্যাট ধরে নিয়ে)
    if getattr(chat, 'username', None) == SOURCE_BOT_USERNAME:
        msg = event.raw_text

        # ডেভেলপার নাম পরিবর্তন (স্পেস/লাইনব্রেক ভেরিয়েশন হ্যান্ডেল করতে regex)
        new_msg = re.sub(
            r'@Axit_dev\s*&\s*@MeNoFace',
            '@Anonymous_XZ & @WW_Owner',
            msg
        )

        try:
            await client.send_message(target_id, new_msg)
            print("মেসেজ এডিট করে ফরোয়ার্ড করা হয়েছে।")
        except FloodWaitError as e:
            print(f"FloodWait: {e.seconds} সেকেন্ড অপেক্ষা করতে হবে।")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"এরর হয়েছে: {e}")

async def main():
    print("Bot is running...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
