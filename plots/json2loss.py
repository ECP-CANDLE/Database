
# JSON TO LOSS

# NOTE: Run this with './json2table loss' (shell script wrapper)

# Converts a directory of runs into a simple loss over time table
# The output file format for each line is
# timestamp load
# where the timestamp is floating point Unix hours
#   relative to first event
# and the loss is the validation loss reported in the JSON

# Tested with
# Cori: /global/homes/p/pbalapra/candle/nt3_mlrMBO-rs-360-01

import logging

# Set PYTHONPATH=$PWD
from plottools import *

(root_dir, output_file) = get_args()

# List of all run directories to be processed
rundirs = get_rundirs(root_dir)

logging.info("Found %i directories." % len(rundirs))

# List of events, each a tuple: (timestamp, val_loss)
events = []

for rundir in rundirs:
    Js = get_jsons(rundir)
    for J in Js:
        record_count = len(J)
        record_penult = J[record_count-2]
        record_stop   = J[record_count-1]
        val_loss      = record_penult["validation_loss"]["set"]
        time_str_stop = record_stop  ["end_time"]["set"]
        secs_stop     = date2secs(time_str_stop)
        # Store the event tuple
        events.append((secs_stop,  val_loss))

logging.info("Found %i events." % len(events))

if len(events) == 0:
    abort("No events!")

# Sort by timestamp
events.sort()

# Get first event time
first = events[0][0]

fp_out = open(output_file, "w")

# Run through the events in timestamp order,
# record val_loss at each timestamp
load = 0
for event in events:
    t = (event[0] - first)/3600
    fp_out.write("%0.6f %f\n" % (t, event[1]))

fp_out.close()
logging.info("Wrote %s ." % output_file)
