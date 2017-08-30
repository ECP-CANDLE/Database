
# JSON TO CSV

# NOTE: Run this with './json2table csv params.txt root_dir out.csv'
#       (shell script wrapper)
# where:
#        params.txt is the list of parameter names you want
#        root_dir is the data directory
#        out.csv is the output CSV file
# The parameter names will be on line 1 of the CSV

# Converts a directory of runs into a CSV file
# The output file format for each line is
# val_loss param1 param2 ...

import logging

# Set PYTHONPATH=$PWD
from plottools import *

if len(sys.argv) != 4:
    abort("usage: <params txt> <root directory> <output file>")
params_txt  = sys.argv[1]
root_dir    = sys.argv[2]
output_file = sys.argv[3]

# Parameters selected by user
selected = file2tokens(params_txt)

# List of all run directories to be processed
rundirs = get_rundirs(root_dir)
logging.info("Found %i directories." % len(rundirs))

# The CSV file
fp_out = open(output_file, "w")

# Write CSV header
fp_out.write("val_loss,")
header = ",".join(selected)
fp_out.write(header)
fp_out.write("\n")

def write_values(fp, val_loss, D, selected):
    # I think we have to do this for consistent ordering
    L = [ str(val_loss) ] + [ D[param] for param in selected ]
    # print(L)
    fp.write(",".join(L))
    fp.write("\n")

for rundir in rundirs:

    Js = get_jsons(rundir)
    if len(Js) == 0:
        continue

    # Get parameters from the first JSON file
    record_start = Js[0][0]
    params = record_start["parameters"]
    D = {}
    for entry in params:
        tokens = entry.split(":")
        param = tokens[0]
        if param in selected:
            value = tokens[1].strip()
            D[param] = value

    # Get minimum val_loss in the directory
    val_losses = []
    for J in Js:
        record_count  = len(J)
        record_penult = J[record_count-2]
        val_losses.append(record_penult["validation_loss"]["set"])
    val_loss = min(val_losses)

    write_values(fp_out, val_loss, D, selected)

fp_out.close()
logging.info("Wrote %s ." % output_file)
