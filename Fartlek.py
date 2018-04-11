'''
This creates a randomized Fartlek run.

A Fartlek run is one typically done with two or more people where each person
will take turns choosing how far and fast they are to run, e.g. "sprint to
the next tree" or "job until the end of the block."

USER INPUTS: minimum interval length, maximum interval length, and run length

OUTPUTS: Randomized interval lengths and paces.
'''

# IMPORTS
import random

# USER INPUTS

# Minimum interval length
while True:
    try:
        print("\n")
        min_interval = int(input("Shortest interval length (seconds): "))
    except:
        print("\n")
        print("ERROR: Must input an integer.")
        continue
    if min_interval <= 0:
        print("\n")
        print("ERROR: Must input a positive integer.")
        continue
    else:
        break
        
# Maximum interval length
while True:
    try:
        print("\n")
        max_interval = int(input("Longest interval length (seconds): "))
    except:
        print("\n")
        print("ERROR: Must input an integer.")
        continue
    if max_interval <= 0:
        print("\n")
        print("ERROR: Must input a positive integer.")
        continue
    elif max_interval < min_interval:
        print("\n")
        print(f"ERROR: Cannot have a maximum interval length shorter than the previously-defined minimum interval length ({min_interval} seconds)!")
    else:
        break
        
# Total run time
while True:
    try:
        print("\n")
        total_run_time = int(input("Total run time (minutes): "))
    except:
        print("\n")
        print("ERROR: Must input an integer.")
        continue
    if max_interval <= 0:
        print("\n")
        print("ERROR: Must input a positive integer.")
        continue
    elif total_run_time < max_interval/60:
        print("\n")
        print(f"ERROR: Cannot run for less time than the previously-defined maximum interval length ({max_interval/60} minutes)!")
    else:
        break

# INITIALIZE
running_time = 0
interval = 0
interval_list = []
pace_list = []

# BUILD

# Interval length options
time_options = list(range(min_interval,max_interval+min_interval,min_interval))

# Create randomized intervals
while running_time < total_run_time * 60:
    interval = random.choices(time_options)[0]
    interval_list.append(interval)
    running_time += interval

# Create a randomized pace list
for x in range(0,len(interval_list)):
    pace_list.append(random.randint(1,3))

for i in range(0,len(pace_list)):
    if pace_list[i] == 1:
        pace_list[i] = "slow"
    elif pace_list[i] == 2:
        pace_list[i] = "steady"
    elif pace_list[i] == 3:
        pace_list[i] = "fast"

print("\n"*100)
print(f"Total run time: {running_time/60} minutes")
print(f"Number of intervals: {len(interval_list)}")
print("\n")

for i in range(1,len(pace_list)+1):
    print(f"Interval {i}: {interval_list[i-1]} seconds {pace_list[i-1]}")
