from celery import shared_task
import logging
from config import settings
bot_token = settings.TELEGRAM_API_TOKEN
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def check_and_send_reminders():
    """
        Отправляет напоминания о привычках пользователям через Telegram.
    """
    good_habit = Habit.objects.filter(sign_of_pleasant=False)
    logging.info(good_habit)

    for habit in good_habit:
        logging.info(habit)
        logging.info(habit.owner.chat_id)
        if habit.owner.chat_id:
            chat_id = habit.owner.chat_id
            message = f"Напоминание: {habit.action} в {habit.place} в {habit.time.strftime('%H:%M')}"

            if habit.reward:
                message += f" Награда за выполнение: {habit.reward}."

            if habit.related_habit:
                related_habit_action = habit.related_habit.action
                message += f" Связанная привычка: {related_habit_action}."

            send_telegram_message(chat_id, message, bot_token)
