import datetime
import pandas as pd
import numpy as np
from Event import Event
from GoogleMaps import calculate_time_matrix
from collections import defaultdict, OrderedDict
import random
from datetimerange import DateTimeRange
import time
from itertools import permutations
from pprint import pprint
from itertools import product

class Timetable:

    def __init__(self):
        self.clear_data()

    def show(self):
        print(self.timetable)

    def add_event(self, event, df=False):

        self.events.append(event)
        if df:
            event_entry = {'Name': event.name, 'Location': event.location, 'Duration': event.duration,
                           'Start Time': event.start_time, 'End Time': event.end_time,
                           'Status': event.fixed}
            self.timetable = self.timetable.append(event_entry, ignore_index=True)

    def add_event_list(self, event_list, df=False):
        for event in event_list:
            self.add_event(event, df=df)
        # self.generate_permutations()


    def remove_event(self, event):
        pass

    def clear_timetable(self):
        self.timetable = pd.DataFrame(columns = ['Name', 'Location', 'Duration', 'Start Time', 'End Time', 'Status'])
        base = datetime.datetime.strptime('1900-01-01 0000', '%Y-%m-%d %H%M')
        self.dates_used_dict = OrderedDict()
        for x in range(1440):
            self.dates_used_dict[base + datetime.timedelta(minutes=x)] = False

    def clear_data(self):
        self.clear_timetable()
        self.events = []
        self.locations = []
        self.location_matrix = defaultdict(dict)
        self.perms_dict = {}


    def use_date(self, dt):
        self.dates_used_dict[dt] = True

    def use_dates(self, start_dt, end_dt):
        val = start_dt
        for _ in range(int(((end_dt-start_dt).seconds/60) + 1)):
            if self.dates_used_dict[val]:
                return False
            self.use_date(val)
            val += datetime.timedelta(minutes=1)

    def create_location_matrix(self, events=None):
        if events:
            self.events=events
        self.locations = [event.location for event in self.events]
        #
        # for event in self.events:
        #     if event.alternative_locations:
        #         self.locations.extend(event.alternative_locations)
        #     else:
        #         self.locations.append(event.location)

        # self.locations = list(set(self.locations))
        self.location_matrix = calculate_time_matrix(self.locations)

    def compute_travel_time(self, event1, event2):
        travel_time = self.location_matrix[event1.location][event2.location]
        return travel_time

    def generate_permutations(self, events=None) -> dict:
        # print(self.locations)
        if events:
            self.events=events
        self.create_location_matrix(events)
        # perms = list(permutations(self.locations, len(self.locations)))
        print("Calculating permutations...")
        perms = [p for p in product(self.locations, repeat=len(self.locations))]
        print("Creating permutation mapping...")
        # print(perms)
        for idx in range(len(perms)):
            i = perms[idx]
            score = 0
            for jdx in range(len(i) - 1):
                j = i[jdx]
                j_next = i[jdx + 1]
                # print(j)
                # pprint(self.location_matrix)
                score += self.location_matrix[j][j_next]
            # if score < min_score:
            #     min_score = score
            #     path = i
            self.perms_dict[i] = score

        print("Done!")

    def calculate_score(self, events_list):
        path = [event.location for event in events_list]
        # print("-------------")
        # pprint(self.perms_dict)
        return self.perms_dict[tuple(path)]


    def create_random_timetable(self, events=None):
        if events:
            self.events = events
        schedule = []
        impossible=False
        earliest = datetime.datetime.strptime('1900-01-01 0700', '%Y-%m-%d %H%M')
        latest = datetime.datetime.strptime('1900-01-01 2359', '%Y-%m-%d %H%M')

        for event in self.events:
            if event.fixed:
                for start, end in event.timeframe:
                    # Convert start and end times to datetime objects
                    val = datetime.datetime.strptime(start, '%H%M')
                    # print(dates_used_dict)

                    event.start_time = start
                    event.end_time = end

                    for _ in range(event.duration+1):
                        if self.dates_used_dict[val]:
                            raise ValueError(val)
                        self.use_date(val)
                        val += datetime.timedelta(minutes=1)
                    
                    schedule.append(event)

        self.events.sort(key = lambda x: (x.priority, x.duration))

        for event in self.events:
            for start, end in event.timeframe:
                start = datetime.datetime.strptime(start, '%H%M')
                end = datetime.datetime.strptime(end, '%H%M')
                duration = datetime.timedelta(minutes=event.duration)

                if not event.fixed:
                    random_time = round_datetime_10_mins(random_date(start, end))
                    random_end = random_time + duration
                    # print(event.name, random_time, random_end)
                    i=0
                    while (random_time <= earliest or random_end >= latest or
                            self.dates_used_dict[random_time] or
                            self.dates_used_dict[random_end] or
                            self.dates_used_dict[random_date(random_time, random_end)] or
                            self.dates_used_dict[middle_date(random_time, random_end)]):
                        i+=1
                        random_time = round_datetime_10_mins(random_date(start, end))
                        random_end = random_time + duration
                        if event.alternative_locations:
                            event.location = event.alternative_locations[i%len(event.alternative_locations)]
                            # print(event.name, random_time, random_end)

                    event.start_time = random_time.strftime("%H%M")
                    event.end_time = random_end.strftime("%H%M")

                    schedule.append(event)
                    self.use_dates(random_time, random_end)


        schedule.sort(key=lambda x: (x.start_time))
        score = self.calculate_score(schedule)

        # print([(event.name, event.start_time, event.end_time) for event in self.events])
        return (schedule, score)

    def create_optimum_schedule(self, event_list):
        min_score = 10000
        optimum_schedule = []

        self.generate_permutations(event_list)

        for _ in range(300):
            self.clear_timetable()
            # self.add_event_list(event_list)
            self.events = event_list
            schedule, score = self.create_random_timetable()

            if score<min_score:
                min_score = score
                optimum_schedule = schedule

        return (optimum_schedule, min_score)

def compare_datetime(a, b):
    return (a.minutes == b.minutes and a.hours == b.hours)

def round_datetime_10_mins(dt):
    a, b = divmod(round(dt.minute, -1), 60)
    return datetime.datetime.strptime('%i%02i' % ((dt.hour + a) % 24, b), "%H%M")

def middle_date(start, end, printing=False):
    delta = end - start
    int_delta = (delta.seconds/60)
    random_minute = int_delta//2
    if printing:
        print("RANDOM", random_minute)
    return start + datetime.timedelta(minutes=random_minute)

def random_date(start, end, printing=False):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.seconds/60)
    random_minute = random.randint(0,int_delta)
    if printing:
        print("RANDOM", random_minute)
    return start + datetime.timedelta(minutes=random_minute)

if __name__ == '__main__':
    timetable = Timetable()
    dorm_morn = Event("Dorm", "Harrison Residence Hall", 0, [("0700", "0705")], fixed=True)
    dorm_eve = Event("Dorm", "HArrison Residence Hall", 0, [("2330", "2335")], fixed=True)
    cs1331 = Event("CS1331", "Klaus", 50, [("0825", "0915")], fixed=True)
    psyc2280 = Event("PSYC 2280", "Skiles", 50, [("0930", "1020")], fixed=True)
    math1554 = Event("Math 1554", "Crosland Library", 50, [("1400", "1450")], fixed=True)
    # TODO: WHat about online class?
    buzz_studios = Event("Buzz Studios", "College of Computing", 60, [("1830", "1930")], fixed=True)
    gym = Event("Gym", "CRC", 90, [("0900", "2000")], fixed=False)
    breakfast = Event("Breakfast", "North Ave Dining Hall", 30, [("0700", "1000")], fixed=False, alternative_locations=["Brittain Dining Hall", "North Ave Dining Hall", "West Village"])
    evening_snack = Event("Evening snack", "West Village", 30, [("1600", "1800")], fixed=False, alternative_locations=["Brittain Dining Hall", "North Ave Dining Hall", "West Village"])
    afternoon_meal = Event("Afternoon Meal", "Brittain Dining Hall", 30, [("1100", "1400")], fixed=False, alternative_locations=["Brittain Dining Hall", "North Ave Dining Hall", "West Village"])
    studying = Event("Studyin", "CULC", 20, [("0800", "2200")], fixed=False)
    # brown
    event_list = [dorm_morn,
                  cs1331,
                  afternoon_meal,
                  psyc2280,
                  gym,
                  breakfast,
                  math1554,
                  evening_snack]

    start = time.time()

    # timetable.generate_permutations(event_list)
    # timetable.add_event_list(event_list)
    # schedule, score = timetable.create_optimum_schedule(event_list)
    schedule, score = timetable.create_optimum_schedule(event_list)
    schedule.sort(key=lambda x: x.start_time)

    end = time.time()
    print(end-start)

    # timetable.clear_timetable()
    # timetable.add_event_list(schedule, df=True)
    # timetable.show()
    pprint([(event.name, event.start_time, event.end_time, event.location) for event in schedule])
    print(score)