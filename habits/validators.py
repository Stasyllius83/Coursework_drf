
from rest_framework import serializers
from datetime import timedelta

from habits.models import Habit


class choose_related_habit_or_reward():

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get("related_habit")
        reward = value.get("reward")
        if (related_habit != 0) and (reward != 0):
            raise serializers.ValidationError("Нельзя одновременно выбирать связанную привычку и указывать вознаграждение")


class long_execution_time():

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_complete = value.get('time_to_complete')
        if time_to_complete > timedelta(minutes=2):
            raise serializers.ValidationError("Время выполнения должно быть не больше 120 секунд")


class related_is_pleasant():

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get("related_habit")
        sign_of_pleasant = value.get("sign_of_pleasant")
        related_habit_obj = Habit.objects.filter(habit_id=related_habit)
        if related_habit_obj.sign_of_pleasant != sign_of_pleasant:
            raise serializers.ValidatorError("В связанные привычки могут попадать только привычки с признаком приятной привычки")


class pleasant_format():

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        sign_of_pleasant = value.get("sign_of_pleasant")
        pleasant_habit = Habit.objects.filter(sign_of_pleasant=sign_of_pleasant)
        print(pleasant_habit)
        print(pleasant_habit.reward)
        print(pleasant_habit.related_habit)
        print(pleasant_habit.sign_of_pleasant)
        if pleasant_habit.reward != None or pleasant_habit.related_habit != None:
            raise serializers.ValidatorError("У приятной привычки не может быть вознаграждения или связанной привычки")


class completion_duration():

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_complete = value.get("time_to_complete")
        if 0 <= time_to_complete >= 7:
            raise serializers.ValidatorError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")
