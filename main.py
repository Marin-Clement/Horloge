import tkinter as tk
from datetime import datetime, timedelta

root = tk.Tk()
root.title("Clock")


def time():
    global current_time
    current_time += timedelta(seconds=1)
    string = current_time.strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
    if current_time.strftime("%H:%M:%S") == alarm_time.strftime("%H:%M:%S"):
        alarm()


def change_time():
    global current_time
    hour = int(hour_var.get())
    minute = int(minute_var.get())
    second = int(second_var.get())
    current_time = current_time.replace(hour=hour, minute=minute, second=second)
    string = current_time.strftime('%H:%M:%S %p')
    lbl.config(text=string)


def set_alarm():
    global alarm_time
    hour = int(alarm_hour_var.get())
    minute = int(alarm_minute_var.get())
    second = int(alarm_second_var.get())
    alarm_time = alarm_time.replace(hour=hour, minute=minute, second=second)
    string = alarm_time.strftime('%H:%M:%S %p')
    alarm_lbl.config(text=f"Alarm set at : {string}")


def alarm():
    alarm_lbl.config(fg="red")
    alarm_lbl.config(text="Alarm !!! Wake Up")
    alarm_lbl.after(5000, alarm_off)


def alarm_off():
    alarm_lbl.config(fg="black")
    alarm_lbl.config(text=f"Alarm set at : {alarm_time.strftime('%H:%M:%S %p')}")


current_time = datetime.now()
alarm_time = datetime.now()

lbl = tk.Label(root, font=('calibri', 40, 'bold'),
               background='black',
               foreground='white')
lbl.pack(anchor='center')

hour_var = tk.StringVar(value=str(current_time.hour))
hour_entry = tk.Entry(root, textvariable=hour_var)
hour_entry.pack()

minute_var = tk.StringVar(value=str(current_time.minute))
minute_entry = tk.Entry(root, textvariable=minute_var)
minute_entry.pack()

second_var = tk.StringVar(value=str(current_time.second))
second_entry = tk.Entry(root, textvariable=second_var)
second_entry.pack()

change_time_button = tk.Button(root, text='ChangeTime', command=change_time)
change_time_button.pack()

alarm_hour_var = tk.StringVar(value=str(alarm_time.hour))
alarm_hour_entry = tk.Entry(root, textvariable=alarm_hour_var)
alarm_hour_entry.pack()

alarm_minute_var = tk.StringVar(value=str(alarm_time.minute))
alarm_minute_entry = tk.Entry(root, textvariable=alarm_minute_var)
alarm_minute_entry.pack()

alarm_second_var = tk.StringVar(value=str(alarm_time.second))
alarm_second_entry = tk.Entry(root, textvariable=alarm_second_var)
alarm_second_entry.pack()

set_alarm_button = tk.Button(root, text='Set Alarm', command=set_alarm)
set_alarm_button.pack()

alarm_lbl = tk.Label(root, font = ('calibri', 20, 'bold'), background='white', foreground='black')
alarm_lbl.pack(anchor='center')

time()
root.mainloop()

