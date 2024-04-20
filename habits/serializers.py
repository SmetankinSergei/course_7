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

    def validate(self, data):
        if 'bounded_habit' in data and 'gift' in data:
            raise serializers.ValidationError("Cannot specify both bounded_habit and gift.")
        return data

    def validate_duration(self, value):
        if value > 120:
            raise serializers.ValidationError("Duration cannot be greater than 120 seconds.")
        return value

    class Meta:
        model = GoodHabit
        fields = '__all__'

    bounded_habit = serializers.PrimaryKeyRelatedField(queryset=NiceHabit.objects.all())
    gift = serializers.CharField(max_length=250)


class NiceHabitSerializer(HabitSerializer):

    def validate(self, data):
        if 'bounded_habit' in data:
            raise serializers.ValidationError("Cannot specify bounded_habit for a nice habit.")
        return data

    def validate_is_nice(self, value):
        if 'bounded_habit' in self.initial_data:
            raise serializers.ValidationError("Nice habit cannot have a bounded_habit.")
        return value

    class Meta:
        model = NiceHabit
        fields = '__all__'

    is_nice = serializers.BooleanField()
