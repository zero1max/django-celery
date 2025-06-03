import random
import requests
from celery import shared_task
from django.conf import settings

quotes = [
    "💪 Bugun kuchli bo‘l, ertangi kun g‘alaba sen bilan!",
    "🚀 Harakat qilgan odam, oxir-oqibat muvaffaqiyatga erishadi!",
    "🌟 Orzularingiz uchun kurashing, siz bunga loyiqsiz!",
    "🔥 Har kun — yangi imkoniyat. Qani boshladik!",
    "🎯 Maqsadingiz yo‘lidagi har bir qadam — g‘alabaga yaqinlashishdir!"
]

@shared_task
def send_motivational_quote(tgid):
    quote = random.choice(quotes)
    bot_token = settings.TELEGRAM_BOT_TOKEN  # settings.py ga joylashtiring
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": tgid,
        "text": quote
    }
    requests.post(url, data=payload)
