import os
import random
from time import sleep
from telethon import events
from telethon import TelegramClient
APP_ID  = input("[~] Enter APP ID :")
API_HASH = input("[~] Enter API HASH :")
topac = TelegramClient("session", APP_ID, API_HASH)
topac.start()
@topac.on(events.NewMessage(outgoing=True, pattern=r".فويز"))
async def iqvois(vois):
  await vois.edit("جار البحث")
  sleep(1)
  tt = random.randint(1,2314)
  url = f"https://t.me/AC2AA/{tt}"
  await vois.client.send_file(vois.chat_id,url,caption="- @iiit5",parse_mode="html")
  await vois.delete()

topac.run_until_disconnected()
