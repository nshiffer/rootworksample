# Author Nicholas Shiffer
# Github: nshiffer
# Contact: shiffer.7@osu.edu

import create_update_driver
import input_parsing as inp
from datetime import datetime
import sys

# This is the program entry point
# exampl: ./test_cases/given_test.txt
try:
    in_file = str(sys.argv[1])
except:
    print("Error with command line args, default file used")
    in_file = "./test_cases/given_test.txt"
#open, read and close file
with open(in_file) as fp:
    file_lines = fp.readlines()
out_array = {}
#parse each line and add to array of objects
for line in file_lines:
    line_array = line.split()
    inp.determine_action(line_array, out_array)
# print output in expected format
for driver in out_array:
    out_array[driver].prettyPrintInfo()
