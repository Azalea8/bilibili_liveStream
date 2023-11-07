import json
import schedule
import time

import requests

def job():
    response = requests.get("https://open.tophub.today/hot")
    temp = json.loads(response.text)

    temp = temp["data"]["items"][0: 10]
    msg = "用户点击实时榜\n\n"

    for t in temp:
        msg += f"{t['sitename']} || {t['title']}\n\n"

    params = {
        'user_id': 2574292235,
        'message': msg,
    }
    requests.get(url='http://127.0.0.1:5700/send_private_msg', params=params)


schedule.every().day.at("08:00").do(job)
schedule.every().day.at("14:25").do(job)
schedule.every().day.at("20:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
