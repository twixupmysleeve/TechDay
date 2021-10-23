import datetime
import pandas as pd
import numpy as np
from Event import Event
from GoogleMaps import calculate_time_matrix
from collections import defaultdict


class Timetable:

    def __init__(self):
        self.clear_timetable()

    def add_event(self, event):
        event_entry = {'Name': event.name, 'Location': event.location, 'Duration': event.duration,
                       'Start Time': event.start_time, 'End Time': event.end_time,
                       'Status': event.fixed}
        self.events.append(event)
        # self.timetable = self.timetable.append(event_entry, ignore_index=True)

    def add_event_list(self, event_list):
        for event in event_list:
            self.add_event(event)

    def remove_event(self, event):
        pass

    def clear_timetable(self):
        self.timetable = pd.DataFrame(columns = ['Name', 'Location', 'Duration', 'Start Time', 'End Time', 'Status'])
        self.events = []
        self.location_matrix = defaultdict(dict)

    def create_location_matrix(self):
        locations = [event.location for event in self.events]
        self.location_matrix = calculate_time_matrix(locations)

    def compute_travel_time(self, event1, event2):
        travel_time = self.location_matrix[event1.location][event2.location]
        return travel_time

    def create_timetable(self):
        schedule = []
        base = datetime.datetime.strptime('1900-01-01 0000', '%Y-%m-%d %H%M')
        dates_used_dict = {}
        for x in range(1440):
            dates_used_dict[base + datetime.timedelta(minutes=x)]=False
            # if True means date has been used, if False means date hasn't been used

        earliest = datetime.datetime.strptime('0800', '%H%M')
        latest = datetime.datetime.strptime('2359', '%H%M')

        for event in self.events:
            if event.fixed:
                for start, end in event.timeframe:
                    # Convert start and end times to datetime objects
                    val = datetime.datetime.strptime(start, '%H%M')
                    # print(dates_used_dict)

                    event.start_time = start
                    event.end_time = end

                    for _ in range(event.duration+1):
                        if dates_used_dict[val]:
                            raise ValueError(val)
                        dates_used_dict[val] = True
                        val += datetime.timedelta(minutes=1)
                    
                    schedule.append(event)

        self.events.sort(key = lambda x: (x.priority, x.duration))

        


        schedule.sort(key=lambda x: (x.start_time))
        # print([(event.name, event.start_time, event.end_time) for event in self.events])
        return ([(i.name, i.start_time, i.end_time) for i in schedule])

def compare_datetime(a, b):
    return (a.minutes == b.minutes and a.hours == b.hours)

if __name__ == '__main__':
    timetable = Timetable()

    cs1331 = Event("CS1331", "Klaus", 50, [("0825", "0915")], fixed=True)
    inta1200 = Event("INTA 1200", "Instructional Center", 50, [("1400", "1450")], fixed=True)
    math1552 = Event("Math 1552", "Skiles", 50, [("1100", "1150")], fixed=True)
    engl1102 = Event("ENGL 1102", "Skiles", 75, [("1700", "1815")], fixed=True)
    gym = Event("Gym", "CRC", 90, [("0900", "2000")], fixed=False)
    evening_snack = Event("Evening snack", "Willage", 30, [("1400", "1800")], fixed=False)
    afternoon_meal = Event("Afternoon Meal", "Brittain", 30, [("1200", "1400")], fixed=False)
    studying = Event("Studyin", "LLL", 30, [("0800", "2000")], fixed=False)

    event_list = [math1552, gym, inta1200, cs1331, evening_snack, afternoon_meal, studying, engl1102]

    timetable.add_event_list(event_list)

    print(timetable.create_timetable())

"""if user_input_condition():
    break
else:
    print('Duration of event is greater than timeframe provided!')
    pass"""
