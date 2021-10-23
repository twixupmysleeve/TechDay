import datetime as dt
import pandas as pd
import numpy as np
from Event import Event

def main_run():
    timetable_dataframe()

def event_definer():
    name = input("Enter Name of Event: ")
    location = input("Enter Location of Event: ")
    duration = int(input("Enter Duration of Event, in minutes: "))
    start_time = int(input("Enter Start Time of Event: "))
    end_time = int(input("Enter End Time of Event: "))
    status_temp = input("Is the event Fixed? Yes or No: ")
    status_final = False
    if status_temp == 'Yes':
        status_final = True
    return Event(name, location, duration, start_time, end_time, status_final)

#test = Event("Vasav", "Skiles", 180, [1100, 1400])

def timetable_dataframe():
    timetable = pd.DataFrame(columns = ['Name', 'Location', 'Duration', 'Start Time', 'End Time', 'Status'])
    while True:
        user_input_status = input("Add another event? Yes or No: ")
        if user_input_status == 'Yes':
            event_values = event_definer()
            event_entry = {'Name':event_values.name, 'Location':event_values.location , 'Duration':event_values.duration, 'Start Time':event_values.start_time, 'End Time':event_values.end_time, 'Status':event_values.fixed}
            timetable = timetable.append(event_entry, ignore_index = True)
        else:
            print(timetable)
            break

main_run()
