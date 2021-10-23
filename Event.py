import datetime as dt
import pandas as pd
import numpy as np

class Event:
    def __init__(self, name, location, duration, timeframe, fixed=False):
        self.name = name
        self.location = location
        self.timeframe = timeframe
        self.duration = duration
        self.fixed = fixed



