import datetime
from celery import shared_task
from django.utils import timezone
from .models import GoodHabit, NiceHabit
from .telegram import send_telegram_notification


@shared_task
def check_habits_reminders():
    current_time = timezone.now().time()
    good_habits = GoodHabit.objects.filter(time__gte=current_time,
                                           time__lte=(current_time + datetime.timedelta(minutes=10)))
    nice_habits = NiceHabit.objects.filter(time__gte=current_time,
                                           time__lte=(current_time + datetime.timedelta(minutes=10)))

    for habit in good_habits:
        send_habit_notification(habit)
    for habit in nice_habits:
        send_habit_notification(habit)


def send_habit_notification(habit):
    message = f"Не забудьте выполнить привычку {habit.name} в {habit.time}!"
    send_telegram_notification.delay(habit.owner.telegram_chat_id, message)
