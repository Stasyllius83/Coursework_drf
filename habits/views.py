from django.shortcuts import render
from rest_framework import generics
from habits.models import Habit
from rest_framework.permissions import IsAuthenticated, AllowAny
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()
