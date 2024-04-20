import telegram

from config.settings import TELEGRAM_BOT_TOKEN


def send_telegram_notification(chat_id, message):
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=chat_id, text=message)
