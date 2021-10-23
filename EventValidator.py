import numpy as np
import pandas as pd
import datetime
from Timetable import Timetable
from Event import Event
from Rearrange import optimize

def event_name():
    try:
        name = input('Enter name of the event: ')
        return name
    except Exception as error:
        print(error)
        print('Error! Try Again')
        event_name()

def event_location():
    try:
        location = input('Enter location of the event: ')
        return location
    except:
        print('Error! Try Again')
        event_location()

#If user enters both timeframe and duration, program should only run event_duration_x_timeframe.
#If user enters only timeframe, program should only run event_timeframe
#Otherwise, it'll run other functions as required

def event_duration():
    try:
      duration = int(input("Enter duration of event: "))
      return duration
    except:
      print("Error! Try again")
      event_duration()

def event_start_time():
    try:
        start_time = input("Enter Start Time of Event: ")
        start_time_final = start_time[0] + start_time[1] + start_time[2] + start_time[3]
        time_start_obj = datetime.datetime.strptime(start_time_final, '%H%M')
        return time_start_obj
    except Exception:
        print('Error! Try Again')
        event_start_time()

def event_end_time():
    try:
        end_time = input("Enter End Time of Event: ")
        end_time_final = end_time[0] + end_time[1] + end_time[2] + end_time[3]
        time_end_obj = datetime.datetime.strptime(end_time_final, '%H%M')
        return time_end_obj
    except:
        print('Error! Try Again')
        event_end_time()

def event_timeframe():
    try:
        start_time = event_start_time()
        end_time = event_end_time()
        list_timeframe = [()]
    except:
        print('Error! Try Again')
        event_duration_x_timeframe()

def event_duration_x_timeframe():
    try:
        start_time = event_start_time()
        end_time = event_end_time()
        duration = event_duration()
        duration_in_min = (end_time-start_time).seconds/60
        if (duration_in_min < float(duration)):
            print('Duration of event is greater than timeframe provided!')
            event_duration_x_timeframe()
        else:
            list_event_duration_timeframe = [(start_time, end_time), duration]
            return list_event_duration_timeframe
    except:
        print('Error! Try Again')
        event_duration_x_timeframe()




#check function below 8----D
def event_validator(name, location, duration, start_time, end_time):

    start_time_final = start_time[0] + start_time[1] + start_time[2] + start_time[3]
    time_start_obj = datetime.datetime.strptime(start_time_final, '%H%M')

    end_time_final = end_time[0] + end_time[1] + end_time[2] + end_time[3]
    time_end_obj = datetime.datetime.strptime(end_time_final, '%H%M')

    duration_in_min = (time_end_obj-time_start_obj).seconds/60
    if (duration_in_min < float(duration)):
        print('Duration of event is greater than timeframe provided!')
    else:
        list_event_duration_timeframe = [start_time, end_time, duration]
        return list_event_duration_timeframe

event_validator('hi', 'yo', 30,'1240', '1300')
