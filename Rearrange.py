import numpy as np
import pandas as pd
from Timetable import Timetable
from Event import Event

def optimize(timetable):
    schedule = []
    for event in timetable.events:
        if event.fixed:
            schedule.append(event)
    # print([i.name for i in schedule])
    schedule.sort(key=lambda x:-int(x.start_time))




