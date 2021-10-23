import numpy as np
import pandas as pd
from Timetable import Timetable
from Event import Event
from Rearrange import optimize


monday = Timetable()

inta1200 = Event("INTA 1200", "Instructional Center", 50, "1400", "1450", fixed=True)
math1552 = Event("Math 1552", "Skiles", 50, "1100", "1150", fixed=True)
gym = Event("Gym", "CRC", 90, "0900", "2000", fixed=True)
evening_snack = Event("Evening snack", "Willage", 30, "1400", "1800", fixed=False)

events_list = [math1552, gym, inta1200, evening_snack]
optimized_events = optimize(events_list, 2)

print([i.name for i in optimized_events])
monday.add_event_list(optimized_events)

print(monday.timetable)
