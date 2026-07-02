from telethon import TelegramClient, events
import re

# আপনার ডিটেইলস বসান
api_id = '35062802'
api_hash = '8ea88b1b1320503d5b343edaf7969a11'
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats='-1004414373197'))
async def handler(event):
    message = event.raw_text
    # বডি অংশ আলাদা করার Regex লজিক
    match = re.search(r'Body:\n(.*?)\n\n', message, re.DOTALL)
    if match:
        clean_body = match.group(1).strip()
        # এখানে আপনার টার্গেট আইডি বসান
        await client.send_message('6147968753', clean_body)

client.start()
client.run_until_disconnected()
