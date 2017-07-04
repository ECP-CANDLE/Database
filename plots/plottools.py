
# PLOT TOOLS

# Tools that support the plotters in this directory

from datetime import datetime
import glob
import json
import os
import sys

# The time format used in the JSON
time_fmt = "%Y-%m-%d %H:%M:%S"
# The Unix epoch
epoch = datetime.utcfromtimestamp(0)

START = 1
STOP  = 2

def abort(msg):
    print msg
    exit(1)

def get_args():
    """ Process input arguments """
    if len(sys.argv) != 3:
        abort("usage: <root directory> <output file>")
    root_dir   = sys.argv[1]
    output_file = sys.argv[2]
    return (root_dir, output_file)

def get_rundirs(root_dir):
    """ Fill in rundirs, omitting miscellaneous files """
    rundirs = []
    entries = glob.glob(root_dir+"/*")
    for entry in entries:
        if os.path.isdir(entry):
            rundirs.append(entry)
    return rundirs

def date2secs(date_string):
    """Convert date string from JSON to floating-point seconds"""
    tokens = date_string.split(".")
    prefix = tokens[0]
    suffix = tokens[1]
    d = datetime.strptime(prefix, time_fmt)
    secs = (d - epoch).total_seconds()
    microsecs = int(suffix)
    return secs+microsecs/1000000.0

def get_json(rundir):
    """ Find the JSON file for the given rundir """
    output = rundir+"/output"
    json_files = glob.glob(output+"/*.json")
    count = len(json_files)
    if count != 1:
        abort("rundir: %s has %i JSON files!" % (rundir,count))
    json_file = json_files[0]
    # Open and parse the JSON file for start/stop events
    with open(json_file, "r") as fp:
        J = json.load(fp)
    return J
