import numpy as np
import pandas as pd
import datetime
from Timetable import Timetable
from Event import Event
from Rearrange import optimize
from datetime import timedelta

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
        duration_in_min = (end_time-start_time).seconds/60
        list_timeframe = [(start_time, end_time), duration_in_min]
        return list_timeframe
    except:
        print('Error! Try Again')
        event_duration_timeframe()

def event_start_and_duration():
    try:
        start_time = event_start_time()
        duration = event_duration()
        end_time = start_time + timedelta(minutes=duration)
        list_timeframe = [(start_time, end_time), duration]
        return list_timeframe
    except Exception as error:
        print(error)
        print('Error! Try Again')
        event_start_and_duration()

def event_end_and_duration():
    try:
        end_time = event_end_time()
        duration = event_duration()
        start_time = end_time - timedelta(minutes=duration)
        list_timeframe = [(start_time, end_time), duration_in_min]
        return list_timeframe
    except:
        print('Error! Try Again')
        event_end_and_duration()

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

def several_timeframes_x_duration():
    try:
        duration = event_duration_x_timeframe()[1]
        TimeframeList = events_duration_x_timeframe()[0]
        while True:
            start_time = event_start_time()
            end_time = event_end_time()
            duration_in_min = (end_time - start_time).seconds / 60
            if (duration_in_min < float(duration)):
                print('Duration of event is greater than timeframe provided!')
                event_timesframe()
            else:
                TimeframeList.append((start_time, end_time))
        return TimeframeList
    except:
        print('Error! Try Again')
        several_timeframes_duration()

def several_timeframes():
    try:
        duration = event_timeframe()[1]
        TimeframeList = events_timeframe()[0]
        while True:
            start_time = event_start_time()
            end_time = event_end_time()
            duration_in_min = (end_time - start_time).seconds / 60
            if (duration_in_min < float(duration)):
                print('Duration of event is greater than timeframe provided!')
                event_timeframe()
            else:
                TimeframeList.append((start_time, end_time))
        return TimeframeList
    except:
        print('Error! Try Again')
        several_timeframes_duration()

def several_duration_end():
    try:
        duration = event_end_and_duration()[1]
        TimeframeList = events_end_and_duration()[0]
        while True:
            start_time = event_start_time()
            end_time = event_end_time()
            duration_in_min = (end_time - start_time).seconds / 60
            if (duration_in_min < float(duration)):
                print('Duration of event is greater than timeframe provided!')
                event_timeframe()
            else:
                TimeframeList.append((start_time, end_time))
        return TimeframeList
    except:
        print('Error! Try Again')
        #figure:several_timeframes_duration()

def several_duration_end():
    try:
        duration = event_start_and_duration()[1]
        TimeframeList = events_start_and_duration()[0]
        while True:
            start_time = event_start_time()
            end_time = event_end_time()
            duration_in_min = (end_time - start_time).seconds / 60
            if (duration_in_min < float(duration)):
                print('Duration of event is greater than timeframe provided!')
                event_timeframe()
            else:
                TimeframeList.append((start_time, end_time))
        return TimeframeList
    except:
        print('Error! Try Again')
        #figure:several_timeframes_duration()


def event_validator(event):
    duration, start_time, end_time = event.duration, event.start_time, event.end_time

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

event = Event('hi', 'yo', 30,'1240', '1300')
event_validator(event)
event_start_and_duration()
event_timeframe()
