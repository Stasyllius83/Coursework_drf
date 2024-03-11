from rest_framework.response import Response


def send_telegram_message(chat_id, message, bot_token):
    URL = "http//api.telegram.org/bot"

    #response = request.post(
    #    url=f"{URL}{bot_token}/sendMessage",
    #   data={
    #   'chat_id'=chat_id,
    #   'text'=message
    #}
    #)
