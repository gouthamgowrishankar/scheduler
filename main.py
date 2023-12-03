from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import requests


app= FastAPI()

test_list = ["1"] * 10


def check_list_len():
     res = requests.get('https://user-login-8rw0.onrender.com/')
     print(res.content)
     return res

@app.on_event('startup')
def init_data():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_list_len, 'interval', minutes=3)
    scheduler.start()

@app.get('/')
def root():
    return {'meassge': 'scheduler app'}