from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование привычек"""

    def setUp(self):

        self.user = User.objects.create(
            email="test1@test1.ru",
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        self.user.set_password("test")
        self.user.save()

        self.habit = Habit.objects.create(
            owner= "1",
            place= "None",
            time= "2024-03-15",
            action= "Сьесть десерт",
            sign_of_pleasant= "True",
            related_habit= "None",
            periodicity= "7",
            reward="None",
            time_to_complete= "0:01:30",
            is_published= "False"
        )

        """Имитация авторизации пользователя по JWT токену."""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тестирование создания привычки"""
        data = {
                "owner": "test1@test1.ru",
                "place": "Спортивная площадка",
                "time": "2024-03-14",
                "action": "Пробежка",
                "sign_of_pleasant": "False",
                "related_habit": "null",
                "periodicity": "2",
                "reward": "null",
                "time_to_complete": "0:01:30",
                "is_published": "True"
            }

        response = self.client.post(
            reverse('habits:habit-create'),
            data=data
        )
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
