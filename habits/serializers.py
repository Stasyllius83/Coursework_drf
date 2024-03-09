from rest_framework import serializers

from habits.models import Habit
from habits.validators import completion_duration, choose_related_habit_or_reward, long_execution_time, \
    pleasant_format, related_is_pleasant

class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для привычки"""
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """Дополнительная валидация для сериализатора"""
        choose_related_habit_or_reward(data.get('related_habit'), data.get('reward'))
        long_execution_time(data.get('time_to_complete'))
        related_is_pleasant(data.get('related_habit'), data.get('sign_of_pleasant'))
        pleasant_format(data.get('sign_of_pleasant'))
        completion_duration(data.get('time_to_complete'))
