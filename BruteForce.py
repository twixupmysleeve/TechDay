import datetime
import pandas as pd
import numpy as np
from Event import Event
from GoogleMaps import calculate_time_matrix
from collections import defaultdict
from itertools import permutations
import time

locations = ["Harrison Residence Hall Georgia Tech", "Howey Physics Georgia Tech", "Atlantic station Atlanta",
               "CRC Georgia Tech", "Skiles Building", "College of Computing Georgia Tech",
               "Instructional Center Georgia Tech", "North Avenue Dining Hall"]

location_matrix = calculate_time_matrix(locations)

min_score = 1000000
path = []

start = time.time()
perms = list(permutations(locations, len(locations)))
# print(perms)
for idx in range(len(perms)):
    i = perms[idx]
    score = 0
    for jdx in range(len(i)-1):
        j = i[jdx]
        j_next = i[jdx+1]
        # print(j)
        score += location_matrix[j][j_next]
    if score < min_score:
        min_score = score
        path = i
end = time.time()

print(end-start)
print(min_score, path)

