
# JSON TO LOAD

# Converts a directory of runs into a simple load over time table
# The output file format for each line is
# timestamp load
# where the timestamp is floating point Unix seconds
# and the load is the number of models running

# Tested with
# root_dir=/projects/Candle_ECP/pbalapra/Experiments/nt3_mlrMBO-360-10

from datetime import datetime
import glob
import json
import os
import sys

def abort(msg):
    print msg
    exit(1)

# Process input arguments
if len(sys.argv) != 3:
    abort("usage: <root directory> <output file>")
root_dir   = sys.argv[1]
output_file = sys.argv[2]

# List of all run directories to be processed
rundirs = []
# Fill in rundirs, omitting miscellaneous files
entries = glob.glob(root_dir+"/*")
for entry in entries:
    if os.path.isdir(entry):
        rundirs.append(entry)

# The time format used in the JSON        
time_fmt = "%Y-%m-%d %H:%M:%S"
# The Unix epoch
epoch = datetime.utcfromtimestamp(0)

def date2secs(date_string):
    """Convert date string from JSON to floating-point seconds"""
    tokens = date_string.split(".")
    prefix = tokens[0]
    suffix = tokens[1]
    d = datetime.strptime(prefix, time_fmt)
    secs = (d - epoch).total_seconds()
    microsecs = int(suffix)
    return secs+microsecs/1000000.0

START = 1
STOP  = 2
# List of events, each a tuple: (timestamp, START|STOP)
events = []

for rundir in rundirs:
    # Find the JSON file
    output = rundir+"/output"
    json_files = glob.glob(output+"/*.json")
    count = len(json_files)
    if count != 1:
        abort("rundir: %s has %i JSON files!" % (rundir,count))
    json_file = json_files[0]
    # Open and parse the JSON file for start/stop events
    with open(json_file, "r") as fp:
        J = json.load(fp)
    record_count = len(J)
    record_start = J[0]
    record_stop  = J[record_count-1]
    time_str_start = record_start["start_time"]
    time_str_stop  = record_stop ["end_time"]["set"]
    secs_start = date2secs(time_str_start)
    secs_stop  = date2secs(time_str_stop)
    # Store the event tuples
    events.append((secs_start,START))
    events.append((secs_stop,STOP))

print("Found %i events." % len(events))

# Sort by timestamp
events.sort()

fp_out = open(output_file, "w")
fp_out.write("0 0\n")

# Run through the events in timestamp order,
# record load at each transition point
load = 0
for event in events:
    t = event[0]
    if event[1] == START:
        load = load+1
    elif event[1] == STOP:
        load = load-1
    else:
        abort("Unknown event!")
    fp_out.write("%0.3f %i\n" % (t, load))

fp_out.close()
