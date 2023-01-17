from tkinter import *
from WorldTimeAPI import service as serv
from datetime import datetime
import time as t

myclient = serv.Client('timezone')
requests = {"area": "Europe", "location": "Berlin"}

response = myclient.get(**requests)
date_object = datetime.strptime(response.datetime, "%Y-%m-%dT%H:%M:%S.%f%z")


def pass_time():
    hour = date_object.hour
    min = date_object.minute
    sec = date_object.second
    print("Successfully get current time:", hour, min, sec)
    while True:
        t.sleep(1)
        sec += 1
        if sec == 60:
            min += 1
            sec = 0
        if min == 60:
            hour += 1
            min = 0
        if hour == 24:
            hour = 0
        print("Current time:", hour, min, sec)

pass_time()
