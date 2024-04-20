# import telegram
# from celery import shared_task
# from django.conf import settings
#
# @shared_task
# def send_telegram_notification(chat_id, message):
#     bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
#     bot.send_message(chat_id=chat_id, text=message)
