
# PLOT TOOLS

# Tools that support the plotters in this directory

from datetime import datetime
import glob
import json
import logging
import os
import sys

# The time format used in the JSON
time_fmt = "%Y-%m-%d %H:%M:%S"
# The Unix epoch
epoch = datetime.utcfromtimestamp(0)

# Differentiate between start and stop events
START = 1
STOP  = 2

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)-9s%(message)s',)

def abort(msg):
    logging.critical(msg)
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
    return secs + microsecs/1000000.0

def get_jsons(rundir):
    """ Find the JSON files for the given rundir """

    # USER: Select a subdir:
    # subdir = "output"
    subdir = "save"
    output = rundir+"/"+subdir
    json_files = glob.glob(output+"/*.json")

    results = []
    for json_file in json_files:
        size = os.path.getsize(json_file)
        if size == 0:
            logging.warning("file size is 0: %s", json_file)
            continue
        with open(json_file, "r") as fp:
            try:
                J = json.load(fp)
            except ValueError as e:
                abort("Error loading: %s\n%s" % (json_file,str(e)))
        results.append(J)
    return results

def file2tokens(filename):
    result = []
    with open(filename, "r") as fp:
        for line in fp:
            # Strip comments
            splits = line.split("#")
            line = splits[0]
            # Ignore whitespace
            line = line.strip()
            # Omit blank lines
            if len(line) == 0:
                continue
            result.append(line)
    return result
