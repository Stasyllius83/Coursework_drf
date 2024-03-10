from rest_framework import serializers

from habits.models import Habit
from habits.validators import Completion_duration, Choose_related_habit_or_reward, Long_execution_time, \
    Pleasant_format, Related_is_pleasant

class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для привычки"""
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """Дополнительная валидация для сериализатора"""
        Choose_related_habit_or_reward(data)
        Long_execution_time(data)
        Related_is_pleasant(data)
        Pleasant_format(data)
        Completion_duration(data)

        return data
