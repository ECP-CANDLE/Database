
# JSON TO TIME

# NOTE: Run this with './json2table time' (shell script wrapper)

# Converts a directory of runs into a list of run times

import logging

# Set PYTHONPATH=$PWD
from plottools import *

(root_dir, output_file) = get_args()

# List of all run directories to be processed
rundirs = get_rundirs(root_dir)

logging.info("Found %i directories." % len(rundirs))

fp_out = open(output_file, "w")

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
        duration = secs_stop - secs_start
        fp_out.write("%f\n" % duration)


fp_out.close()
logging.info("Wrote %s ." % output_file)
