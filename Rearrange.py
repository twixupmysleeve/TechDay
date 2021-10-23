import numpy as np
import pandas as pd
from Timetable import Timetable
from Event import Event
import random
import datetime
from random import randrange
import time

def optimize(events_list, location_matrix):
    schedule = []
    fixed_times = []
    earliest = datetime.datetime.strptime('0800', '%H%M')
    latest = datetime.datetime.strptime('2359', '%H%M')
    for event in events_list:
        for start, end in event.timeframe:
            start = datetime.datetime.strptime(start, '%H%M')
            end = datetime.datetime.strptime(end, '%H%M')
            if event.fixed:
                schedule.append(event)
                step = datetime.timedelta(minutes=1)
                val = start
                while val <= end:
                    fixed_times.append(val)
                    val += step
                # fixed_times.extend(range(int(event.start_time), int(event.end_time)))

    events_list.sort(key=lambda x: x.duration)
    # print([i.name for i in schedule])
    # print(fixed_times)
    # all_times = fixed_times

    for event in events_list:
        # print([i.strftime("%H%M") for i in fixed_times])
        for start, end in event.timeframe:
            start = datetime.datetime.strptime(start, '%H%M')
            end = datetime.datetime.strptime(start, '%H%M')
            duration = datetime.timedelta(minutes=event.duration)

            if not event.fixed:
                random_time = random_date(start, end)
                random_end = random_time + duration

                print(event.name, random_time, random_end)

                while random_time in fixed_times or random_end in fixed_times:
                    # consider the range of values from random_time to random_end
                    print(random_time in fixed_times,random_end in fixed_times)
                    print(random_time <= earliest, random_end >= latest)
                    print(type(random_end))

                    if random_end >= latest:
                        start -= datetime.timedelta(minutes=30)
                        end -= datetime.timedelta(minutes=30)

                    random_time = random_date(start, end, printing=True)
                    random_end = random_time + duration
                    print(event.name, random_time, random_end)
                    print("FIXED:",  len(all_times))
                    print("FIXED SET:", len(set(all_times)))
                # break

                event.start_time = random_time.strftime("%H%M")
                event.end_time = random_end.strftime("%H%M")
                schedule.append(event)
                step = datetime.timedelta(minutes=1)
                val = start
                while val <= end:
                    all_times.append(val)
                    val += step
    # print([(i.name, i.start_time, i.end_time) for i in schedule])
    schedule.sort(key=lambda x:(x.start_time))
    print(len(fixed_times), len(set(fixed_times)))
    return schedule
    # if len(fixed_times) - len(set(fixed_times)) == 0:
    #     return schedule
    # else:
    #     return optimize(events_list, location_matrix)

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
    monday = Timetable()

    cs1331 = Event("CS1331", "Klaus", 50, [("0825", "0915")], fixed=True)
    inta1200 = Event("INTA 1200", "Instructional Center", 50, [("1400", "1450")], fixed=True)
    math1552 = Event("Math 1552", "Skiles", 50, [("1100", "1150")], fixed=True)
    gym = Event("Gym", "CRC", 90, [("0900", "2000")], fixed=False)
    evening_snack = Event("Evening snack", "Willage", 30, [("1400", "1800")], fixed=False)
    afternoon_meal = Event("Afternoon Meal", "Brittain", 30,[("1200", "1400")], fixed=False)
    studying = Event("Studyin", "LLL", 30, [("0800", "2000")], fixed=False)

    events_list = [math1552, gym, inta1200, cs1331, evening_snack, afternoon_meal, studying]

    start = time.time()
    for i in range(10):
        optimized_events = optimize(events_list, 2)
        print([(i.name, i.start_time, i.end_time) for i in optimized_events])
    end = time.time()
    print(end-start)


    # for i in range(60,2200):
    #     base60 = numberToBase(i, 60)
    #     print(base60[0]*100 + base60[1])
    

