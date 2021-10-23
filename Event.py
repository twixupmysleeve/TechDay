import datetime as dt
import pandas as pd
import numpy as np


class Event:
    def __init__(self, name: str, location: str, duration: int, timeframe: tuple, priority=1, fixed=False):
        """
        Event class
        :param name: name of Event
        :param location: location of Event
        :param duration: time in minutes
        :param timeframe: list of tuples => [(start time in hrs, end time in hrs)]
        :param fixed: boolean representing variability
        """
        self.name = name
        self.location = location
        self.timeframe = timeframe
        self.duration = duration
        self.fixed = fixed
        self.priority = priority

        self.start_time = self.timeframe[0][0]
        self.end_time = self.timeframe[0][1]



# math1552 = Event("Math 1552", "Skiles", 50, [(1100, 1150)], fixed=True)
