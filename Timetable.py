import datetime
import pandas as pd
import numpy as np
from Event import Event

def main_run():
    user_input_condition()

def event_definer():
    try:
        name = input("Enter Name of Event: ")
        location = input("Enter Location of Event: ")
        duration = int(input("Enter Duration of Event, in minutes: "))
        #while True:
        start_time = input("Enter Start Time of Event: ")
        start_time_final = start_time[0] + start_time[1] + ":" + start_time[2] + start_time[3]
        end_time = input("Enter End Time of Event: ")
        end_time_final = end_time[0] + end_time[1] + ":" + end_time[2] + end_time[3]
        status_temp = input("Is the event Fixed? Yes or No: ")
        status_final = False
        if status_temp == 'Yes':
            status_final = True

        return Event(name, location, duration, start_time_final, end_time_final, status_final)
    except Exception as error:
        print(error)
        print('Please provide correct input!')
        event_definer()

test = Event("Vasav", "Skiles", 180, '1120', '1400', fixed=False)

def user_input_condition():
    # input_data = event_definer()
    input_data = event_definer()
    date_time_start = input_data.start_time
    time_start_obj = datetime.datetime.strptime(date_time_start, '%H%M')
    date_time_end = input_data.end_time
    time_end_obj = datetime.datetime.strptime(date_time_end, '%H%M')
    duration_in_min = (time_end_obj-time_start_obj).seconds/60
    if duration_in_min < input_data.duration:
        print('Duration of event is greater than timeframe provided!')
        #event_definer()

def timetable_dataframe():
    timetable = pd.DataFrame(columns = ['Name', 'Location', 'Duration', 'Start Time', 'End Time', 'Status'])
    while True:
        user_input_status = input("Add another event? Yes or No: ")
        if user_input_status == 'Yes':
            event_values = event_definer()
            event_entry = {'Name':event_values.name, 'Location':event_values.location , 'Duration':event_values.duration, 'Start Time':event_values.start_time, 'End Time':event_values.end_time, 'Status':event_values.fixed}
            timetable = timetable.append(event_entry, ignore_index = True)
        else:
            return timetable

main_run()


"""if user_input_condition():
    break
else:
    print('Duration of event is greater than timeframe provided!')
    pass"""
