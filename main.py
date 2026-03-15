import os
import asyncio
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "0"))
api_hash = os.getenv("API_HASH", "")
phone_number = os.getenv("PHONE_NUMBER", "")
channel_id = int(os.getenv("CHANNEL_ID", "0"))

client = TelegramClient("session_name", api_id, api_hash)

files = [
    "photo_2026-01-25_00-15-35.jpg",
    "merge_two_images_into_one_seamless_ultra-realistic_cinematic_8k_photograph_take_the_cat_from_the_fi_3qn58jy9gj5mrfncuyws_3.png",
    "ChatGPT Image Jan 16, 2026, 09_30_35 PM.png",
]


async def main():
    await client.start(phone=phone_number)
    print("Yuborish boshlandi...")
    while True:
        for file in files:
            if os.path.exists(file):
                await client.send_file(channel_id, file)
                print(f"{file} yuborildi")
            else:
                print(f"{file} topilmadi")
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())

