
# JSON TO LOAD

# NOTE: Run this with './json2table load' (shell script wrapper)

# Converts a directory of runs into a simple load over time table
# The output file format for each line is
# timestamp load
# where the timestamp is floating point Unix hours
#   relative to first event
# and the load is the number of models running

# Tested with
# root_dir=/projects/Candle_ECP/pbalapra/Experiments/nt3_mlrMBO-360-10

import logging

# Set PYTHONPATH=$PWD
from plottools import *

(root_dir, output_file) = get_args()

# List of all run directories to be processed
rundirs = get_rundirs(root_dir)

logging.info("Found %i directories." % len(rundirs))

# List of events, each a tuple: (timestamp, START|STOP)
events = []

for rundir in rundirs:
    Js = get_jsons(rundir)
    for J in Js:
        record_count = len(J)
        record_start = J[0]
        record_stop  = J[record_count-1]
        time_str_start = record_start["start_time"]
        time_str_stop  = record_stop ["end_time"]["set"]
        secs_start = date2secs(time_str_start)
        secs_stop  = date2secs(time_str_stop)
        # Store the event tuples
        events.append((secs_start, START))
        events.append((secs_stop,  STOP ))

logging.info("Found %i events." % len(events))

if len(events) == 0:
    abort("No events!")

import json

with open('result1.json', 'w') as fp:
    json.dump(events, fp)

# Sort by timestamp
events.sort()

with open('result2.json', 'w') as fp:
    json.dump(events, fp)


# Get first event time
first = events[0][0]

fp_out = open(output_file, "w")
fp_out.write("0 0\n")

# Run through the events in timestamp order,
# record load at each transition point
load = 0
for event in events:
    t = (event[0] - first)/3600
    if event[1] == START:
        load = load+1
    elif event[1] == STOP:
        load = load-1
    else:
        abort("Unknown event!")
    fp_out.write("%0.6f %i\n" % (t, load))

fp_out.close()
logging.info("Wrote %s ." % output_file)
