from rest_framework import serializers
from habits.models import GoodHabit, NiceHabit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = None

    name = serializers.CharField(max_length=100)
    place = serializers.CharField(max_length=250)
    time = serializers.TimeField()
    period = serializers.CharField(max_length=10)
    duration = serializers.IntegerField()
    is_public = serializers.BooleanField()

    def create(self, validated_data):
        if self.Meta.model:
            habit = self.Meta.model.objects.create(**validated_data)
            return habit


class GoodHabitSerializer(HabitSerializer):
    class Meta:
        model = GoodHabit
        fields = '__all__'

    bounded_habit = serializers.PrimaryKeyRelatedField(queryset=NiceHabit.objects.all())
    gift = serializers.CharField(max_length=250)


class NiceHabitSerializer(HabitSerializer):
    class Meta:
        model = NiceHabit
        fields = '__all__'

    is_nice = serializers.BooleanField()
