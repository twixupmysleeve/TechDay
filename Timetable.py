import datetime
import pandas as pd
import numpy as np
from Event import Event


class Timetable:
    def __init__(self):
        self.clear_timetable()

    def add_event(self, event):
        event_entry = {'Name': event.name, 'Location': event.location, 'Duration': event.duration,
                       'Start Time': event.start_time, 'End Time': event.end_time,
                       'Status': event.fixed}
        self.events.append(event)
        self.timetable = self.timetable.append(event_entry, ignore_index=True)
        
    def add_event_list(self, event_list):
        for event in event_list:
            self.add_event(event)

    def remove_event(self, event):
        pass

    def clear_timetable(self):
        self.timetable = pd.DataFrame(columns = ['Name', 'Location', 'Duration', 'Start Time', 'End Time', 'Status'])
        self.events = []

# TODO: Convert all the below functions into OOP
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
        # print(error)
        print('Please provide correct input!')
        event_definer()

test = Event("Vasav", "Skiles", 50, '1100', '1150', fixed=True)

def user_input_condition():
    # TODO: These conditions should be in the Event class
    # input_data = event_definer()
    input_data = test
    date_time_start = input_data.start_time
    time_start_obj = datetime.datetime.strptime(date_time_start, '%H%M')
    date_time_end = input_data.end_time
    time_end_obj = datetime.datetime.strptime(date_time_end, '%H%M')
    duration_in_min = (time_end_obj-time_start_obj).seconds/60
    if duration_in_min < input_data.duration:
        print('Duration of event is greater than timeframe provided!')
        #event_definer()

def timetable_dataframe():
    # def timetable_dataframe(timetable):
    timetable = pd.DataFrame(columns = ['Name', 'Location', 'Duration', 'Start Time', 'End Time', 'Status'])
    while True:
        # TODO: We don't need this because we're going to be using
        #  some UI later which will use buttons to handle this
        user_input_status = input("Add another event? Yes or No: ")
        if user_input_status == 'Yes':
            event_values = event_definer()
            event_entry = {'Name':event_values.name, 'Location':event_values.location , 'Duration':event_values.duration, 'Start Time':event_values.start_time, 'End Time':event_values.end_time, 'Status':event_values.fixed}
            timetable = timetable.append(event_entry, ignore_index = True)
        else:
            return timetable

# main_run()

if __name__ == '__main__':
    timetable = Timetable()
    math1552 = Event("Math 1552", "Skiles", 50, "1100", "1150", fixed=True)
    gym = Event("Gym", "CRC", 90, "0900", "2000", fixed=False)
    inta1200 = Event("INTA 1200", "Instructional Center", 50, "1400", "1450", fixed=True)
    eveningSnack = Event("Evening snack", "Willage", 30, "1600", "1800", fixed=False)

    timetable.add_event(math1552)
    timetable.add_event(gym)
    timetable.add_event(inta1200)
    timetable.add_event(eveningSnack)

    print(timetable.timetable)

"""if user_input_condition():
    break
else:
    print('Duration of event is greater than timeframe provided!')
    pass"""
