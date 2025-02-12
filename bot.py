import praw
from telegram import Bot
from telegram.ext import Updater, CommandHandler
import time

# Reddit API setup
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

# Telegram Bot setup
telegram_bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'
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
