from telethon import TelegramClient, events
from telethon.sessions import StringSession 
from requests import post
from dotenv import load_dotenv
import os

load_dotenv()
STRING = os.getenv('STRING')
API_KEY = os.getenv('API_KEY')
API_HASH = os.getenv('API_HASH')
OCR_API_KEY = os.getenv('OCR_KEY')

OCR_URL = 'https://api.api-ninjas.com/v1/imagetotext'
HEADERS = {'X-Api-Key': OCR_API_KEY}

c = TelegramClient(StringSession(STRING), API_KEY, API_HASH)
c.start()

@c.on(events.NewMessage(from_users=[1877720720]))
async def _fastly(e):
 if not e.photo:
    return
 p = await e.download_media('ocr.jpg')
 _req = post(OCR_URL, headers=HEADERS, files={'image': open(p, 'rb')})
 data = _req.json()
 _text = data[0]['text']
 await e.respond(str(_text))
 os.remove('ocr.jpg')
 
c.run_until_disconnected()
