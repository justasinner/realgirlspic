import os
import praw
from telegram import Bot
from telegram.ext import Updater, CommandHandler
import time

# Reddit API setup
reddit = praw.Reddit(
    client_id=os.getenv('pfslWzrltzUkPia0QkTYjQ'),
    client_secret=os.getenv('2OEekbm94bNx7kj1fAhBKAEYTeLhRw'),
    user_agent=os.getenv('Brian_Augustine')
)

# Telegram Bot setup
telegram_bot_token = os.getenv('7682959518:AAG1HHJvftnycY36CE2cJsLB--Zisjlbd6o')
chat_id = os.getenv('https://t.me/+GQzREOcwT6IzMjU6')
bot = Bot(token=telegram_bot_token)

def fetch_and_send_photos(context):
    subreddit = reddit.subreddit('RealGirls')
    for submission in subreddit.new(limit=5):
        if submission.url.endswith(('jpg', 'jpeg', 'png')):
            bot.send_photo(chat_id=chat_id, photo=submission.url, caption=submission.title)

def start(update, context):
    update.message.reply_text('Bot started!')

def main():
    updater = Updater(token=telegram_bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    while True:
        fetch_and_send_photos(updater)
        time.sleep(60)  # Fetch new photos every minute

if __name__ == '__main__':
    main()
