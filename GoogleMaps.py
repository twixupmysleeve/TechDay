import googlemaps
from datetime import datetime
import requests
import smtplib
from collections import defaultdict
from pprint import pprint

API_KEY = 'AIzaSyAqLW1ckmji2yoawB5ti-s4Uka6i24fvC4'


def make_url(origins, destinations):
    URL = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations="
    for destination in destinations:
        URL += destination
        URL += "|"
    URL = URL[:-1]
    URL += '&origins='
    for origin in origins:
        URL += origin
        URL += "|"
    URL = URL[:-1]
    URL += "&mode=walking"
    URL += "&key="
    URL += API_KEY
    URL = URL.replace(" ", '')
    return URL


def calculate_time_matrix(locations):
    origins = locations
    destinations = origins

    search_url = make_url(origins, destinations)
    print(search_url)
    map_info = requests.get(search_url).json()["rows"]
    # print(map_info)
    time_matrix = defaultdict(dict)
    # print("Making time matrix")
    for i in range(len(origins)):
        for j in range(len(destinations)):
            # time_text = map_info[i]["elements"][j]["duration"][
            #     "text"]
            # print(map_info)
            time_minutes = round(map_info[i]["elements"][j]["duration"]["value"] / 60, 2)
            time_matrix[origins[i]][destinations[j]] = time_minutes
            # print("Time between " + origins[i] + " and " + destinations[j] + " is: " + str(
            #     time_minutes) + " mins")
    # print("Time matrix ready!")
    return time_matrix


if __name__ == "__main__":
    locations = ["Harrison Residence Hall Georgia Tech", "Howey Physics Georgia Tech", "Skiles Building",
               "CRC Georgia Tech", "Skiles Building", "College of Computing Georgia Tech",
               "Instructional Center Georgia Tech", "North Avenue Dining Hall"]
    pprint(calculate_time_matrix(locations))
