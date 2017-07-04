
# JSON TO RATE

# NOTE: Run this with './json2table rate' (shell script wrapper)

# Converts a directory of runs into a learning rate over time table
# The output file format for each line is
# timestamp rate
# where the timestamp is floating point Unix hours
#   relative to first event
# and the rate is defined in the README

# Tested with dataset on Theta:
# root_dir=/projects/Candle_ECP/pbalapra/Experiments/nt3_mlrMBO-360-10

import math

# Set PYTHONPATH=$PWD
from plottools import *

(root_dir, output_file) = get_args()

# List of all run directories to be processed
rundirs = get_rundirs(root_dir)

# List of events, each a tuple: (timestamp, START|STOP)
events = []

def get_param(parameters, param):
    token = param+": "
    chars = len(token)
    for parameter in parameters:
        if parameter.startswith(token):
            s = parameter[chars:]
            return int(s)

training_size = 1120.0

for rundir in rundirs:
    J = get_json(rundir)
    record_count = len(J)
    record_start = J[0]
    record_stop  = J[record_count-1]
    epochs = record_count-2
    parameters = J[0]["parameters"]
    batch_size       = get_param(parameters, "batch_size")
    trainable_params = get_param(parameters, "trainable_params")
    time_str_start = record_start["start_time"]
    time_str_stop  = record_stop ["end_time"]["set"]
    secs_start = date2secs(time_str_start)
    secs_stop  = date2secs(time_str_stop)
    duration = secs_stop - secs_start
    rate = trainable_params * math.ceil(training_size/batch_size) * epochs / duration
    # Store the event tuples
    events.append((secs_start, START, rate))
    events.append((secs_stop,  STOP,  rate))

print("Found %i events." % len(events))

# Sort by timestamp
events.sort()

# Get first event time
first = events[0][0]

fp_out = open(output_file, "w")
fp_out.write("0 0\n")

# Run through the events in timestamp order,
# record rate at each transition point
rate = 0
for event in events:
    t = (event[0] - first) / 3600
    if event[1] == START:
        rate = rate+event[2]
    elif event[1] == STOP:
        rate = rate-event[2]
    else:
        abort("Unknown event!")
    fp_out.write("%0.6f %i\n" % (t, rate))

fp_out.close()
