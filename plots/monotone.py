
# MONOTONE

# Produce a monotonically decreasing output plot from noisy data
# Input:  columns: t x
# Output: columns: t_i x_i , sampled such that x_i <= x_j
#                            for j > i.

from string import *
import sys

# Set PYTHONPATH=$PWD
from plottools import *

if len(sys.argv) != 3:
    abort("usage: <input file> <output file>")
input_file  = sys.argv[1]
output_file = sys.argv[2]

val_loss_min = sys.float_info.max

with open(input_file, "r")  as fp_i, \
     open(output_file, "w") as fp_o:
    for line in fp_i:
        (t, val_loss_string) = split(line)
        val_loss = float(val_loss_string)
        if val_loss < val_loss_min:
            val_loss_min = val_loss
            fp_o.write("%s %f\n" % (t, val_loss_min))
    # Ensure the last data point is written for the plot:
    if val_loss >= val_loss_min:
        fp_o.write("%s %f\n" % (t, val_loss_min))
