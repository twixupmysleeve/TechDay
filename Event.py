import datetime as dt
import pandas as pd
import numpy as np


class Event:
    def __init__(self, name: str, location: str, duration: int, start_time: str, end_time: str, fixed=False):
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
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.fixed = fixed

# math1552 = Event("Math 1552", "Skiles", 50, [(1100, 1150)], fixed=True)
