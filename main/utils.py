import requests
from config.settings import BOT_ADMIN_ID, BOT_TOKEN


def send_bot_message(form_data):
    post_data = "\n".join(["{}: {}".format(k, v) for k, v in form_data.items()])
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={BOT_ADMIN_ID}&text={post_data}")