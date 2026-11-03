import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

URL = "https://district5.scenecinemas.com/"

def send_message(text):
    api = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(api, data={
        "chat_id": CHAT_ID,
        "text": text
    })

def check_tickets():
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    page = response.text.lower()

    if "avengers: doomsday" in page and "advanced booking" in page:
        send_message(
            "🚨 Avengers: Doomsday\n"
            "الفيلم ظهر في صفحة الحجز على Scene Cinemas!\n"
            "افتح الموقع وتأكد من مواعيد District 5:\n"
            + URL
        )

check_tickets()
