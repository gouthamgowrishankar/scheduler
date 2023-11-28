from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler


app= FastAPI()

test_list = ["1"] * 10


def check_list_len():
    global test_list
    print(f"check_list_len：{len(test_list)}")

@app.on_event('startup')
def init_data():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_list_len, 'cron', second='*/15')
    scheduler.start()

@app.get('/')
def root():
    return {'meassge': 'scheduler app'}