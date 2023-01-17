import tkinter as tk
from datetime import datetime, timedelta

root = tk.Tk()
root.title("Clock")

on = True


def stop_time():
    global on
    if on:
        on = False
    else:
        on = True
        time()


def time():
    if on:
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
    alarm_lbl.config(text="Alarm !!!")
    alarm_lbl.after(5000, alarm_off)


def alarm_off():
    alarm_lbl.config(fg="black")
    alarm_lbl.config(text=f"Alarm set at : {alarm_time.strftime('%H:%M:%S %p')}")


def toggle_am_pm():
    global current_time
    if current_time.strftime("%p") == "AM":
        current_time = current_time.replace(hour=(current_time.hour+12) % 24)
    else:
        current_time = current_time.replace(hour=(current_time.hour-12) % 24)
    string = current_time.strftime('%H:%M:%S %p')
    lbl.config(text=string)


current_time = datetime.now()
alarm_time = datetime.now()

lbl = tk.Label(root, font=('arial', 40, 'bold'), background='black', foreground='white', width=20)
lbl.pack(anchor='center')

toggle_am_pm_button = tk.Button(root, text='Toggle AM/PM', command=toggle_am_pm)
toggle_am_pm_button.pack()

frame = tk.Frame(root)
frame.pack()

hour_var = tk.StringVar(value=str(current_time.hour))
hour_entry = tk.Entry(frame, textvariable=hour_var)
hour_entry.grid(row=0, column=0)

minute_var = tk.StringVar(value=str(current_time.minute))
minute_entry = tk.Entry(frame, textvariable=minute_var)
minute_entry.grid(row=0, column=1)

second_var = tk.StringVar(value=str(current_time.second))
second_entry = tk.Entry(frame, textvariable=second_var)
second_entry.grid(row=0, column=2)

change_time_button = tk.Button(frame, text='Change Time', command=change_time)
change_time_button.grid(row=0, column=3, pady=10)


alarm_frame = tk.Frame(root)
alarm_frame.pack()

alarm_hour_var = tk.StringVar(value=str(alarm_time.hour))
alarm_hour_entry = tk.Entry(alarm_frame, textvariable=alarm_hour_var)
alarm_hour_entry.grid(row=0, column=0)

alarm_minute_var = tk.StringVar(value=str(alarm_time.minute))
alarm_minute_entry = tk.Entry(alarm_frame, textvariable=alarm_minute_var)
alarm_minute_entry.grid(row=0, column=1)

alarm_second_var = tk.StringVar(value=str(alarm_time.second))
alarm_second_entry = tk.Entry(alarm_frame, textvariable=alarm_second_var)
alarm_second_entry.grid(row=0, column=2)

set_alarm_button = tk.Button(alarm_frame, text='Set Alarm', command=set_alarm)
set_alarm_button.grid(row=0, column=3, pady=10)

alarm_lbl = tk.Label(root, font=('arial', 20, 'bold'), background='white', foreground='black')
alarm_lbl.pack(anchor='center')


stop_time_button = tk.Button(root, text='Stop Time', command=stop_time)
stop_time_button.pack()

time()
root.mainloop()
