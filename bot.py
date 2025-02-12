import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import praw
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent='telegram_bot_script'
)

async def fetch_and_send_photos():
    subreddit = reddit.subreddit('RealGirls')
    for submission in subreddit.new(limit=10):
        if submission.url.endswith(('.jpg', '.jpeg', '.png')):
            await bot.send_photo(chat_id='https://t.me/+GQzREOcwT6IzMjU6', photo=submission.url)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Бот запущен и будет публиковать новые фотографии из r/RealGirls.")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(fetch_and_send_photos())
    executor.start_polling(dp, skip_updates=True)
