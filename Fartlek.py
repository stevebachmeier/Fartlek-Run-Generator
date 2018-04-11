'''
This creates a randomized Fartlek run.

A Fartlek run is one typically done with two or more people where each person
will take turns choosing how far and fast they are to run, e.g. "sprint to
the next tree" or "job until the end of the block."

USER INPUTS: minimum interval length, maximum interval length, and run length

OUTPUTS: Randomized interval lengths and paces.
'''

# ----IMPORTS----
import random

# ----USER INPUTS----

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
        
# Run length
while True:
    try:
        print("\n")
        run_length = int(input("Desired run length (minutes): "))
    except:
        print("\n")
        print("ERROR: Must input an integer.")
        continue
    if max_interval <= 0:
        print("\n")
        print("ERROR: Must input a positive integer.")
        continue
    elif run_length < max_interval/60:
        print("\n")
        print(f"ERROR: Cannot run for less time than the previously-defined maximum interval length ({max_interval/60} minutes)!")
    else:
        break

# ----INITIALIZE----
running_time = 0
interval = 0
interval_list = []
pace_list = []

# ----BUILD----
# Interval length options
time_options = list(range(min_interval,max_interval+min_interval,min_interval))

# Create randomized intervals
while running_time < run_length * 60:
    interval = random.choices(time_options)[0]
    interval_list.append(interval)
    running_time += interval
    
while running_time > run_length:
    if interval_list[-1] < (running_time/60 - run_length)*60:
        remove_interval = interval_list.pop()
        running_time -= remove_interval
        continue
    else:
        reduce_interval = (running_time/60 - run_length)*60
        interval_list[-1] -= reduce_interval
        running_time -= reduce_interval
        break

# Create a randomized pace list
pace_list.append(random.randint(1,3))
for x in range(1,len(interval_list)):
    if pace_list[-1] == 1:
        pace_list.append(random.randint(2,3))
    elif pace_list[-1] == 2:
        pace_list.append(random.choices([1,3])[0])
    elif pace_list[-1] == 3:
        pace_list.append(random.randint(1,2))

for i in range(0,len(pace_list)):
    if pace_list[i] == 1:
        pace_list[i] = "slow"
    elif pace_list[i] == 2:
        pace_list[i] = "steady"
    elif pace_list[i] == 3:
        pace_list[i] = "fast"

# ----PRINT RESULTS----
print("\n"*100)
print(f"Total run time: {running_time/60} minutes")
print(f"Number of intervals: {len(interval_list)}")
print("\n")

for i in range(1,len(pace_list)+1):
    print(f"Interval {i}: {interval_list[i-1]} seconds {pace_list[i-1]}")