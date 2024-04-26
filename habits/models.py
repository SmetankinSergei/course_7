from django.db import models
from django.db.models import CASCADE, DO_NOTHING

from habits.constants import PERIODS


NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('users.User', on_delete=CASCADE, null=True)
    place = models.CharField(max_length=250)
    time = models.TimeField()
    period = models.CharField(max_length=10, choices=PERIODS, default='EVERYDAY')
    duration = models.PositiveIntegerField(default=10)
    is_public = models.BooleanField(default=False)

    class Meta:
        abstract = True


class GoodHabit(Habit):
    bounded_habit = models.ForeignKey('NiceHabit', on_delete=DO_NOTHING)
    gift = models.CharField(max_length=250, **NULLABLE)


class NiceHabit(Habit):
    is_nice = models.BooleanField(default=True)
